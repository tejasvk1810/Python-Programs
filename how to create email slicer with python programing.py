#how to create email slicer with python programming

#an email slicer is very useful program  for separating the username & domain name of an email address. in this examples,i(tejas khairnar) will explain how to write a program to create an email slicer with python
#tejas1810@datacode.com(example)

email=input("Please Enter The Your Email : ").strip()#strip-it is use for remove white space 
username=email[:email.index('@')]
domain_name=email[email.index('@')+1:]#here we use +1 beacuse in starting position it also consider @ and we have ti require after the position of @
format=(f"your username is'{username}' and your domain is '{domain_name}'")
print(format)