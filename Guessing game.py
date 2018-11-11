import random
list = [1,2,3,5,6,7,8,9]
data = random.choice(list)
guess = 1

print ("Guess a number ")
ans = int(input())

if(ans == data):
    print("Correct guess ")




while (ans != data ):


    if (ans > data):
        print("Your guess is too high")
    elif(ans < data):
        print("Your guess is too low")
    guess +=1
    print ("Guess a number ")
    ans = int(input())
    if (ans==data):
        print("Good guess")


print ("The number of guesses is ",guess)