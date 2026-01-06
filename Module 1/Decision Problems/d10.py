#Find the largest of 3 numbers

n1=int(input("enter first no :"))
n2=int(input("enter the second no :"))
n3= int(input("enter the third no : "))
if (n1>n2) and (n1>n3):
    print(n1 , "is largest")    
elif n2>n1 and n2>n3:
    print(n2 , "is largest" )

else:
    print(n3 , "is largest")        



#output
#enter first no :2
#enter the second no :1
#enter the third no : 1
#2 is largest