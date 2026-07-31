## Part1: Object-Oriented Programming ##
## Ex1: Creat a class ##

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

## Create instances of the Student class ##
Student1 = Student("Alice", 20)
Student2 = Student("Bob", 22)
Student3 = Student("Charlie", 19)

## Call the introduce method for each student ##
Student1.introduce()
Student2.introduce()
Student3.introduce()

## Ex2: Circle class ##
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

## Create an instance of the Circle class ##
circle1 = Circle(5)

## Part2: Numpy ##
## Ex1: Create arrays
import numpy as np

## Craete a matrix or a 1D array ##
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
c = np.array([[4], [5], [6]])
## Zero matrixes ##
np.zeros(3)
np.zeros([3, 3])
## One matrixes ##
np.ones(4)
np.ones([2,3])
## To split a range ##
np.arange(0, 10, 2)
np.linspace(0, 1, 5)

## Ex2: Array properties ##
## Show the number of rows and columns ##
a.shape
## Show the number of components ##
b.size
## Show type of components ##
b.dtype
## Show Dimensions of the materix ##
b.ndim

## Ex3: Operations ##
# We had: a = np.array([1, 2, 3, 4]) #
d = np.array([5, 6, 7, 8])

e = d + a
f = d - a
g = a * d
h = d/a
i = a ** d

print(f"The summation is: {e}")
print(f"The difference is: {f}")
print(f"The multiplication is: {g}")
print(f"The devision is: {h}")
print(f"The power is: {i}")

## Ex4: Broadcasting ##
print(f"{a + 5}")
print(f"{a * 5}")

## Ex5: Statistics ##
print(f"{a + 5}")
print(f"{a + 5}")
print(f"The mean value of a is: {np.mean(a)}")
print(f"The standard deviation value of a is: {np.std(a)}")
print(f"The maximum value of a is: {np.max(a)}")
print(f"The minimum value of a is: {np.min(a)}")
print(f"The sum of components in a is: {np.sum(a)}")

## Ex5: Indexing ##
b1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(f"{a[2]}")
print(f"{a[1:3]}")
print(f"{b1[:,0]}")

## Ex6: Reshape ##
## Reshape a matrix to desired numbers of rows and columns ##
a_new = a.reshape(2,2)
a_new
## Convert a multi-dimensional NumPy array into a 1D array ##
b_new = b.flatten()
b_new

## Mini Challenge: Generate a 5×5 matrix of random integers from 0–100. --> mean, max, min, first row, last column ##
## Create a random matrix ##
random_matrix = np.random.randint(1,101, size=(5,5))

print(random_matrix)
print(f"The mean value of the random_matrix is: {np.mean(random_matrix)}")
print(f"The maximum value of the random_matrix is: {np.max(random_matrix)}")
print(f"The minimum value of the random_matrix is: {np.min(random_matrix)}")
print(f"The first row of the random_matrix is: {np.array(random_matrix[0,:])}")
print(f"The last column of the random_matrix is: {np.array(random_matrix[:,-1])}")


## Stretch Goal: Create a fake sensor signal ##
import numpy as np
## Create 1000 samples of a Gaussian signal with mean_value = 0 and standars_deviation = 1 ##
signal = np.random.normal(0, 1, 1000)
print(signal)

print(f"The mean value of signal is: {np.mean(signal)}")
print(f"The standard deviation of signal is: {np.std(signal)}")
print(f"The max value of signal is: {np.max(signal)}")
print(f"The min value of signal is: {np.min(signal)}")


