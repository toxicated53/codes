import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

boston = fetch_openml(name='boston', version=1, as_frame=True)

df = boston.frame

print("First 5 Rows of Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

plt.title("Correlation Heatmap")
plt.show()

# Linear Regression Formula:
# y = b0 + b1x1 + b2x2 + ... + bnxn
df = df.apply(pd.to_numeric)
X = df.drop('MEDV', axis=1)
y = df['MEDV']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nModel Evaluation:")

print("Mean Absolute Error:",
      metrics.mean_absolute_error(y_test, y_pred))

print("Mean Squared Error:",
      metrics.mean_squared_error(y_test, y_pred))

print("Root Mean Squared Error:",
      np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print("R2 Score:",
      metrics.r2_score(y_test, y_pred))

plt.figure(figsize=(8,6))

plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.scatter(y_test, y_pred)
plt.title("Actual vs Predicted Prices")

plt.show()
