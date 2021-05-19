
# This code will encode the data by giving shifting to the character, so that only the person who knows to decode
# only could it
shift = int(input("Enter the shift: "))     # Enter the shift by which you want to shift the data

data = input("Enter the data: ")            # Enter the data

for i in data:
    if i == ' ':
        print(' ', end='')                              # If space, leave space
    else:
        if i.isupper():                                 # If the letter is uppercase
            if (ord(i)+shift) < 91:                     # and ascii+shift<91    ord(i) will give ascii value of i
                print(chr(ord(i)+shift), end='')        # print shifted character
            elif (ord(i)+shift) >= 91:                  # else
                print(chr(ord(i)+shift-26), end='')     # print ascii+shift-26
        elif i.islower():                               # If letter is lower
            if (ord(i)+shift) < 123:                    # and ascii+shift<123
                print(chr(ord(i)+shift), end='')        # print shifted character
            elif (ord(i)+shift) >= 123:                 # else
                print(chr(ord(i)+shift-26), end='')     # print ascii+shift-26

# chr(ord(i)+shift) will give character with that ascii
# This is purely mathematics based with some logic
