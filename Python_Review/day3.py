## Part1: Conditionals ##
# EX1:
 ## Get the age ##
print("Please enter your age:")
age = int(input())
## Check if the age is under 18, between 18 and 65, or older than 65 ##
if age < 18: 
    print("Child")
elif age < 65:
    print("Adult")
else:
    print("Senior")


# Ex2:
## Get 3 numbers ##
print("Please enter 3 numbers:")
num1 = float(input())
num2 = float(input())
num3 = float(input())
## Show the maximum of entered numbers ##
if num1>num2 and num1>num3:
    print(f"The maximum is: {num1}")
elif num2>num1 and num2>num3:
    print(f"The maximum is: {num2}")
else:
    print(f"The maximum is: {num3}")
#print(f"The maximum is: {max(num1, num2, num3)}")


# Ex3:
## Get the number ##
print("Please enter a number:")
num = float(input())
## Check if it is positive or negetive ##
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("The number is zero")


## Part2: Strings ##
# Ex1:
str1 = "Python Programming"
#print("Please enter your text:")
#str1 = input()
print(len(str1))
print(str1.lower())
print(str1.upper())

# Ex2:
## Count the number of occurrences of a character in a string ##
str2 = "a"
print(str1.count(str2))

# Ex3:
## Ask for a name and print Hello <name> ! ##
print("Please enter your name:")
print("Hello " + input() + "!")

# Ex4:
## Learn other string methods ##
str4 = "   Python Programming Exercises      "
print(str4.strip())
print(str4.replace("Python","Java"))
print("str4.split() = ", str4.split())
print(str4.strip().startswith("Python"))
print(str4.endswith(" "))


## Part3: Tuples ### 
# Ex1:
## Print the elements of a tuple ##
student = ("John", 30, "Computer Science")
for item in student: print(f"{item}")

## Packing and unpacking tuples with indexes ##
print(f"Name: {student[0]}, Age: {student[1]}, Major: {student[2]}")

## Packing and unpacking tuples with variables ##
name, age, major = student
print(f"Name: {name}, Age: {age}, Major: {major}")

## Part4: Dictionaries ##
# Ex1:
## Create a dictionary and print every key and value ##
student = {
    "name": "John",
    "age" : 30,
    "major" : "Computer Science"
}
for key, value in student.items():
    print(f"{key}: {str(value)}")


for key, value in student.items():
    print(f"{key} : {str(value)}")

# Ex2:
## Add a new key-value pair to the dictionary ##
student["country"] = "Germany"
for key, value in student.items():
    print(f"{key} : {str(value)}")

# Ex3:
## Change the age of the student ##
student["age"] = 20
for key, value in student.items():
    print(f"{key} : {str(value)}")

# Ex4:
## Delete the major of the student ##
del student["major"]
for key, value in student.items():
    print(f"{key} : {str(value)}")


## Part5: Numpy ##
import numpy as np
a = np.array([1, 2, 3, 4, 5])

print(a * 2)
print(a + 5)
print(a.mean())
print(a.max())
print(a.min())
print(a.sum())