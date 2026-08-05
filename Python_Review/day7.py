## Pandas Data Cleaning and Analysis ##
## Part 1: Practice ##
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Bob", "Sara", "Tom", "Tom"],
    "Age": [22, None, 25, 24, 30, 30],
    "Department": ["IT", "Sales", "Sales", "IT", "Sales", "Sales"],
    "Score": ["85", "70", "70", "90", "80", "80"]
}

df = pd.DataFrame(data)

## Ex1: Missing values ##
print(f"{df.isna().sum()}")  # Check for missing values
df_2 = df.dropna()  # Drop rows with missing values
print(f"{df_2.isna().sum()}")  # Check again for missing values
df_3 = df.fillna(0)  # Fill missing values with 100
print(df_3)  # Check again for missing values

## Ex2: Removing duplicates ##
df_4 = df_2.duplicated()  # Check for duplicates
print(df_4)
df_5 = df_2.drop_duplicates()  # Drop duplicates
print(df_5)  # Check again for duplicates

## Ex3: Data Renaming ##
df_5["Department"] = df_5["Department"].replace({"IT": "Information Technology", "Sales": "Sales and Marketing"})  # Rename values in column
print(df_5)  # Check the renamed column

## Ex4: Data Type Conversion ##
df_5["Score"] = df_5["Score"].astype(str)  # Convert column to string
print(df_5.dtypes)  # Check the data types of the columns
print(df_5)  # Check the data types of the columns

## Ex5: Data Grouping ##
df_6 = df_5.groupby("Department")  # Group by a column
print(df_6)  # Check the grouped data   

## Ex6: Data Aggregation ##
df_7 = df_6.agg({"Age": "mean", "Score": "max"})  # Aggregate data
print(df_7)  # Check the aggregated data    

## Ex7: Counting Categories ##
df_8 = df_5["Department"].value_counts()  # Count occurrences of each category
print(df_8)  # Check the counts

## Part 2: Data Cleaning Exercises ##

data = {
    "Name": ["Alice", "Bob", "Sara", "David", "Alice", "Emma"],
    "Department": ["IT", "Sales", "IT", "Sales", "IT", None],
    "Age": [24, 31, 27, None, 24, 29],
    "Salary": [42000, 51000, 47000, 55000, 42000, None]
}

df = pd.DataFrame(data)

## Ex1: Display the DataFrame and inspect its information ##
df.head()  # Display the first few rows of the DataFrame
df.tail()  # Display the last few rows of the DataFrame
df.shape  # Check the shape of the DataFrame
df.columns  # Check the column names of the DataFrame
df.index  # Check the index of the DataFrame
df.dtypes  # Check the data types of the columns
df.duplicated
df.info()  # Check the data types of the columns
df.describe()  # Check the summary statistics of the columns


## Ex2: Find missing values in each column ##
missing_values = df.isna().sum()  # Check for missing values in each column
print(missing_values)  # Display the missing values

## Ex3: Replace the missing department with "Unknown" ##
filled_df = df.fillna({"Department": "Unknown"})  # Fill missing values in the "Department" column with "Unknown"
print(filled_df)  # Display the DataFrame with missing values filled

## Ex4: Replace the missing age with the average age ##
filled_df_2 = df.fillna({"Age": df["Age"].mean()})  # Fill missing values in the "Age" column with the average age
print(filled_df_2)  # Display the DataFrame with missing values filled

## Ex5: Replace the missing salary with the average salary ##
filled_df_3 = filled_df_2.fillna({"Salary": df["Salary"].mean()}) # Fill missing values in the "Salary" column with the average salary
print(filled_df_3)  # Display the DataFrame with missing values filled

## Ex6: Remove duplicate rows ##
df_no_duplicates = filled_df_3.drop_duplicates()  # Drop duplicate rows from the DataFrame
print(df_no_duplicates)  # Display the DataFrame without duplicates

## Ex7: Rename Name to Employee_Name ##
df_renamed = df_no_duplicates.rename(columns={"Name": "Employee_Name"})  # Rename the "Name" column to "Employee_Name"
print(df_renamed)  # Display the DataFrame with the renamed column

## Ex8: Convert Age to integer ##
df_renamed["Age"] = df_renamed["Age"].astype(int)  # Convert the "Age" column to integer
print(df_renamed.dtypes)  # Display the data types of the columns   

## Part 3: Analysis Exercises ##
## Ex1: Average salary of all employees ##
average_salary = df_renamed["Salary"].mean()  # Calculate the average salary of all employees
print(f"Average Salary: {average_salary}")  # Display the average salary

##Ex2: Highest salary ##
highest_salary = df_renamed["Salary"].max()  # Find the highest salary
print(f"Highest Salary: {highest_salary}")  # Display the highest salary

## Ex3: Employee with the highest salary ##
Top_salary_employee = df_renamed[df_renamed["Salary"] == highest_salary] # Find the employee(s) with the highest salary
print(Top_salary_employee)  # Display the employee with the highest salary

## Ex4: Number of employees in each department ##
employees_per_department = df_renamed.groupby("Department").size()  # Count the number of employees in each department
print(employees_per_department)  # Display the number of employees in each department

## Ex5: Average salary for each department ##
salary_average_per_department = df_renamed.groupby("Department").agg({"Salary" : "mean"}) # Calculate the average salary for each department
print(salary_average_per_department)  # Display the average salary for each department

## Ex6: Average age for each department ##
average_age_per_department = df_renamed.groupby("Department").agg({"Age" : "mean"}) # Calculate the average age for each department
print(average_age_per_department)  # Display the average age for each department

## Ex7: Employees whose salary is greater than €45,000 ##
top_salaries = df_renamed[df_renamed["Salary"] > 45000]  # Filter employees with salary greater than €45,000
print(top_salaries)  # Display the filtered DataFrame   

## Ex8: Employees sorted by salary from highest to lowest ##
sorted_salary = df_renamed.sort_values(by = "Salary", ascending = False)  # Sort employees by salary from highest to lowest
print(sorted_salary)  # Display the sorted DataFrame