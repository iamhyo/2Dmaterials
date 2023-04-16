#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ElMD import ElMD
from ElMD import elmd
import re
import pandas as pd
import numpy as np

bottom_up = pd.read_csv("./2Dmatpedia bottom-up.csv")
top_down = pd.read_csv("./2Dmatpedia top-down.csv")
icsd = pd.read_csv("./icsd_cryspnet_trans.csv")
MP = pd.read_csv("./MP_cryspnet_trans.csv")
oqmd = pd.read_csv("./oqmd_cryspnet_trans.csv")

MP = MP.drop(['Unnamed: 0'],axis=1)
icsd = icsd.drop(['Unnamed: 0'],axis=1)
oqmd = oqmd.drop(['Unnamed: 0'],axis=1)


# In[14]:


icsd_bottom = []
bottom_icsd = []
A = []
B = []
C = []
F = []

for i in range (len(icsd)):
    a = icsd.iloc[i,10]
    aa = icsd.iloc[i,0]
    for j in range (len(bottom_up)):
        b = bottom_up.iloc[j,3]
        bb = bottom_up.iloc[j,2]
        bbb = bottom_up.iloc[j,0]
        if a==b:
            icsd_bottom.append(aa)
            bottom_icsd.append(bb)
            B.append(bbb)
            
icsd_bottom = pd.DataFrame(icsd_bottom)
bottom_icsd = pd.DataFrame(bottom_icsd)
B = pd.DataFrame(B)

for k in range (len(icsd_bottom)):
    if elmd(icsd_bottom.iloc[k,0],bottom_icsd.iloc[k,0])<2:
        c = icsd_bottom.iloc[k,0],bottom_icsd.iloc[k,0],B.iloc[k,0],elmd(icsd_bottom.iloc[k,0],bottom_icsd.iloc[k,0])
        A.append(c)
        
        
A = pd.DataFrame(A)
C = []

for l in range(len(A)):
    check_number = A.iloc[l,0],A.iloc[l,1]
    numbers_icsd = re.findall(r'\d+',A.iloc[l,0])
    numbers_bottom = re.findall(r'\d+',A.iloc[l,1])
    if numbers_icsd == numbers_bottom:
        gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2]
        C.append(gogo)
    else:
        pd_numbers_icsd = pd.DataFrame(numbers_icsd)
        pd_numbers_bottom = pd.DataFrame(numbers_bottom)
        gaza = pd_numbers_icsd.apply(pd.to_numeric).sum()
        gaboza = pd_numbers_bottom.apply(pd.to_numeric).sum()
        plz = pd.DataFrame(gaza%gaboza)
        if plz.loc[0,0] == 0 :
            gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2],A.iloc[l,3]
            C.append(gogo)

pd.DataFrame(C)
C = pd.DataFrame(C)
C
C.to_csv("bottom_up_icsd_2_True.csv", index=False)


# In[15]:


icsd_top = []
top_icsd = []
A = []
B = []
C = []
F= []
for i in range (len(icsd)):
    a = icsd.iloc[i,10]
    aa = icsd.iloc[i,0]
    for j in range (len(top_down)):
        b = top_down.iloc[j,3]
        bb = top_down.iloc[j,2]
        bbb = top_down.iloc[j,0]
        if a==b:
            icsd_top.append(aa)
            top_icsd.append(bb)
            B.append(bbb)
            
icsd_top = pd.DataFrame(icsd_top)
top_icsd = pd.DataFrame(top_icsd)
B = pd.DataFrame(B)

for k in range (len(icsd_top)):
    if elmd(icsd_top.iloc[k,0],top_icsd.iloc[k,0])<2:
        c = icsd_top.iloc[k,0],top_icsd.iloc[k,0], B.iloc[k,0], elmd(icsd_top.iloc[k,0],top_icsd.iloc[k,0])
        A.append(c)
        
        
A = pd.DataFrame(A)
C = []

