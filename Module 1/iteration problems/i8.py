#Find the factors of a number

n=int(input("Enter a number: "))
print ("factors of ",n,"are:")
for i in range (1,n+1):
    if n%i==0:
        print(i)


#output
#Enter a number: 4
#factors of  4 are:
#1
#2
#4