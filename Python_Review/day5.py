## Part1: NumPy Fundamentals ##
import numpy as np

## Ex1: Create a vector from 1 to 20 ##
vector = np.arange(1, 21, 1)
print(vector)

## Ex2: Create a 5×5 matrix of random integers (0–100) ##
matrix = np.random.randint(0, 101, size=(5, 5))
print(matrix)

## Ex3: Create a 1000-sample Gaussian signal ##
signal = np.random.normal(0, 1, 1000)
print(signal)

## Part2: Array Shape Operations ##

print(f"The shape of matrix is: {np.shape(matrix)}")
print(f"Matrix has a {np.ndim(matrix)}_D dimension")
print(f"The size of vector is: {np.size(vector)}")
matrix_of_vector = vector.reshape(4,5)
print(matrix_of_vector)
vector_of_matrix = matrix.flatten()
print(vector_of_matrix)
vector_of_matrix_ravel = matrix.ravel()
print(vector_of_matrix_ravel)
matrix_transpose = matrix.T
print(matrix_transpose)

## Ex1: Create numbers 1–24 ##
numbers = np.arange(1,25)
print(numbers)
print(f"A 4×6 matrix of numbers is: {numbers.reshape(4,6)}")
print(f"A 2×12 matrix of numbers is: {numbers.reshape(2,12)}")
print(f"A 3×8 matrix of numbers is: {numbers.reshape(3,8)}")
print(f"A flat form of numbers is: {numbers.ravel()}")


## Part3: Indexing & Slicing ##
matrix3 = np.random.randint(0, 20, size=(5,5))
print(matrix3)

## Ex1: Given a 5×5 matrix, Print row 2 ##
print(f"The row 2 of matrix3 is: {np.array(matrix3[1, :])}")

## Ex2: , Print column 4 ##
print(f"The column 4 of matrix3 is: {np.array(matrix3[:, 3])}")

## Ex3: Print the center 3×3 ##
print(f"The central 3×3 submatrix of matrix3 is: {np.array(matrix3[1:4, 1:4])}")

## Ex4: Print values > 50 ##
print(f"The values of matrix3 that are greater than 5 are: {matrix3[matrix3>15]}")

## Part4: Mathematical Operations ##
## Ex1: Create two random 3×3 matrices and compute: Sum, Difference, Element-wise product, Matrix product ##
matrix1 = np.random.randint(0, 50, size=(3,3))
matrix2 = np.random.randint(0, 50, size=(3,3))
print(f"matrix 1 is: {matrix1} and matrix 2 is: {matrix2}")
print(f"The sum of matrix 1 and matrix 2 is: {np.add(matrix1, matrix2)}")
print(f"The difference of matrix 1 from matrix 2 is: {(matrix1 - matrix2)}")
print(f"The Element-wise product of matrix 1 and matrix 2 is: {(matrix1 * matrix2)}")
print(f"The product of matrix 1 and matrix 2 is: {(matrix1 @ matrix2)}")

## Part5: Statistics ##
## Ex1: For a random 10×10 matrix calculate: Mean, Standard deviation, Maximum, Minimum, Sum ##
ten_by_ten_matrix = np.random.randint(0, 50, size= (10, 10))
print(ten_by_ten_matrix)
print(f"The mean value of the ten_by_ten_matrix is: {np.mean(ten_by_ten_matrix)}")
print(f"The standard deviation value of the ten_by_ten_matrix is: {np.std(ten_by_ten_matrix)}")

## Print max value of all elements ##
print(f"The maximum value of the ten_by_ten_matrix is: {np.max(ten_by_ten_matrix)}")
## Print the index of max value of all elements ##
print(f"The index of the maximum value of the ten_by_ten_matrix is: {np.argmax(ten_by_ten_matrix)}")
## Print the max value of each row ##
print(f"The maximum value of each row of the ten_by_ten_matrix is: {np.max(ten_by_ten_matrix, axis=1)}")
## Print the index of max value of each row ##
print(f"The index of the maximum value of the ten_by_ten_matrix is: {np.argmax(ten_by_ten_matrix, axis=1)}")
## Print the max value of each column ##
print(f"The maximum value of each row of the ten_by_ten_matrix is: {np.max(ten_by_ten_matrix, axis=0)}")

print(f"The minimum value of the ten_by_ten_matrix is: {np.min(ten_by_ten_matrix)}")
print(f"The index of the minimum value of the ten_by_ten_matrix is: {np.argmin(ten_by_ten_matrix)}")

## Print the sum of all elements ##
print(f"The sum of the ten_by_ten_matrix elements is: {np.sum(ten_by_ten_matrix)}")

## Mini Challenge ##
## Generate a 100×5 random dataset ##
data = np.random.uniform(0, 50, (100,5))

## Compute mean of each column ##
(row, column) = (np.shape(data))
column = int(column)
for number in range(0,column):  
    print(f"The mean of column {number +1} is: {np.mean(data[:,number])}")
### or: ###
print(f"The mean of columns is: {data.mean(axis=0)}")

## Compute Standard deviation of each column ##
for number in range(0,column):  
    print(f"The standard deviation of column {number +1} is: {np.std(data[:,number])}")

### or: ###
print(f"The standard deviation of columns is: {data.std(axis=0)}")

## Normalize each column ##
normalized = (data - data.mean(axis=0)) / data.std(axis=0)
print(normalized[1:7,:])

## Verify that each normalized column has approximately mean = 0 and std = 1 ##
normalized_mean = normalized.mean(axis=0)
print(normalized_mean)

normalized_std = normalized.std(axis=0)
print(normalized_std)