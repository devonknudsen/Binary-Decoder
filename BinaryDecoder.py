# Persians: Sydney Anderson, Tram Doan, Devon Knudsen, Zackary Phillips, Promyse Ward, James Wilson
# GitHub Repo: https://github.com/devonknudsen/Binary-Decoder
# Written in Python 3.7.

# converts a binary string into a character
def binaryToChar(b):
    asc = int(b,2)

    #check for backspace
    if(asc == 8):
        return -1
    char = chr(asc)

    return char

def bit7(binaryString):
    # splits the binary string up into groups of 7
    binaryArr = [binaryString[i:i+7] for i in range(0, len(binaryString), 7)]

    charString = ""
    
    # converts each binary string to a character
    # and appends it to a string
    for i in range(0, int(len(binaryString)/7)):
        charCheck = binaryToChar(binaryArr[i])

        if(charCheck != -1):
            charString += charCheck
        else:
            charString = charString[:-1]

    return charString
    
def bit8(binaryString):
    # splits the binaryString string up into groups of 8
    binaryArr = [binaryString[i:i+8] for i in range(0, len(binaryString), 8)]

    charString = ""
    
    # converts each binary string to a character
    # and appends it to a string
    for i in range(0, int(len(binaryString)/8)): 
        charCheck = binaryToChar(binaryArr[i])

        if(charCheck != -1):
            charString += charCheck
        else:
            charString = charString[:-1]

    return charString

# MAIN
f = input()

# 7 bit Binary
if (len(f) % 7 == 0):
    print(bit7(f))
    
# 8 bit Binary
if (len(f) % 8 == 0):
    print(bit8(f))
    
