# Write a Python function to reverses a string if its length is a multiple of 4.



# s = "Jogendra"
# if len(s)%4==0:
#     print(s[::-1])


# using function
s = input("enter : ")
def reverse_string(str1):
    if len(str1) % 4 == 0:
        print(str1[::-1])    
reverse_string(s)
