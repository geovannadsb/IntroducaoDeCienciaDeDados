# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11Uh8ALfb4B65pzub3gJVvaPSsu4JO51E

Geovanna Dos Santos Benedito
RA: 22502439
"""

import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

TRAIN = '/content/drive/MyDrive/with header/train.csv'

df = pd.read_csv(TRAIN)
df

df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]].corr()

def sex_to_id(sex):
    if sex == 'male':
        return 0
    else:
        return 1

df["sex_id"] = df["Sex"].apply(sex_to_id)
df

df.corr(numeric_only=True)

corr = df.corr(numeric_only=True)
corr

import seaborn as sns

sns.heatmap(corr, annot=True)

import matplotlib.pyplot as plt

df.groupby('Survived')["Fare"].plot.hist(alpha=.3)
plt.legend(["not survived","survived"])

#AGRUPAMENTO POR SOBREVIVENCIA

df.groupby('Survived')["Fare"].value_counts()

df.groupby('Survived')["Pclass"].value_counts()

df.groupby('Survived')["Age"].value_counts()

df.groupby('Survived')["Sex"].value_counts()

#Taxa paga de cada grupo

df.groupby('Pclass')["Fare"].describe()

#Idade de cada grupo

df.groupby('Pclass')["Age"].describe()

# frequencia de cada grupo
df["Survived"].value_counts() / len(df) * 100

df["Age"].value_counts() / len(df) * 100

df["Sex"].value_counts() / len(df) * 100

df["Fare"].value_counts() / len(df) * 100

#Plotar informações para cada grupo

df['Survived'].value_counts().plot.pie()

df['Age'].value_counts().plot.pie()

df['Sex'].value_counts().plot.pie()

#Correlação entre variáveis

df.corr(numeric_only=True)