for l in range(len(A)):
    check_number = A.iloc[l,0],A.iloc[l,1]
    numbers_icsd = re.findall(r'\d+',A.iloc[l,0])
    numbers_top = re.findall(r'\d+',A.iloc[l,1])
    if numbers_icsd == numbers_top:
        gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2]
        C.append(gogo)
    else:
        pd_numbers_icsd = pd.DataFrame(numbers_icsd)
        pd_numbers_top = pd.DataFrame(numbers_top)
        gaza = pd_numbers_icsd.apply(pd.to_numeric).sum()
        gaboza = pd_numbers_top.apply(pd.to_numeric).sum()
        plz = pd.DataFrame(gaza%gaboza)
        if plz.loc[0,0] == 0 :
            gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2],A.iloc[l,3]
            C.append(gogo)
            
pd.DataFrame(C)
C = pd.DataFrame(C)
C
C.to_csv("top_dowm_icsd_2_True.csv", index=False)        


# In[16]:


MP_bottom = []
bottom_MP = []
A = []
B = []
C = []
F = []
for i in range (len(MP)):
    a = MP.iloc[i,10]
    aa = MP.iloc[i,0]
    for j in range (len(bottom_up)):
        b = bottom_up.iloc[j,3]
        bb = bottom_up.iloc[j,2]
        bbb = bottom_up.iloc[j,0]
        if a==b:
            MP_bottom.append(aa)
            bottom_MP.append(bb)
            B.append(bbb)
            
            
MP_bottom = pd.DataFrame(MP_bottom)
bottom_MP = pd.DataFrame(bottom_MP)
B = pd.DataFrame(B)

for k in range (len(MP_bottom)):
    if elmd(MP_bottom.iloc[k,0],bottom_MP.iloc[k,0])<2:
        c = MP_bottom.iloc[k,0],bottom_MP.iloc[k,0],B.iloc[k,0],elmd(MP_bottom.iloc[k,0],bottom_MP.iloc[k,0])
        A.append(c)

A = pd.DataFrame(A)
C = []

for l in range(len(A)):
    check_number = A.iloc[l,0],A.iloc[l,1]
    numbers_MP = re.findall(r'\d+',A.iloc[l,0])
    numbers_bottom = re.findall(r'\d+',A.iloc[l,1])
    if numbers_MP == numbers_bottom:
        gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2]
        C.append(gogo)
    else:
        pd_numbers_MP = pd.DataFrame(numbers_MP)
        pd_numbers_bottom = pd.DataFrame(numbers_bottom)
        gaza = pd_numbers_MP.apply(pd.to_numeric).sum()
        gaboza = pd_numbers_bottom.apply(pd.to_numeric).sum()
        plz = pd.DataFrame(gaza%gaboza)
        if plz.loc[0,0] == 0 :
            gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2],A.iloc[l,3]
            C.append(gogo)

pd.DataFrame(C)
C = pd.DataFrame(C)
C
C.to_csv("bottom_up_MP_2_True.csv", index=False)


# In[17]:


MP_top = []
top_MP = []
A = []
B = []
C = []
F = []
for i in range (len(MP)):
    a = MP.iloc[i,10]
    aa = MP.iloc[i,0]
    for j in range (len(top_down)):
        b = top_down.iloc[j,3]
        bb = top_down.iloc[j,2]
        bbb = top_down.iloc[j,0]
        if a==b:
            MP_top.append(aa)
            top_MP.append(bb)
            B.append(bbb)
            
MP_top = pd.DataFrame(MP_top)
top_MP = pd.DataFrame(top_MP)
B = pd.DataFrame(B)

for k in range (len(MP_top)):
    if elmd(MP_top.iloc[k,0],top_MP.iloc[k,0])<2:
        c = MP_top.iloc[k,0],top_MP.iloc[k,0],B.iloc[k,0],elmd(MP_top.iloc[k,0],top_MP.iloc[k,0])
        A.append(c)
        
A = pd.DataFrame(A)
C = []

