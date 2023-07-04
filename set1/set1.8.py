def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
 
input_number = 5
factorial_result = factorial(input_number)
if factorial_result is None:
    print("Cannot calculate factorial of a negative number.")
else:
    print("Factorial of", input_number, "is", factorial_result, ".")
