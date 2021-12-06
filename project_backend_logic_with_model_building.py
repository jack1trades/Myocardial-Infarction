# -*- coding: utf-8 -*-
"""project_backend_logic_with_model_building.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18cLAeIID6JQzJi1_I1nejkjig92iJrOQ
"""

import pandas as pd
import seaborn as sns
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

"""# Reading Dataset"""

df=pd.read_csv("Myocardial infarction complications.csv")

df.drop('ID',
  axis=1, inplace=True)

df.info()

df

missing_list=df.isnull().sum().tolist()

"""# Counting null values for continuous values"""

b=[]
cont=["AGE","S_AD_KBRIG","D_AD_KBRIG","S_AD_ORIT","D_AD_ORIT","K_BLOOD","NA_BLOOD","ALT_BLOOD","AST_BLOOD","KFK_BLOOD","L_BLOOD","ROE"]
for i in cont:
    a=df[i].isnull().sum()
    b.append(a)
b

missing_list

df.columns.to_list()

"""# Making list of Categorical and continous varibale for imputataions"""

continuous_param_list=["AGE","S_AD_KBRIG","D_AD_KBRIG","S_AD_ORIT","D_AD_ORIT","K_BLOOD","NA_BLOOD","ALT_BLOOD","AST_BLOOD","KFK_BLOOD","L_BLOOD","ROE"]

len(continuous_param_list)

categorical_param_list=[ 'SEX','INF_ANAM','STENOK_AN','FK_STENOK','IBS_POST','IBS_NASL','GB','SIM_GIPERT','DLIT_AG','ZSN_A',
'nr_11','nr_01','nr_02','nr_03','nr_04','nr_07','nr_08','np_01','np_04','np_05','np_07',
 'np_08',
 'np_09',
 'np_10',
 'endocr_01',
 'endocr_02',
 'endocr_03',
 'zab_leg_01',
 'zab_leg_02',
 'zab_leg_03',
 'zab_leg_04',
 'zab_leg_06',
 'O_L_POST',
 'K_SH_POST',
 'MP_TP_POST',
 'SVT_POST',
 'GT_POST',
 'FIB_G_POST',
 'ant_im',
 'lat_im',
 'inf_im',
 'post_im',
 'IM_PG_P',
 'ritm_ecg_p_01',
 'ritm_ecg_p_02',
 'ritm_ecg_p_04',
 'ritm_ecg_p_06',
 'ritm_ecg_p_07',
 'ritm_ecg_p_08',
 'n_r_ecg_p_01',
 'n_r_ecg_p_02',
 'n_r_ecg_p_03',
 'n_r_ecg_p_04',
 'n_r_ecg_p_05',
 'n_r_ecg_p_06',
 'n_r_ecg_p_08',
 'n_r_ecg_p_09',
 'n_r_ecg_p_10',
 'n_p_ecg_p_01',
 'n_p_ecg_p_03',
 'n_p_ecg_p_04',
 'n_p_ecg_p_05',
 'n_p_ecg_p_06',
 'n_p_ecg_p_07',
 'n_p_ecg_p_08',
 'n_p_ecg_p_09',
 'n_p_ecg_p_10',
 'n_p_ecg_p_11',
 'n_p_ecg_p_12',
 'fibr_ter_01',
 'fibr_ter_02',
 'fibr_ter_03',
 'fibr_ter_05',
 'fibr_ter_06',
 'fibr_ter_07',
 'fibr_ter_08',
 'GIPO_K',
 'GIPER_NA',
 'TIME_B_S',
 'R_AB_1_n',
 'R_AB_2_n',
 'R_AB_3_n',
 'NA_KB',
 'NOT_NA_KB',
 'LID_KB',
 'NITR_S',
 'NA_R_1_n',
 'NA_R_2_n',
 'NA_R_3_n',
 'NOT_NA_1_n',
 'NOT_NA_2_n',
 'NOT_NA_3_n',
 'LID_S_n',
 'B_BLOK_S_n',
 'ANT_CA_S_n',
 'GEPAR_S_n',
 'ASP_S_n',
 'TIKL_S_n',
 'TRENT_S_n',
 'FIBR_PREDS',
 'PREDS_TAH',
 'JELUD_TAH',
 'FIBR_JELUD',
 'A_V_BLOK',
 'OTEK_LANC',
 'RAZRIV',
 'DRESSLER',
 'ZSN',
 'REC_IM',
 'P_IM_STEN',
 'LET_IS']

