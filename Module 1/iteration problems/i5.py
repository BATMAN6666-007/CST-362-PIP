#Find the sum of odd numbers in a set of N numbers
n=int(input("Enter the value of n: "))
sum=0
for i in range(n):
    num=int(input("Enter number: "))
    if num%2!=0:
        sum+=num
print("Sum of odd numbers is:", sum)    



#output
#Enter the value of n: 3
#Enter number: 22
#Enter number: 1
#Enter number: 3
#Sum of odd numbers is: 4