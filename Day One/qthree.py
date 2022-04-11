# RANDOM PASSWORD GENERATOR
import random
import string

print("Hello There! Welcome to the password generator")

#asking user how long they want the password to be
length = int(input('n\Enter the length of password: '))

#defining the data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols

#using random module to generate password
#passing the combined data along with the length of the password
temp = random.sample(all, length)
password = "".join(temp)

print(password)

#reducing the number of lines of code by eliminating the storage of data
ev = string.ascii_letters + string.digits + string.punctuation
pas = "".join(random.sample(ev,length))
print(pas)
