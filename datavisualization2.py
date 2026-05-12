import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = sns.load_dataset('titanic')

# Box Plot
plt.figure(figsize=(8,6))

sns.boxplot(
    x='sex',
    y='age',
    hue='survived',
    data=df
)

plt.title("Age Distribution by Gender and Survival")

plt.xlabel("Gender")
plt.ylabel("Age")

plt.show()
