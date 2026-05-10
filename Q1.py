#Task 1
def swap(x,y):
    if not (isinstance(x, (int, float)) and  isinstance(y, (int,float))):
        return -1
    else:
        x, y = y, x
        return x, y
        
#Task 2
result1 = swap("Apple","10")
print("result1:", result1)
# output : result1: -1

result2 = swap(-9,17)
print("result2:", result2)
# output : result2: (17, -9)

