#CHECK IF A NUMBER IS POSITIVE,NEGATIVE,ZERO
# in this example, you will learn to check whether a number entered by user is positive, negative or zero. this problem is solved if...elif...else  &nested  if...else statement

#through if...elif...else
sharad=float(input("Enter a number : "))
if sharad >0:
    print("positive number")
elif sharad==0:
    print("zero")
else:
    print("Negative number")
        
#using the nested if:
sharad=float(input("enter the number"))
if sharad >=0:
    if sharad==0:
        print("zero")
    else:
        print("positive number")
else:
    print("negative number")


#execute one block 5 times
for i in range(5):
    sharad=float(input("Enter a number : "))
    if sharad >0:
      print("positive number")
    elif sharad==0:
      print("zero")
    else:
       print("Negative number")    
