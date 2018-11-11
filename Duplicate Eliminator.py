def duplicates(x):
    return list(set(x))


def duplicate_v2(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)




a = [1,2,3,4,4,4,5,5,5,8,8,8]
print (a)

print (duplicates(a))
print (duplicate_v2(a))