len(categorical_param_list)

"""# Median imputation for continuous values"""

for column in continuous_param_list:
    df[column].fillna(df[column].median(),inplace=True)

"""# Mode Imputation for categorical values """

for column in categorical_param_list:
    df[column].fillna(df[column].mode()[0],inplace=True)

missing_list=df.isnull().sum().tolist()

missing_list.count(0)

df['S_AD_KBRIG'].isin([140]).sum()

df['K_BLOOD'].isin([4.1]).sum()

df['IBS_POST'].isin([2]).sum()

df['SIM_GIPERT'].isin([0]).sum()

df['DLIT_AG'].isin([0]).sum()

df.dtypes

df_new = df['LET_IS']
df_new

"""# Function for normalizing continuous data """

for column in continuous_param_list:
    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())

df

"""# Feature Engg using chi2"""

from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

column_list = df.columns.tolist()

column_list.remove('LET_IS')
len(column_list)

test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, y)
fit.scores_

len(fit.scores_)

"""# Making dict of score and feature  using df.columns as list and chi2 score as values as to get idea of weights of each columns"""

d=dict();
for i in range(len(fit.scores_)):
    d[column_list[i]]= fit.scores_[i]

d

"""# Filtering the dict based on values of score you wish to have among the chi2 predicted scores eg- 10,15,20"""

high_score_features={k:v for (k,v) in d.items() if v > 15}

high_score_features

len(high_score_features)

selected_features = []
for k,v in high_score_features.items():
    selected_features.append(k)
selected_features

"""# Making Data set Compatible with Feature Engg selected features only and dropping rest features automatically and no updation from user needed"""

for i in df.columns:
    if i not in selected_features:
        df.drop(i,axis=1, inplace=True)
    else:
        pass

df['LET_IS'] = df_new

df

a=df.isnull().sum()
a.sum()

"""# Checking balance for y which shows large imbalance and we need dataset balancing for it """

df.LET_IS.value_counts()

"""# Balancing imbalanced dataset for train set only"""

from sklearn.model_selection import train_test_split
import numpy as np
x_train, x_test, y_train, y_test = train_test_split(df.drop(labels=['LET_IS'], axis=1),df['LET_IS'],test_size=0.2,random_state=41)


# ## Train dataset balancing

from imblearn.over_sampling import SMOTE
sm = SMOTE()
x_train_res, y_train_res = sm.fit_resample(x_train, y_train)
unique, counts = np.unique(y_train_res, return_counts=True)
print(list(zip(unique, counts)))
#y_train_res
#X_train_res

"""# Decision Tree  method"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier(criterion = 'entropy',max_depth=10)
dtree.fit(x_train_res, y_train_res)
# Test Accuracy,confusion matrix, classification report
y_pred_DT_test=dtree.predict(x_test)
print ('Accuracy test:', accuracy_score(y_test, y_pred_DT_test))
print ('Confusion matrix:', confusion_matrix(y_test, y_pred_DT_test))
print ('classification report test:', classification_report(y_test, y_pred_DT_test))
# Train Accuracy
y_pred_DT_train=dtree.predict(x_train_res)
print ('Accuracy train:', accuracy_score(y_train_res, y_pred_DT_train))

"""# Finding optimum value of max_depth for improving accuracy for DT using Gridsearch CV on train balanced dataset"""

from sklearn.model_selection import GridSearchCV
max_depth = np.array(range(1,10))
param_grid = dict(max_depth=max_depth)
model = DecisionTreeClassifier(criterion = 'entropy')
grid = GridSearchCV(estimator=model, param_grid=param_grid)
grid.fit(x_train_res, y_train_res)
print(grid.best_score_)
print(grid.best_params_)

"""# KNN Method """

