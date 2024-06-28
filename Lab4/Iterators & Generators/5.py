n = int(input())
generator = (i for i in range(n, -1, -1))
for number in generator:
    print(number)