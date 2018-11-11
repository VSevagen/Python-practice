list = [int(x) for x in input().split()]
list1 = [int(y) for y in input().split()]
list2 = []
a = len(list)
b = len(list1)
print(a)
print(b)

for i in range (0,a):
    for j in range (0,b):
        if (list[i]==list1[j]):
            list2.append(list[i])

print(list2)
