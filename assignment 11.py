#Question 1
import re
j=0
email=input("enter email")
a=re.finditer("^[a-z A-Z 0-9][_a-zA-Z0-9.]*(@)(gmail.com|yahoo.com)$",email)
for m in a:
    j=m.group()
if email==j:
    print("valid email")
else:
    print("invalid email")

#Question 2
import re
i=0
n=input("enter number")
a=re.finditer("^[6-9]\d{9}",n)
for m in a:
    i=m.group()
if n==i:
    print("valid Indian phone number")
else:
    print("Invalid Indian phone number")