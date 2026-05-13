import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Display First Rows
print(df.head())

# Statistical Summary
print(df.describe())

# Missing Values
print(df.isnull().sum())

# Dataset Dimensions
print(df.shape)

# Datatypes
print(df.dtypes)

# Dataset Information
print(df.info())

# Fill Missing Values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Convert Datatype
df['Age'] = df['Age'].astype(int)

# Normalize Fare Column
df['Fare'] = (df['Fare'] - df['Fare'].min()) / \
             (df['Fare'].max() - df['Fare'].min())

# Convert Categorical to Numerical
df['Sex'] = df['Sex'].map({
    'male': 0,
    'female': 1
})

# Final Output
print(df.head())
