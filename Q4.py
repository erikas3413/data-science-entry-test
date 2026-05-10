#Q4 

def string_reverse(s):
    if not isinstance(s, str):
        return -1
    
    reversed_str = ""           # start with empty string
    for char in s:              # go through each character
        reversed_str = char + reversed_str   # add it to the FRONT
    return reversed_str

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

result1 = string_reverse("Hello World")
print(result1)
# Output: dlroW olleH

result2 = string_reverse("Python")
print(result2)
# Output: nohtyP