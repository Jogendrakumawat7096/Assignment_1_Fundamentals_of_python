# Write a Python program to get the Factorial number of given number

n = int(input("Enter N Value:"))
factorial=1
if n < 0:
    print("factorial not available for negative number")
elif n == 0:
    print("Zero Factorial number is 1")
else:
    for i in range(1,n + 1):
       factorial = factorial*i
    print("The factorial of",n,"is",factorial)
