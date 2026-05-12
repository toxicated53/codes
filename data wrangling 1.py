import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# -----------------------------------
# 1. Import Required Libraries
# -----------------------------------
print("Libraries Imported Successfully")

# -----------------------------------
# 2. Load Open Source Dataset
# Dataset: Titanic Dataset
# Source:
# https://www.kaggle.com/c/titanic
# -----------------------------------

import seaborn as sns

df = sns.load_dataset('titanic')# -----------------------------------
# 3. Load Dataset into DataFrame
# -----------------------------------
print("\nFirst 5 Rows of Dataset:\n")
print(df.head())

# -----------------------------------
# 4. Data Preprocessing
# -----------------------------------

# Check dimensions
print("\nDimensions of Dataset:")
print(df.shape)

# Dataset Information
print("\nDataset Information:\n")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:\n")
print(df.describe())

# Check Missing Values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Variable Types
print("\nData Types:\n")
print(df.dtypes)

# -----------------------------------
# 5. Data Formatting and Normalization
# -----------------------------------

# Convert age to float type
df['age'] = df['age'].astype(float)

df['age'] = df['age'].fillna(df['age'].mean())

df['age_normalized'] = (
    (df['age'] - df['age'].min()) /
    (df['age'].max() - df['age'].min())
)

print("\nNormalized Age Column:\n")
print(df[['age', 'age_normalized']].head())

# -----------------------------------
# 6. Convert Categorical to Numeric
# -----------------------------------

label_encoder = LabelEncoder()

df['sex'] = label_encoder.fit_transform(df['sex'])

print("\nCategorical Variable Converted:\n")
print(df[['sex']].head())

# Final Dataset
print("\nFinal Dataset:\n")
print(df.head())
