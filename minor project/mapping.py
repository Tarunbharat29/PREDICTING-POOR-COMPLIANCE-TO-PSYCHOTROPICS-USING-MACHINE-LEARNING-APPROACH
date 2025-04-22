#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np;
import pandas as pd;
import seaborn as sns;
import matplotlip as plt;
from sklearn.preprocessing import LabelEncoder


# In[2]:


import numpy as np;
import pandas as pd;
import seaborn as sns;
import matplotlip as plt;
from sklearn.preprocessing import LabelEncoder


# In[3]:


df = pd.read_excel('/home/tarun/Documents/minor project/Combine data.xlsx')


# In[4]:


sns.heatmap(df.isnull())


# In[5]:


# Calculate the percentage of null values in each column
null_percentage = df.isnull().mean() * 100

# Filter columns with more than 20% null values
columns_with_high_nulls = null_percentage[null_percentage > 20]

print("Columns with more than 20% null values and their percentages:")
print(columns_with_high_nulls)


# In[6]:


df.shape


# # ????
# 
# 

# In[7]:


df.replace('nil',0,inplace = True)
df.replace('Nil',0,inplace = True)
df.replace('Nil ',0,inplace = True)
df.replace('NIl',0,inplace = True)


# In[8]:


df


# In[9]:


df.to_csv('dataset.csv', index=False)


# In[10]:


df = pd.read_csv('/home/tarun/Documents/minor project/dataset.csv')


# In[11]:


df


# In[12]:


df.dtypes


# In[13]:


df['Cluster_1_date'] = pd.to_datetime(df['Cluster_1_date'] , format = 'mixed')


# In[14]:


df.dtypes


# In[15]:


df['Cluster_1_date'] = pd.to_datetime(df['Cluster_1_date'])


# In[16]:


df['Date of screening'].isnull().sum()


# In[17]:


df['Date of screening'].isnull().sum()


# In[18]:


df['Date of screening'] = pd.to_datetime(df['Date of screening'])


# In[19]:


df.dtypes


# In[20]:


df['Age at presentation (in yrs)'].isnull().sum()


# In[21]:


df['Age at last follow up'].isnull().sum()


# In[22]:


df['Sex (m/f)'].isnull().sum()


# In[23]:


df['Sex (m/f)'].unique()


# In[24]:


df['Sex (m/f)'].replace(' male','male',inplace= True)


# In[25]:


df['Sex (m/f)'].unique()


# ## label the featue 'Sex (m/f)'
# label the Male : 1 and female : 0

# In[26]:


df['Sex (m/f)'] = df['Sex (m/f)'].map({'male': 1, 'female': 0})


# In[27]:


df


# In[28]:


df['Religion'].unique()


# In[29]:


df['Religion'].replace('hinduism','Hinduism',inplace = True)


# In[30]:


df['Religion'].unique()


# ## label the fature 'Religion'
# ##This will convert the Religion" column into numerical values:
# 
# Hindu → 1
# Muslim → 2
# Christian → 3
# 

# In[31]:


df['Religion'] = df['Religion'].map({'Hinduism': 1, 'Christianity': 3,'Islam' : 2})


# In[32]:


df


# In[33]:


df['Religion'].isnull().sum()


# In[34]:


df['Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)'].isnull().sum()


# In[35]:


df['Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)'].unique()


# In[36]:


df['Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)'].replace('Primary','primary',inplace = True)


# In[37]:


df['Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)'].replace('play school/preprimary','Pre primary/play school',inplace = True)


# In[38]:


df['Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)'].unique()


# In[39]:


df['Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)']


# ## label the Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)
# ##Pre primary/play school' : 1,'primary' : 2,'high school' :3,'higher secondary' :4,'others' :5,'no formal education' : 0 

# In[40]:


df['Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)'] = df['Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)'].map({'Pre primary/play school' : 1,'primary' : 2,'high school' :3,'higher secondary' :4,'others' :5,'no formal education' : 0 })


# In[41]:


df['Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)'].isnull().sum()


# In[42]:


df['Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)'].unique()


# In[43]:


df.dtypes


# In[44]:


df['Education at presentation (Primary 1 to 5, High school 6-10, higher secondary 11 and 12)'].unique()


# In[45]:


df


# In[46]:


df['Max education attained'].unique()


# In[47]:


df['Max education attained'].replace('Primary','primary',inplace = True)


# In[48]:


df['Max education attained'].unique()


# In[49]:


df['Max education attained'].replace('graduation','others',inplace = True)


# In[50]:


df['Max education attained'].isnull().sum()


# ## label the feature 'Max education attained'
# ### 'Pre primary/playschool' : 1,'primary' : 2,'high school' :3,'higher secondary' :4,'others' :5,'no formal education' : 0 

# In[51]:


df['Max education attained'] = df['Max education attained'].map({'Pre primary/playschool' : 1,'primary' : 2,'high school' :3,'higher secondary' :4,'others' :5,'no formal education' : 0 })


# In[52]:


df['Max education attained'].isnull().sum()


# In[53]:


df['Max education attained'].unique()


# In[54]:


df


# ## label the feature "Rural/Urban"
# 
# ### rural' :1,'urban' : 2

# In[55]:


df['Rural/Urban'].unique()


# In[56]:


df['Rural/Urban'].replace('Rural','rural',inplace = True)


# In[57]:


df['Rural/Urban'].replace('Urban','urban',inplace = True)


# In[58]:


df['Rural/Urban'].unique()


# In[59]:


df['Rural/Urban'].isnull().sum()


# In[60]:


#df['Rural/Urban'].fillna(method = 'ffill',inplace = True)


# In[61]:


df['Rural/Urban'].isnull().sum()


# In[62]:


df['Rural/Urban'] = df['Rural/Urban'].map({'rural' :1,'urban' : 2})


# In[63]:


df['Rural/Urban'].unique()


# In[64]:


df


# In[65]:


df['Distance from LGBRIMH (in KM)'].isnull().sum()


# In[66]:


#avg = df['Distance from LGBRIMH (in KM)'].mean()
#df['Distance from LGBRIMH (in KM)'] = df['Distance from LGBRIMH (in KM)'].fillna(avg)


# In[67]:


df['Distance from LGBRIMH (in KM)'].isnull().sum()


# ## Socioeconomic status
# 
# ### 'LSES' : 1,'MSES' : 2, 'HSES' : 3
# 
# 
# Socioeconomic Status (SES) in the medical field refers to a person's or a family's social and economic position in relation to others. It is an important factor because it can influence health outcomes and access to healthcare
# 
# 1. LSES: Low Socioeconomic Status
# 2. MSES :Middle Socioeconomic Status
# 3. HSES: High Socioeconomic Status
# 

# In[68]:


df['Socioeconomic status'].isnull().sum()


# In[69]:


df['Socioeconomic status'].unique()


# In[70]:


df['Socioeconomic status'] = df['Socioeconomic status'].map({'LSES' : 1,'MSES' : 2, 'HSES' : 3})


# In[71]:


df['Socioeconomic status'].isnull().sum()


# In[72]:


df['Socioeconomic status'].dtypes


# In[73]:


df['Socioeconomic status']


# # Referral feature
# 

# In[74]:


df['Referral'].unique()


# In[75]:


df['Referral'].isnull().sum()


# # Brought by
# 
# ## 'Mother' : 1,'Father' : 2 , 'Both parents' : 3 , 'Relatives' : 4 , 'Others' : 5

# In[76]:


df['Brought by'].unique()


# In[77]:


df['Brought by'].dtypes


# In[78]:


df['Brought by'].isnull().sum()


# In[79]:


df['Brought by'] = df['Brought by'].map({'Mother' : 1,'Father' : 2 , 'Both parents' : 3 , 'Relatives' : 4 , 'Others' : 5 })


# In[80]:


df['Brought by'].isnull().sum()


# In[81]:


df['Brought by'].dtypes


# # Age at onset(in years)

# In[82]:


df['Age at onset(in years)'].dtypes


# In[83]:


df['Age at onset(in years)'].isnull().sum()


# In[84]:


#avg = df['Age at onset(in years)'].mean()
#df['Age at onset(in years)'] = df['Age at onset(in years)'].fillna(avg)


# In[85]:


df['Age at onset(in years)'].isnull().sum()


# In[86]:


df['Age at onset(in years)'].dtypes


# In[87]:


df


# # Chief complaint 1
# 

# In[88]:


df['Chief complaint 1'].unique()


# # Chief complaint 3

# In[89]:


df['Chief complaint 2'].unique()


# # Chief complaint 2

# In[90]:


df['Chief complaint 3'].unique()


# # Occupation of parents

# In[91]:


df['Occupation of parents'].unique()


# # Time period between onset to first consultation at LGBRIMH (DUI) (in days)

# In[92]:


df['Time period between onset to first consultation at LGBRIMH (DUI) (in days)'].isnull().sum()


# In[93]:


##df['Time period between onset to first consultation at LGBRIMH (DUI) (in days)'].fillna(method='ffill', inplace=True)


# In[94]:


df['Time period between onset to first consultation at LGBRIMH (DUI) (in days)'].isnull().sum()


# # Type of Family (Nuclear/Joint/single parent/orphan/ foster family
# 
# ### Joint':1,'Nuclear' : 2,'Single parent' : 3,'Foster family' : 4

# In[95]:


df['Type of Family (Nuclear/Joint/single parent/orphan/ foster family'].unique()


# In[96]:


df['Type of Family (Nuclear/Joint/single parent/orphan/ foster family'].isnull().sum()


# In[97]:


df['Type of Family (Nuclear/Joint/single parent/orphan/ foster family'].replace('joint','Joint',inplace = True)


# In[98]:


df['Type of Family (Nuclear/Joint/single parent/orphan/ foster family'].unique()


# In[99]:


df['Type of Family (Nuclear/Joint/single parent/orphan/ foster family'] = df['Type of Family (Nuclear/Joint/single parent/orphan/ foster family'].map({'Joint':1,'Nuclear' : 2,'Single parent' : 3,'Foster family' : 4})


# In[100]:


df['Type of Family (Nuclear/Joint/single parent/orphan/ foster family'].isnull().sum()


# # Family environment
# 
# ### 'Atypical':1 , 'Typical' :2

# In[101]:


df['Family environment'].unique()


# In[102]:


df['Family environment'].isnull().sum()


# In[103]:


df['Family environment'] = df['Family environment'].map({'Atypical':1 , 'Typical' :2})


# In[104]:


df['Family environment'].dtypes


# # Details of family abnormality (describe)

# In[105]:


df['Details of family abnormality (describe)'].unique()


# In[106]:


df['Details of family abnormality (describe)'].isnull().sum()


# # Family h/o stillbirth/abortion
# 
# ### 'No' : 0, 'Yes' : 1

# In[107]:


df['Family h/o stillbirth/abortion'].unique()


# In[108]:


df['Family h/o stillbirth/abortion'].isnull().sum()


# In[109]:


df['Family h/o stillbirth/abortion'] = df['Family h/o stillbirth/abortion'].map({'No' : 0, 'Yes' : 1})


# In[110]:


df['Family h/o stillbirth/abortion'].isnull().sum()


# # Family history(general medical)
# 
# ### Not present' : 0, 'First degree relative' : 1, 'Second degree relative' : 2,'Third degree relative' : 3, 'Multiple generations' : 4

# In[111]:


df['Family history(general medical)'].unique()


# In[112]:


df['Family history(general medical)'].isnull().sum()


# In[113]:


df['Family history(general medical)'] = df['Family history(general medical)'].map({'Not present' : 0, 'First degree relative' : 1, 'Second degree relative' : 2,'Third degree relative' : 3, 'Multiple generations' : 4})


# In[114]:


df['Family history(general medical)'].isnull().sum()


# # Family history (psychiatric/neurological)
# 
#  ### 'Not present' : 0, 'First degree relative' :1, 'Second degree relative': 2, 'Third degree relative' : 3, 'Multiple generations' : 4

# In[115]:


df['Family history (psychiatric/neurological)'].unique()


# In[116]:


df['Family history (psychiatric/neurological)'].isnull().sum()


# In[117]:


df['Family history (psychiatric/neurological)'] = df['Family history (psychiatric/neurological)'].map({'Not present' : 0, 'First degree relative' :1, 'Second degree relative': 2, 'Third degree relative' : 3, 'Multiple generations' : 4})


# In[118]:


df['Family history (psychiatric/neurological)'].isnull().sum()


# # Faith healer visited before consultation or not(yes/no)
# 
# ### 'yes' : 1,'no' : 0

# In[119]:


df['Faith healer visited before consultation or not(yes/no)'].isnull().sum()


# In[120]:


df['Faith healer visited before consultation or not(yes/no)'].unique()


# In[121]:


df['Faith healer visited before consultation or not(yes/no)'] = df['Faith healer visited before consultation or not(yes/no)'].map({'yes' : 1,'no' : 0})


# In[122]:


df['Faith healer visited before consultation or not(yes/no)'].isnull().sum()


# # Antenatal risk factor
# 
# ### 'No' : 0,'Yes' : 1}

# In[123]:


df['Antenatal risk factor'].isnull().sum()


# In[124]:


df['Antenatal risk factor'].unique()


# In[125]:


df['Antenatal risk factor'].replace('no' , 'No',inplace = True)


# In[126]:


df['Antenatal risk factor'].unique()


# In[127]:


df['Antenatal risk factor'] = df['Antenatal risk factor'].map({'No' : 0,'Yes' : 1})


# In[128]:


df['Antenatal risk factor'].isnull().sum()


# # Place of delivery (Home/hospital)
# 
# ### 'Home': 1,'Hospital' : 2,'Other' : 3

# In[129]:


df['Place of delivery (Home/hospital)'].isnull().sum()


# In[130]:


df['Place of delivery (Home/hospital)'].unique()


# In[131]:


df['Place of delivery (Home/hospital)'].replace('hospital', 'Hospital', inplace = True)


# In[132]:


df['Place of delivery (Home/hospital)'].unique()


# In[133]:


df['Place of delivery (Home/hospital)'] = df['Place of delivery (Home/hospital)'].map({'Home': 1,'Hospital' : 2,'Other' : 3})


# In[134]:


df['Place of delivery (Home/hospital)'].unique()


# In[135]:


df['Place of delivery (Home/hospital)'].isnull().sum()


# # Birth weight(in kg)

# In[136]:


df['Birth weight(in kg)'].isnull().sum()


# In[137]:


df['Birth weight(in kg)'].dtypes


# In[138]:


df['Birth weight(in kg)'].replace('normal',2.5,inplace =True)


# In[139]:


df['Birth weight(in kg)'].unique()


# In[140]:


df['Birth weight(in kg)'].replace('No',2.5,inplace =True)


# # Neonatal complication
# 
# ### 'No' : 0,'yes' :1

# In[141]:


df['Neonatal complication'].isnull().sum()


# In[142]:


df['Neonatal complication'].unique()


# In[143]:


df['Neonatal complication'].replace('no','No', inplace = True )


# In[144]:


df['Neonatal complication'].unique()


# In[145]:


df['Neonatal complication'] = df['Neonatal complication'].map({'No' : 0,'yes' :1})


# In[146]:


df['Neonatal complication'].isnull().sum()


# In[147]:


df['Neonatal complication'].dtypes


# # Postnatal complication
# 
# ### 'No' : 0,'Yes' :1

# In[148]:


df['Postnatal complication'].unique()


# In[149]:


df['Postnatal complication'].replace('no','No', inplace = True)


# In[150]:


df['Postnatal complication'].unique()


# In[151]:


df['Postnatal complication'].isnull().sum()


# In[152]:


df['Postnatal complication'] = df['Postnatal complication'].map({'No' : 0,'Yes' :1})


# In[153]:


df['Postnatal complication'].isnull().sum()


# In[154]:


df['Postnatal complication'].unique()


# # Developmental history
# 
# ### 'Global delay' : 1,'Speech and language delay' : 2, 'Normal' : 3, 'Socioemotional delay' : 4, 'Cognitive delay' : 5, 'Motor delay' : 6

# In[155]:


df['Developmental history'].unique()


# In[156]:


df['Developmental history'].isnull().sum()


# In[157]:


df['Developmental history'] = df['Developmental history'].map({'Global delay' : 1,'Speech and language delay' : 2, 'Normal' : 3, 'Socioemotional delay' : 4, 'Cognitive delay' : 5, 'Motor delay' : 6})


# In[158]:


df['Developmental history'].isnull().sum()


# In[159]:


df['Developmental history'].unique()


# # Age of school entry(in years)

# In[160]:


df['Age of school entry(in years)'].isnull().sum()


# # Type of school
# 
# ### 'Nil':0,'Regular':1,'Playschool' : 2, 'Religious' :3,'Special' : 4}

# In[161]:


df['Type of school'].isnull().sum()


# In[162]:


df['Type of school'].unique()


# In[163]:


df['Type of school'].replace('regular','Regular',inplace = True)


# In[164]:


df['Type of school'].replace('Regular ','Regular',inplace = True)


# In[165]:


df['Type of school'].unique()


# In[166]:


df['Type of school'] = df['Type of school'].map({'Nil':0,'Regular':1,'Playschool' : 2, 'Religious' :3,'Special' : 4})


# In[167]:


df['Type of school'].unique()


# In[168]:


df['Type of school'].isnull().sum()


# # School adjustment
# 
# ###  'poorly adjusted' : 1,'well adjusted' : 2,'Nil' : 0}

# In[169]:


df['School adjustment'].unique()


# In[170]:


df['School adjustment'].isnull().sum()


# In[171]:


df['School adjustment'] = df['School adjustment'].map({'poorly adjusted' : 1,'well adjusted' : 2,'Nil' : 0})


# In[172]:


df['School adjustment'].isnull().sum()


# # Academic performance
# 
# ### 'Nil' : 0, 'poor' : 1, 'average' : 2,'Good': 3}

# In[173]:


df['Academic performance'].unique()


# In[174]:


df['Academic performance'].isnull().sum()


# In[175]:


df['Academic performance'].replace('poor ','poor',inplace = True)


# In[176]:


df['Academic performance'].unique()


# In[177]:


df['Academic performance'] = df['Academic performance'].replace({'Nil' : 0, 'poor' : 1, 'average' : 2,'Good': 3})


# In[178]:


