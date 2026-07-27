numbers  =[5, 4, 3, 2, 1]
print(numbers[0])
print(numbers[-1])
numbers[2] = 10
print(numbers)
print(sum(numbers))
def average(numbers : list[float]) -> float:
    ## Calculate the average of a list of floats ##
    average_val = sum(numbers)/len(numbers)
    return average_val

print(average(numbers))

def minimum(numbers : list[float]) -> float:
    ## Find the minimum value in a list of floats ##
    minimum_val = min(numbers)
    return minimum_val

print(minimum(numbers))

def maximum(numbers : list[float]) -> float:
    ## Find the maximum in a list of floats ##
    maximum_val = max(numbers)
    return maximum_val

print(maximum(numbers))

def is_even(numbers : list[int]) -> bool:
   ## Check if each component is even or odd ##
   result = []
   for number in numbers: 
      result.append(number%2 == 0)
   return result

print(is_even(numbers))

def print_even(numbers : list[int]) -> list[int]:
    result = []
    for number in numbers:
        if number%2 == 0:
            result.append(number)
    return result

print(print_even(numbers))

def square(numbers) :
    return [number**2 for number in numbers]

print(square(numbers))

def sum_withouth_func(numbers : list[float]) -> float:
    result = 0
    for number in numbers:
        result += number
    return result

print(sum_withouth_func(numbers))