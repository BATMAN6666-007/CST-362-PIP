
#Convert the seconds to hours : minute : seconds
n=int(input("Enter the seconds:"))
hours=n//3600
n=n%3600
minutes=n//60
seconds=n%60
print("The time is %d:%d:%d"%(hours,minutes,seconds))



#output
#Enter the seconds:5677
#The time is 1:34:37