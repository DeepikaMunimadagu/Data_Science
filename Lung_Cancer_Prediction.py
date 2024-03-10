import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
cancer_data = pd.read_csv("Lung_Cancer_Dataset.csv",header=0,sep=",")
cancer_data.head(10)
sns.countplot(x="LUNG_CANCER",data=cancer_data)
sns.countplot(x="LUNG_CANCER",hue="GENDER",data=cancer_data)
cancer_data["AGE"].plot.hist()
cancer_data.info()
sns.countplot(x="ANXIETY",data=cancer_data)
#DATA WRANGLING
cancer_data.isnull()
cancer_data.isnull().sum()
sns.heatmap(cancer_data.isnull(),yticklabels=False,cmap="viridis")
cancer_data.head(5)
gender = pd.get_dummies(cancer_data['GENDER'],drop_first=True)
gender.head(5)
lung = pd.get_dummies(cancer_data['LUNG_CANCER'],drop_first=True)
lung.head(5)
#TRAIN DATA
X=cancer_data.drop("LUNG_CANCER",axis=1)
y=cancer_data["LUNG_CANCER"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
from sklearn.linear_model import LogisticRegression
logmodel=LogisticRegression()
print(cancer_data.columns)
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
cancer_data['GENDER_encoded'] = label_encoder.fit_transform(cancer_data['GENDER'])
# Assuming X contains features and y contains target variable
X = cancer_data.drop(columns=['GENDER', 'LUNG_CANCER'])
y = cancer_data['LUNG_CANCER']
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Fit the model
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)
from sklearn.metrics import classification_report
classification_report(y_test,predictions)
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,predictions)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,predictions)
