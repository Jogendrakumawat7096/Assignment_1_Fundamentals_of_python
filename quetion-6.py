# Write python program that swap two number with temp variable and without temp variable.

a =int(input("Enter a value : "))
b =int(input("Enter b value : "))


# with temp variable
temp = a
a=b
b=temp

print("value of a after swap:",a)
print("value of b after swap:",b)


 
# Swapping of two variables
# without using third variable
a = 10
b = 50
a, b = b, a
 
print("Value of a:", a)
print("Value of b:", b)


