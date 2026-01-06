#A Python program to read a number N and print the even numbers in reverse order starting
#from N

n=int(input("Enter the value of n: "))
for i in range (n,-1,-1):
    if i%2==0:
        print(i) 


        #output
        #Enter the value of n: 5
#4
#2
#0