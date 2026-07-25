def average (numbers: list[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    average = sum(numbers) / len(numbers)
    return average

def maximum (numbers:list[float]) -> float:
    """Return the maximum value in a list of numbers."""
    maximum = max(numbers)
    return maximum

def minimum (numbers:list[float]) -> float:
    """Return the minimum value in a list of numbers."""
    minimum = min(numbers)
    return minimum

def standard_deviation (numbers:list[float]) -> float:
    """Return the standard deviation of a list of numbers."""
    variance = sum((numbers[number] - average(numbers))**2 for number in numbers)
    std = (variance/len(numbers))**(1/2)
    return std

numbers = [10, 20, 30, 40, 50]
print(f"The Average is: {average(numbers)}")
print(f"The Maximum is: {maximum(numbers)}")
print(f"The Minimum is: {minimum(numbers)}")
print(f"The Standard Deviation is: {standard_deviation(numbers)}")