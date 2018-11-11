import random
list = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","b","n","m"]
list2 = ["1","2","3","4","5","6","7","8","9","0"]
list3 = ["!","@","#","$","%","^","&","*","(",")","-"]


def weak_pass():
    data = random.choice(list)
    data2 = random.choice(list2)
    data3 = random.choice(list3)

    ans = data+data2+data3
    return ans

def strong_pass():
    char = random.choice(list)
    num1 = random.choice(list2)
    num2 = random.choice(list2)
    spec = random.choice(list3)

    ans1 = char+num1+num2+spec
    return ans1

print(" Press 1 for strong password or 2 for weak password ")
input = int(input())
if input == 1:
    password = strong_pass()
    print (password)

else:
    password = weak_pass()
    print(password)