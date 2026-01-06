#Determine the nature of the solution of the quadratic equation
a=int(input("Enter the value of n: "))
b=int(input("Enter the value of a: "))
c=int(input("Enter the value of b: "))

D=b**2 - 4*a*c
if D>0:
    print("Real and Distinct Roots")
elif D==0:
    print("Real and Equal Roots")
else:
    print("Imaginary Roots")



    #output
    #Enter the value of n: 56
    #Enter the value of a: 4
    #Enter the value of b: 6
    #Imaginary Roots