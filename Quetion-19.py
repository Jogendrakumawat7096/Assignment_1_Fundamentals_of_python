'''Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''

s =input("Enter strng")

s1= s.find("not")
s2=s.find("poor")

s.replace(s[s1:s2],"good")
print(s)
