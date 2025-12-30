#Swap 2 numbers using a temporary variable

n=int(input("enter first number: "))
m=int(input("enter second number: "))

temp=n
n=m
m=temp  
print("the value of n after swapping:",n)
print("the value of m after swapping:",m)

#output
#enter first number: 5
#enter second number: 7
#the value of n after swapping: 7
#the value of m after swapping: 5