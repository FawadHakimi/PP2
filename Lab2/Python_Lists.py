a = ['Ali', 'Fawad', 'Musawer', 'Ahmad', 'Daulat']
print(a[0])
print(a[2])
print(a[-1])
print(a[1:3])
print(a[:4])
print(a[3:])

if "Fawad" in a:
    print("Yes, it is available")

a[2] = "Murat"
print(a)

a.insert(2, "Alex")
print(a)

a.append("MOHAMMAD")
print(a)

a.remove("Ali")
print(a)

a.pop(2)
print(a)

#del a
#clear a()

Books = ['Math', 'Physics', 'Chemistry', 'English']
for x in Books:
    print(x)

Animals = ['Cat', 'Dog', 'Tiger', 'Lion']
i = 0
while i < len(Animals):
    print(Animals[i])
    i+=1

Schools = ['KBTU', 'KAZNU', 'KIMEP', 'ABAI']
Schools.sort()
print(Schools)

Schools = ['KBTU', 'KAZNU', 'KIMEP', 'ABAI']
Schools.sort(reverse = True)
print(Schools)

Schools = ['KBTU', 'KAZNU', 'KIMEP', 'ABAI']
Schools.reverse()
print(Schools)

join = Animals + Schools
print(join)