df['Academic performance'].isnull().sum()


# In[179]:


df['Academic performance'].unique()


# # School dropout present (yes/no)
# 
# ### 'No': 0,'Yes' : 1

# In[180]:


df['School dropout present (yes/no)'].unique()


# In[181]:


df['School dropout present (yes/no)'].isnull().sum()


# In[182]:


df['School dropout present (yes/no)'].replace('yes','Yes',inplace = True)


# In[183]:


df['School dropout present (yes/no)'].replace('no','No',inplace = True)


# In[184]:


df['School dropout present (yes/no)'].unique()


# In[185]:


df['School dropout present (yes/no)'].map({'No': 0,'Yes' : 1})


# In[186]:


df['School dropout present (yes/no)'].isnull().sum()


# # Detail of past psychiatric history 1

# In[187]:


df['Detail of past psychiatric history 1'].unique()


# # Past treatment 1
# 
# ### 'Nil' : 0,'Never treated' : 1,'Pharmacotherapy only' : 2,'combination therapy' : 3,'Yes' : 4,'Non-pharmacological therapy' : 5

# In[188]:


df['Past treatment 1'].unique()


# In[189]:


df['Past treatment 1'].isnull().sum()


# In[190]:


#df['Past treatment 1'].fillna('Nil' ,inplace = True)


# In[191]:


df['Past treatment 1'].isnull().sum()


# In[192]:


df['Past treatment 1'] = df['Past treatment 1'].map({'Never treated' : 1,'0' : 0, 'Pharmacotherapy only' : 2,
       'combination therapy' : 3, 'Yes' : 4, 'Non-pharmacological therapy' : 5})


# In[193]:


df['Past treatment 1'].unique()


# In[194]:


df['Past treatment 1'].isnull().sum()


# In[195]:


#df['Past treatment 1'].fillna(0,inplace = True)


# In[196]:


df['Past treatment 1'].isnull().sum()


#  #  Past treatment medication 1

# In[197]:


df['Past treatment medication 1'].unique()


# # Starting dose past medication 1

# In[198]:


df['Starting dose past medication 1'].unique()


# In[199]:


df['Starting dose past medication 1'].isnull().sum()


# In[200]:


df['Starting dose past medication 1'].replace('40mg','40',inplace = True)


# In[201]:


df['Starting dose past medication 1'].unique()


# In[202]:


#df['Starting dose past medication 1'].fillna(method = 'ffill',inplace =True)


# In[203]:


df['Starting dose past medication 1'].isnull().sum()


# # Age of starting of past medication 1(in years)

# In[204]:


df['Age of starting of past medication 1(in years)'].isnull().sum()


# In[205]:


df['Age of starting of past medication 1(in years)'].replace('40mg','40',inplace = True)


# In[206]:


df['Age of starting of past medication 1(in years)'].isnull().sum()


# In[207]:


df['Age of starting of past medication 1(in years)'].unique()


# In[208]:


#df['Age of starting of past medication 1(in years)'].fillna(method = 'ffill',inplace = True)


# In[209]:


df.iloc[:,0:10]


# In[210]:


df.iloc[:,0:40]


# In[211]:


df['Age of starting of past medication 1(in years)'].replace('Nil ' ,0,inplace =True)


# In[212]:


df['Age of starting of past medication 1(in years)'].replace('Nil' ,0,inplace =True)


# In[213]:


df['Age of starting of past medication 1(in years)'].unique()


# In[214]:


df['Age of starting of past medication 1(in years)'] = df['Age of starting of past medication 1(in years)'].astype(float)


# # Past maintenance dose1 (in mg)

# In[215]:


df['Age of starting of past medication 1(in years)'].dtypes


# In[216]:


df['Past maintenance dose1 (in mg)'].isnull().sum()


# In[217]:


#df['Past maintenance dose1 (in mg)']= df['Past maintenance dose1 (in mg)'].fillna(0)


# In[218]:


df['Past maintenance dose1 (in mg)'].isnull().sum()


# # downlod the enrire dataset 

# In[219]:


##df.to_csv('your_dataframe.csv', index=False)


# In[220]:


import os

# Get current working directory
current_location = os.getcwd()
print("Current Location:", current_location)


# In[221]:


df.dtypes


# In[222]:


df.isnull().sum()


# In[223]:


df.info()


# In[224]:


# Get the names of columns with object data types
object_column_names = df.select_dtypes(include=['object']).columns.tolist()
print(object_column_names)


# # Side effects of past medication 1
# 
# ### 'weight gain, menstrual irregularities' : 1, nil : 0

# In[225]:


df['Side effects of past medication 1'].dtypes


# In[226]:


df['Side effects of past medication 1'].unique()


# In[227]:


df['Side effects of past medication 1'].isnull().sum()


# In[228]:


#df['Side effects of past medication 1'].fillna(method = 'ffill' , inplace = True)


# In[229]:


df['Side effects of past medication 1'].isnull().sum()


# In[230]:


df['Side effects of past medication 1'].dtypes


# In[231]:


df['Side effects of past medication 1'] = df['Side effects of past medication 1'].map({'0': 0, 'weight gain, menstrual irregularities' : 1}) 


# In[232]:


df['Side effects of past medication 1'].isnull().sum()


# In[233]:


df['Side effects of past medication 1'].unique()


# # Age of occurance past side effects 1(in years)

# In[234]:


df['Age of occurance past side effects 1(in years)'].dtypes


# In[235]:


df['Age of occurance past side effects 1(in years)'].unique()


# In[236]:


df['Age of occurance past side effects 1(in years)'].replace('10',10, inplace = True)


# In[237]:


df['Age of occurance past side effects 1(in years)'].unique()


# In[238]:


df['Age of occurance past side effects 1(in years)'].dtypes


# # Duration of past side effect 1(in months)

# In[239]:


df['Duration of past side effect 1(in months)'].dtypes


# In[240]:


df['Duration of past side effect 1(in months)'].isnull().sum()


# In[241]:


avg = df['Duration of past side effect 1(in months)'].mean()


# In[242]:


#df['Duration of past side effect 1(in months)'].fillna(avg,inplace = True)


# In[243]:


df['Duration of past side effect 1(in months)'].isnull().sum()


# # Response to past medication 1
# 
# ### 'NIL' : 0,'Good' : 1,'Partial' : 2,'Poor' : 3,'No' :4

# In[244]:


df['Response to past medication 1'].dtypes


# In[245]:


df['Response to past medication 1'].unique()


# In[246]:


df['Response to past medication 1'].replace('partial','Partial',inplace = True)


# In[247]:


df['Response to past medication 1'].unique()


# In[248]:


df['Response to past medication 1'].replace('0','NIL',inplace = True)


# In[249]:


df['Response to past medication 1'].unique()


# In[250]:


df['Response to past medication 1'] = df['Response to past medication 1'].map({'NIL' : 0,'Good' : 1,'Partial' : 2,'Poor' : 3,'No' :4})


# In[251]:


df['Response to past medication 1'].unique()


# In[252]:


df['Response to past medication 1'].isnull().sum()


# In[253]:


#df['Response to past medication 1'].fillna(0,inplace = True)


# In[254]:


df['Response to past medication 1'].isnull().sum()


# In[255]:


df['Response to past medication 1'].dtypes


# # Detail of past history 2
# 
# ### 'Seizures not controlled with Clobazam':1,'Current condition' : 2,'Current illness' : 3,'Post traumatic stress disorder' : 4,'depressive disorder' : 5,'Treated at NIMHANS for current issue' : 6,'ATPD' : 7,'Current Condition' : 8, 'Jaundice' : 9, 'Fever and fits' :10}

# In[256]:


df['Detail of past history 2'].dtypes


# In[257]:


df['Detail of past history 2'].unique()


# In[258]:


df['Detail of past history 2'].isnull().sum()


# In[259]:


#df['Detail of past history 2'].fillna(0,inplace = True)


# In[260]:


df['Detail of past history 2'].isnull().sum()


# In[261]:


df['Detail of past history 2'] = df['Detail of past history 2'].map({'0': 0,'Seizures not controlled with Clobazam':1,'Current condition' : 2,'Current illness' : 3,'Post traumatic stress disorder' : 4,'depressive disorder' : 5,'Treated at NIMHANS for current issue' : 6,'ATPD' : 7,'Current Condition' : 8, 'Jaundice' : 9, 'Fever and fits' :10})


# In[262]:


df['Detail of past history 2'].unique()


# In[263]:


df['Detail of past history 2'].dtypes


# # Past treatment 2
# 
# ### '0' : 0,'Pharmacotherapy only' : 1,'Combination therapy' : 2

# In[264]:


df['Past treatment 2'].dtypes


# In[265]:


df['Past treatment 2'].unique()


# In[266]:


df['Past treatment 2'].isnull().sum()


# In[267]:


#df['Past treatment 2'].fillna(0,inplace = True)


# In[268]:


df['Past treatment 2'].isnull().sum()


# In[269]:


df['Past treatment 2'] = df['Past treatment 2'].map({'0' : 0,'Pharmacotherapy only' : 1,'Combination therapy' : 2})


# In[270]:


#df['Past treatment 2'].fillna(0,inplace = True)


# In[271]:


df['Past treatment 2'].isnull().sum()


# In[272]:


df['Past treatment 2'].dtypes


# # Past treatment medication 2
# 
# ### 'sodium valproate' : 1,'lorazepam' : 2, 'Levetiracetam' :3,'Paroxetine' : 4, 'Sodium Valproate' : 5, 'Escitalopram' : 6, 'Lorazepam' : 7,'Methylphenidate' :8, 'Clonazepam' : 9, 'Risperidone' : 10, 'Lithium' : 11,'Sodium valproate' : 12, 'Piracetam' : 13, 'piracetam' : 14, 'Resperidone' : 15,'Trihexyphenidyl' : 16, 'Divalproex' : 17, 'Folic acid' : 18, 'Phenobarbitone' : 19

# In[273]:


df['Past treatment medication 2'].dtypes


# In[274]:


df['Past treatment medication 2'].unique()


# In[275]:


df['Past treatment medication 2'] = df['Past treatment medication 2'].map({'0' :0, 'sodium valproate' : 1,'lorazepam' : 2, 'Levetiracetam' :3,
      'Paroxetine' : 4, 'Sodium Valproate' : 5, 'Escitalopram' : 6, 'Lorazepam' : 7,
      'Methylphenidate' :8, 'Clonazepam' : 9, 'Risperidone' : 10, 'Lithium' : 11,
      'Sodium valproate' : 12, 'Piracetam' : 13, 'piracetam' : 14, 'Resperidone' : 15,
      'Trihexyphenidyl' : 16, 'Divalproex' : 17, 'Folic acid' : 18, 'Phenobarbitone' : 19})


# In[276]:


df['Past treatment medication 2'].unique()


# In[277]:


df['Past treatment medication 2'].isnull().sum()


# In[278]:


#df['Past treatment medication 2'].fillna(0,inplace = True)


# In[279]:


df['Past treatment medication 2'].isnull().sum()


# In[280]:


df['Past treatment medication 2'].dtypes


# # Starting dose past medication 2

# In[281]:


df['Starting dose past medication 2'].dtypes


# In[282]:


df['Starting dose past medication 2'].isnull().sum()


# In[283]:


#df['Starting dose past medication 2'].fillna(0,inplace = True)


# In[284]:


df['Starting dose past medication 2'].isnull().sum()


# # Age of starting of past medication 2(in years)

# In[285]:


df['Age of starting of past medication 2(in years)'].dtypes


# In[286]:


df['Age of starting of past medication 2(in years)'].isnull().sum()


# In[287]:


#df['Age of starting of past medication 2(in years)'].fillna(0,inplace = True)


# In[288]:


df['Age of starting of past medication 2(in years)'].isnull().sum()


# # Past maintenance dose2

# In[289]:


df['Past maintenance dose2'].dtypes


# In[290]:


df['Past maintenance dose2'].isnull().sum()


# In[291]:


#df['Past maintenance dose2'].fillna(0,inplace = True)


# In[292]:


df['Past maintenance dose2'].isnull().sum()


# # Side effects of past medication 2
# 
# ### 'no':0,'yes':1,'0' : 0

# In[293]:


df['Side effects of past medication 2'].dtypes


# In[294]:


df['Side effects of past medication 2'].unique()


# In[295]:


df['Side effects of past medication 2'] =df['Side effects of past medication 2'].map({'no':0,'yes':1,'0' : 0})


# In[296]:


df['Side effects of past medication 2'].unique()


# In[297]:


df['Side effects of past medication 2'].isnull().sum()


# In[298]:


#df['Side effects of past medication 2'].fillna(0,inplace = True)


# In[299]:


df['Side effects of past medication 2'].isnull().sum()


# # Age of occurance past side effects 2(in years)
# 
# ## we can drop this feature

# In[300]:


df['Age of occurance past side effects 2(in years)'].dtypes


# In[301]:


df['Age of occurance past side effects 2(in years)'].isnull().sum()


# In[302]:


df['Age of occurance past side effects 2(in years)'].unique()


# In[303]:


#df['Age of occurance past side effects 2(in years)'].fillna(0,inplace = True)


# In[304]:


df['Age of occurance past side effects 2(in years)'].isnull().sum()


# # Duration of past side effect 2(in months)
# 
# # We can drop this also

# In[305]:


df['Duration of past side effect 2(in months)'].dtypes


# In[306]:


df['Duration of past side effect 2(in months)'].unique()


# In[307]:


df['Duration of past side effect 2(in months)'].replace('Nli',0,inplace = True)


# In[308]:


df['Duration of past side effect 2(in months)'].isnull().sum()


# In[309]:


#df['Duration of past side effect 2(in months)'].fillna(0,inplace = True)


# In[310]:


df['Duration of past side effect 2(in months)'].isnull().sum()


# In[311]:


df['Duration of past side effect 2(in months)'].unique()


# # Response to past medication 2
# 
# 'No':0, 'Good' :1 , 'Partial' : 2

# In[312]:


df['Response to past medication 2'].dtypes


# In[313]:


df['Response to past medication 2'].unique()


# In[314]:


df['Response to past medication 2'] = df['Response to past medication 2'].map({'0':0, 'No':0, 'Good' :1 , 'Partial' : 2})


# In[315]:


df['Response to past medication 2'].unique()


# In[316]:


df['Response to past medication 2'].isnull().sum()


# In[317]:


#df['Response to past medication 2'].fillna(0,inplace = True)


# In[318]:


df['Response to past medication 2'].isnull().sum()


# In[319]:


df['Response to past medication 2'].dtypes


# # Detail of past history 3
# 
# ## 'Detail of past history 3'].map({'0' : 0, 'current illness' : 1, 'Specific phobia' :2,
#  ##      'Depressive disorder' : 3, 'Treated at NIMHANS for current issue' : 4, 
#    ##    'ATPD': 5, 'Current condition' :6, 'Feaver and fits' :7 

# In[320]:


df['Detail of past history 3'].dtypes


# In[321]:


df['Detail of past history 3'].unique()


# In[322]:


df['Detail of past history 3'] = df['Detail of past history 3'].map({'0' : 0, 'current illness' : 1, 'Specific phobia' :2,
       'Depressive disorder' : 3, 'Treated at NIMHANS for current issue' : 4, 
       'ATPD': 5, 'Current condition' :6, 'Feaver and fits' :7 })


# In[323]:


df['Detail of past history 3'].unique()


# In[324]:


df['Detail of past history 3'].isnull().sum()


# In[325]:


#df['Detail of past history 3'].fillna(0,inplace = True)


# In[326]:


df['Detail of past history 3'].dtypes


# # Past treatment  3
# 
# ### 'Past treatment  3'].map({'0' : 0,'Combination therapy' : 1, 'Pharmacological' : 2,
# ###    'Pharmacotherapy only ': 3

# In[327]:


df['Past treatment  3'].dtypes


# In[328]:


df['Past treatment  3'].unique()


# In[329]:


df['Past treatment  3'] = df['Past treatment  3'].map({'0' : 0,'Combination therapy' : 1, 'Pharmacological' : 2,
       'Pharmacotherapy only ': 3})


# In[330]:


df['Past treatment  3'].unique()


# In[331]:


df['Past treatment  3'].isnull().sum()


# In[332]:


#df['Past treatment  3'].fillna(0,inplace = True)


# In[333]:


df['Past treatment  3'].isnull().sum()


# In[334]:


df['Past treatment  3'].dtypes


# # Past treatment medication 3
# 
# ### 'Risperidone' : 1, 'Aripiprazole' : 2, 'Trihexyphenidyl' : 3,
# ###       'Olanzapine' : 4, 'Rabeprazole' : 4, 'Clozapine' : 5, 'Chlorpromazine' : 6,
# ###       'Resperidone' : 7, 'Evion' : 8

# In[335]:


df['Past treatment medication 3'].dtypes


# In[336]:


df['Past treatment medication 3'].unique()


# In[337]:


df['Past treatment medication 3']= df['Past treatment medication 3'].map({'0' : 0, 'Risperidone' : 1, 'Aripiprazole' : 2, 'Trihexyphenidyl' : 3,
       'Olanzapine' : 4, 'Rabeprazole' : 4, 'Clozapine' : 5, 'Chlorpromazine' : 6,
       'Resperidone' : 7, 'Evion' : 8})


# In[338]:


df['Past treatment medication 3'].unique()


# In[339]:


df['Past treatment medication 3'].isnull().sum()


# In[340]:


df['Past treatment medication 3'].dtypes


# # Starting dose past medication 3 

# In[341]:


df['Starting dose past medication 3 '].dtypes


# In[342]:


df['Starting dose past medication 3 '].isnull().sum()


# In[343]:


#df['Starting dose past medication 3 '].fillna(0 , inplace = True)


# In[344]:


df['Starting dose past medication 3 '].isnull().sum()


# # Age of starting past medication 3 (in years)
# 
# 
# ###

# In[345]:


df['Age of starting past medication 3 (in years)'].dtypes


# In[346]:


df['Age of starting past medication 3 (in years)'].isnull().sum()


# In[347]:


#df['Age of starting past medication 3 (in years)'].fillna(0,inplace = True)


# In[348]:


df['Age of starting past medication 3 (in years)'].isnull().sum()


# In[349]:


