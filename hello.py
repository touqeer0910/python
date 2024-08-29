import math

def easy_gcd():
    """Calculate the GCD of two integers using the built-in math.gcd function."""
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    result = math.gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {result}.")

# Example usage
if __name__ == "__main__":
    easy_gcd()