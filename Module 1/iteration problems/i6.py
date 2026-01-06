#Write a Python program to print even numbers from a starting number to an ending number
s = int(input("Enter the starting number: "))
e= int(input("Enter the ending number: "))
for i in range (s,e,1):
    if i%2==0:
        print(i)    



        #output
       # Enter the starting number: 2
       #Enter the ending number: 6
        #2
         #4