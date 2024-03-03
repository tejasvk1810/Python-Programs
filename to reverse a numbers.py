#python program to reverse a number
#in  this example, you willlearn to reverse a number
#reverse a number using the while loop
sharad=1234
reverse_sharad=0 # for storing
while sharad !=0:
    digit=sharad%10  #here first 4 remainder means 4 is separated
    reverse_sharad=reverse_sharad*10+digit
    sharad//=10
print("reverse number :"+str(reverse_sharad))

#now we will do by string slicing 
sharad=123456
print(str(sharad)[::-1])#star:stop:step

#
 