df['Age of starting past medication 3 (in years)'].unique()


# # Past maintenance dose 3

# In[350]:


df['Past maintenance dose 3'].dtypes


# In[351]:


df['Past maintenance dose 3'].isnull().sum()


# In[352]:


#df['Past maintenance dose 3'].fillna(0,inplace = True)


# In[353]:


df['Past maintenance dose 3'].isnull().sum()


# In[354]:


df['Past maintenance dose 3'].unique()


# #  Side effects past medication 3
# 
# ## we can drop this feature

# In[355]:


df['Side effects past medication 3'].dtypes


# In[356]:


df['Side effects past medication 3'].isnull().sum()


# In[357]:


#df['Side effects past medication 3'].fillna(0,inplace = True)


# In[358]:


df['Side effects past medication 3'].isnull().sum()


# In[359]:


df['Side effects past medication 3'].unique()


# # Age of occurance of past side effects 3 (in years)
# 
# ## we can drop this feature also

# In[360]:


df['Age of occurance of past side effects 3 (in years)'].dtypes


# In[361]:


df['Age of occurance of past side effects 3 (in years)'].isnull().sum()


# In[362]:


#df['Age of occurance of past side effects 3 (in years)'].fillna(0,inplace = True)


# In[363]:


df['Age of occurance of past side effects 3 (in years)'].unique()


# In[364]:


df['Age of occurance of past side effects 3 (in years)'].isnull().sum()


# # Duration of past side effects 3 (in months)
# 
# ### we can drop this

# In[365]:


df['Duration of past side effects 3 (in months)'].dtypes


# In[366]:


df['Duration of past side effects 3 (in months)'].isnull().sum()


# In[367]:


df['Duration of past side effects 3 (in months)'].unique()


# In[368]:


#df['Duration of past side effects 3 (in months)'].fillna(0,inplace = True)


# In[369]:


df['Duration of past side effects 3 (in months)'].isnull().sum()


# # Response to past medication 3

# In[370]:


df['Response to past medication 3'].dtypes


# In[371]:


df['Response to past medication 3'].unique()


# In[372]:


df['Response to past medication 3'].replace('nIL',0,inplace = True)


# In[373]:


df['Response to past medication 3'].unique()


# In[374]:


df['Response to past medication 3'].replace('n',0,inplace = True)


# In[375]:


df['Response to past medication 3'].unique()


# In[376]:


df['Response to past medication 3'].isnull().sum()


# In[377]:


#df['Response to past medication 3'].fillna(0,inplace = True )


# In[378]:


df['Response to past medication 3'].isnull().sum()


# In[379]:


df['Response to past medication 3'].unique()


# In[380]:


df['Response to past medication 3'] = df['Response to past medication 3'].map({'Partial' : 2, 'Good' : 1})


# In[381]:


df['Response to past medication 3'].unique()


# In[382]:


#df['Response to past medication 3'].fillna(0,inplace = True)


# In[383]:


df['Response to past medication 3'].isnull().sum()


# In[384]:


df['Response to past medication 3'].dtypes


# # Change in doctor
# 
# ### 'No' : 2, 'Yes (single)' : 1, 'Yes(multiple)' : 3, ' 'Yes(single)' : 1 nil : 0

# In[385]:


df['Change in doctor'].dtypes


# In[386]:


df['Change in doctor'].unique()


# In[387]:


df['Change in doctor'].isnull().sum()


# In[388]:


df['Change in doctor'] = df['Change in doctor'].map({'No' : 2, 'Yes (single)' : 1, 'Yes(multiple)' : 3, '0' : 0, 'Yes(single)' : 1})


# In[389]:


df['Change in doctor'].unique()


# In[390]:


df['Change in doctor'].isnull().sum()


# In[391]:


# df['Change in doctor'].fillna(0,inplace = True)


# In[392]:


df['Change in doctor'].isnull().sum()


# # Past/Current medical conditions

# In[393]:


df['Past/Current medical conditions'].dtypes


# In[394]:


df['Past/Current medical conditions'].unique()


# In[395]:


df['Past/Current medical conditions'].isnull().sum()


# In[396]:


df['Past/Current medical conditions'] = df['Past/Current medical conditions'].map({'yes' : 1,'No' : 2,'Nil': 0,'0' : 0})


# In[397]:


df['Past/Current medical conditions'].unique()


# In[398]:


df['Past/Current medical conditions'].isnull().sum()


# In[399]:


df['Past/Current medical conditions'].dtypes


# # Age of onset of medical conditions (in years)

# In[400]:


df['Age of onset of medical conditions (in years)'].dtypes


# In[401]:


df['Age of onset of medical conditions (in years)'].unique()


# In[402]:


df['Age of onset of medical conditions (in years)'].replace('Yes',0,inplace = True)


# In[403]:


df['Age of onset of medical conditions (in years)'].replace('No',0,inplace = True)


# In[404]:


df['Age of onset of medical conditions (in years)'].unique()


# In[405]:


df['Age of onset of medical conditions (in years)'].replace('0',np.nan,inplace = True)


# In[406]:


df['Age of onset of medical conditions (in years)'].isnull().sum()


# # Details of medical conditions

# In[407]:


df['Details of medical conditions'].dtypes


# In[408]:


df['Details of medical conditions'].unique()


# In[409]:


df['Details of medical conditions'].isnull().sum()


# # Treatments for medical conditions
# 
# 
# ### 'never treated' : 1, 'NIL' : 1, 'injection insulin' : 2, 'CECT Brain done' : 3,
# ###       'Medications' : 4, 'Yes' : 5, 'No' : 6, 'yes' : 5, 'Tab- Resperidone' : 7,
# ###       'Syp Gardenal 2ml BD' : 8, 'INJ. Diazepam & phenobarbitone 30 mg' : 9})

# In[410]:


df['Treatments for medical conditions'].dtypes


# In[411]:


df['Treatments for medical conditions'].unique()


# In[412]:


df['Treatments for medical conditions'].isnull().sum()


# In[413]:


df['Treatments for medical conditions'] = df['Treatments for medical conditions'].map({'never treated' : 1, '0' : 0, 'injection insulin' : 2, 'CECT Brain done' : 3,
       'Medications' : 4, 'Yes' : 5, 'No' : 6, 'yes' : 5, 'Tab- Resperidone' : 7,
       'Syp Gardenal 2ml BD' : 8, 'INJ. Diazepam & phenobarbitone 30 mg' : 9})


# In[414]:


df['Treatments for medical conditions'].isnull().sum()


# In[415]:


df['Treatments for medical conditions'].unique()


#  # Severity of medical conditions
# 
# ### 'Severe' : 1,'Mild' : 2,'Moderate' : 3, 'nil' : 0}

# In[416]:


df['Severity of medical conditions'].dtypes


# In[417]:


df['Severity of medical conditions'].unique()


# In[418]:


df['Severity of medical conditions'].isnull().sum()


# In[419]:


df['Severity of medical conditions'].replace('Mnil',0,inplace = True)


# In[420]:


df['Severity of medical conditions'].replace('severe','Severe',inplace = True)


# In[421]:


df['Severity of medical conditions'].unique()


# In[422]:


df['Severity of medical conditions'] = df['Severity of medical conditions'].map({'Severe' : 1,'Mild' : 2,'Moderate' : 3,'0' : 0})


# In[423]:


df['Severity of medical conditions'].unique()


# In[424]:


df['Severity of medical conditions'].isnull().sum()


# In[425]:


df['Severity of medical conditions'].dtypes


# # weight (in Kg)

# In[426]:


df['weight (in Kg)'].dtypes


# In[427]:


df['weight (in Kg)'].isnull().sum()


# In[428]:


#df['weight (in Kg)'].fillna(method = 'ffill',inplace = True)


# In[429]:


df['weight (in Kg)'].isnull().sum()


# # weight z score

# In[430]:


df['weight z score'].dtypes


# In[431]:


df['weight z score'].unique()


# In[432]:


df['weight z score'].isnull().sum()


# # height (in cm)

# In[433]:


df['height (in cm)'].dtypes


# In[434]:


df['height (in cm)'].unique()


# In[435]:


df['height (in cm)'].isnull().sum()


# In[436]:


#df.drop('height (in cm)', axis=1, inplace=True)


# # height z score

# In[437]:


df['height z score'].dtypes


# In[438]:


df['height z score'].unique()


# In[439]:


df['height z score'].isnull().sum()


# In[440]:


#df.drop('height z score',axis = 1, inplace = True)


# # head circumference (in cm)

# In[441]:


df['head circumference (in cm)'].dtypes


# In[442]:


df['head circumference (in cm)'].unique()


# In[443]:


df['head circumference (in cm)'].isnull().sum()


# In[444]:


#df.drop('head circumference (in cm)',axis = 1, inplace = True)


# # head circumference z score
# 
# ### we can drop this

# In[445]:


df['head circumference z score'].dtypes


# In[446]:


df['head circumference z score'].unique()


# In[447]:


df['head circumference z score'].isnull().sum()


# # systemic examination(abnormal/normal)
# 
# ### 'Normal' : 1, 'Abnormal' : 2
# 

# In[448]:


df['systemic examination(abnormal/normal)'].unique()


# In[449]:


df['systemic examination(abnormal/normal)'].isnull().sum()


# In[450]:


df['systemic examination(abnormal/normal)'].replace('abnormal','Abnormal',inplace = True)


# In[451]:


df['systemic examination(abnormal/normal)'].unique()


# In[452]:


df['systemic examination(abnormal/normal)'] = df['systemic examination(abnormal/normal)'].map({'Normal' : 1, 'Abnormal' : 2})


# In[453]:


df['systemic examination(abnormal/normal)'].isnull().sum()


# In[454]:


df['systemic examination(abnormal/normal)'].dtypes


# # systemic examination details (main finding only)
# 

# In[455]:


df['systemic examination details (main finding only)'].dtypes


# In[456]:


df['systemic examination details (main finding only)'].unique()


# In[457]:


df['systemic examination details (main finding only)'].isnull().sum()


# # Mental status examination/Behavioral Observation details (abnormal/normal)
# 
# ### 'normal':1,'abnormal' : 2

# In[458]:


df['Mental status examination/Behavioral Observation details (abnormal/normal)'].dtypes


# In[459]:


df['Mental status examination/Behavioral Observation details (abnormal/normal)'].unique()


# In[460]:


df['Mental status examination/Behavioral Observation details (abnormal/normal)'].isnull().sum()


# In[461]:


df['Mental status examination/Behavioral Observation details (abnormal/normal)']= df['Mental status examination/Behavioral Observation details (abnormal/normal)'].map({'normal':1,'abnormal' : 2})


# In[462]:


df['Mental status examination/Behavioral Observation details (abnormal/normal)'].isnull().sum()


# In[463]:


#df['Mental status examination/Behavioral Observation details (abnormal/normal)'].fillna(method = 'ffill',inplace = True)


# In[464]:


df['Mental status examination/Behavioral Observation details (abnormal/normal)'].isnull().sum()


# In[465]:


df['Mental status examination/Behavioral Observation details (abnormal/normal)'].dtypes


# # Mental status examination/Behavioral observation details (main finding only in description)

# In[466]:


df['Mental status examination/Behavioral observation details (main finding only in description)'].dtypes


# In[467]:


df['Mental status examination/Behavioral observation details (main finding only in description)'].unique()


# In[468]:


df['Mental status examination/Behavioral observation details (main finding only in description)'].isnull().sum()


# In[469]:


#df['Mental status examination/Behavioral observation details (main finding only in description)'].fillna(method = 'ffill',inplace = True)


# In[470]:


df['Mental status examination/Behavioral observation details (main finding only in description)'].isnull().sum()


# In[471]:


df['Mental status examination/Behavioral observation details (main finding only in description)'].dtypes


# # Screening diagnosis 

# In[472]:


df['Screening diagnosis '].dtypes


# In[473]:


df['Screening diagnosis '].unique()


# In[474]:


df['Screening diagnosis '].isnull().sum()


# In[475]:


#df['Screening diagnosis '].fillna(method = 'ffill',inplace = True)


# In[476]:


df['Screening diagnosis '].isnull().sum()


# # detailed workup diagnosis

# In[477]:


df['detailed workup diagnosis'].dtypes


# In[478]:


df['detailed workup diagnosis'].unique()


# In[479]:


df['detailed workup diagnosis'].isnull().sum()


# # Follow up diagnosis changed or not (yes/no)

# In[480]:


df['Follow up diagnosis changed or not (yes/no)'].dtypes


# In[481]:


df['Follow up diagnosis changed or not (yes/no)'].unique()


# In[482]:


df['Follow up diagnosis changed or not (yes/no)'].isnull().sum()


# In[483]:


df['Follow up diagnosis changed or not (yes/no)'] = df['Follow up diagnosis changed or not (yes/no)'].map({'Yes':1,'No':0})


# In[484]:


df['Follow up diagnosis changed or not (yes/no)'].dtypes


# # If yes, changed once or multiple times (once/multiple)
# 
# ### 'Once' : 1,  'NIL' : 0, 'Twice' : 2, 'Multiple' : 4, 'No' : 5, 'thrice' : 3

# In[485]:


df['If yes, changed once or multiple times (once/multiple)'].dtypes


# In[486]:


df['If yes, changed once or multiple times (once/multiple)'].unique()


# In[487]:


df['If yes, changed once or multiple times (once/multiple)'].replace('once','Once',inplace = True)


# In[488]:


df['If yes, changed once or multiple times (once/multiple)'].replace('twice','Twice',inplace = True)


# In[489]:


df['If yes, changed once or multiple times (once/multiple)'].replace('multiple','Multiple',inplace = True)


# In[490]:


df['If yes, changed once or multiple times (once/multiple)'].isnull().sum()


# In[491]:


df['If yes, changed once or multiple times (once/multiple)'].unique()


# In[492]:


df['If yes, changed once or multiple times (once/multiple)'] = df['If yes, changed once or multiple times (once/multiple)'].map({'Once' : 1, '0' : 0, 'NIL' : 0, 'Twice' : 2, 'Multiple' : 4, 'No' : 5, 'thrice' : 3})


# In[493]:


df['If yes, changed once or multiple times (once/multiple)'].isnull().sum()


# In[494]:


#df['If yes, changed once or multiple times (once/multiple)'].fillna(0,inplace = True)


# In[495]:


df['If yes, changed once or multiple times (once/multiple)'].isnull().sum()


# In[496]:


df['If yes, changed once or multiple times (once/multiple)'].dtypes


# # If yes, after how many days from first presentation diagnosis changed (in days)

# In[497]:


df['If yes, after how many days from first presentation diagnosis changed (in days)'].dtypes


# In[498]:


df['If yes, after how many days from first presentation diagnosis changed (in days)'].unique()


# In[499]:


df['If yes, after how many days from first presentation diagnosis changed (in days)'].replace('NIL',0,inplace = True)


# In[500]:


df['If yes, after how many days from first presentation diagnosis changed (in days)'].dtypes


# # If yes, diagnosis changed to what

# In[501]:


df['If yes, diagnosis changed to what'].dtypes


# In[502]:


df['If yes, diagnosis changed to what'].unique()


# In[503]:


df['If yes, diagnosis changed to what'].isnull().sum()


# In[504]:


#df['If yes, diagnosis changed to what'].fillna(0,inplace = True)


# In[505]:


df['If yes, diagnosis changed to what'].isnull().sum()


# In[506]:


df['If yes, diagnosis changed to what'].dtypes


# # Axis 1_1

# In[507]:


df['Axis 1_1'].dtypes


# In[508]:


df['Axis 1_1'].unique()


# In[509]:


df['Axis 1_1'].isnull().sum()


# In[510]:


#df['Axis 1_1'].fillna(0,inplace = True)


# In[511]:


df['Axis 1_1'].isnull().sum()


# # Axis 1_2

# In[512]:


df['Axis 1_2'].dtypes


# In[513]:


df['Axis 1_2'].unique()


# In[514]:


df['Axis 1_2'].isnull().sum()


# In[515]:


#df['Axis 1_2'].fillna(0,inplace = True)


# # Axis 1_3

# In[516]:


df['Axis 1_3'].dtypes


# In[517]:


df['Axis 1_3'].unique()


# In[518]:


df['Axis 1_3'].isnull().sum()


# In[519]:


#df['Axis 1_3'].fillna(0,inplace = True)


# # Axis 1_4

# In[520]:


df['Axis 1_4'].dtypes


# In[521]:


df['Axis 1_4'].unique()


# In[522]:


df['Axis 1_4'].replace('NIL',0,inplace = True)


# In[523]:


df['Axis 1_4'].unique()


# In[524]:


df['Axis 1_4'].isnull().sum()


# In[525]:


df['Axis 1_4'] = df['Axis 1_4'].map({'Nicotine use diorder' : 1, 'conduct features' :2,
       'Separation anxiety' : 3, 'Specific phobia' : 4, 'Deferred' : 5})


# In[526]:


df['Axis 1_4'].unique()


# In[527]:


df['Axis 1_4'].isnull().sum()


# In[528]:


#df['Axis 1_4'].fillna(0,inplace = True)


# In[529]:


df['Axis 1_4'].isnull().sum()


# In[530]:


df['Axis 1_4'].dtype


# # Axis 2

# In[531]:


df['Axis 2'].dtype


# In[532]:


df['Axis 2'].unique()


# In[533]:


df['Axis 2'].replace('NIL',0,inplace = True)


# In[534]:


df['Axis 2'].replace(' Nil',0,inplace = True)


# In[535]:


df['Axis 2'].replace('Nl',0,inplace = True)


# In[536]:


df['Axis 2'].replace('N',0,inplace = True)


# In[537]:


df['Axis 2'].replace('Nill',0,inplace = True)


# In[538]:


df['Axis 2'].unique()


# In[539]:


df['Axis 2'].isnull().sum()


# In[540]:


#df['Axis 2'].fillna(0,inplace = True)


# In[541]:


df['Axis 2'] = df['Axis 2'].map({'0' : 0, 'motor coordination disorder' : 1, 'DSL' : 2, 'SLD' : 3,
       'Delayed speech and language' : 4, 'Delay Speech and language' : 5,
       'Specific learning disorder' : 6,
       '? Mixed expressivie and receptivea language disorder' : 7, 'Deferred' : 8,
       'Delay  Speech' : 9, 'Delayed  Speech & Languange' : 10,'ESD' :11,
       '? SLD' : 12})


