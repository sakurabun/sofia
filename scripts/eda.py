import pandas as pd
import os
import re
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
df = pd.read_csv("../data/name_gender.csv")

# print basic info
print(df.head())
print(df.info())
print(df['Gender'].value_counts())


# make sure the dir exists
if not os.path.exists('../eda'):
    os.makedirs('../eda')

# gender distribution
sns.countplot(data=df, x='Gender')
plt.title('Gender distribution')
plt.savefig("../eda/gender_distribution.png")
plt.show()

# name length analysis
df['name_length'] = df['Name'].apply(len)
sns.histplot(data=df, x='name_length', bins=20)
plt.title('name length distribution')
plt.savefig("../eda/name_length_distribution.png")
plt.show()

# ---- the analysis of the approach that has been used ----

# first letter frequency
df['first letter'] = df['Name'].str[0].str.upper()
plt.figure(figsize=(12, 5))
sns.countplot(data=df, x='first letter', order=sorted(df['first letter'].unique()))
plt.title('first letter frequency')
plt.savefig("../eda/first_letter_freq.png")
plt.show()

# last letter frequency
df['last letter'] = df['Name'].str[-1].str.upper()
df['last letter'] = df['last letter'].apply(lambda x: re.sub(r'[^A-Za-z]', '', x))
df = df[df['last letter'] != '']
plt.figure(figsize=(12, 5))
sns.countplot(data=df, x='last letter', order=sorted(df['last letter'].unique()))
plt.title('last letter frequency')
plt.savefig("../eda/last_letter_freq.png")
plt.show()