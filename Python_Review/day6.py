## Day 6: Pandas ##
## Ex1: Create a DataFrame from a dictionary of lists ##
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Score": [85, 90, 95, 80]
}
df = pd.DataFrame(data)
print(df)

## Ex2: Read a CSV file into a DataFrame ##
df_csv = pd.read_csv("data1.csv")
## Display DataFrame information ##
print(df_csv.head())
print(df_csv.head(3))
print(df_csv.tail())
print(df_csv.shape)
print(df_csv.columns)
print(df_csv.dtypes)
print(df_csv.info())
print(df_csv.describe())

## Ex3: Select specific columns and/or rows##
print(df_csv["Brand"])
print(df_csv[["Brand", "Availability"]])  # This line will raise an error; use double brackets instead
print(df_csv.loc[0]) ## Select a single row by index
print(df_csv.loc[0:2]) ## Select rows by index range
print(df_csv.loc[1:2, ["Brand", "Availability"]]) ## Select specific rows and columns   

## Ex4: Using iloc (position) ##
print(df_csv.iloc[0])
print(df_csv.iloc[0:3])
print(df_csv.iloc[0:3, 3:5]) ## Select specific rows and columns by position    

## Ex5: Filter rows based on conditions ##
filtered_df = df_csv[df_csv["Price"] > 500]
print(filtered_df.shape)

filtered_df2 = df_csv[df_csv["Availability"] == "pre_order"]
print(filtered_df2.shape)

filtered_df3 = df_csv[(df_csv["Availability"] == "pre_order") & (df_csv["Price"] > 500)]
print(filtered_df3.shape)

## Ex6: Sort the DataFrame ##
df_sorted = df_csv.sort_values(by="Price", ascending=False) ## Sort by Price in descending order
print(df_sorted.head(3))

### Ex7: Create new columns ##
df_csv["Soldable"] = df_csv["Availability"] == "in_stock" ## Create a new column based on a condition   
print(df_csv.head(3))

df_csv["Features"] = df_csv["Color"] + " " + df_csv["Size"] ## Create a new column by combining existing columns
print(df_csv.head(3))

df_csv["Stock_in_5_Years"] = df_csv["Stock"] * 2 ## Create a new column by performing arithmetic operations on existing columns
print(df_csv.head(3))

## Ex8: Drop columns ##
df_csv.drop(columns=["Soldable", "Features", "Stock_in_5_Years"], inplace=True) ## Drop the newly created columns
print(df_csv.head(3))

## Ex9: Grouping and Aggregation ##
grouped_df = df_csv.groupby("Brand").agg({"Price": "mean", "Stock": "sum"}) ## Group by Brand and calculate mean Price and sum of Stock
print(grouped_df)



## Part2: CSV Practice ##
## Ex1: Read a CSV file into a DataFrame ##
df_csv2 = pd.read_csv("students.csv")
print(df_csv2.head())
print(df_csv2.describe())
print(df_csv2.info())

import numpy as np
print(f"The Average Score is: {df_csv2['Score'].mean()}") ### Find the average score
print(f"The Maximum Age is: {df_csv2['Age'].max()} that belongs to {df_csv2['Name'].iloc[df_csv2['Age'] == df_csv2['Age'].max()].values[0]}") ## Find the oldest student
print(f"The Maximum Score is: {df_csv2['Score'].max()} that belongs to {df_csv2['Name'].iloc[df_csv2['Score'] == df_csv2['Score'].max()].values[0]}") ## Find the highest score

