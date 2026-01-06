#Check whether a number is perfect number or not
n=int(input("Enter a number: "))
sum=0
for i in range(1, n):
    if n%i==0:
        sum+=i
if sum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")   


#output
# #Enter a number: 6
#6 is a perfect number


