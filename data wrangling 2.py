import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------
# Create Academic Performance Dataset
# ---------------------------------------

data = {
    'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    
    'Maths': [85, 90, np.nan, 76, 95, 200, 88, 92, 79, 84],
    
    'Science': [78, 85, 89, np.nan, 91, 87, 300, 90, 80, 82],
    
    'English': [75, 80, 79, 85, np.nan, 88, 92, 91, 77, 79]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# ---------------------------------------
# 1. Missing Values and Inconsistencies
# ---------------------------------------

print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing values using mean
df['Maths'] = df['Maths'].fillna(df['Maths'].mean())

df['Science'] = df['Science'].fillna(df['Science'].mean())

df['English'] = df['English'].fillna(df['English'].mean())

print("\nDataset After Handling Missing Values:\n")
print(df)

# ---------------------------------------
# 2. Detect and Handle Outliers
# ---------------------------------------

# Boxplots before removing outliers
plt.figure(figsize=(8,5))

sns.boxplot(data=df[['Maths', 'Science', 'English']])

plt.title("Boxplot Before Removing Outliers")

plt.show()

# Remove outliers using IQR method
for column in ['Maths', 'Science', 'English']:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[column] = np.where(
        df[column] > upper,
        upper,
        np.where(df[column] < lower, lower, df[column])
    )

print("\nDataset After Handling Outliers:\n")
print(df)

# Boxplots after removing outliers
plt.figure(figsize=(8,5))

sns.boxplot(data=df[['Maths', 'Science', 'English']])

plt.title("Boxplot After Removing Outliers")

plt.show()

# ---------------------------------------
# 3. Data Transformation
# ---------------------------------------

# Apply log transformation
df['Science_Log'] = np.log(df['Science'])

print("\nDataset After Log Transformation:\n")
print(df[['Science', 'Science_Log']])

# Histogram of transformed data
plt.figure(figsize=(6,4))

plt.hist(df['Science_Log'], bins=10)

plt.title("Histogram of Log Transformed Science Marks")

plt.xlabel("Science_Log")

plt.ylabel("Frequency")

plt.show()
