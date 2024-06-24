def check_33(x):
    for i in range(len(x)-1):
        if x[i:i+2]==[3,3]:
            return True
    return False
print(check_33([2, 5, 6]))
print(check_33([3, 3, 1, 3]))
print(check_33([11, 3, 3]))