# In[542]:


df['Axis 2'].isnull().sum()


# In[543]:


df['Axis 2'].fillna(0,inplace = True)


# In[544]:


df['Axis 2'].isnull().sum()


# In[545]:


df['Axis 2'].unique()


# # Axis 5

# In[546]:


df['Axis 5'].isnull().sum()


# In[547]:


df['Axis 5'].dtypes


# In[548]:


df['Axis 5'].unique()


# In[549]:


#df['Axis 5'].fillna(method = 'ffill',inplace = True)


# In[550]:


df['Axis 5'].isnull().sum()


# # significant psychosocial stressor
# 
# ### 'No' : 0,'Yes' : 1,'nil' : '2'   ## drop

# In[551]:


df['significant psychosocial stressor'].dtypes


# In[552]:


df['significant psychosocial stressor'].isnull().sum()


# In[553]:


df['significant psychosocial stressor'].unique()


# In[554]:


df['significant psychosocial stressor'] = df['significant psychosocial stressor'].map({'No' : 0,'Yes' : 1,'0' : 0})


# In[555]:


df['significant psychosocial stressor'].isnull().sum()


# In[556]:


df['significant psychosocial stressor'].dtypes


# In[557]:


df['significant psychosocial stressor'].unique()


# # name of Medication 1

# In[558]:


df['name of Medication 1'].dtypes


# In[559]:


df['name of Medication 1'].unique()


# In[560]:


df['name of Medication 1'].isnull().sum()


# # medication 1 starting dose (in mg)

# In[561]:


df['medication 1 starting dose (in mg)'].dtypes


# In[562]:


df['medication 1 starting dose (in mg)'].isnull().sum()


# # Avg dose of medication 1 (Mode value of medication) (in mg)

# In[563]:


df['Avg dose of medication 1 (Mode value of medication) (in mg)'].dtypes


# In[564]:


df['Avg dose of medication 1 (Mode value of medication) (in mg)'].isnull().sum()


# In[565]:


#df['Avg dose of medication 1 (Mode value of medication) (in mg)'].fillna(0,inplace = True)


# # Maximum dose of medication 1 (in mg)

# In[566]:


df['Maximum dose of medication 1 (in mg)'].dtypes


# In[567]:


df['Maximum dose of medication 1 (in mg)'].isnull().sum()


# In[568]:


df['Maximum dose of medication 1 (in mg)'].fillna(0,inplace = True)


# In[569]:


df['Maximum dose of medication 1 (in mg)'].dtypes


# # Total duration of medication 1 (in days) 

# In[570]:


df['Total duration of medication 1 (in days) '].dtypes


# In[571]:


df['Total duration of medication 1 (in days) '].isnull().sum()


# In[572]:


#df['Total duration of medication 1 (in days) '].fillna(0,inplace = True)


# In[573]:


df['Total duration of medication 1 (in days) '].isnull().sum()


# # Continued medication 1/stopped/changed
# 
# ### 'Continued medication 1/stopped/changed'].map({'Stopped' :1, 'loss to follow-up' :2, 'Continued' : 3,
# ###       'Changed d/t poor tolerance' : 4, '0': 0, 'Reduced d/t resolution' : 5,

# In[574]:


df['Continued medication 1/stopped/changed'].dtypes


# In[575]:


df['Continued medication 1/stopped/changed'].unique()


# In[576]:


df['Continued medication 1/stopped/changed']= df['Continued medication 1/stopped/changed'].map({'Stopped' :1, 'loss to follow-up' :2, 'Continued' : 3,
       'Changed d/t poor tolerance' : 4, '0': 0, 'Reduced d/t resolution' : 5,
       'Changed d/t non response': 6})


# In[577]:


df['Continued medication 1/stopped/changed'].unique()


# In[578]:


df['Continued medication 1/stopped/changed'].isnull().sum()


# In[579]:


#df['Continued medication 1/stopped/changed'].fillna(0,inplace = True)


# In[580]:


df['Continued medication 1/stopped/changed'].isnull().sum()


# # Response to medication 1 (Good/partial/no)
# 
# ### 'Partial': 3, 'Good' : 1, '0' : 0, 'No' : 2
# 
# ## Drop

# In[581]:


df['Response to medication 1 (Good/partial/no)'].dtypes


# In[582]:


df['Response to medication 1 (Good/partial/no)'].isnull().sum()


# In[583]:


df['Response to medication 1 (Good/partial/no)'].unique()


# In[584]:


df['Response to medication 1 (Good/partial/no)'].replace('good','Good',inplace = True)


# In[585]:


df['Response to medication 1 (Good/partial/no)'].replace('partial','Partial',inplace = True)


# In[586]:


df['Response to medication 1 (Good/partial/no)'].replace('no','No',inplace = True)


# In[587]:


df['Response to medication 1 (Good/partial/no)'].unique()


# In[588]:


df['Response to medication 1 (Good/partial/no)'].isnull().sum()


# In[589]:


df['Response to medication 1 (Good/partial/no)'].unique()


# In[590]:


df['Response to medication 1 (Good/partial/no)'] = df['Response to medication 1 (Good/partial/no)'].map({'Partial': 3, 'Good' : 1, '0' : 0, 'No' : 2})


# In[591]:


df['Response to medication 1 (Good/partial/no)'].unique()


# In[592]:


df['Response to medication 1 (Good/partial/no)'].isnull().sum()


# In[593]:


#df['Response to medication 1 (Good/partial/no)'].fillna(method = 'bfill',inplace = True)


# In[594]:


df['Response to medication 1 (Good/partial/no)'].isnull().sum()


# # Side effect of medication 1

# In[595]:


df['Side effect of medication 1'].dtypes


# In[596]:


df['Side effect of medication 1'].unique()


# In[597]:


df['Side effect of medication 1'].isnull().sum()


# In[598]:


df['Side effect of medication 1'].replace('no','No',inplace = True)


# In[599]:


df['Side effect of medication 1'].replace('yes','Yes',inplace = True)


# In[600]:


df['Side effect of medication 1'].replace('Vomiting','Vomitimg',inplace = True)


# In[601]:


df['Side effect of medication 1'].unique()


# In[602]:


df['Side effect of medication 1'] = df['Side effect of medication 1'].map({'No' : 1, 'irregular menstruation, weight gain, grade 2 fatty liver' : 2,
       'Yes' : 3, '0' : 0, 'eneuresis' : 4, 'hypersalivation' : 5,
       'Maculopapular rash over chin, lips , cheeks' : 6, 'sedation' : 7,
       'Gum hypertrophy' : 8, 'Bradykinesia' : 9, 'Blurred vision' : 10,
       'weight gain, sedation' : 11, 'Vomitimg' : 12, 'Weight gain' : 13, 'Amenorrhea' : 14,
       'Veiw of gastric irritation' : 15})


# In[603]:


df['Side effect of medication 1'].unique()


# In[604]:


#df['Side effect of medication 1'].fillna(0,inplace = True)


# # onset of side effect post starting med 1 ( in days)

# In[605]:


df['onset of side effect post starting med 1 ( in days)'].dtypes


# In[606]:


df['onset of side effect post starting med 1 ( in days)'].isnull().sum()


# In[607]:


df['onset of side effect post starting med 1 ( in days)'].fillna(0,inplace = True)


# In[608]:


df['onset of side effect post starting med 1 ( in days)'].isnull().sum()


# # total duration of side effect of medication 1 (in days)
# 

# In[609]:


# Apply str.lower() to all object (string) columns
df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)


# In[610]:


df['total duration of side effect of medication 1 (in days)'].dtypes


# In[611]:


df['total duration of side effect of medication 1 (in days)'].unique()


# In[612]:


df['total duration of side effect of medication 1 (in days)'].replace('nl',0,inplace = True)


# In[613]:


df['total duration of side effect of medication 1 (in days)'].isnull().sum()


# In[614]:


#df['total duration of side effect of medication 1 (in days)'].fillna(0,inplace = True)


# In[615]:


df['total duration of side effect of medication 1 (in days)'].dtypes


# In[616]:


df['total duration of side effect of medication 1 (in days)'].unique()


# In[617]:


df['total duration of side effect of medication 1 (in days)'] = df['total duration of side effect of medication 1 (in days)'].astype(int)


# In[618]:


df['total duration of side effect of medication 1 (in days)'].dtypes


# # Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) 

# In[619]:


df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '].dtypes


# In[620]:


df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '].isnull().sum()


# In[621]:


df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '].unique()


# In[622]:


df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '].replace('x',0,inplace = True)


# In[623]:


df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '].unique()


# In[624]:


df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '].replace('nil',0,inplace = True)


# In[625]:


df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '].unique()


# In[626]:


#df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '].fillna(method = 'bfill',inplace = True)


# In[627]:


df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '].isnull().sum()


# In[628]:


df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '] = df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '].astype(float)


# In[629]:


df['Medication possession ratios 1(MPRs) in lgb;x-syrup (total number of days when medications were taken divided by summation of total number of days when medications were taken with total off medication period) '].dtypes


# # name of Medication 2

# In[630]:


df['name of Medication 2'].dtypes


# In[631]:


df['name of Medication 2'] = df['name of Medication 2'].str.lower()


# In[632]:


df['name of Medication 2'].unique()


# In[633]:


df['name of Medication 2'].isnull().sum()


# # Medication 2 starting dose (in mg)

# In[634]:


df['Medication 2 starting dose (in mg)'].isnull().sum()


# In[635]:


df['Medication 2 starting dose (in mg)'].dtypes


# In[636]:


df['Medication 2 starting dose (in mg)'].unique()


# In[637]:


df['Medication 2 starting dose (in mg)'].replace('10`',10,inplace = True)


# In[638]:


df['Medication 2 starting dose (in mg)'].replace('nil',0,inplace = True)


# In[639]:


df['Medication 2 starting dose (in mg)'] = df['Medication 2 starting dose (in mg)'].astype(float)


# In[640]:


df['Medication 2 starting dose (in mg)'].dtypes


# In[641]:


df['Medication 2 starting dose (in mg)']


# In[642]:


df['Medication 2 starting dose (in mg)'].isnull().sum()


# # Avg dose of medication 2 (in mg)

# In[643]:


df['Avg dose of medication 2 (in mg)'].dtypes


# In[644]:


df['Avg dose of medication 2 (in mg)'].isnull().sum()


# In[645]:


#df['Avg dose of medication 2 (in mg)'].fillna(0,inplace = True)


# # Maximum dose of medication 2 (in mg)

# In[646]:


df['Maximum dose of medication 2 (in mg)'].dtypes


# In[647]:


df['Maximum dose of medication 2 (in mg)'].isnull().sum()


# In[648]:


df['Maximum dose of medication 2 (in mg)'].fillna(0,inplace = True)


# # Total duration of medication 2(in days) 

# In[649]:


df['Total duration of medication 2(in days) '].dtypes


# In[650]:


df['Total duration of medication 2(in days) '].isnull().sum()


# In[651]:


#df['Total duration of medication 2(in days) '].fillna(0,inplace = True)


# In[652]:


df['Total duration of medication 2(in days) '].unique()


# In[653]:


df['Total duration of medication 2(in days) '].replace('stopped ',0,inplace = True)


# In[654]:


df['Total duration of medication 2(in days) '].replace('0.13',13,inplace = True)


# In[655]:


df['Total duration of medication 2(in days) '].unique()


# In[656]:


df['Total duration of medication 2(in days) '] = df['Total duration of medication 2(in days) '].astype(int)


# In[657]:


df['Total duration of medication 2(in days) '].dtypes


# # Continued medication 2/stopped/changed
# 
# ### 'loss to follow-up' : 1, 'reduced d/t resolution' : 2, 'continued' : 3, '0' : 0,
# ###       'stopped and restarted' : 4, 'stopped' : 5, 'changed d/t non response' : 6,
# ###       'change due to financial reason' : 7, 'stopped ': 5}

# In[658]:


df['Continued medication 2/stopped/changed'].dtypes


# In[659]:


df['Continued medication 2/stopped/changed'].isnull().sum()


# In[660]:


df['Continued medication 2/stopped/changed'].isnull().sum()


# In[661]:


df['Continued medication 2/stopped/changed'].unique()


# In[662]:


df['Continued medication 2/stopped/changed'] = df['Continued medication 2/stopped/changed'].map({'loss to follow-up' : 1, 'reduced d/t resolution' : 2, 'continued' : 3, '0' : 0,
       'stopped and restarted' : 4, 'stopped' : 5, 'changed d/t non response' : 6,
       'change due to financial reason' : 7, 'stopped ': 5})


# In[663]:


df['Continued medication 2/stopped/changed'].unique()


# In[664]:


df['Continued medication 2/stopped/changed'].isnull().sum()


# In[665]:


#df['Continued medication 2/stopped/changed'].fillna(0,inplace = True)


# In[666]:


df['Continued medication 2/stopped/changed'].isnull().sum()


# In[667]:


df['Continued medication 2/stopped/changed'].dtypes


# # Response to medication 2 (Good/partial/no)
# 
# ### 'good' : 1, 'partial' : 2, '0': 0,'no' : 3
# 
# ## drop

# In[668]:


df['Response to medication 2 (Good/partial/no)'].dtypes


# In[669]:


df['Response to medication 2 (Good/partial/no)'].unique()


# In[670]:


df['Response to medication 2 (Good/partial/no)'].isnull().sum()


# In[671]:


df['Response to medication 2 (Good/partial/no)'] = df['Response to medication 2 (Good/partial/no)'].map({'good' : 1, 'partial' : 2, '0': 0,'no' : 3})


# In[672]:


df['Response to medication 2 (Good/partial/no)'].unique()


# In[673]:


df['Response to medication 2 (Good/partial/no)'].isnull().sum()


# In[674]:


#df['Response to medication 2 (Good/partial/no)'].fillna(method = 'ffill',inplace = True)


# In[675]:


df['Response to medication 2 (Good/partial/no)'].isnull().sum()


# # Side effect of medication 2
# 
# ## 'no' : 2,  'yes' : 1, 'sedation' : 3, 'nil' : 0

# In[676]:


df['Side effect of medication 2'].dtypes


# In[677]:


df['Side effect of medication 2'].isnull().sum()


# In[678]:


df['Side effect of medication 2'].unique()


# In[679]:


df['Side effect of medication 2'] = df['Side effect of medication 2'].map({'no' : 2, '0' : 0, 'yes' : 1, 'sedation' : 3, 'nil' : 0})


# In[680]:


df['Side effect of medication 2'].isnull().sum()


# In[681]:


#df['Side effect of medication 2'].fillna(0,inplace = True)


# In[682]:


df['Side effect of medication 2'].isnull().sum()


# In[683]:


df['Side effect of medication 2'].dtypes


# # onset of side effect post starting med 2 ( in days)

# In[684]:


df['onset of side effect post starting med 2 ( in days)'].dtypes


# In[685]:


df['onset of side effect post starting med 2 ( in days)'].isnull().sum()


# In[686]:


#df['onset of side effect post starting med 2 ( in days)'].fillna(0,inplace = True)


# In[687]:


df['onset of side effect post starting med 2 ( in days)'].isnull().sum()


# # total duration of side effect of medication 2 (in days)

# In[688]:


df['total duration of side effect of medication 2 (in days)'].dtypes


# In[689]:


df['total duration of side effect of medication 2 (in days)'].isnull().sum()


# In[690]:


#df['total duration of side effect of medication 2 (in days)'].fillna(0,inplace = True)


# In[691]:


df['total duration of side effect of medication 2 (in days)'].dtypes


# # Medication possession ratios 2(MPRs) in lgb;x-syrup
# 

# In[692]:


df['Medication possession ratios 2(MPRs) in lgb;x-syrup'].dtypes


# In[693]:


df['Medication possession ratios 2(MPRs) in lgb;x-syrup'].unique()


# In[694]:


df['Medication possession ratios 2(MPRs) in lgb;x-syrup'].replace('x',0,inplace = True)


# In[695]:


df['Medication possession ratios 2(MPRs) in lgb;x-syrup'].isnull().sum()


# In[696]:


#df['Medication possession ratios 2(MPRs) in lgb;x-syrup'].fillna(method = 'bfill',inplace = True)


# In[697]:


df['Medication possession ratios 2(MPRs) in lgb;x-syrup'].isnull().sum()


# In[698]:


df['Medication possession ratios 2(MPRs) in lgb;x-syrup'] =df['Medication possession ratios 2(MPRs) in lgb;x-syrup'].astype(float)


# In[699]:


df['Medication possession ratios 2(MPRs) in lgb;x-syrup'].dtypes


# In[700]:


df['Medication possession ratios 2(MPRs) in lgb;x-syrup'].isnull().sum()


# # name of Medication 3

# In[701]:


df['name of Medication 3'].dtypes


# In[702]:


df['name of Medication 3'].isnull().sum()


# In[703]:


df['name of Medication 3'].unique()


# # Medication 3 starting dose (in mg)

# In[704]:


df['Medication 3 starting dose (in mg)'].dtypes


# In[705]:


df['Medication 3 starting dose (in mg)'].isnull().sum()


# In[706]:


df['Medication 3 starting dose (in mg)'].unique()


# In[707]:


df['Medication 3 starting dose (in mg)'].replace('risperidone',0,inplace = True)


# In[708]:


df['Medication 3 starting dose (in mg)'].unique()


# In[709]:


df['Medication 3 starting dose (in mg)'] = df['Medication 3 starting dose (in mg)'].astype(float)


# In[710]:


df['Medication 3 starting dose (in mg)'].dtypes


# In[711]:


df['Medication 3 starting dose (in mg)'].isnull().sum()


# # Avg dose of medication 3 (in mg)

# In[712]:


df['Avg dose of medication 3 (in mg)'].dtypes


# In[713]:


df['Avg dose of medication 3 (in mg)'].isnull().sum()


# In[714]:


#df['Avg dose of medication 3 (in mg)'].fillna(method = 'ffill',inplace = True)


# # Maximum dose of medication 3 (in mg)

# In[715]:


df['Maximum dose of medication 3 (in mg)'].dtypes


# In[716]:


df['Maximum dose of medication 3 (in mg)'].isnull().sum()


# In[717]:


df['Maximum dose of medication 3 (in mg)'].fillna(0,inplace = True)


# In[718]:


df['Maximum dose of medication 3 (in mg)'].isnull().sum()


# # Total duration of medication 3 (in days

# In[719]:


df['Total duration of medication 3 (in days'].dtypes


# In[720]:


df['Total duration of medication 3 (in days'].isnull().sum()


# In[721]:


#df['Total duration of medication 3 (in days'].fillna(method = 'ffill',inplace = True)


# In[722]:


df['Total duration of medication 3 (in days'].isnull().sum()


# In[723]:


df['Total duration of medication 3 (in days'].unique()


# # continued medication 3/stopped/changed

# In[724]:


df['continued medication 3/stopped/changed'].dtypes


# In[725]:


df['continued medication 3/stopped/changed'].isnull().sum()


# In[726]:


df['continued medication 3/stopped/changed'].unique()


# In[727]:


df['continued medication 3/stopped/changed'] = df['continued medication 3/stopped/changed'].map({'0' : 0, 'continued' : 1, 'loss to follow-up' : 2, 'stopped' : 3,
       'reduced d/t resolution' : 4, 'changed d/t non response' : 5,
       'changed d/t poor tolerance' : 6})


# In[728]:


df['continued medication 3/stopped/changed'].unique()


# In[729]:


df['continued medication 3/stopped/changed'].isnull().sum()


# In[730]:


#df['continued medication 3/stopped/changed'].fillna(method = 'ffill',inplace = True)


# In[731]:


df['continued medication 3/stopped/changed'].isnull().sum()


# # Response to medication 3 (Good/partial/no)
# 
# ### 'nil' : 0, 'good' : 1,  'no': 3, 'partial' : 2

# In[732]:


df['Response to medication 3 (Good/partial/no)'].dtypes


# In[733]:


df['Response to medication 3 (Good/partial/no)'].isnull().sum()


# In[734]:


df['Response to medication 3 (Good/partial/no)'].unique()


# In[735]:


df['Response to medication 3 (Good/partial/no)'] = df['Response to medication 3 (Good/partial/no)'].map({'0' : 0, 'good': 1,'no': 3, 'partial' : 2})


# In[736]:


df['Response to medication 3 (Good/partial/no)'].unique()


# In[737]:


df['Response to medication 3 (Good/partial/no)'].isnull().sum()


# # Side effect of medication 3
# 
# ## nil :0, 'yes' : 1, 'sedation':2, 'tremors' : 3

# In[738]:


df['Side effect of medication 3'].dtypes


# In[739]:


df['Side effect of medication 3'].isnull().sum()


# In[740]:


df['Side effect of medication 3'].unique()


# In[741]:


df['Side effect of medication 3'] = df['Side effect of medication 3'].map({'0' :0, 'yes' : 1, 'sedation':2, 'tremors' : 3})


# In[742]:


df['Side effect of medication 3'].unique()


# In[743]:


df['Side effect of medication 3'].isnull().sum()


# In[744]:


#df['Side effect of medication 3'].fillna(method = 'ffill',inplace = True)


# In[745]:


df['Side effect of medication 3'].isnull().sum()


# # onset of side effect post starting med 3 ( in days)

# In[746]:


df['onset of side effect post starting med 3 ( in days)'].dtypes


# In[747]:


df['onset of side effect post starting med 3 ( in days)'].isnull().sum()


# In[748]:


#df['onset of side effect post starting med 3 ( in days)'].fillna(method = 'ffill',inplace = True)


# In[749]:


df['onset of side effect post starting med 3 ( in days)'].isnull().sum()


# In[750]:


df['onset of side effect post starting med 3 ( in days)'].unique()


# # total duration of side effect of medication 3 (in days)

# In[751]:


df['total duration of side effect of medication 3 (in days)'].dtypes


# In[752]:


df['total duration of side effect of medication 3 (in days)'].isnull().sum()


# In[753]:


#df['total duration of side effect of medication 3 (in days)'].fillna(method = 'ffill',inplace = True)


# In[754]:


df['total duration of side effect of medication 3 (in days)'].isnull().sum()


# In[755]:


df['total duration of side effect of medication 3 (in days)'].unique()


# # Medication possession ratios 3(MPRs) in lgb;x-syrup

# In[756]:


df['Medication possession ratios 3(MPRs) in lgb;x-syrup'].dtypes


# In[757]:


df['Medication possession ratios 3(MPRs) in lgb;x-syrup'].isnull().sum()


# In[758]:


df['Medication possession ratios 3(MPRs) in lgb;x-syrup'].unique()


# In[759]:


#df['Medication possession ratios 3(MPRs) in lgb;x-syrup'].fillna(method = 'bfill',inplace = True)


# In[760]:


df['Medication possession ratios 3(MPRs) in lgb;x-syrup'].replace('x',0,inplace = True)


# In[761]:


df['Medication possession ratios 3(MPRs) in lgb;x-syrup'].isnull().sum()


# In[762]:


df['Medication possession ratios 3(MPRs) in lgb;x-syrup'] = df['Medication possession ratios 3(MPRs) in lgb;x-syrup'].astype(float)


# In[763]:


df['Medication possession ratios 3(MPRs) in lgb;x-syrup'].dtypes


# # name of Medication 4

# In[764]:


df['name of Medication 4'].dtypes


# In[765]:


df['name of Medication 4'].unique()


# In[766]:


df['name of Medication 4'].isnull().sum()


# In[767]:


#df['name of Medication 4'].fillna(method = 'ffill',inplace = True)


# In[768]:


df['name of Medication 4'].isnull().sum()


# # Medication 4 starting dose (in mg)

# In[769]:


df['Medication 4 starting dose (in mg)'].dtypes


# In[770]:


df['Medication 4 starting dose (in mg)'].unique()


# In[771]:


df['Medication 4 starting dose (in mg)'].replace('1 tbsp',5,inplace = True)


# In[772]:


df['Medication 4 starting dose (in mg)'].replace('olanzapine',0,inplace = True)


# In[773]:


df['Medication 4 starting dose (in mg)'].unique()


# In[774]:


df['Medication 4 starting dose (in mg)'].isnull().sum()


# In[775]:


#df['Medication 4 starting dose (in mg)'].fillna(method = 'ffill',inplace = True)


# In[776]:


df['Medication 4 starting dose (in mg)'].isnull().sum()


# In[777]:


df['Medication 4 starting dose (in mg)'] = df['Medication 4 starting dose (in mg)'].astype(float)


# In[778]:


df['Medication 4 starting dose (in mg)'].isnull().sum()


# In[779]:


df['Medication 4 starting dose (in mg)'].dtypes


# # Avg dose of medication 4 (in mg)

# In[780]:


df['Avg dose of medication 4 (in mg)'].dtypes


# In[781]:


df['Avg dose of medication 4 (in mg)'].isnull().sum()


# In[782]:


#df['Avg dose of medication 4 (in mg)'].fillna(method = 'ffill',inplace = True)


# In[783]:


df['Avg dose of medication 4 (in mg)'].isnull().sum()


# In[784]:


df['Avg dose of medication 4 (in mg)'].unique()


# In[785]:


df['Avg dose of medication 4 (in mg)'].replace('1 tbsp',5,inplace = True)


# In[786]:


df['Avg dose of medication 4 (in mg)'] = df['Avg dose of medication 4 (in mg)'].astype(float)


# In[787]:


df['Avg dose of medication 4 (in mg)'].dtypes


# # Maximum dose of medication 4 (in mg)

# In[788]:


df['Maximum dose of medication 4 (in mg)'].dtypes


# In[789]:


df['Maximum dose of medication 4 (in mg)'].isnull().sum()


# In[790]:


#df['Maximum dose of medication 4 (in mg)'].fillna(method = 'ffill',inplace = True)


# In[791]:


df['Maximum dose of medication 4 (in mg)'].unique()


# In[792]:


df['Maximum dose of medication 4 (in mg)'].replace('1 tbsp',5,inplace = True)


# In[793]:


df['Maximum dose of medication 4 (in mg)'] = df['Maximum dose of medication 4 (in mg)'].astype(float)


# In[794]:


df['Maximum dose of medication 4 (in mg)'].dtypes


# # Total duration of medication 4 (in days)

# In[795]:


df['Total duration of medication 4 (in days)'].dtypes


# In[796]:


df['Total duration of medication 4 (in days)'].isnull().sum()


# In[797]:


#df['Total duration of medication 4 (in days)'].fillna(method = 'ffill',inplace = True)


# In[798]:


df['Total duration of medication 4 (in days)'].isnull().sum()


# In[799]:


df['Total duration of medication 4 (in days)'].unique()


# In[800]:


df['Total duration of medication 4 (in days)'].replace('il',inplace = True)


# In[801]:


df['Total duration of medication 4 (in days)'] = df['Total duration of medication 4 (in days)'].astype(int)


# In[802]:


df['Total duration of medication 4 (in days)'].dtypes


# # continued medication 4/stopped/changed
# 
# ### 'nil' : 0, 'reduced d/t resolution' : 1, 'stopped' : 2, 'continued' : 3,
# ###        'changed d/t non response' : 4, 'loss to follow-up' : 5,
# ###       'reduce due to side effects' : 6,  'stopped ' : 2

# In[803]:


df['continued medication 4/stopped/changed'].dtypes


# In[804]:


df['continued medication 4/stopped/changed'].unique()


# In[805]:


df['continued medication 4/stopped/changed'] = df['continued medication 4/stopped/changed'].map({'0' : 0, 'reduced d/t resolution' : 1, 'stopped' : 2, 'continued' : 3,
       'changed d/t non response' : 4, 'loss to follow-up' : 5,
       'reduce due to side effects' : 6,  'stopped ' : 2})


# In[806]:


df['continued medication 4/stopped/changed'].unique()


# In[807]:


df['continued medication 4/stopped/changed'].isnull().sum()


# In[808]:


#df['continued medication 4/stopped/changed'].fillna(0,inplace = True)


# In[809]:


df['continued medication 4/stopped/changed'].isnull().sum()


# # Response to medication 4(Good/partial/no)
# 
# ### 'nil' : 0, 'good' : 1, 'no' : 3, 'partial' : 2

# In[810]:


df['Response to medication 4(Good/partial/no)'].dtypes


# In[811]:


df['Response to medication 4(Good/partial/no)'].unique()


# In[812]:


df['Response to medication 4(Good/partial/no)'].isnull().sum()


# In[813]:


df['Response to medication 4(Good/partial/no)'] = df['Response to medication 4(Good/partial/no)'].map({'0' : 0, 'good' : 1, 'no' : 3, 'partial' : 2})


# In[814]:


df['Response to medication 4(Good/partial/no)'].unique()


# In[815]:


df['Response to medication 4(Good/partial/no)'].isnull().sum()


# In[816]:


df['Response to medication 4(Good/partial/no)'].dtypes


# # Side effect of medication 4
# 
# ### '0' : 0, 'gum hypertrophy':1,'hypersalivation' : 2, 'yes' : 3

# In[817]:


df['Side effect of medication 4'].dtypes


# In[818]:


df['Side effect of medication 4'].isnull().sum()


# In[819]:


df['Side effect of medication 4'].unique()


# In[820]:


df['Side effect of medication 4'] = df['Side effect of medication 4'].map({'0' : 0, 'gum hypertrophy':1,'hypersalivation' : 2, 'yes' : 3})


# In[821]:


df['Side effect of medication 4'].isnull().sum()


# In[822]:


#df['Side effect of medication 4'].fillna(method = 'ffill',inplace = True)


# In[823]:


df['Side effect of medication 4'].isnull().sum()


# In[824]:


df['Side effect of medication 4'].dtypes


# # onset of side effect post starting med 4 ( in days)

# In[825]:


df['onset of side effect post starting med 4 ( in days)'].dtypes


# In[826]:


df['onset of side effect post starting med 4 ( in days)'].isnull().sum()


# In[827]:


df['onset of side effect post starting med 4 ( in days)'].fillna(method = 'ffill',inplace = True)


# In[828]:


df['onset of side effect post starting med 4 ( in days)'].isnull().sum()


# In[829]:


df['onset of side effect post starting med 4 ( in days)'].unique()


# # total duration of side effect of medication 4 (in days)

# In[830]:


df['total duration of side effect of medication 4 (in days)'].dtypes


# In[831]:


df['total duration of side effect of medication 4 (in days)'].isnull().sum()


# In[832]:


df['total duration of side effect of medication 4 (in days)'].fillna(method = 'ffill',inplace = True)


# In[833]:


df['total duration of side effect of medication 4 (in days)'].unique()


# In[834]:


df['total duration of side effect of medication 4 (in days)'].isnull().sum()


# # Medication possession ratios 4(MPRs) in lgb;x-syrup

# In[835]:


df['Medication possession ratios 4(MPRs) in lgb;x-syrup'].dtypes


# In[836]:


df['Medication possession ratios 4(MPRs) in lgb;x-syrup'].unique()


# In[837]:


df['Medication possession ratios 4(MPRs) in lgb;x-syrup'].replace('x',30,inplace = True)


# In[838]:


df['Medication possession ratios 4(MPRs) in lgb;x-syrup'].unique()


# In[839]:


df['Medication possession ratios 4(MPRs) in lgb;x-syrup'].isnull().sum()


# In[840]:


df['Medication possession ratios 4(MPRs) in lgb;x-syrup'].fillna(method = 'ffill',inplace = True)


# In[841]:


df['Medication possession ratios 4(MPRs) in lgb;x-syrup'].isnull().sum()


# In[842]:


df['Medication possession ratios 4(MPRs) in lgb;x-syrup'].dtypes


# In[843]:


df['Medication possession ratios 4(MPRs) in lgb;x-syrup'] = df['Medication possession ratios 4(MPRs) in lgb;x-syrup'].astype(float)


# # name of Medication 5

# In[844]:


df['name of Medication 5'].dtypes


# In[845]:


df['name of Medication 5'].unique()


# In[846]:


df['name of Medication 5'].isnull().sum()


# # Medication 5 starting dose (in mg)

# In[847]:


df['Medication 5 starting dose (in mg)'].dtypes


# In[848]:


df['Medication 5 starting dose (in mg)'].unique()


# In[849]:


df['Medication 5 starting dose (in mg)'].isnull().sum()


# In[850]:


df['Medication 5 starting dose (in mg)'].replace('0.5.',0.5,inplace = True)


# In[851]:


df['Medication 5 starting dose (in mg)'] = df['Medication 5 starting dose (in mg)'].astype(float)


# In[852]:


df['Medication 5 starting dose (in mg)'].dtypes


# # Avg dose of medication 5 (in mg)

# In[853]:


df['Avg dose of medication 5 (in mg)'].dtypes


# In[854]:


df['Avg dose of medication 5 (in mg)'].isnull().sum()


# In[855]:


df['Avg dose of medication 5 (in mg)'].unique()


# # Maximum dose of medication 5(in mg)

# In[856]:


df['Maximum dose of medication 5(in mg)'].dtypes


# In[857]:


df['Maximum dose of medication 5(in mg)'].isnull().sum()


# # Total duration of medication 5 (in days)

# In[858]:


df['Total duration of medication 5 (in days)'].dtypes


# In[859]:


df['Total duration of medication 5 (in days)'].isnull().sum()


# In[860]:


df['Total duration of medication 5 (in days)'].fillna(method = 'ffill',inplace = True)


# In[861]:


df['Total duration of medication 5 (in days)'].isnull().sum()


# # continued medication 5/stopped/changed
# 
# ### 'nil' : 0, 'reduced d/t resolution' : 1, 'stopped' : 2, 'continued' : 3,
# ###       'changed d/t non response' : 4, 'loss to follow-up' : 5,
# ###       'changed d/t poor tolerance' : 6

# In[862]:


df['continued medication 5/stopped/changed'].dtypes


# In[863]:


df['continued medication 5/stopped/changed'].unique()


# In[864]:


#df['continued medication 5/stopped/changed'] = df['continued medication 5/stopped/changed'].map({'0' : 0, 'reduced d/t resolution' : 1, 'stopped' : 2, 'continued' : 3,
       'changed d/t non response' : 4, 'loss to follow-up' : 5,
       'changed d/t poor tolerance' : 6})


# In[865]:


df['continued medication 5/stopped/changed'].unique()


# In[866]:


df['continued medication 5/stopped/changed'].isnull().sum()


# In[867]:


df['continued medication 5/stopped/changed'].fillna(0,inplace = True)


# In[868]:


df['continued medication 5/stopped/changed'].isnull().sum()


# # Response to medication 5(Good/partial/no)
# 
# ### 'nil' : 0, 'good' : 1, 'no' : 3, 'partial' : 2

# In[869]:


df['Response to medication 5(Good/partial/no)'].dtypes


# In[870]:


df['Response to medication 5(Good/partial/no)'].unique()


# In[871]:


df['Response to medication 5(Good/partial/no)'].isnull().sum()


# In[872]:


#df['Response to medication 5(Good/partial/no)'] = df['Response to medication 5(Good/partial/no)'].map({'0' : 0, 'good' : 1, 'no' : 3, 'partial' : 2})


# In[873]:


df['Response to medication 5(Good/partial/no)'].unique()


# In[874]:


df['Response to medication 5(Good/partial/no)'].isnull().sum()


# In[875]:


df['Response to medication 5(Good/partial/no)'].fillna(method = 'ffill',inplace = True)


# In[876]:


df['Response to medication 5(Good/partial/no)'].isnull().sum()


# In[877]:


df['Response to medication 5(Good/partial/no)'].dtypes


# # Side effect of medication 5

# In[878]:


df['Side effect of medication 5'].dtypes


# In[879]:


df['Side effect of medication 5'].unique()


# In[880]:


df['Side effect of medication 5'].isnull().sum()


# In[881]:


df['Side effect of medication 5'].fillna(method = 'ffill',inplace = True)


# In[882]:


#df['Side effect of medication 5'] = df['Side effect of medication 5'].map({'0' : 0,'hypotension' : 1})


# In[883]:


df['Side effect of medication 5'].isnull().sum()


# In[884]:


df['Side effect of medication 5'].dtypes


# # onset of side effect post starting med 5 ( in days)

