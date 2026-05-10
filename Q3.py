#Q3

#Task 1

def update_dictionary(dct, key, value):
    if not isinstance(dct, dict):
        return -1
    if key in dct:
        print("Original value:", dct[key])
    dct[key] = value
    return dct

#Task 2

result1 = update_dictionary({}, "name", "Alice")
print(result1)
# Output: {'name': 'Alice'}

result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)
# Output:
# Original value: 25
# {'age': 26}