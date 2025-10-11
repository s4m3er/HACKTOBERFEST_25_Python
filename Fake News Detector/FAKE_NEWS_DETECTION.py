#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import string
import re
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


# In[9]:


data_fake=pd.read_csv("Fake.csv")
data_true=pd.read_csv("True.csv")


# In[11]:


data_fake.head()


# In[13]:


data_true.tail()


# In[15]:


data_fake["class"]=0
data_true['class']=1


# In[17]:


data_fake.shape, data_true.shape


# In[19]:


data_fake_manual_testing = data_fake.tail(10)
for i in range(23480,23470,-1):
    data_fake.drop([i],axis = 0, inplace = True)


data_true_manual_testing = data_true.tail(10)
for i in range(21416,21406,-1):
    data_true.drop([i],axis = 0, inplace = True)


# In[21]:


data_fake.shape, data_true.shape


# In[23]:


data_fake_manual_testing['class']=0
data_true_manual_testing['class']=1


# In[25]:


data_fake_manual_testing.head(10)


# In[27]:


data_true_manual_testing.head(10)


# In[29]:


data_merge=pd.concat([data_fake, data_true], axis = 0)
data_merge.head(10)


# In[31]:


data_merge.columns


# In[33]:


data=data_merge.drop(['title','subject','date'], axis = 1)


# In[35]:


data.isnull().sum()


# In[37]:


data = data.sample(frac = 1)


# In[39]:


data.head()


# In[41]:


data.reset_index(inplace = True)
data.drop(['index'], axis = 1, inplace = True)


# In[43]:


data.columns


# In[45]:


data.head()


# In[49]:


def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text


# In[51]:


data['text'] = data['text'].apply(wordopt)


# In[52]:


x = data['text']
y = data['class']


# In[55]:


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25)


# In[57]:


from sklearn.feature_extraction.text import TfidfVectorizer

vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)


# In[58]:


from sklearn.linear_model import LogisticRegression


# In[61]:


LR = LogisticRegression()
LR.fit(xv_train, y_train)


# In[63]:


pred_lr = LR.predict(xv_test)


# In[65]:


LR.score(xv_test, y_test)


# In[67]:


print (classification_report(y_test, pred_lr))


# In[71]:


from sklearn.tree import DecisionTreeClassifier

DT = DecisionTreeClassifier()
DT.fit(xv_train, y_train)


# In[70]:


pred_dt = DT.predict(xv_test)


# In[74]:


DT.score(xv_test, y_test)


# In[76]:


print (classification_report(y_test, pred_dt))


# In[78]:


from sklearn.ensemble import GradientBoostingClassifier

GB = GradientBoostingClassifier(random_state = 0)
GB.fit(xv_train, y_train)


# In[79]:


pred_gb = GB.predict(xv_test)


# In[80]:


GB.score(xv_test, y_test)


# In[81]:


print(classification_report(y_test, pred_gb))


# In[86]:


from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier(random_state = 0)
RF.fit(xv_train, y_train)


# In[87]:


pred_rf = RF.predict(xv_test)


# In[88]:


RF.score(xv_test, y_test)


# In[92]:


print (classification_report(y_test, pred_rf))


# In[94]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

KNN = KNeighborsClassifier(n_neighbors=5)
KNN.fit(xv_train, y_train)


# In[96]:


pred_knn = KNN.predict(xv_test)


# In[97]:


KNN.score(xv_test, y_test)


# In[98]:


print(classification_report(y_test, pred_knn))


# In[102]:


def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"

def manual_testing(news):
    testing_news = {"text": [news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test['text'] = new_def_test["text"].apply(wordopt)
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)

    pred_LR = LR.predict(new_xv_test)
    pred_DT = DT.predict(new_xv_test)
    pred_GB = GB.predict(new_xv_test)
    pred_RF = RF.predict(new_xv_test)
    pred_knn = KNN.predict(new_xv_test)

    print("\n\nLR Prediction: {} \nDT Prediction: {} \nGBC Prediction: {} \nRFC Prediction: {} \nKNN Prediction: {}".format(
        output_lable(pred_LR[0]),
        output_lable(pred_DT[0]),
        output_lable(pred_GB[0]),
        output_lable(pred_RF[0]),
        output_lable(pred_knn[0])
    ))



# In[104]:


news = str(input())
manual_testing(news)


# In[112]:


news=str(input())
manual_testing(news)


# In[116]:


news=str(input())
manual_testing(news)


# In[122]:


news=str(input())
manual_testing(news)


# In[ ]:




