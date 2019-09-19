# Written in Python 3.7.
#111010111100111100101111001001110101110010110111111011111110100010000011100001100001111001111100110111010110000111100111110100111001011011111101110110111111011011111001000100011001011110010
import sys

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
    # and adds it to a string
    for i in range(0, int(len(binaryString)/7)):
        charCheck = binaryToChar(binaryArr[i])
        #this will remove the char at the end 
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
    # and adds it to a string
    for i in range(0, int(len(binaryString)/8)): 
        charCheck = binaryToChar(binaryArr[i])
        #this will remove the char at the end
        if(charCheck != -1):
            charString += charCheck
        else:
            charString = charString[:-1]
    return charString

# Main Code
f = sys.stdin.read()

# 7 bit
if (len(f) % 7 == 0):
    print(bit7(f))
    
# 8 bit
if (len(f) % 8 == 0):
    print(bit8(f))
    