for l in range(len(A)):
    check_number = A.iloc[l,0],A.iloc[l,1]
    numbers_MP = re.findall(r'\d+',A.iloc[l,0])
    numbers_top = re.findall(r'\d+',A.iloc[l,1])
    if numbers_MP == numbers_top:
        gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2]
        C.append(gogo)
    else:
        pd_numbers_MP = pd.DataFrame(numbers_MP)
        pd_numbers_top = pd.DataFrame(numbers_top)
        gaza = pd_numbers_MP.apply(pd.to_numeric).sum()
        gaboza = pd_numbers_top.apply(pd.to_numeric).sum()
        plz = pd.DataFrame(gaza%gaboza)
        if plz.loc[0,0] == 0 :
            gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2],A.iloc[l,3]
            C.append(gogo)

        

pd.DataFrame(C)
C = pd.DataFrame(C)
C
C.to_csv("top_down_MP_2_True.csv", index=False)


# In[18]:


oqmd_bottom = []
bottom_oqmd = []

A = []
B = []
C = []
F = []
for i in range (len(oqmd)):
    a = oqmd.iloc[i,10]
    aa = oqmd.iloc[i,0]
    for j in range (len(bottom_up)):
        b = bottom_up.iloc[j,3]
        bb = bottom_up.iloc[j,2]
        bbb = bottom_up.iloc[j,0]
        if a==b:
            oqmd_bottom.append(aa)
            bottom_oqmd.append(bb)
            B.append(bbb)
            
oqmd_bottom = pd.DataFrame(oqmd_bottom)

bottom_oqmd = pd.DataFrame(bottom_oqmd)
B = pd.DataFrame(B)

for k in range (len(oqmd_bottom)):
    if elmd(oqmd_bottom.iloc[k,0],bottom_oqmd.iloc[k,0])<2:
        c = oqmd_bottom.iloc[k,0], bottom_oqmd.iloc[k,0], B.iloc[k,0],elmd(oqmd_bottom.iloc[k,0],bottom_oqmd.iloc[k,0])
        A.append(c)
        
A = pd.DataFrame(A)
C = []

for l in range(len(A)):
    check_number = A.iloc[l,0],A.iloc[l,1]
    numbers_oqmd = re.findall(r'\d+',A.iloc[l,0])
    numbers_bottom = re.findall(r'\d+',A.iloc[l,1])
    if numbers_oqmd == numbers_bottom:
        gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2]
        C.append(gogo)
    else:
        pd_numbers_oqmd = pd.DataFrame(numbers_oqmd)
        pd_numbers_bottom = pd.DataFrame(numbers_bottom)
        gaza = pd_numbers_oqmd.apply(pd.to_numeric).sum()
        gaboza = pd_numbers_bottom.apply(pd.to_numeric).sum()
        plz = pd.DataFrame(gaza%gaboza)
        if plz.loc[0,0] == 0 :
            gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2],A.iloc[l,3]
            C.append(gogo)


pd.DataFrame(C)
C = pd.DataFrame(C)
C
C.to_csv("bottom_up_oqmd_2_True.csv", index=False)        


# In[20]:


oqmd_top = []
top_oqmd = []
A = []
B = []
C = []
F = []
for i in range (len(oqmd)):
    a = oqmd.iloc[i,10]
    aa = oqmd.iloc[i,0]
    for j in range (len(top_down)):
        b = top_down.iloc[j,3]
        bb = top_down.iloc[j,2]
        bbb = top_down.iloc[j,0]
        if a==b:
            oqmd_top.append(aa)
            top_oqmd.append(bb)
            B.append(bbb)
            
oqmd_top = pd.DataFrame(oqmd_top)
top_oqmd = pd.DataFrame(top_oqmd)
B = pd.DataFrame(B)

for k in range (len(oqmd_top)):
    if elmd(oqmd_top.iloc[k,0],top_oqmd.iloc[k,0])<2:
        
        c = oqmd_top.iloc[k,0],top_oqmd.iloc[k,0],B.iloc[k,0],elmd(oqmd_top.iloc[k,0],top_oqmd.iloc[k,0])
        A.append(c)
        
        
