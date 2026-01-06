#Write a Python program that takes a single character as input from the user and checks if it is
#a vowel or a consonant. If the input is not an alphabetic character, print ”Invalid input.”

n=input("Enter a single character: ")
if n.isalpha():
    if n.lower() in "aeiou":
        print("It is a vowel.")
    else:
        print("It is a consonant.")
else:
    print("Invalid input.") 
   


     #output:
    #Enter a single character: a
     #It is a vowel.