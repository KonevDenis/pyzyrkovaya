print("Hello World")
jojo = open("number.txt", "r")
number = jojo.readline()
print(number)
spisok = number.split()
spisok1 = []
print(spisok)
for a in spisok:
    spisok1.append(int(a))
print(spisok1)
n = len(spisok)
print(n)
for p in range(0, n):
    for i in range (0, n-1):
        if spisok1[i] > spisok1[i+1]:
            spisok1[i], spisok1[i+1] = spisok1[i+1], spisok1[i]
    print (spisok1)

