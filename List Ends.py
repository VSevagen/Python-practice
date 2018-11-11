def new_list():

    list = [int(x) for x in input().split()]
    a = len(list)
    print (a)
    list1 = []

    list1.append(list[0])
    list1.append(list[a-1])
    print(list1)

game=new_list()
