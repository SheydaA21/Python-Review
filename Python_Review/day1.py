numbers = []
def Average (numbers):
    Ave = sum(numbers) / len(numbers)
    return Ave

def Maximum (numbers):
    Max = max(numbers)
    return Max

def Minimum (numbers):
    Min = min(numbers)
    return Min

def Standard_Deviation (numbers):
    Num = sum((numbers[i] - Average(numbers))**2 for i in range(len(numbers)))
    STD = (Num**2/len(numbers))**(1/2)
    return STD

numbers = [10, 20, 30, 40, 50]
print(f"The Average is: {Average(numbers)}")
print(f"The Maximum is: {Maximum(numbers)}")
print(f"The Minimum is: {Minimum(numbers)}")
print(f"The Standard Deviation is: {Standard_Deviation(numbers)}")