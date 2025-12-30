
#Area and perimeter of a triangle ( p=a+b+c, a=sqrt(s(s-a)s-b)(s-c))

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
p=n1+n2+n3
import math
area= math.sqrt(p*(p-n1)*(p-n2)*(p-n3))
print("the perimeter of triangle is:",p)
print("the area of triangle is:",area)

#output
#Enter first number:2
#Enter second number:3
#Enter third number:4
#the perimeter of triangle is: 9
#the area of triangle is: 43.474130238568314