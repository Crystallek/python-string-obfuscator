import string

while True:
    path = input("path to txt file pls ")
    completedString = ""

    with open(path, "r", encoding="utf-8") as f:
        totalString = f.readlines()

    def findindex(array, sub):
        counter = 0
        while counter <= len(array) - 1:
            if str(sub) == array[counter]: 
                return counter
            else: 
                counter += 1

    for a in totalString:
        indlowercase = findindex(string.ascii_lowercase, a[4])
        delind = int((len(string.ascii_lowercase) - indlowercase) / 2)
        str1 = a[8 + delind]
        str2 = a[10 + delind*3]
        str3 = a[12 + delind*6]
        str4 = a[14 + delind*6 + delind*4]
        unobf = str1 + str2 + str3 + str4
        bytes_object = bytes.fromhex(unobf[2:])
        ascii_string = bytes_object.decode("ASCII")
        completedString = completedString + ascii_string

    print(f"Obfuscated string: {totalString}")
    print(f"Deobfuscated string: {completedString}")