A = pd.DataFrame(A)
C = []

for l in range(len(A)):
    check_number = A.iloc[l,0],A.iloc[l,1]
    numbers_oqmd = re.findall(r'\d+',A.iloc[l,0])
    numbers_top = re.findall(r'\d+',A.iloc[l,1])
    if numbers_oqmd == numbers_top:
        gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2],A.iloc[l,3]
        C.append(gogo)
    else:
        pd_numbers_oqmd = pd.DataFrame(numbers_oqmd)
        pd_numbers_top = pd.DataFrame(numbers_top)
        gaza = pd_numbers_oqmd.apply(pd.to_numeric).sum()
        gaboza = pd_numbers_top.apply(pd.to_numeric).sum()
        plz = pd.DataFrame(gaza%gaboza)
        if plz.loc[0,0] == 0 :
            gogo = A.iloc[l,0],A.iloc[l,1],A.iloc[l,2]
            C.append(gogo)

pd.DataFrame(C)
C = pd.DataFrame(C)
C
C.to_csv("top_down_oqmd_2_True.csv", index=False)        


# In[28]:


BU_OQMD = pd.read_csv("bottom_up_oqmd_2_True.csv")
BU_MP = pd.read_csv("bottom_up_MP_2_True.csv")
BU_ICSD = pd.read_csv("bottom_up_icsd_2_True.csv")

TD_OQMD = pd.read_csv("top_down_oqmd_2_True.csv")
TD_MP = pd.read_csv("top_down_MP_2_True.csv")
TD_ICSD = pd.read_csv("top_dowm_icsd_2_True.csv")

BU_OQMD['ElMD']=0
BU_MP['ElMD']=0
BU_ICSD['ElMD']=0

BU_MP['ElMD']=0
BU_OQMD['ElMD']=0
BU_ICSD['ElMD']=0


# In[30]:


A=[]

for i in range(len(BU_OQMD)):
    elmd_oqmd = elmd(BU_OQMD.iloc[i,0],BU_OQMD.iloc[i,1])
    
    A.append(elmd_oqmd)
    
    
BU_OQMD['ElMD']=A


A=[]

for i in range(len(BU_MP)):
    elmd_mp = elmd(BU_MP.iloc[i,0],BU_MP.iloc[i,1])
    
    A.append(elmd_mp)
    
    
BU_MP['ElMD']=A


A=[]

for i in range(len(BU_ICSD)):
    elmd_icsd = elmd(BU_ICSD.iloc[i,0],BU_ICSD.iloc[i,1])
    
    A.append(elmd_icsd)
    
    
BU_ICSD['ElMD']=A

A=[]

for i in range(len(TD_OQMD)):
    elmd_oqmd = elmd(TD_OQMD.iloc[i,0],TD_OQMD.iloc[i,1])
    
    A.append(elmd_oqmd)
    
    
TD_OQMD['ElMD']=A


A=[]

for i in range(len(TD_MP)):
    elmd_mp = elmd(TD_MP.iloc[i,0],TD_MP.iloc[i,1])
    
    A.append(elmd_mp)
    
    
TD_MP['ElMD']=A


A=[]

for i in range(len(TD_ICSD)):
    elmd_icsd = elmd(TD_ICSD.iloc[i,0],TD_ICSD.iloc[i,1])
    
    A.append(elmd_icsd)
    
    
TD_ICSD['ElMD']=A


# In[38]:


BU_OQMD.to_csv("BU_OQMD_ElMD.csv")
BU_MP.to_csv("BU_MP_ElMD.csv")
BU_ICSD.to_csv("BU_ICSD_ElMD.csv")

TD_OQMD.to_csv("TD_OQMD_ElMD.csv")
TD_MP.to_csv("TD_MP_ElMD.csv")
TD_ICSD.to_csv("TD_ICSD_ElMD.csv")