# In[885]:


df['onset of side effect post starting med 5 ( in days)'].dtypes


# In[886]:


df['onset of side effect post starting med 5 ( in days)'].isnull().sum()


# In[887]:


df['onset of side effect post starting med 5 ( in days)'].fillna(method = 'ffill',inplace = True)


# In[888]:


df['onset of side effect post starting med 5 ( in days)'].isnull().sum()


# In[889]:


df['onset of side effect post starting med 5 ( in days)'].dtypes


# # total duration of side effect of medication 5 (in days)

# In[890]:


df['total duration of side effect of medication 5 (in days)'].dtypes


# In[891]:


df['total duration of side effect of medication 5 (in days)'].isnull().sum()


# In[892]:


df['total duration of side effect of medication 5 (in days)'].fillna(0,inplace = True)


# In[893]:


df['total duration of side effect of medication 5 (in days)'].isnull().sum()


# # name of Medication 6

# In[894]:


df['name of Medication 6'].dtypes


# In[895]:


df['name of Medication 6'].isnull().sum()


# In[896]:


df['name of Medication 6'].unique()


# # Medication 6 starting dose

# In[897]:


df['Medication 6 starting dose'].dtypes


# In[898]:


df['Medication 6 starting dose'].isnull().sum()


# # Avg dose of medication 6

# In[899]:


df['Avg dose of medication 6'].dtypes


# In[900]:


df['Avg dose of medication 6'].isnull().sum()


# # Maximum dose of medication 6

# In[901]:


df['Maximum dose of medication 6'].dtypes


# In[902]:


df['Maximum dose of medication 6'].isnull().sum()


# # Total duration of medication 6

# In[903]:


df['Total duration of medication 6'].dtypes


# In[904]:


df['Total duration of medication 6'].isnull().sum()


# # continued medication 6/stopped/changed
# 
# ### nil' : 0, 'changed d/t poor tolerance' : 1, 'changed d/t non response' : 2,
# ###       'continued' : 3, 'reduced d/t resolution' : 4, 'stopped' : 5, 
# ###       'loss to follow-up' : 6

# In[905]:


df['continued medication 6/stopped/changed'].dtypes


# In[906]:


df['continued medication 6/stopped/changed'].unique()


# In[907]:


df['continued medication 6/stopped/changed'].isnull().sum()


# In[908]:


#df['continued medication 6/stopped/changed'] = df['continued medication 6/stopped/changed'].map({'0' : 0, 'changed d/t poor tolerance' : 1, 'changed d/t non response' : 2,
 #      'continued' : 3, 'reduced d/t resolution' : 4, 'stopped' : 5, 
  #     'loss to follow-up' : 6})


# In[909]:


df['continued medication 6/stopped/changed'].unique()


# In[910]:


df['continued medication 6/stopped/changed'].isnull().sum()


# In[911]:


df['continued medication 6/stopped/changed'].fillna(method = 'ffill',inplace = True)


# In[912]:


df['continued medication 6/stopped/changed'].dtypes


# # Response to medication 6(Good/partial/no)
# 
# ### 'nil' : 0,'partial' : 2, 'good' : 1, 'no' : 3

# In[913]:


df['Response to medication 6(Good/partial/no)'].dtypes


# In[914]:


df['Response to medication 6(Good/partial/no)'].unique()


# In[915]:


df['Response to medication 6(Good/partial/no)'].isnull().sum()


# In[916]:


#df['Response to medication 6(Good/partial/no)'] = df['Response to medication 6(Good/partial/no)'].map({'0' : 0,'partial' : 2, 'good' : 1, 'no' : 3})


# In[917]:


df['Response to medication 6(Good/partial/no)'].unique()


# In[918]:


df['Response to medication 6(Good/partial/no)'].isnull().sum()


# In[919]:


df['Response to medication 6(Good/partial/no)'].dtypes


# # Side effect of medication 6

# In[920]:


df['Side effect of medication 6'].dtypes


# In[921]:


df['Side effect of medication 6'].unique()


# In[922]:


#df['Side effect of medication 6'] = df['Side effect of medication 6'].map({'0' : 0, 'skin rashes' : 1, 'switch to mania' : 2})


# In[923]:


df['Side effect of medication 6'].unique()


# In[924]:


df['Side effect of medication 6'].isnull().sum()


# In[925]:


df['Side effect of medication 6'].fillna(0,inplace = True)


# In[926]:


df['Side effect of medication 6'].dtypes


# In[927]:


df['Side effect of medication 6'].isnull().sum()


# # onset of side effect post starting med 6 ( in days)

# In[928]:


df['onset of side effect post starting med 6 ( in days)'].dtypes


# In[929]:


df['onset of side effect post starting med 6 ( in days)'].unique()


# In[930]:


df['onset of side effect post starting med 6 ( in days)'].replace('77.1',77,inplace = True)


# In[931]:


df['onset of side effect post starting med 6 ( in days)'].replace('ni',0,inplace = True)


# In[932]:


df['onset of side effect post starting med 6 ( in days)'].replace('nil',0,inplace = True)


# In[933]:


df['onset of side effect post starting med 6 ( in days)'].unique()


# In[934]:


df['onset of side effect post starting med 6 ( in days)'].dtypes


# In[935]:


df['onset of side effect post starting med 6 ( in days)'].isnull().sum()


# In[936]:


df['onset of side effect post starting med 6 ( in days)'].fillna(0,inplace = True)


# In[937]:


df['onset of side effect post starting med 6 ( in days)'].isnull().sum()


# In[938]:


df['onset of side effect post starting med 6 ( in days)'] = df['onset of side effect post starting med 6 ( in days)'].astype(int)


# In[939]:


df['onset of side effect post starting med 6 ( in days)'].dtypes


# In[940]:


df['onset of side effect post starting med 6 ( in days)'].isnull().sum()


# # total duration of side effect of medication 6 (in days)

# In[941]:


df['total duration of side effect of medication 6 (in days)'].dtypes


# In[942]:


df['total duration of side effect of medication 6 (in days)'].isnull().sum()


# In[943]:


df['total duration of side effect of medication 6 (in days)'].fillna(0,inplace = True)


# In[944]:


df['total duration of side effect of medication 6 (in days)'].isnull().sum()


# # Medication possession ratios 6(MPRs) in lgb;x-syrup

# In[945]:


df['Medication possession ratios 6(MPRs) in lgb;x-syrup'].dtypes


# In[946]:


df['Medication possession ratios 6(MPRs) in lgb;x-syrup'].isnull().sum()


# # name of Medication 7

# In[947]:


df['name of Medication 7'].dtypes


# In[948]:


df['name of Medication 7'].unique()


# In[949]:


df['name of Medication 7'].isnull().sum()


# # Medication 7 starting dose

# In[950]:


df['Medication 7 starting dose'].dtypes


# In[951]:


df['Medication 7 starting dose'].isnull().sum()


# # Avg dose of medication 7

# In[952]:


df['Avg dose of medication 7'].dtypes


# In[953]:


df['Avg dose of medication 7'].isnull().sum()


# # Maximum dose of medication 7

# In[954]:


df['Maximum dose of medication 7'].dtypes


# In[955]:


df['Maximum dose of medication 7'].isnull().sum()


# # Total duration of medication 7

# In[956]:


df['Total duration of medication 7'].dtypes


# In[957]:


df['Total duration of medication 7'].isnull().sum()


# # continued medication 7/stopped/changed
# 
# ### 'nil : 0', 'stopped' : 1, 'reduced d/t resolution' : 2, 'continued' : 3,
# ###       'changed d/t non response' : 4, 'loss to follow-up': 5

# In[958]:


df['continued medication 7/stopped/changed'].dtypes


# In[959]:


df['continued medication 7/stopped/changed'].isnull().sum()


# In[960]:


df['continued medication 7/stopped/changed'].unique()


# In[961]:


#df['continued medication 7/stopped/changed'] = df['continued medication 7/stopped/changed'].map({'0' : 0, 'stopped' : 1, 'reduced d/t resolution' : 2, 'continued' : 3,
 #      'changed d/t non response' : 4,'loss to follow-up' : 5})


# In[962]:


df['continued medication 7/stopped/changed'].unique()


# In[963]:


df['continued medication 7/stopped/changed'] .isnull().sum()


# In[964]:


df['continued medication 7/stopped/changed'].fillna(method = 'ffill',inplace = True)


# In[965]:


df['continued medication 7/stopped/changed'].isnull().sum()


# In[966]:


df['continued medication 7/stopped/changed'].dtypes


# # Response to medication 7(Good/partial/no)
# 
# ### 'nil' : 0, 'good' : 1, 'partial' : 2, 'no': 3

# In[967]:


df['Response to medication 7(Good/partial/no)'].dtypes


# In[968]:


df['Response to medication 7(Good/partial/no)'].isnull().sum()


# In[969]:


df['Response to medication 7(Good/partial/no)'].unique()


# In[970]:


#df['Response to medication 7(Good/partial/no)'] = df['Response to medication 7(Good/partial/no)'].map({'0' : 0, 'good' : 1, 'partial' : 2, 'no': 3})


# In[971]:


df['Response to medication 7(Good/partial/no)'].unique()


# In[972]:


df['Response to medication 7(Good/partial/no)'].fillna(method = 'ffill',inplace = True)


# In[973]:


df['Response to medication 7(Good/partial/no)'].isnull().sum()


# # Side effect of medication 7

# In[974]:


df['Side effect of medication 7'].dtypes


# In[975]:


df['Side effect of medication 7'].unique()


# In[976]:


df['Side effect of medication 7'].isnull().sum()


# In[977]:


#df['Side effect of medication 7'] = df['Side effect of medication 7'].map({'weight gain' : 1,'0' : 0})


# In[978]:


df['Side effect of medication 7'].isnull().sum()


# In[979]:


df['Side effect of medication 7'].dtypes


# # onset of side effect post starting med 7 ( in days)

# In[980]:


df['onset of side effect post starting med 7 ( in days)'].dtypes


# In[981]:


df['onset of side effect post starting med 7 ( in days)'].isnull().sum()


# In[982]:


df['onset of side effect post starting med 7 ( in days)'].unique()


# In[983]:


df['onset of side effect post starting med 7 ( in days)'].replace(115.7,115,inplace = True)


# In[984]:


df['onset of side effect post starting med 7 ( in days)'].unique()


# In[985]:


df['onset of side effect post starting med 7 ( in days)'] = df['onset of side effect post starting med 7 ( in days)'].astype(int)


# In[986]:


df['onset of side effect post starting med 7 ( in days)'].dtypes


# # total duration of side effect of medication 7 (in days)

# In[987]:


df['total duration of side effect of medication 7 (in days)'].dtypes


# In[988]:


df['total duration of side effect of medication 7 (in days)'].isnull().sum()


# In[989]:


df['total duration of side effect of medication 7 (in days)'].unique()


# # Medication possession ratios 7(MPRs) in lgb;x-syrup

# In[990]:


df['Medication possession ratios 7(MPRs) in lgb;x-syrup'].dtypes


# In[991]:


df['Medication possession ratios 7(MPRs) in lgb;x-syrup'].isnull().sum()


# # name of Medication 8

# In[992]:


df['name of Medication 8'].dtypes


# In[993]:


df['name of Medication 8'].isnull().sum()


# In[994]:


df['name of Medication 8'].unique()


# # Medication 8 starting dose

# In[995]:


df['Medication 8 starting dose'].dtypes


# In[996]:


df['Medication 8 starting dose'].isnull().sum()


# In[997]:


df['Medication 8 starting dose'].unique()


# # Avg dose of medication 8

# In[998]:


df['Avg dose of medication 8'].dtypes


# In[999]:


df['Avg dose of medication 8'].isnull().sum()


# In[1000]:


df['Avg dose of medication 8'].unique()


# # Maximum dose of medication 8

# In[1001]:


df['Maximum dose of medication 8'].dtypes


# In[1002]:


df['Maximum dose of medication 8'].isnull().sum()


# In[1003]:


df['Maximum dose of medication 8'].unique()


# # Total duration of medication 8

# In[1004]:


df['Total duration of medication 8'].dtypes


# In[1005]:


df['Total duration of medication 8'].isnull().sum()


# In[1006]:


df['Total duration of medication 8'].unique()


# # Continued medication 8/stopped/changed
# 
# ### 'nil' : 0, 'continued' : 1, 'stopped' : 2, 'loss to follow-up' : 3

# In[1007]:


df['Continued medication 8/stopped/changed'].dtypes


# In[1008]:


df['Continued medication 8/stopped/changed'].unique()


# In[1009]:


df['Continued medication 8/stopped/changed'].isnull().sum()


# In[1010]:


#df['Continued medication 8/stopped/changed'] = df['Continued medication 8/stopped/changed'].map({'0' : 0, 'continued' : 1, 'stopped' : 2, 'loss to follow-up': 3})


# In[1011]:


df['Continued medication 8/stopped/changed'].unique()


# In[1012]:


df['Continued medication 8/stopped/changed'].isnull().sum()


# In[1013]:


df['Continued medication 8/stopped/changed'].dtypes


# # Response to medication 8(Good/partial/no)
# 
# ### '0' : 0, 'good' : 1, 'partial' : 2, 'no' : 3}

# In[1014]:


df['Response to medication 8(Good/partial/no)'].dtypes


# In[1015]:


df['Response to medication 8(Good/partial/no)'].unique()


# In[1016]:


df['Response to medication 8(Good/partial/no)'].isnull().sum()


# In[1017]:


#df['Response to medication 8(Good/partial/no)'] = df['Response to medication 8(Good/partial/no)'].map({'0' : 0, 'good' : 1, 'partial' : 2, 'no' : 3})


# In[1018]:


df['Response to medication 8(Good/partial/no)'].unique()


# In[1019]:


df['Response to medication 8(Good/partial/no)'].isnull().sum()


# In[1020]:


df['Response to medication 8(Good/partial/no)'].fillna(method = 'ffill',inplace = True)


# In[1021]:


df['Response to medication 8(Good/partial/no)'].isnull().sum()


# In[1022]:


df['Response to medication 8(Good/partial/no)'].dtypes


# # Side effect of medication 8

# In[1023]:


df['Side effect of medication 8'].dtypes


# In[1024]:


df['Side effect of medication 8'].isnull().sum()


# In[1025]:


df['Side effect of medication 8'].unique()


# # onset of side effect post starting med 8 ( in days)

# In[1026]:


df['onset of side effect post starting med 8 ( in days)'].dtypes


# In[1027]:


df['onset of side effect post starting med 8 ( in days)'].isnull().sum()


# In[1028]:


df['onset of side effect post starting med 8 ( in days)'].unique()


# # total duration of side effect of medication 8 (in days)

# In[1029]:


df['total duration of side effect of medication 8 (in days)'].dtypes


# In[1030]:


df['total duration of side effect of medication 8 (in days)'].isnull().sum()


# In[1031]:


df['total duration of side effect of medication 8 (in days)'].unique()


# # Medication possession ratios 8(MPRs) in lgb;x-syrup

# In[1032]:


df['Medication possession ratios 8(MPRs) in lgb;x-syrup'].dtypes


# In[1033]:


df['Medication possession ratios 8(MPRs) in lgb;x-syrup'].isnull().sum()


# In[1034]:


df['Medication possession ratios 8(MPRs) in lgb;x-syrup'].unique()


# In[1035]:


df['Medication possession ratios 8(MPRs) in lgb;x-syrup'].replace('x',0,inplace = True)


# In[1036]:


df['Medication possession ratios 8(MPRs) in lgb;x-syrup'].unique()


# In[1037]:


df['Medication possession ratios 8(MPRs) in lgb;x-syrup'] = df['Medication possession ratios 8(MPRs) in lgb;x-syrup'].astype(float)


# In[1038]:


df['Medication possession ratios 8(MPRs) in lgb;x-syrup'].dtypes


# # name of Medication 9
# 
# ### 0' :0, 'chlorpromazine' : 1, 'lithium' : 2, 'atomoxetine' : 3, 'melatonin' : 4,
# ###       'thyroxin' : 5, 'clonidine' : 6, 'methylphenidate' : 7
# 

# In[1039]:


df['name of Medication 9'].dtypes


# In[1040]:


df['name of Medication 9'].unique()


# In[1041]:


df['name of Medication 9'].isnull().sum()


# In[1042]:


##df['name of Medication 9'] = df['name of Medication 9'].map({'0' :0, 'chlorpromazine' : 1, 'lithium' : 2, 'atomoxetine' : 3, 'melatonin' : 4,
       'thyroxin' : 5, 'clonidine' : 6, 'methylphenidate' : 7})


# In[1043]:


df['name of Medication 9'].unique()


# In[1044]:


df['name of Medication 9'].isnull().sum()


# # Medication 9 starting dose

# In[1045]:


df['Medication 9 starting dose'].dtypes


# In[1046]:


df['Medication 9 starting dose'].unique()


# In[1047]:


df['Medication 9 starting dose'].isnull().sum()


# # Avg dose of medication 9

# In[1048]:


df['Avg dose of medication 9'].dtypes


# In[1049]:


df['Avg dose of medication 9'].isnull().sum()


#  # Maximum dose of medication 9

# In[1050]:


df['Maximum dose of medication 9'].dtypes


# In[1051]:


df['Maximum dose of medication 9'].isnull().sum()


# # Total duration of medication 9

# In[1052]:


df['Total duration of medication 9'].dtypes


# In[1053]:


df['Total duration of medication 9'].isnull().sum()


# # continued medication 9/stopped/changed
# 
# 
# ###  'nil' : 0, 'stopped' : 1,'continued' : 2, 'loss to follow-up' : 3})

# In[1054]:


df['continued medication 9/stopped/changed'].dtypes


# In[1055]:


df['continued medication 9/stopped/changed'].unique()


# In[1056]:


df['continued medication 9/stopped/changed'].isnull().sum()


# In[1057]:


df['continued medication 9/stopped/changed'].fillna(0,inplace = True)


# In[1058]:


#df['continued medication 9/stopped/changed'] = df['continued medication 9/stopped/changed'].map({'0' : 0, 'stopped' : 1,'continued' : 2, 'loss to follow-up' : 3})


# In[1059]:


df['continued medication 9/stopped/changed'].unique()


