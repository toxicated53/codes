import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset (Inbuilt Iris)
# -----------------------------
df = sns.load_dataset('iris')

print("First 5 Rows:\n")
print(df.head())

# -----------------------------
# 1. Features and Their Types
# -----------------------------
print("\nFeatures and Data Types:\n")
print(df.dtypes)

# -----------------------------
# 2. Histograms for Each Feature
# -----------------------------
df.hist(figsize=(10,8))
plt.suptitle("Histogram of Iris Features")
plt.show()

# -----------------------------
# 3. Boxplot for Each Feature
# -----------------------------
plt.figure(figsize=(10,6))
sns.boxplot(data=df.drop('species', axis=1))  # exclude categorical column
plt.title("Boxplot of Iris Features")
plt.show()

# -----------------------------
# 4. Compare Distributions & Outliers
# -----------------------------
print("\nSummary Statistics:\n")
print(df.describe())
