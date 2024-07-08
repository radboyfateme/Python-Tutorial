import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)
# print(string.printable)

print(string.capwords('hanar'))

t1=string.Template('Answer is: $x > $y')
s=t1.substitute(x=23, y=14)
print(s)