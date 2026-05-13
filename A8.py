import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = sns.load_dataset('titanic')

# Display first 5 rows
print(df.head())

# -----------------------------
# Pattern Analysis using Seaborn
# -----------------------------

# Count plot for survived passengers
plt.figure(figsize=(6,4))

sns.countplot(x='survived', data=df)

plt.title("Survival Count")
plt.show()

# Gender vs Survival
plt.figure(figsize=(6,4))

sns.countplot(x='sex', hue='survived', data=df)

plt.title("Gender vs Survival")
plt.show()

# Passenger Class vs Survival
plt.figure(figsize=(6,4))

sns.countplot(x='pclass', hue='survived', data=df)

plt.title("Passenger Class vs Survival")
plt.show()

# -----------------------------
# Histogram of Fare Distribution
# -----------------------------
plt.figure(figsize=(8,5))

plt.hist(df['fare'].dropna(), bins=30)

plt.xlabel("Fare")
plt.ylabel("Number of Passengers")

plt.title("Fare Distribution Histogram")

plt.show()
