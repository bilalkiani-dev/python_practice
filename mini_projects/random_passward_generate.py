import random
import string

pasch = string.ascii_letters+string.digits+string.punctuation
pass_len = 12
passward = ""
for i in range(pass_len):
    passward+= random.choice(pasch)
print("Your strong random passward is: ",passward)

# we can do the samem work with list comprehension [function for in in range(n)]

passwardd = "".join([random.choice(pasch) for i in range(pass_len)])
print("your strong random passward is: ", passwardd)