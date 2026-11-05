#Recursive function: Factorial Utility
def factorial(n):
    if n<0:
            print("Error! number can't be nagative")
    elif n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(0))
print(factorial(-3))