## Part 1: groupby and aggregation ##
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Sara", "David", "Alice", "Emma"],
    "Department": ["IT", "Sales", "IT", "Sales", "IT", None],
    "Age": [24, 31, 27, None, 24, 29],
    "Salary": [42000, 51000, 47000, 55000, 42000, None]
}
df = pd.DataFrame(data)

## Data Cleaning ##
df1 = df.isna()  # Check for missing values
print(df1)

# Fill missing values in the Department column with "Unknown" 
# And fill missing values in the Age and Salary columns with the mean of their respective columns 
df = df.fillna({"Department": "Unknown", "Age" : df["Age"].mean(), "Salary" : df["Salary"].mean()})  

## Ex1: Grouping ##
per_department_salary_mean = df.groupby("Department")["Salary"].mean() # Calculate the mean of salary of each department
print(f"Mean salary per department are:{per_department_salary_mean}")
per_department_salary_sum = df.groupby("Department")["Salary"].sum()
print(f"Sum of salaries per department are: {per_department_salary_sum}")
per_department_salary_max = df.groupby("Department")["Salary"].max()
print(f"Maximum of salaries per department are: {per_department_salary_max}")

## Ex2: Multiple aggregations ##
multiple_agg = df.groupby("Department")["Salary"].agg(["mean", "min", "max"]) 
print(multiple_agg)

## Ex3: Group by multiple columns ##
multiple_columns = df.groupby(["Department", "Age"])["Salary"].mean()
print(multiple_columns)

## Ex4: Value_counts() ##
department_counts = df["Department"].value_counts()
print(f"Count of employees per department are: {department_counts}")

## Ex5: Combining DataFrames ##
data1 = {
    "Name": ["Alice", "Bob", "Sara", "David"],
    "Department": ["IT", "Sales", "IT", "Sales"],
    "Age": [24, 31, 27, None],
    "Salary": [42000, 51000, 47000, 55000]
}
data2 = {
    "Name": ["Alice", "Emma", "John", "Kami"],
    "Department": ["IT", None, "HR", "Sales"],
    "Age": [24, 29, 35, 45],
    "Salary": [42000, None, 60000, 45000]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)
#df1.dropna(inplace=True)  # Drop rows with missing values in df1
df1 = df1.fillna({"Age": int(df1["Age"].mean())}, inplace=True)  # Fill missing value in df1   
df1["Age"] = df1["Age"].astype(int)

df2 = df2.fillna({"Department": "Unknown", "Salary": df2["Salary"].mean()}, inplace=True)  # Fill missing values in df2   

df3 = pd.merge(df1, df2, on="Name", how="outer", suffixes=("_df1", "_df2")) # Merge 
print(df3)

inner = pd.merge(df1, df2, on="Name", how="inner") #inner merge
print(inner)

left = pd.merge(df1, df2, on="Name", how="left") #left merge
print(left)

right = pd.merge(df1, df2, on="Name", how="right") #right merge
print(right)

df4 = pd.merge(df1, df2, how="outer") # Merge with outer join
print(df4)

df5 = pd.concat([df1, df2]) # Concatenate (since the columns are the same, it will stack them vertically)
print(df5)

df5 = df5.drop_duplicates() # Drop duplicates
print(df5)

df6 = pd.concat([df1, df2], axis=1) # Concatenate (since the columns are the same, it will stack them horizontally)
print(df6)
