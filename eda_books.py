import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("books.csv")
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

# Remove £ sign and convert Price to float
df["Price"] = df["Price"].str.replace("£", "").astype(float)

print("\nUpdated Data Types:")
print(df.dtypes)

print("\nStatistical Summary After Cleaning:")
print(df.describe())

# Most expensive book
max_price_book = df[df["Price"] == df["Price"].max()]
print("\nMost Expensive Book:")
print(max_price_book)

# Cheapest book
min_price_book = df[df["Price"] == df["Price"].min()]
print("\nCheapest Book:")
print(min_price_book)

# Histogram of Prices
plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=8, color='skyblue', edgecolor='black')
plt.title("Price Distribution of Books")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Bar chart for Availability
availability_counts = df["Availability"].value_counts()
plt.figure(figsize=(6,4))
availability_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title("Book Availability")
plt.xlabel("Availability Status")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.show()

# Simple Outlier Detection using IQR
Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df["Price"] < Q1 - 1.5*IQR) | (df["Price"] > Q3 + 1.5*IQR)]
print("\nOutliers in Price:")
print(outliers)
