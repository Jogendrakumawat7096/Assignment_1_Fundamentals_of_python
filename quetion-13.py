# Write a Python program to count the number of characters (character frequency) in a string

str1 = input ("Enter string: ")
d1=dict()
for i in str1:
    if i in d1:
        d1[i] = d1[i]+1
    else:
        d1[i]=1
print(d1)


   


    
