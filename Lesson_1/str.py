
# String methods in Python
# WE USE IT TO MANIPULATE STRINGS
# String methods are built-in functions that allow you to perform various operations on strings.
string = " yamen hisham "

string = string.strip() # removes leading and trailing whitespace
title = string.title() # converts the first character of each word to uppercase
upper = string.upper() # converts all characters to uppercase
lower = string.lower() # converts all characters to lowercase
cap = string.capitalize() # converts the first character of the string to uppercase

print("srip", string)
print("title", title) 
print("upper" ,upper)
print("lower",lower)
print("cap", cap) 


# string replace 
string = "I love math" 

new_string = string.replace("math", "python") # replaces a substring with another substring

print(new_string) # I love python


# Count occurrences of a substring
text = "hello hello hello"
print(text.count("l")) # returns the number of occurrences of the substring "hello" in the string 

print(text.find("l")) # returns the index of the first occurrence of the substring "hello" in the string # returns the number of occurrences of the substring "hello" in the string from index 0 to index 5