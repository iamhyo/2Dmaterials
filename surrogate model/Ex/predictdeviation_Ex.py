#!/usr/bin/env python
# coding: utf-8

# In[308]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import string as str
import sys
import math
from pycaret.regression import *
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

c2db= pd.read_csv("new_c2db_SDCD.csv")
MatGAN = pd.read_csv("RELAX_MatGAN_SDCD_True.csv")
c2db['Ex']=0
c2db['Ey']=0
for i in range(len(c2db)):
    c2db['Ex'].iloc[i] = ((c2db['C11'].iloc[i]*c2db['C22'].iloc[i])-(c2db['C12'].iloc[i]*c2db['C21'].iloc[i]))/c2db['C22'].iloc[i]
    c2db['Ey'].iloc[i] = ((c2db['C11'].iloc[i]*c2db['C22'].iloc[i])-(c2db['C12'].iloc[i]*c2db['C21'].iloc[i]))/c2db['C11'].iloc[i]


# In[277]:


MatGAN = MatGAN.drop(['Index','Formula'],axis=1)
len(MatGAN)


# In[278]:


c2db=c2db[c2db['C11']>0]
c2db=c2db[c2db['C12']>0]
c2db=c2db[c2db['C21']>0]
c2db=c2db[c2db['C22']>0]


# In[279]:


c2db=c2db.drop(['C11','C12','C13','C21','C22','C23','C31','C32','Index'],axis=1)


# In[280]:


## Ex 관련 모델 만들기


# In[281]:


MatGAN_Ex = MatGAN.drop(['Ey','C33'],axis=1)
c2db_Ex = c2db.drop(['Ey','C33'],axis=1)


# In[282]:


c2db_Ex = c2db_Ex[c2db_Ex['Ex']>0]
len(c2db_Ex)


# In[283]:


reg_1 = setup(data=c2db_Ex, target='Ex', train_size =0.8, silent=True, session_id =2222)


# In[284]:


compare_models()


# In[285]:


et = create_model('et')


# In[286]:


c2db_Ex=c2db_Ex.dropna()
X= c2db_Ex.drop('Ex',axis=1)
Y=c2db_Ex['Ex']
X_train_0, X_test, Y_train_0, y_test = train_test_split(X,Y,test_size=0.2)


# In[287]:


MatGAN = pd.read_csv("RELAX_MatGAN_SDCD_True.csv")
MatGAN = MatGAN.drop(['Index','Formula'],axis=1)
MatGAN_Ex = MatGAN.drop(['Ey','C33'],axis=1)
MatGAN_Ex_cycle_0 = MatGAN_Ex
MatGAN_Ex_cycle_0_X = MatGAN_Ex_cycle_0.drop('Ex',axis=1)
MatGAN_Ex_cycle_0_Y = MatGAN_Ex_cycle_0['Ex']


# In[ ]:





# In[ ]:





# 이거야

# In[3]:


for i in range(0,2):
    print(i)
    
    A=[]
    B=[]
    C=[]
    
    for j in range(0,50):
        X_train_0,X_test,Y_train_0,y_test=train_test_split(X,Y,test_size=0.2)
        print(j)
        print('***************')
        if i == 0:    
            
            et.fit(globals()['X_train_{}'.format(i)],globals()['Y_train_{}'.format(i)])
        
        else:
            
            
            globals()["X_train_{}".format(i)] = pd.concat([X_train_0,globals()['MatGAN_Ex_add_{}_X'.format(i-1)]]).reset_index(drop=bool,inplace=False)
            globals()["Y_train_{}".format(i)] = pd.concat([Y_train_0,globals()['MatGAN_Ex_add_{}_Y'.format(i-1)]]).reset_index(drop=bool,inplace=False)
            et.fit(globals()['X_train_{}'.format(i)],globals()['Y_train_{}'.format(i)])
            
        globals()["cycle_{i}_{j}".format(i=i,j=j)] = et.predict(globals()['MatGAN_Ex_cycle_{}_X'.format(i)])
        globals()['pd_cycle_{i}_{j}'.format(i=i,j=j)] = pd.DataFrame(globals()["cycle_{i}_{j}".format(i=i,j=j)])
        globals()['MAE_{i}_{j}'.format(i=i,j=j)] = mean_absolute_error(globals()['MatGAN_Ex_cycle_{}_Y'.format(i)],globals()['cycle_{i}_{j}'.format(i=i,j=j)])
        
        globals()['RMSE_{i}_{j}'.format(i=i,j=j)] = mean_squared_error(globals()['MatGAN_Ex_cycle_{}_Y'.format(i)],globals()['cycle_{i}_{j}'.format(i=i,j=j)])
        globals()['r2_score_{i}_{j}'.format(i=i,j=j)] = r2_score(globals()['MatGAN_Ex_cycle_{}_Y'.format(i)],globals()['cycle_{i}_{j}'.format(i=i,j=j)])
        
    
    globals()['pred_{}'.format(i)] = pd.concat([globals()['pd_cycle_{i}_0'.format(i=i)],globals()['pd_cycle_{i}_1'.format(i=i)]
                                            ,globals()['pd_cycle_{i}_2'.format(i=i)],globals()['pd_cycle_{i}_3'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_5'.format(i=i)],globals()['pd_cycle_{i}_7'.format(i=i)]
                                                ,globals()['pd_cycle_{i}_4'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_9'.format(i=i)],globals()['pd_cycle_{i}_6'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_11'.format(i=i)],globals()['pd_cycle_{i}_8'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_13'.format(i=i)],globals()['pd_cycle_{i}_10'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_15'.format(i=i)],globals()['pd_cycle_{i}_12'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_17'.format(i=i)],globals()['pd_cycle_{i}_14'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_19'.format(i=i)],globals()['pd_cycle_{i}_16'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_21'.format(i=i)],globals()['pd_cycle_{i}_18'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_23'.format(i=i)],globals()['pd_cycle_{i}_20'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_25'.format(i=i)],globals()['pd_cycle_{i}_22'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_27'.format(i=i)],globals()['pd_cycle_{i}_24'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_29'.format(i=i)],globals()['pd_cycle_{i}_26'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_31'.format(i=i)],globals()['pd_cycle_{i}_28'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_33'.format(i=i)],globals()['pd_cycle_{i}_30'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_35'.format(i=i)],globals()['pd_cycle_{i}_32'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_37'.format(i=i)],globals()['pd_cycle_{i}_34'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_39'.format(i=i)],globals()['pd_cycle_{i}_36'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_41'.format(i=i)],globals()['pd_cycle_{i}_38'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_43'.format(i=i)],globals()['pd_cycle_{i}_40'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_45'.format(i=i)],globals()['pd_cycle_{i}_42'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_47'.format(i=i)],globals()['pd_cycle_{i}_44'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_49'.format(i=i)],globals()['pd_cycle_{i}_46'.format(i=i)]
                                               ,globals()['pd_cycle_{i}_48'.format(i=i)]
                                               ],axis=1)
    globals()['std_{}'.format(i)] = []

    for k in range(len(globals()['pred_{}'.format(i)])):
        globals()['std_{}'.format(i)].append(np.std(globals()['pred_{}'.format(i)].loc[k]))
    
    globals()['pd_std_{}'.format(i)] = pd.DataFrame(globals()['std_{}'.format(i)])
    globals()['top_20_deviation_{}'.format(i)] = globals()['pd_std_{}'.format(i)].sort_values(by=0, ascending=False)[0:20]
    
    globals()['MatGAN_Ex_add_{}'.format(i)] = pd.merge(globals()['top_20_deviation_{}'.format(i)],globals()['MatGAN_Ex_cycle_{}'.format(i)],left_index=True,right_index=True,how='left').drop(0,axis=1).reset_index(drop=bool,inplace=False)
    
    globals()['MatGAN_Ex_cycle_{}'.format(i)]['check']=0
    
    for k in range (len(globals()['MatGAN_Ex_cycle_{}'.format(i)])):
        if pd.DataFrame(globals()['MatGAN_Ex_cycle_{}'.format(i)].index)[0].iloc[k] in globals()['MatGAN_Ex_add_{}'.format(i)].index.tolist():
            globals()['MatGAN_Ex_cycle_{}'.format(i)]['check'].iloc[k]=1

            
    globals()['MatGAN_Ex_cycle_{}'.format(i+1)] = globals()['MatGAN_Ex_cycle_{}'.format(i)][globals()['MatGAN_Ex_cycle_{}'.format(i)]['check']==0].reset_index(drop=bool,inplace=False)
    globals()['MatGAN_Ex_cycle_{}'.format(i+1)] = globals()['MatGAN_Ex_cycle_{}'.format(i+1)].drop('check',axis=1).reset_index(drop=bool,inplace=False)
    globals()['MatGAN_Ex_cycle_{}'.format(i)] = globals()['MatGAN_Ex_cycle_{}'.format(i)].drop('check',axis=1).reset_index(drop=bool,inplace=False)
    
    globals()['MatGAN_Ex_add_{}_Y'.format(i)] = globals()['MatGAN_Ex_add_{}'.format(i)]['Ex']
    globals()['MatGAN_Ex_add_{}_X'.format(i)] = globals()['MatGAN_Ex_add_{}'.format(i)].drop('Ex',axis=1)
    
    if i !=0:
        
        globals()['MatGAN_Ex_add_{}_X'.format(i)] = pd.concat([globals()['MatGAN_Ex_add_{}_X'.format(i)],globals()['MatGAN_Ex_add_{}_X'.format(i-1)]]).reset_index(drop=bool,inplace=False)
        globals()['MatGAN_Ex_add_{}_Y'.format(i)] = pd.concat([globals()['MatGAN_Ex_add_{}_Y'.format(i)],globals()['MatGAN_Ex_add_{}_Y'.format(i-1)]]).reset_index(drop=bool,inplace=False)



    globals()['MatGAN_Ex_cycle_{}_Y'.format(i+1)] = globals()['MatGAN_Ex_cycle_{}'.format(i+1)]['Ex'].reset_index(drop=bool,inplace=False)
    globals()['MatGAN_Ex_cycle_{}_X'.format(i+1)] = globals()['MatGAN_Ex_cycle_{}'.format(i+1)].drop('Ex',axis=1).reset_index(drop=bool,inplace=False)


# In[412]:


for i in range(0,20):
    globals()['r2_score_{}'.format(i)] = []
    globals()['MAE_{}'.format(i)] = []
    globals()['RMSE_{}'.format(i)] = []
    for j in range(0,50):
        globals()['r2_score_{}'.format(i)].append(globals()['r2_score_{i}_{j}'.format(i=i,j=j)])
        globals()['MAE_{}'.format(i)].append(globals()['MAE_{i}_{j}'.format(i=i,j=j)])
        globals()['RMSE_{}'.format(i)].append(globals()['RMSE_{i}_{j}'.format(i=i,j=j)])
        
    pd.DataFrame(globals()['r2_score_{}'.format(i)]).to_csv("r2_score_{}.csv".format(i))
    pd.DataFrame(globals()['MAE_{}'.format(i)]).to_csv("MAE_score_{}.csv".format(i))
    pd.DataFrame(globals()['RMSE_{}'.format(i)]).to_csv("RMSE_score_{}.csv".format(i))


# In[409]:





# In[ ]:




