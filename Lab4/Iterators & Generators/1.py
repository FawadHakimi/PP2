n = int(input())
square_generator = (i*i for i in range(1, n+1))

for x in square_generator:
    print(x)