# In[1060]:


df['continued medication 9/stopped/changed'].isnull().sum()


# In[1061]:


df['continued medication 9/stopped/changed'].dtypes 


# # Response to medication 9(Good/partial/no)
# 
# ###  'nil' : 0, 'good' : 1,'no' : 2

# In[1062]:


df['Response to medication 9(Good/partial/no)'].dtypes


# In[1063]:


df['Response to medication 9(Good/partial/no)'].unique()


# In[1064]:


df['Response to medication 9(Good/partial/no)'].isnull().sum()


# In[1065]:


df['Response to medication 9(Good/partial/no)'].fillna(0,inplace = True)


# In[1066]:


#df['Response to medication 9(Good/partial/no)'] = df['Response to medication 9(Good/partial/no)'].map({'0' : 0, 'good' : 1,'no' : 2})


# In[1067]:


df['Response to medication 9(Good/partial/no)'].unique()


# In[1068]:


df['Response to medication 9(Good/partial/no)'].fillna(0,inplace = True)


# In[1069]:


df['Response to medication 9(Good/partial/no)'].unique()


# In[1070]:


df['Response to medication 9(Good/partial/no)'].dtypes


# # Side effect of medication 9

# In[1071]:


df['Side effect of medication 9'].dtypes


# In[1072]:


df['Side effect of medication 9'].unique()


# In[1073]:


df['Side effect of medication 9'].isnull().sum()


# # onset of side effect post starting med 9 ( in days)

# In[1074]:


df['onset of side effect post starting med 9 ( in days)'].dtypes


# In[1075]:


df['onset of side effect post starting med 9 ( in days)'].unique()


# In[1076]:


df['onset of side effect post starting med 9 ( in days)'].isnull().sum()


# # total duration of side effect of medication 9 (in days)

# In[1077]:


df['total duration of side effect of medication 9 (in days)'].dtypes


# In[1078]:


df['total duration of side effect of medication 9 (in days)'].unique()


# In[1079]:


df['total duration of side effect of medication 9 (in days)'].isnull().sum()


# # Medication possession ratios 9(MPRs) in lgb;x-syrup

# In[1080]:


df['Medication possession ratios 9(MPRs) in lgb;x-syrup'].dtypes


# In[1081]:


df['Medication possession ratios 9(MPRs) in lgb;x-syrup'].unique()


# In[1082]:


df['Medication possession ratios 9(MPRs) in lgb;x-syrup'].isnull().sum()


# # name of Medication 10
# 
# 
# ### '0' : 0, 'melatonin' : 1, 'risperidone' : 2, 'aripiprazole' : 3, 'methylphenidate' :4,
# ###       'lorazepam' : 5})

# In[1083]:


df['name of Medication 10'].dtypes


# In[1084]:


df['name of Medication 10'].unique()


# In[1085]:


df['name of Medication 10'].isnull().sum()


# In[1086]:


#df['name of Medication 10'] = df['name of Medication 10'].map({'0' : 0, 'melatonin' : 1, 'risperidone' : 2, 'aripiprazole' : 3, 'methylphenidate' :4,
       'lorazepam' : 5})


# In[1087]:


df['name of Medication 10'].unique()


# In[1088]:


df['name of Medication 10'].isnull().sum()


# In[1089]:


df['name of Medication 10'].dtypes


# # Medication 10 starting dose

# In[1090]:


df['Medication 10 starting dose'].dtypes


# In[1091]:


df['Medication 10 starting dose'].isnull().sum()


# In[1092]:


df['Medication 10 starting dose'].unique()


# # Avg dose of medication 10

# In[1093]:


df['Avg dose of medication 10'].dtypes


# In[1094]:


df['Avg dose of medication 10'].isnull().sum()


# In[1095]:


df['Avg dose of medication 10'].unique()


# # Maximum dose of medication 10

# In[1096]:


df['Maximum dose of medication 10'].dtypes


# In[1097]:


df['Maximum dose of medication 10'].isnull().sum()


# In[1098]:


df['Maximum dose of medication 10'].unique()


# # Total duration of medication 10

# In[1099]:


df['Total duration of medication 10'].dtypes


# In[1100]:


df['Total duration of medication 10'].isnull().sum()


# In[1101]:


df['Total duration of medication 10'].unique()


# # continued medication 10/stopped/changed
# 
# ### 'Nil' : 0, 'continued' : 1, 'stopped' :2

# In[1102]:


df['continued medication 10/stopped/changed'].dtypes


# In[1103]:


df['continued medication 10/stopped/changed'].isnull().sum()


# In[1104]:


df['continued medication 10/stopped/changed'].unique()


# In[1105]:


#df['continued medication 10/stopped/changed'] = df['continued medication 10/stopped/changed'].map({'0' : 0, 'continued' : 1, 'stopped' :2})


# In[1106]:


df['continued medication 10/stopped/changed'].unique()


# In[1107]:


df['continued medication 10/stopped/changed'].fillna(0,inplace = True)


# In[1108]:


df['continued medication 10/stopped/changed'].isnull().sum()


# In[1109]:


df['continued medication 10/stopped/changed'].dtypes


# # Response to medication 10(Good/partial/no)
# 
# ### 'nil' : 0, 'good' : 1, 'partial' : 2

# In[1110]:


df['Response to medication 10(Good/partial/no)'].dtypes


# In[1111]:


df['Response to medication 10(Good/partial/no)'].unique()


# In[1112]:


df['Response to medication 10(Good/partial/no)'].isnull().sum()


# In[1113]:


#df['Response to medication 10(Good/partial/no)'] = df['Response to medication 10(Good/partial/no)'].map({'0' : 0, 'good' : 1, 'partial' : 2})


# In[1114]:


df['Response to medication 10(Good/partial/no)'].unique()


# In[1115]:


df['Response to medication 10(Good/partial/no)'].isnull().sum()


# In[1116]:


df['Response to medication 10(Good/partial/no)'].fillna(method = 'ffill',inplace = True)


# In[1117]:


df['Response to medication 10(Good/partial/no)'].isnull().sum()


# In[1118]:


df['Response to medication 10(Good/partial/no)'].dtypes


# # Side effect of medication 10

# In[1119]:


df['Side effect of medication 10'].dtypes


# In[1120]:


df['Side effect of medication 10'].unique()


# In[1121]:


df['Side effect of medication 10'].isnull().sum()


# In[1122]:


df['Side effect of medication 10'].fillna(0,inplace = True)


# In[1123]:


df['Side effect of medication 10'].isnull().sum()


# In[1124]:


df['Side effect of medication 10'].unique()


# # onset of side effect post starting med 10 ( in days)

# In[1125]:


df['onset of side effect post starting med 10 ( in days)'].dtypes


# In[1126]:


df['onset of side effect post starting med 10 ( in days)'].unique()


# In[1127]:


df['onset of side effect post starting med 10 ( in days)'].isnull().sum()


# # total duration of side effect of medication 10 (in days)

# In[1128]:


df['total duration of side effect of medication 10 (in days)'].dtypes


# In[1129]:


df['total duration of side effect of medication 10 (in days)'].isnull().sum()


# In[1130]:


df['total duration of side effect of medication 10 (in days)'].unique()


# # Medication possession ratios 10(MPRs) in lgb;x-syrup

# In[1131]:


df['Medication possession ratios 10(MPRs) in lgb;x-syrup'].dtypes


# In[1132]:


df['Medication possession ratios 10(MPRs) in lgb;x-syrup'].isnull().sum()


# In[1133]:


df['Medication possession ratios 10(MPRs) in lgb;x-syrup'].unique()


# In[1134]:


df['Medication possession ratios 10(MPRs) in lgb;x-syrup'].fillna(0,inplace = True)


# # name of Medication 11
# 
# ### nil' : 0, 'clomipramine' : 1, 'melatonin' : 2, 'trihexyphenidyl' : 3, 'zolpidem': 4,
# ###       'clobazam' : 5

# In[1135]:


df['name of Medication 11'].dtypes


# In[1136]:


df['name of Medication 11'].isnull().sum()


# In[1137]:


df['name of Medication 11'].unique()


# In[1138]:


#df['name of Medication 11'] = df['name of Medication 11'].map({'0' : 0, 'clomipramine' : 1, 'melatonin' : 2, 'trihexyphenidyl' : 3, 'zolpidem': 4,
 #      'clobazam' : 5})


# In[1139]:


df['name of Medication 11'].unique()


# In[1140]:


df['name of Medication 11'].isnull().sum()


# In[1141]:


df['name of Medication 11'].dtypes


#  # Medication 11 starting dose

# In[1142]:


df['Medication 11 starting dose'].dtypes


# In[1143]:


df['Medication 11 starting dose'].unique()


# In[1144]:


df['Medication 11 starting dose'].isnull().sum()


# # Avg dose of medication 11

# In[1145]:


df['Avg dose of medication 11'].dtypes


# In[1146]:


df['Avg dose of medication 11'].unique()


# In[1147]:


df['Avg dose of medication 11'].isnull().sum()


# # Maximum dose of medication 11

# In[1148]:


df['Maximum dose of medication 11'].dtypes


# In[1149]:


df['Maximum dose of medication 11'].unique()


# In[1150]:


df['Maximum dose of medication 11'].isnull().sum()


# # Total duration of medication 11

# In[1151]:


df['Total duration of medication 11'].dtypes


# In[1152]:


df['Total duration of medication 11'].unique()


# In[1153]:


df['Total duration of medication 11'].isnull().sum()


# # continued medication 11/stopped/changed
# 
#  ### 'nil' : 0, 'continued' : 1, 'stopped' : 2, 'loss to follow-up' : 3

# In[1154]:


df['continued medication 11/stopped/changed'].dtypes


# In[1155]:


df['continued medication 11/stopped/changed'].unique()


# In[1156]:


#df['continued medication 11/stopped/changed'] = df['continued medication 11/stopped/changed'].map({'0' : 0, 'continued' : 1, 'stopped' : 2, 'loss to follow-up' : 3})


# In[1157]:


df['continued medication 11/stopped/changed'].unique()


# In[1158]:


df['continued medication 11/stopped/changed'].isnull().sum()


# # Response to medication 11(Good/partial/no)
# 
# ### 'Nil' : 0, 'good' : 1, 'partial' :2, 'no' : 3

# In[1159]:


df['Response to medication 11(Good/partial/no)'].dtypes


# In[1160]:


df['Response to medication 11(Good/partial/no)'].unique()


# In[1161]:


df['Response to medication 11(Good/partial/no)'].isnull().sum()


# In[1162]:


df['Response to medication 11(Good/partial/no)'].fillna(0,inplace = True)


# In[1163]:


#df['Response to medication 11(Good/partial/no)'] = df['Response to medication 11(Good/partial/no)'].map({'0' : 0, 'good' : 1, 'partial' :2, 'no' : 3})


# In[1164]:


df['Response to medication 11(Good/partial/no)'].isnull().sum()


# In[1165]:


df['Response to medication 11(Good/partial/no)'].fillna(0,inplace = True)


# In[1166]:


df['Response to medication 11(Good/partial/no)'].isnull().sum()


# # Side effect of medication 11

# In[1167]:


df['Side effect of medication 11'].dtypes


# In[1168]:


df['Side effect of medication 11'].unique()


# In[1169]:


df['Side effect of medication 11'].isnull().sum()


# # onset of side effect post starting med 11 ( in days)

# In[1170]:


df['total duration of side effect of medication 11 (in days)'].dtypes


# In[1171]:


df['total duration of side effect of medication 11 (in days)'].unique()


# In[1172]:


df['total duration of side effect of medication 11 (in days)'].isnull().sum()


# In[1173]:


df['total duration of side effect of medication 11 (in days)'].unique()


# # Medication possession ratios 11(MPRs) in lgb;x-syrup

# In[1174]:


df['Medication possession ratios 11(MPRs) in lgb;x-syrup'].dtypes


# In[1175]:


df['Medication possession ratios 11(MPRs) in lgb;x-syrup'].unique()


# In[1176]:


df['Medication possession ratios 11(MPRs) in lgb;x-syrup'].isnull().sum()


# # name of Medication 12
# 
# ### 'nil' : 0, 'trihexyphenidyl' : 1, 'clonidine' : 2, 'lithium' : 3, 'clonazepam' : 4

# In[1177]:


df['name of Medication 12'].dtypes


# In[1178]:


df['name of Medication 12'].unique()


# In[1179]:


df['name of Medication 12'].isnull().sum()


# In[1180]:


#df['name of Medication 12'] = df['name of Medication 12'].map({'0' : 0, 'trihexyphenidyl' : 1, 'clonidine' : 2, 'lithium' : 3, 'clonazepam' : 4})


# In[1181]:


df['name of Medication 12'].isnull().sum()


# In[1182]:


df['name of Medication 12'].unique()


# # Medication 12 starting dose

# In[1183]:


df['Medication 12 starting dose'].dtypes


# In[1184]:


df['Medication 12 starting dose'].unique()


# In[1185]:


df['Medication 12 starting dose'].replace('nilnil',0,inplace = True)


# In[1186]:


df['Medication 12 starting dose'].unique()


# In[1187]:


df['Medication 12 starting dose'] = df['Medication 12 starting dose'].astype(float)


# In[1188]:


df['Medication 12 starting dose'].dtypes


# In[1189]:


df['Medication 12 starting dose'].isnull().sum()


# # Avg dose of medication 12

# In[1190]:


df['Avg dose of medication 12'].dtypes


# In[1191]:


df['Avg dose of medication 12'].isnull().sum()


# In[1192]:


df['Avg dose of medication 12'].unique()


# # Maximum dose of medication 12

# In[1193]:


df['Maximum dose of medication 12'].dtypes


# In[1194]:


df['Maximum dose of medication 12'].isnull().sum()


# In[1195]:


df['Maximum dose of medication 12'].unique()


# # Total duration of medication 12

# In[1196]:


df['Total duration of medication 12'].dtypes


# In[1197]:


df['Total duration of medication 12'].isnull().sum()


# In[1198]:


df['Total duration of medication 12'].unique()


# # continued medication 12/stopped/changed

# In[1199]:


df['continued medication 12/stopped/changed'].dtypes


# In[1200]:


df['continued medication 12/stopped/changed'].isnull().sum()


# In[1201]:


df['continued medication 12/stopped/changed'].unique()


# In[1202]:


#df['continued medication 12/stopped/changed'] = df['continued medication 12/stopped/changed'].map({'0' : 0, 'continued' :1,'stopped' : 2})


# In[1203]:


df['continued medication 12/stopped/changed'].isnull().sum()


# In[1204]:


df['continued medication 12/stopped/changed'].fillna(0,inplace = True)


# In[1205]:


df['continued medication 12/stopped/changed'].isnull().sum()


# In[1206]:


df['continued medication 12/stopped/changed'].dtypes


# # Response to medication 12(Good/partial/no)
# 
# ### 'nil' : 0, 'good' : 1, 'partial' : 2

# In[1207]:


df['Response to medication 12(Good/partial/no)'].dtypes


# In[1208]:


df['Response to medication 12(Good/partial/no)'].isnull().sum()


# In[1209]:


df['Response to medication 12(Good/partial/no)'].unique()


# In[1210]:


#df['Response to medication 12(Good/partial/no)'] = df['Response to medication 12(Good/partial/no)'].map({'0' : 0, 'good' : 1, 'partial' : 2})


# In[1211]:


df['Response to medication 12(Good/partial/no)'].unique()


# In[1212]:


df['Response to medication 12(Good/partial/no)'].fillna(0,inplace = True )


# In[1213]:


df['Response to medication 12(Good/partial/no)'].isnull().sum()


# # Side effect of medication 12

# In[1214]:


df['Side effect of medication 12'].dtypes


# In[1215]:


df['Side effect of medication 12'].unique()


# In[1216]:


df['Side effect of medication 12'].isnull().sum()


# # onset of side effect post starting med 12 ( in days)

# In[1217]:


df['onset of side effect post starting med 12 ( in days)'].dtypes


# In[1218]:


df['onset of side effect post starting med 12 ( in days)'].unique()


# In[1219]:


df['onset of side effect post starting med 12 ( in days)'].isnull().sum()


# # total duration of side effect of medication 12 (in days)

# In[1220]:


df['total duration of side effect of medication 12 (in days)'].dtypes


# In[1221]:


df['total duration of side effect of medication 12 (in days)'].unique()


# In[1222]:


df['total duration of side effect of medication 12 (in days)'].isnull().sum()


# # Medication possession ratios 12(MPRs) in lgb;x-syrup

# In[1223]:


df['Medication possession ratios 12(MPRs) in lgb;x-syrup'].dtypes


# In[1224]:


df['Medication possession ratios 12(MPRs) in lgb;x-syrup'].unique()


# In[1225]:


df['Medication possession ratios 12(MPRs) in lgb;x-syrup'].isnull().sum()


# # name of Medication 13
# 
# 
# ### '0' : 0, 'clonazepam' : 1

# In[1226]:


df['name of Medication 13'].dtypes


# In[1227]:


df['name of Medication 13'].unique()


# In[1228]:


#df['name of Medication 13'] = df['name of Medication 13'].map({'0' : 0, 'clonazepam' : 1})


# In[1229]:


df['name of Medication 13'].unique()


# In[1230]:


df['name of Medication 13'].isnull().sum()


# # Medication 13 starting dose
# 

# In[1231]:


df['Medication 13 starting dose'].dtypes


# In[1232]:


df['Medication 13 starting dose'].unique()


# In[1233]:


df['Medication 13 starting dose'].isnull().sum()


# # Avg dose of medication 13

# In[1234]:


df['Avg dose of medication 13'].dtypes


# In[1235]:


df['Avg dose of medication 13'].unique()


# In[1236]:


df['Avg dose of medication 13'].isnull().sum()


# # Maximum dose of medication 13

# In[1237]:


df['Maximum dose of medication 13'].dtypes


# In[1238]:


df['Maximum dose of medication 13'].unique()


# In[1239]:


df['Maximum dose of medication 13'].isnull().sum()


# # Total duration of medication 13

# In[1240]:


df['Total duration of medication 13'].dtypes


# In[1241]:


df['Total duration of medication 13'].unique()


# In[1242]:


df['Total duration of medication 13'].isnull().sum()


