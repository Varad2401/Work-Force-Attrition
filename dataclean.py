import numpy as np
import pandas as pd
df=pd.read_csv('D:/Customer churn dataset/train1customerchurn1.csv')
print(df.head(5))
df.columns
df1 = df.copy()
df1.head(7)
df1.columns
df1.shape
df1.dtypes
features = df1.columns
for feature in features:
     print(f'{feature}--->{df[feature].nunique()}')
     
df1.isnull().sum() / df1.shape[0]

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame)
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)
df1=df1.interpolate()

df1=df1.dropna()
df.head()
print(df.head)
df1.to_csv('train_dataset.csv')

df['Unlimited Data'] 

number_columns=['Gender','Age','Married','City','Zip Code','Number of Referrals','Tenure in Months','Offer','Multiple Lines','Internet Service','Internet Type','Premium Tech Support','Streaming TV','Unlimited Data','Contract','Payment Method','Monthly Charge','Total Revenue']     

def unique_values_names(df):
    for column in df:
        if df[column].dtype=='object':
            print(f'{column}:{df[column].unique()}')
            
unique_values_names(df1)

import plotly.express as px 

fig = px.histogram(df1, x = 'Age')
fig.show() 

df1.hist(figsize=(15,15), xrot=30)   

df1['Age']

import matplotlib.pyplot as plt

Customer_Stayed=df1[df1['Customer Status']=='Stayed'].Age
Customer_Churned=df1[df1['Customer Status']=='Churned'].Age
Customer_Joined=df1[df1['Customer Status']=='Joined'].Age

plt.xlabel('Age')
plt.ylabel('Customers Numbers')
plt.hist([Customer_Stayed,Customer_Churned,Customer_Joined], color=['black','red','blue'],label=['Stayed','Churned','Joined'])

plt.title('Customers Behavior ',fontweight ="bold")
plt.legend()

import seaborn as sns

data  = df1.corr()
plt.figure(figsize = (20,10))
sns.heatmap(data, annot = True)

fig, ax = plt.subplots(4,3, figsize = (15,15))
for i, subplot in zip(number_columns, ax.flatten()):
    sns.boxplot(x = 'Customer Status', y = i , data = df1, ax = subplot)





