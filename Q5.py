#Q5 

def check_divisibility(num, divisor):
    # Check both are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return -1
    
    # Guard against division by zero
    if divisor == 0:
        return -1
    
    # Check divisibility
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

result1 = check_divisibility(10, 2)
print(result1)
# Output: True   


result2 = check_divisibility(7, 3)
print(result2)
# Output: False 
