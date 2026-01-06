#Write a Python program that checks the strength of a password entered by the user. The
#program should categorize the password as: ”Weak” if it is less than 6 characters. ”Medium”
#if it is between 6 and 10 characters. ”Strong” if it is more than 10 characters.


n=int(input("Enter the length of the password: "))  
if n < 6:
    print("Weak")
elif 6<=n<10:
    print("Medium")
else:
    print("Strong")    



    #output
    #Enter the length of the password: 6
    #Medium