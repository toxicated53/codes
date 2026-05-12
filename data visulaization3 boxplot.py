import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Iris dataset
df = pd.read_csv(r"C:\Users\Adwait\Downloads\Iris.csv")

# -----------------------------
# Features and Data Types
# -----------------------------
print("Features and their Types:\n")
print(df.dtypes)

# -----------------------------
# Histograms for each feature
# -----------------------------
features = [
    'SepalLengthCm',
    'SepalWidthCm',
    'PetalLengthCm',
    'PetalWidthCm'
]

for feature in features:

    plt.figure(figsize=(6,4))

    plt.hist(df[feature], bins=20)

    plt.title(f"Histogram of {feature}")

    plt.xlabel(feature)
    plt.ylabel("Frequency")

    plt.show()

# -----------------------------
# Boxplots for each feature
# -----------------------------
for feature in features:

    plt.figure(figsize=(6,4))

    sns.boxplot(y=df[feature])

    plt.title(f"Boxplot of {feature}")

    plt.show()
