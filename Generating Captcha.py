import random
b=""
for i in range(6):
    a=random.randint(47,120)
    b=b+chr(a)
print("Captcha:",b)