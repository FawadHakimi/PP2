fruits = ('Pomegranate', 'Banana', 'Orange', 'Pineapple')
print(fruits)

print(fruits[1])

books = ('Math', 'Physics', 'Biology', 'Chemistry')
y = list(books)
y[1] = "History"
x = tuple(y)
print(books)
print(x)

cities = ('Astana', 'Almaty', 'Istanbul', 'Kabul')
#If we want to add another city to this tuple, we can create another tuple and add them.
city = ('Seoul',)
cities += city
print (cities)

