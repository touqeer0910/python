def factorial(number):
    result = 1
    for index in range(1,number+1):
        result *= index
    return result

factorial(5)


# This program is failing for some inputs
def average(lst):
    return sum(lst+lst)/len(lst)