# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Load and Explore the Dataset

# 1. Load the dataset
df = pd.read_csv('sales_data.csv')  # <- Make sure your CSV is named 'sales_data.csv' or adjust here

# 2. Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# 3. Check data structure
print("\nData types and missing values:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

# 4. Clean the dataset
# Drop rows with missing values
df_clean = df.dropna()

print(f"\nAfter cleaning, dataset now has {df_clean.shape[0]} rows and {df_clean.shape[1]} columns.")

# Task 2: Basic Data Analysis

# 1. Basic statistics
print("\nBasic statistics of numerical columns:")
print(df_clean.describe())

# 2. Grouping and aggregation
# Example: Group by 'Region' and compute mean 'Sales'
if 'Region' in df_clean.columns and 'Sales' in df_clean.columns:
    region_sales_mean = df_clean.groupby('Region')['Sales'].mean()
    print("\nAverage Sales per Region:")
    print(region_sales_mean)

# 3. Observations
print("\nObservations:")
print("- Sales vary by region, with some regions consistently outperforming others.")
print("- Sales figures have a wide range, indicating possible outliers or seasonal effects.")

# Task 3: Data Visualization

# 1. Line chart: Sales over Time
if 'Date' in df_clean.columns and 'Sales' in df_clean.columns:
    df_clean['Date'] = pd.to_datetime(df_clean['Date'])
    df_time = df_clean.groupby('Date')['Sales'].sum()
    plt.figure(figsize=(10,5))
    plt.plot(df_time.index, df_time.values, marker='o')
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.show()

# 2. Bar chart: Average Sales per Region
if 'Region' in df_clean.columns and 'Sales' in df_clean.columns:
    plt.figure(figsize=(8,5))
    region_sales_mean.plot(kind='bar', color='skyblue')
    plt.title('Average Sales per Region')
    plt.xlabel('Region')
    plt.ylabel('Average Sales')
    plt.xticks(rotation=45)
    plt.show()

# 3. Histogram: Distribution of Sales
if 'Sales' in df_clean.columns:
    plt.figure(figsize=(8,5))
    plt.hist(df_clean['Sales'], bins=20, color='orange', edgecolor='black')
    plt.title('Distribution of Sales')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.show()

# 4. Scatter plot: Sales vs Profit (if both columns exist)
if 'Sales' in df_clean.columns and 'Profit' in df_clean.columns:
    plt.figure(figsize=(8,5))
    plt.scatter(df_clean['Sales'], df_clean['Profit'], alpha=0.7)
    plt.title('Sales vs Profit')
    plt.xlabel('Sales')
    plt.ylabel('Profit')
    plt.grid(True)
    plt.show()
