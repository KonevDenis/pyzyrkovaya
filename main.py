print("Hello World")
jojo = open("number.txt", "r")
number = jojo.readline()
spisok = number.split()
print(spisok)
n = len(spisok)
print(n)
for p in range(0, n):
    for i in range (0, n-1):
        if spisok[i] > spisok[i+1]:
            spisok[i], spisok[i+1] = spisok[i+1], spisok[i]
    print (spisok)

