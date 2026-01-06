#Write a Python program to print first N terms of an arithmetic progression
n=int(input("Enter the value of n: "))
a=int(input("Enter the first term (a): "))
d=int(input("Enter the common difference (d): "))
for i in range(n):
        print(a + i * d)        


        #output
        #Enter the value of n: 4
#Enter the first term (a): 1
#Enter the common difference (d): 3
#1
#4
#7
#10