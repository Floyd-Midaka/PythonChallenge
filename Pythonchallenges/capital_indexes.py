"This function takes a single paremeter, which is a string,"
"this function returns a list of all the indes in the string that have capital letters"

def capital_indexes(word): 
    'create an empty list'
    char_list = []
    'loop into the string input and enumerate it'
    for index, char in enumerate(word):
        'use the string methond to check if the string input is a uppercase'
        if char.isupper():

            ' append the string input'
            char_list.append(index)
    return char_list
print(capital_indexes("HeLlo"))