# # continued medication 13/stopped/changed
# 
# ### '0' : 0, 'continued' : 1

# In[1243]:


df['continued medication 13/stopped/changed'].dtypes


# In[1244]:


df['continued medication 13/stopped/changed'].unique()


# In[1245]:


#df['continued medication 13/stopped/changed'] = df['continued medication 13/stopped/changed'].map({'0' : 0, 'continued' :1})


# In[1246]:


df['continued medication 13/stopped/changed'].unique()


# In[1247]:


df['continued medication 13/stopped/changed'].isnull().sum()
                                                           


# In[1248]:


df['continued medication 13/stopped/changed'].fillna(0,inplace = True)


# In[1249]:


df['continued medication 13/stopped/changed'].isnull().sum()


# # Response to medication 13(Good/partial/no)
# 
# ### '0' : 0, 'good' : 1

# In[1250]:


df['Response to medication 13(Good/partial/no)'].dtypes


# In[1251]:


df['Response to medication 13(Good/partial/no)'].unique()


# In[1252]:


#df['Response to medication 13(Good/partial/no)'] = df['Response to medication 13(Good/partial/no)'].map({'0' : 0, 'good' : 1})


# In[1253]:


df['Response to medication 13(Good/partial/no)'].isnull().sum()


# In[1254]:


df['Response to medication 13(Good/partial/no)'].fillna(0,inplace = True)


# In[1255]:


df['Response to medication 13(Good/partial/no)'].isnull().sum()


# # Side effect of medication 13

# In[1256]:


df['Side effect of medication 13'].dtypes


# In[1257]:


df['Side effect of medication 13'].isnull().sum()


# In[1258]:


df['Side effect of medication 13'].unique()


#  # onset of side effect post starting med 13 ( in days)

# In[1259]:


df['onset of side effect post starting med 13 ( in days)'].dtypes


# In[1260]:


df['onset of side effect post starting med 13 ( in days)'].isnull().sum()


# In[1261]:


df['onset of side effect post starting med 13 ( in days)'].unique()


# # total duration of side effect of medication 13 (in days)

# In[1262]:


df['total duration of side effect of medication 13 (in days)'].dtypes


# In[1263]:


df['total duration of side effect of medication 13 (in days)'].isnull().sum()


# In[1264]:


df['total duration of side effect of medication 13 (in days)'].unique()


# # Medication possession ratios 13(MPRs) in lgb;x-syrup

# In[1265]:


df['Medication possession ratios 13(MPRs) in lgb;x-syrup'].dtypes


# In[1266]:


df['Medication possession ratios 13(MPRs) in lgb;x-syrup'].isnull().sum()


# In[1267]:


df['Medication possession ratios 13(MPRs) in lgb;x-syrup'].unique()


# # name of Medication 14
# 
# 
# ### '0' : 0, 'melatonin' : 1

# In[1268]:


df['name of Medication 14'].dtypes


# In[1269]:


df['name of Medication 14'].isnull().sum()


# In[1270]:


df['name of Medication 14'].unique()


# In[1271]:


#df['name of Medication 14'] = df['name of Medication 14'].map({'0' : 0, 'melatonin' : 1})


# In[1272]:


df['name of Medication 14'].isnull().sum()


# In[1273]:


df['name of Medication 14'].unique()


# # Medication 14 starting dose

# In[1274]:


df['Medication 14 starting dose'].dtypes


# In[1275]:


df['Medication 14 starting dose'].unique()


# In[1276]:


df['Medication 14 starting dose'].isnull().sum()


# # Avg dose of medication 14

# In[1277]:


df['Avg dose of medication 14'].dtypes


# In[1278]:


df['Avg dose of medication 14'].unique()


# In[1279]:


df['Avg dose of medication 14'].isnull().sum()


# # Total duration of medication 14

# In[1280]:


df['Total duration of medication 14'].dtypes


# In[1281]:


df['Total duration of medication 14'].isnull().sum()


# In[1282]:


df['Total duration of medication 14'].unique()


# # continued medication 14/stopped/changed
# 
# 
# ### 'nil' : 0, 'stopped' : 1

# In[1283]:


df['continued medication 14/stopped/changed'].dtypes


# In[1284]:


df['continued medication 14/stopped/changed'].isnull().sum()


# In[1285]:


df['continued medication 14/stopped/changed'].unique()


# In[1286]:


#df['continued medication 14/stopped/changed'] = df['continued medication 14/stopped/changed'].map({'0' : 0, 'stopped' : 1})


# In[1287]:


df['continued medication 14/stopped/changed'].isnull().sum()


# In[1288]:


df['continued medication 14/stopped/changed'].fillna(0,inplace = True)


# In[1289]:


df['continued medication 14/stopped/changed'].dtypes


# In[1290]:


df['continued medication 14/stopped/changed'].isnull().sum()


# # Response to medication 14(Good/partial/no)

# In[1291]:


df['Response to medication 14(Good/partial/no)'].dtypes


# In[1292]:


df['Response to medication 14(Good/partial/no)'].unique()


# In[1293]:


#df['Response to medication 14(Good/partial/no)'] = df['Response to medication 14(Good/partial/no)'].map({'0' : 0, 'good' : 1})


# In[1294]:


df['Response to medication 14(Good/partial/no)'].unique()


# In[1295]:


df['Response to medication 14(Good/partial/no)'].fillna(0,inplace = True)


# In[1296]:


df['Response to medication 14(Good/partial/no)'].isnull().sum()


# # Side effect of medication 14

# In[1297]:


df['Side effect of medication 14'].dtypes 


# In[1298]:


df['Side effect of medication 14'].unique()


# In[1299]:


#df['Side effect of medication 14'] = df['Side effect of medication 14'].map({'0' : 0,'sedation' : 1})


# In[1300]:


df['Side effect of medication 14'].isnull().sum()


# # onset of side effect post starting med 14 ( in days)

# In[1301]:


df['onset of side effect post starting med 14 ( in days)'].dtypes


# In[1302]:


df['onset of side effect post starting med 14 ( in days)'].unique()


# In[1303]:


df['onset of side effect post starting med 14 ( in days)'].isnull().sum()


# # total duration of side effect of medication 14 (in days)

# In[1304]:


df['total duration of side effect of medication 14 (in days)'].dtypes


# In[1305]:


df['total duration of side effect of medication 14 (in days)'].unique()


# In[1306]:


df['total duration of side effect of medication 14 (in days)'].isnull().sum()


# # Medication possession ratios 14(MPRs) in lgb;x-syrup

# In[1307]:


df['Medication possession ratios 14(MPRs) in lgb;x-syrup'].dtypes


# In[1308]:


df['Medication possession ratios 14(MPRs) in lgb;x-syrup'].unique()


# In[1309]:


df['Medication possession ratios 14(MPRs) in lgb;x-syrup'].isnull().sum()


# # cost of medication
# 
# ### 'purchased' : 1, 'free' : 2, 'both free and purchased' : 3, 'nil' :0 

# In[1310]:


df['cost of medication'].dtypes


# In[1311]:


df['cost of medication'].unique()


# In[1312]:


df['cost of medication'].isnull().sum()


# In[1313]:


#df['cost of medication'] = df['cost of medication'].map({'purchased' : 1, 'free' : 2, 'both free and purchased' : 3, '0' :0 })


# In[1314]:


df['cost of medication'].unique()


# In[1315]:


df['cost of medication'].isnull().sum()


# In[1316]:


df['cost of medication'].fillna(method = 'ffill',inplace = True)


# In[1317]:


df['cost of medication'].isnull().sum()


# In[1318]:


df['cost of medication'].dtypes


# # Other treatments(rehabilitative intervention/IT/CBT/ipt/FT/PMT/BEHAVIOURAL INTERVENTIONS FOR DEVELOPMENTAL DISORDERS, Combination therapy)

# In[1319]:


df['Other treatments(rehabilitative intervention/IT/CBT/ipt/FT/PMT/BEHAVIOURAL INTERVENTIONS FOR DEVELOPMENTAL DISORDERS, Combination therapy)'].dtypes


# In[1320]:


df['Other treatments(rehabilitative intervention/IT/CBT/ipt/FT/PMT/BEHAVIOURAL INTERVENTIONS FOR DEVELOPMENTAL DISORDERS, Combination therapy)'].unique()


# In[1321]:


df['Other treatments(rehabilitative intervention/IT/CBT/ipt/FT/PMT/BEHAVIOURAL INTERVENTIONS FOR DEVELOPMENTAL DISORDERS, Combination therapy)'].isnull().sum()


# In[1322]:


df['Other treatments(rehabilitative intervention/IT/CBT/ipt/FT/PMT/BEHAVIOURAL INTERVENTIONS FOR DEVELOPMENTAL DISORDERS, Combination therapy)'].fillna(method = 'ffill',inplace = True)


# In[1323]:


df['Other treatments(rehabilitative intervention/IT/CBT/ipt/FT/PMT/BEHAVIOURAL INTERVENTIONS FOR DEVELOPMENTAL DISORDERS, Combination therapy)'].isnull().sum()


# # Maximum duration of symptom free period (in days)

# In[1324]:


df['Maximum duration of symptom free period (in days)'].dtypes


# In[1325]:


df['Maximum duration of symptom free period (in days)'].unique()


# In[1326]:


df['Maximum duration of symptom free period (in days)'].isnull().sum()


# In[1327]:


df['Maximum duration of symptom free period (in days)'].fillna(method = 'bfill',inplace = True)


# In[1328]:


df['Maximum duration of symptom free period (in days)'].isnull().sum()


# In[1329]:


df['Maximum duration of symptom free period (in days)'].dtypes


# # Max Duration of resolution of symptoms before recurrence/relapse (in days)

# In[1330]:


df['Max Duration of resolution of symptoms before recurrence/relapse (in days)'].dtypes


# In[1331]:


df['Max Duration of resolution of symptoms before recurrence/relapse (in days)'].isnull().sum()


# In[1332]:


df['Max Duration of resolution of symptoms before recurrence/relapse (in days)'].fillna(method = 'ffill',inplace = True)


# In[1333]:


df['Max Duration of resolution of symptoms before recurrence/relapse (in days)'].isnull().sum()


# In[1334]:


df['Max Duration of resolution of symptoms before recurrence/relapse (in days)'].dtypes


# # No of relapses/exacerbations

# In[1335]:


df['No of relapses/exacerbations'].dtypes


# In[1336]:


df['No of relapses/exacerbations'].isnull().sum()


# In[1337]:


df['No of relapses/exacerbations'].fillna(method = 'ffill',inplace = True)


# In[1338]:


df['No of relapses/exacerbations'].isnull().sum()


# # Off-medications duration (to add all such durations over follow-up in days)

# In[1339]:


df['Off-medications duration (to add all such durations over follow-up in days)'].dtypes


# In[1340]:


df['Off-medications duration (to add all such durations over follow-up in days)'].unique()


# In[1341]:


#df['Off-medications duration (to add all such durations over follow-up in days)'].isnull().sum()


# In[1342]:


#df['Off-medications duration (to add all such durations over follow-up in days)'].fillna(method = 'ffill',inplace = True)


# In[1343]:


df['Off-medications duration (to add all such durations over follow-up in days)'].isnull().sum()


# In[1344]:


df['Off-medications duration (to add all such durations over follow-up in days)'].dtypes


# # Compliant to medications (Poor/Satisfactory/Good) (if off medications period is less than 7 days then it is considered as compliant {Poor-loss to follow up, maximum relapses,medication possession ratio < 0.9; Satisfactory- medication possession ratio 0.9 - 0.95, minimal relapse; Good- no relapse, medication possession ratio < 0.95}
# 
# 
# #### 'satisfactory' : 1, 'poor' : 2, 'good' : 3, 'yes' :4, 'no' : 5

# In[1345]:


df['Compliant to medications (Poor/Satisfactory/Good) (if off medications period is less than 7 days then it is considered as compliant {Poor-loss to follow up, maximum relapses,medication possession ratio < 0.9; Satisfactory- medication possession ratio 0.9 - 0.95, minimal relapse; Good- no relapse, medication possession ratio < 0.95}'].dtypes


# In[1346]:


df['Compliant to medications (Poor/Satisfactory/Good) (if off medications period is less than 7 days then it is considered as compliant {Poor-loss to follow up, maximum relapses,medication possession ratio < 0.9; Satisfactory- medication possession ratio 0.9 - 0.95, minimal relapse; Good- no relapse, medication possession ratio < 0.95}'].unique()


# In[1347]:


df['Compliant to medications (Poor/Satisfactory/Good) (if off medications period is less than 7 days then it is considered as compliant {Poor-loss to follow up, maximum relapses,medication possession ratio < 0.9; Satisfactory- medication possession ratio 0.9 - 0.95, minimal relapse; Good- no relapse, medication possession ratio < 0.95}'].isnull().sum()


# In[1348]:


#df['Compliant to medications (Poor/Satisfactory/Good) (if off medications period is less than 7 days then it is considered as compliant {Poor-loss to follow up, maximum relapses,medication possession ratio < 0.9; Satisfactory- medication possession ratio 0.9 - 0.95, minimal relapse; Good- no relapse, medication possession ratio < 0.95}'].fillna(method = 'bfill',inplace = True)


# In[1349]:


#df['Compliant to medications (Poor/Satisfactory/Good) (if off medications period is less than 7 days then it is considered as compliant {Poor-loss to follow up, maximum relapses,medication possession ratio < 0.9; Satisfactory- medication possession ratio 0.9 - 0.95, minimal relapse; Good- no relapse, medication possession ratio < 0.95}'] = df['Compliant to medications (Poor/Satisfactory/Good) (if off medications period is less than 7 days then it is considered as compliant {Poor-loss to follow up, maximum relapses,medication possession ratio < 0.9; Satisfactory- medication possession ratio 0.9 - 0.95, minimal relapse; Good- no relapse, medication possession ratio < 0.95}'].map({'satisfactory' : 1, 'poor' : 2, 'good' : 3, 'yes' :4, 'no' : 5})


# In[1350]:


df['Compliant to medications (Poor/Satisfactory/Good) (if off medications period is less than 7 days then it is considered as compliant {Poor-loss to follow up, maximum relapses,medication possession ratio < 0.9; Satisfactory- medication possession ratio 0.9 - 0.95, minimal relapse; Good- no relapse, medication possession ratio < 0.95}'].unique()


# In[1351]:


df['Compliant to medications (Poor/Satisfactory/Good) (if off medications period is less than 7 days then it is considered as compliant {Poor-loss to follow up, maximum relapses,medication possession ratio < 0.9; Satisfactory- medication possession ratio 0.9 - 0.95, minimal relapse; Good- no relapse, medication possession ratio < 0.95}'].isnull().sum()


# In[1352]:


df['Compliant to medications (Poor/Satisfactory/Good) (if off medications period is less than 7 days then it is considered as compliant {Poor-loss to follow up, maximum relapses,medication possession ratio < 0.9; Satisfactory- medication possession ratio 0.9 - 0.95, minimal relapse; Good- no relapse, medication possession ratio < 0.95}'].dtypes


# # mean gap ratio at lgb (total no of months of follow-up divided by no of follow-ups) 

# In[1353]:


df['mean gap ratio at lgb (total no of months of follow-up divided by no of follow-ups)'].dtypes


# In[1354]:


df['mean gap ratio at lgb (total no of months of follow-up divided by no of follow-ups)'].isnull().sum()


# In[1355]:


#df['mean gap ratio at lgb (total no of months of follow-up divided by no of follow-ups)'].fillna(method = 'ffill' , inplace = True)


# In[1356]:


df['mean gap ratio at lgb (total no of months of follow-up divided by no of follow-ups)'].replace('so',0,inplace = True)


# In[1357]:


df['mean gap ratio at lgb (total no of months of follow-up divided by no of follow-ups)'] = df['mean gap ratio at lgb (total no of months of follow-up divided by no of follow-ups)'].astype(float)


# In[1358]:


df['mean gap ratio at lgb (total no of months of follow-up divided by no of follow-ups)'].isnull().sum()


# # maximum period of compliance at lgb (in days) (longest streak of good compliance)

# In[1359]:


df['maximum period of compliance at lgb (in days) (longest streak of good compliance)'].dtypes


# In[1360]:


df['maximum period of compliance at lgb (in days) (longest streak of good compliance)'].isnull().sum()


# In[1361]:


#df['maximum period of compliance at lgb (in days) (longest streak of good compliance)'].fillna(method = 'ffill',inplace = True)


# In[1362]:


df['maximum period of compliance at lgb (in days) (longest streak of good compliance)'].isnull().sum()


# # total duration of medication treatment at LGB(in days) (from first consultation to last follow-up)

# In[1363]:


df['total duration of medication treatment at LGB(in days) (from first consultation to last follow-up)'].dtypes


# In[1364]:


df['total duration of medication treatment at LGB(in days) (from first consultation to last follow-up)'].isnull().sum()


# In[1365]:


##df['total duration of medication treatment at LGB(in days) (from first consultation to last follow-up)'].fillna(method = 'ffill',inplace = True)


# In[1366]:


df['total duration of medication treatment at LGB(in days) (from first consultation to last follow-up)'].isnull().sum()


# # Number of In patient cares

# In[1367]:


df['Number of In patient cares'].dtypes


# In[1368]:


df['Number of In patient cares'].isnull().sum()


# In[1369]:


#df['Number of In patient cares'].fillna(method = 'ffill',inplace = True)


# In[1370]:


df['Number of In patient cares'].isnull().sum()


# In[1371]:


df.shape


# In[1372]:


df = df.drop('Final (ignore for now)', axis=1)


# In[1373]:


df.shape


# In[1374]:


sns.heatmap(df.isnull())


# In[1375]:


# Calculate the percentage of null values in each column
null_percentage = df.isnull().mean() * 100

# Filter columns with more than 20% null values
columns_with_high_nulls = null_percentage[null_percentage > 20]

print("Columns with more than 20% null values and their percentages:")
print(columns_with_high_nulls)


# In[1376]:


# df.to_csv('mapping.csv')


# In[1377]:


df.info()


# In[1378]:


# Get columns with object data type
object_columns = df.select_dtypes(include='object').columns

print("Columns with object data type:")
print(object_columns)


# In[ ]:




