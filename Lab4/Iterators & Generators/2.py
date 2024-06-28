n = int(input())
generator = (str(i) for i in range(0, n + 1) if i % 2 == 0)
print(",".join(generator))