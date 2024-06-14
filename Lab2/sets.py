set_books = {'History', 'Geography', 'English', 'Geology'}
print(set_books)
print(len(set_books))

for x in set_books:
    print(x)

print("English" in set_books)

set_books.add("Biology")
print(set_books)

animals = {'Dog', 'Cat', 'Tiger'}
fruits = {'Banana', 'Pomegranate', 'Cherry'}
animals.update(fruits)
print(animals)

s = animals | fruits
print(s)

cities = {'Istanbul', 'Jakarta', 'Miami'}
cities.remove('Istanbul')
print(cities)

Letters = {'A', 'V', 'L', 'B'}
Letters.discard('V')
print(Letters)

Names = {'Ali', 'Murat', 'Wali', 'Daulet'}
Names.pop()
print(Names)

