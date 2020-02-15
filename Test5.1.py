#Test5.1.py
import random

def genpwd(length):
    val = random.randint(10**(length-1),10**length-1)
    return val

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
