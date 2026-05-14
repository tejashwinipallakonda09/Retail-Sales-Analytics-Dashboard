import pandas as pd

df = pd.read_csv("retail_sales_data.csv")

print(df.head())

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())