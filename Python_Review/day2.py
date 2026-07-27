list =[5, 4, 3, 2, 1]
print(list[0])
print(list[-1])
list[2] = 10
print(list)
print(sum(list))
def average(numbers:float) -> float:
    ## Calculate the average of a list of floats ##
    average_val = sum(numbers)/len(numbers)
    return average_val

print(average(list))

def minimum(numbers : float) -> float:
    ## Find the minimum value in a list of floats ##
    minimum_val = min(numbers)
    return minimum_val

print(minimum(list))

def maximum(numbers : float) -> float:
    ## Find the maximum in a list of floats ##
    maximum_val = max(numbers)
    return maximum_val

print(maximum(list))

def is_even(numbers : int) -> bool:
   ## Check if each component is even or odd ##
   result = []
   for number in numbers: 
      result.append(number%2 == 0)
   return result

print(is_even(list))

def print_even(numbers : int) -> int:
    result = []
    for number in numbers:
        if number%2 == 0:
            result.append(number)
    return result

print(print_even(list))

def square(numbers : float) -> float:
    result = []
    for number in numbers:
        result.append(number**2)
    return result

print(square(list))

def sum_withouth_func(numbers : float) -> float:
    result = 0
    for number in numbers:
        result += number
    return result

print(sum_withouth_func(list))