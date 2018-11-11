def Fibonnaci(n):

    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(0, n-2):
        c = a + b
        print(c)
        a = b
        b = c


print("Enter the lenght of sequence you want")
n = int(input())
get_answer = Fibonnaci(n)