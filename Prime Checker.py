print("Enter a number")
ans = int(input())
count = 0

for i in range (1,ans+1):
    if (ans%i==0):
        count+=1


if count == 2:
    print("Number is prime")
else:
    print("NUmber is not prime")