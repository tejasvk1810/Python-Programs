#CHECK THE NUMBER IS EVEN OR ODD

#python program to check if a number is odd or even
#in this example,you will learn to check whether a number entered by the user is even or odd

for i in range(5):
 sharad=int(input("Enter the number : "))
 if (sharad%2)==0:
     print("{0} is a Even number ".format(sharad))
 else:
    print("{0} is a Odd number ".format(sharad))
    
 
    #{0}-for indexing and present the number that we have to given in input
    #format()-tuple data type  and each individual value contained in the tuple can be called bu=y its index number,which starts with the index number 0
