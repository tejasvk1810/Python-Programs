#largest among them
#in this program, you'll learn to find the largest among three numbers using if else & display it
sharad1=10
sharad2=14
sharad3=12
if(sharad1>=sharad2) and (sharad1>=sharad3):
    largest=sharad1
elif(sharad2>=sharad1) and (sharad2>=sharad3):
    largest=sharad2
else:
    largest=sharad3
print("the largest number is : ",largest)

#accept input from user
sharad1=float(input("enter the first number :"))
sharad2=float(input("enter the second number :"))
sharad3=float(input("enter the third number :"))

if(sharad1>=sharad2) and (sharad1>=sharad3):
    largest=sharad1
elif(sharad2>=sharad1) and (sharad2>=sharad3):
    largest=sharad2
else:
    largest=sharad3
print("the largest number is : ",largest)    



