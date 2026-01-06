# Check whether a number is prime or not
n=int(input("Enter a number: "))
if n<=1:
    print(n,"is not a prime number")
else:
    for i in range(2, n):
        if n%i==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")




        #output
        #Enter a number: 4
#4 is not a prime number
