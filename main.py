print("Hello World")
list_2 = [87, 3, 8, 6, 15, 23, 2]
n = len(list_2)
print(n)
for p in range(0, n):
    for i in range (0, n-1):
        if list_2[i] > list_2[i+1]:
            list_2[i], list_2[i+1] = list_2[i+1], list_2[i]
    print (list_2)
