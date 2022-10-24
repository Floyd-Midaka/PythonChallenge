mport math
import os
import random
import re
import sys
import string
# ****************** BODY *********************

def ReverseWords (originalString):
    words = originalString.split()
    newString = ""
    for word in words:
        wordlength = len(word) - 1
        spChars = ""
        for i in range(len(word)):
            index = wordlength - i
            if ((word[index].isalpha) or (word[index].isdigit)):
                newString = newString  + word[index];
            else:
                spChars = spChars + word[index]
        newString = newString + spChars + " ";
    
    return newString;
    pass

# ****************** FOOTER *********************

input = input()

out_ = ReverseWords(input)
print(out_)