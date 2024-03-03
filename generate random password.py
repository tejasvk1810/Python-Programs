#genertate random password

#to write a python program to create a password, declare  a string ofmnumber +uppercase + lower case +special character take a random sample of string of a length given by user:

import random
sharadlen=int(input("please enter the length of the password to generated : "))
sharad="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ0123456789!@#$%^&*?"
password="".join(random.sample(sharad,sharadlen))
print(password)

#sample()- it returns particular list of items