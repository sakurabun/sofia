import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# load dataset
df = pd.read_csv("../data/name_gender.csv")

# preprocess
df['Name'] = df['Name'].str.lower()
df['Gender'] = df['Gender'].map({'M': 1, 'F': 0})
df['first_letter'] = df['Name'].str[0]
df['last_letter'] = df['Name'].str[-1]
df['name_length'] = df['Name'].apply(len)

# select features
X = df[['first_letter', 'last_letter']]
y = df['Gender']

# one hot encode first letter and last letter columns
preprocessor = ColumnTransformer(
    transformers=[
        ('first', OneHotEncoder(), ['first_letter']),
        ('last', OneHotEncoder(), ['last_letter'])
    ])

# first apply the preprocessor and then train the model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

# train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the model finally
model.fit(X_train, y_train)
# save the trained model and encoder
if not os.path.exists('../model'):
    os.makedirs('../model')

# save both the model and the encoder
joblib.dump(model, "../model/gender_model.pkl")

print("model and encoder saved to model/gender_model.pkl")