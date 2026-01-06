#Check whether a number is 3-digit or not
n=int(input("Enter a number: "))    
if 100<=abs(n)<=999:
    print(f"{n} is a 3-digit number")
else:
    print(f"{n} is not a 3-digit number")   



    #output:
   # Enter a number: 56
     # 56 is not a 3-digit number