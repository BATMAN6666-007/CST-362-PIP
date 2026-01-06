#Check whether a number is completely divisible by another number

n=int(input("Enter the first number: "))
m=int(input("Enter the second number: "))
if n%m==0:
    print( n ,"is completely divisible by", m)
else:
    print( n ,"is not completely divisible by", m)

#output:
# Enter the first number: 10
# Enter the second number: 2
# 10 is completely divisible by 2