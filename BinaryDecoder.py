# Written in Python 3.7.

import sys

# converts a binary string into a character
def binaryToChar(b):
    asc = int(b,2)
    char = chr(asc)
    return char

def bit7(binaryString):
    # splits the binary string up into groups of 7
    binaryArr = [binaryString[i:i+7] for i in range(0, len(binaryString), 7)]
    charString = ""
    
    # converts each binary string to a character
    # and adds it to a string
    for i in range(0, int(len(binaryString)/7)):
        charString += binaryToChar(binaryArr[i])
    return charString
    
def bit8(binaryString):
    # splits the binaryString string up into groups of 8
    binaryArr = [binaryString[i:i+8] for i in range(0, len(binaryString), 8)]
    charString = ""
    
    # converts each binary string to a character
    # and adds it to a string
    for i in range(0, int(len(binaryString)/8)):
        charString += binaryToChar(binaryArr[i])
    return charString

# Main Code
f = sys.stdin.read()

# 7 bit
if (len(f) % 7 == 0):
    print(bit7(f))
    
# 8 bit
if (len(f) % 8 == 0):
    print(bit8(f))
    
# Need to handle backspace in a separate case
    # Can strip off last character in list
    # output = output[:-1]