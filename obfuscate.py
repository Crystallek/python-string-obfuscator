import secrets
import string
import random
import time
import os

chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.hexdigits + string.punctuation
my_secure_rng = secrets.SystemRandom()

while True:
    x = str(input("string to obfuscate: "))

    def findindex(array, sub):
        counter = 0
        while counter <= len(array) - 1:
            if str(sub) == array[counter]: 
                return counter
            else: 
                counter += 1

    totalString = []
    completedString = ""

    for k in x:
        rint = random.randint(1, 7)
        converted = str(hex(ord(k)))
        string00 = ''.join(secrets.choice(chars) for i in range(4))
        string0 = ''.join(secrets.choice(chars) for i in range(2))
        string1 = ''.join(secrets.choice(chars) for i in range(rint))
        string2 = ''.join(secrets.choice(chars) for i in range(rint*2))
        string3 = ''.join(secrets.choice(chars) for i in range(rint*3))
        string4 = ''.join(secrets.choice(chars) for i in range(rint*4))
        string5 = ''.join(secrets.choice(chars) for i in range(rint*5))
        pogstring = string00 + string.ascii_lowercase[len(string.ascii_lowercase) - rint*2] + string0 + string.punctuation[len(string.punctuation) - rint*2] + string1 + converted[0] + string.ascii_lowercase[len(string.ascii_lowercase) - rint] + string2 + converted[1] + string.ascii_uppercase[len(string.ascii_uppercase) - rint*3] + string3 + converted[2] +  string.digits[len(string.digits) - rint*2 - 5] + string4 + converted[3] + string5 
        totalString.append(pogstring)
    print(totalString)

    filename = f"obfuscated{round(time.time())}.txt"

    with open(filename, "a", encoding="utf-8") as f:
        for i in totalString:
            f.write(f"{i}\n")
    print(f"written to {os.path.dirname(__file__)}\{filename}")
