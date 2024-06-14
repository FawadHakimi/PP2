Dict_cars = {"Brand" : "BMW",
             "Model" : 2023,             
             "price" : 100000 }
print(Dict_cars)
print(Dict_cars["price"])

Dict_cars.update({"price" : 99999})
print(Dict_cars)

print(len(Dict_cars))

x = Dict_cars.keys()
print(x)
y = Dict_cars.values()
print(y)

names = {"Singer" : "Tyla",
         "Wealth" : "10 Million",
         "Country": "South Africa"}
names["Fav color"] = "Red"
print(names)
names.update({"Wealth" : "12 Million"})
print(names)


names.pop("Wealth")
print(names)

names_2 = names.copy()
print(names_2)