model_KNN = KNeighborsClassifier(n_neighbors=2)
model_KNN.fit(x_train_res, y_train_res)
# Test Accuracy,confusion matrix, classification report
y_pred_KNN_test=model_KNN.predict(x_test)
print ('Accuracy test:', accuracy_score(y_test, y_pred_KNN_test))
print ('Confusion matrix test:', confusion_matrix(y_test, y_pred_KNN_test))
print ('classification report test:', classification_report(y_test, y_pred_KNN_test))
# Train Accuracy
y_pred_KNN_train=model_KNN.predict(x_train_res)
print ('Accuracy train:', accuracy_score(y_train_res, y_pred_KNN_train))

"""# Finding optimum value of n_neighbours for improving accuracy for KNN using Gridsearch CV on train balanced dataset"""

from sklearn.model_selection import GridSearchCV
import numpy

n_neighbors = numpy.array(range(1,40))
param_grid = dict(n_neighbors=n_neighbors)

model_1 = KNeighborsClassifier()
grid = GridSearchCV(estimator=model_1, param_grid=param_grid)
grid.fit(x_train_res, y_train_res)

print(grid.best_score_)
print(grid.best_params_)

"""# Random Forest """

from sklearn.ensemble import RandomForestClassifier
num_trees = 130
max_features = 4
model_RF = RandomForestClassifier(n_estimators=num_trees, max_features=max_features)
model_RF.fit(x_train_res, y_train_res)
# Test Accuracy,confusion matrix, classification report
y_pred_RF_test=model_RF.predict(x_test)
print ('Accuracy test:', accuracy_score(y_test, y_pred_RF_test))
print ('Confusion matrix test:', confusion_matrix(y_test, y_pred_RF_test))
print ('classification report test:', classification_report(y_test, y_pred_RF_test))
# Train Accuracy
y_pred_RF_train=model_RF.predict(x_train_res)
print ('Accuracy train:', accuracy_score(y_train_res, y_pred_RF_train))

"""# Finding optimum value of n_estimators and max_features for improving accuracy for RF using Gridsearch CV on train balanced dataset"""

from sklearn.model_selection import GridSearchCV
n_neighbors = np.array(range(100,150))
param_grid = dict(n_estimators=n_neighbors)
model = RandomForestClassifier()
grid = GridSearchCV(estimator=model, param_grid=param_grid)
grid.fit(x_train_res, y_train_res)
print(grid.best_score_)
print(grid.best_params_)

from sklearn.model_selection import GridSearchCV
max_features = np.array(range(1,5))
param_grid = dict(max_features=max_features)
model = RandomForestClassifier()
grid = GridSearchCV(estimator=model, param_grid=param_grid)
grid.fit(x_train_res, y_train_res)
print(grid.best_score_)
print(grid.best_params_)

df

"""# Testing individual models for Overall dataset"""

array = df.values
X_overall = array[:, 0:-1]
Y_overall = array[:, -1]

X_overall

Y_overall

# DT for Overall

y_pred_DT_overall=dtree.predict(X_overall)
print ('Accuracy overall:', accuracy_score(Y_overall, y_pred_DT_overall))
print ('classification report overall:', classification_report(Y_overall, y_pred_DT_overall))

# KNN for Overall

y_pred_KNN_overall=model_KNN.predict(X_overall)
print ('Accuracy overall:', accuracy_score(Y_overall, y_pred_KNN_overall))
print ('classification report overall:', classification_report(Y_overall, y_pred_KNN_overall))

# RF for overall

y_pred_RF_overall=model_RF.predict(X_overall)
print ('Accuracy overall:', accuracy_score(Y_overall, y_pred_RF_overall))
print ('classification report overall:', classification_report(Y_overall, y_pred_RF_overall))

df["y_pred_DT_overall"] = y_pred_DT_overall
df["y_pred_KNN_overall"] = y_pred_KNN_overall
df["y_pred_RF_overall"] = y_pred_RF_overall

df.to_csv("Final_dataframe_with_predictions.csv")

"""# Finding From above methods RF gives high Accuracy For test,train, and also for overall dataset. So Random forest is best method for prediction and obtaining classification and is selected for final deployment."""