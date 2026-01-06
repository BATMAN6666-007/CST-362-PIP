#Find the large digit in a two-digit number
num = int(input("Enter a two-digit number: "))
n=num // 10
m=num % 10  
if n>m:
    print("The largest digit is:",n)
elif m>n:
    print("The largest digit is:",m)
else:
    print("Both digits are equal:",n)   

      #OUTPUT
    #Enter a two-digit number: 34
    #The largest digit is: 4