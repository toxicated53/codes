import pandas as pd
import numpy as np

# ---------------------------------------
# Load Iris Dataset
# ---------------------------------------

df = pd.read_csv(r"C:\Users\Adwait\Downloads\Iris.csv")

print("First 5 Rows of Dataset:\n")
print(df.head())

# ---------------------------------------
# 1. Summary Statistics Grouped by Species
# ---------------------------------------

print("\nSummary Statistics Grouped by Species:\n")

grouped_data = df.groupby('Species')['SepalLengthCm']

print(grouped_data.describe())

# Create list of numeric values for each category
print("\nNumeric Values for Each Species:\n")

for species in df['Species'].unique():

    values = df[df['Species'] == species]['SepalLengthCm'].tolist()

    print(f"\n{species}:\n")

    print(values)

# ---------------------------------------
# 2. Basic Statistical Details
# ---------------------------------------

species_list = df['Species'].unique()

for species in species_list:

    print("\n-----------------------------------")
    print(f"Statistics for {species}")
    print("-----------------------------------")

    species_data = df[df['Species'] == species]

    print("\nMean:\n")
    print(species_data.mean(numeric_only=True))

    print("\nMedian:\n")
    print(species_data.median(numeric_only=True))

    print("\nMinimum Values:\n")
    print(species_data.min(numeric_only=True))

    print("\nMaximum Values:\n")
    print(species_data.max(numeric_only=True))

    print("\nStandard Deviation:\n")
    print(species_data.std(numeric_only=True))

    print("\nPercentiles:\n")
    print(species_data.quantile([0.25, 0.50, 0.75], numeric_only=True))
