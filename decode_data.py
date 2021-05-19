
# This code will encode the data by giving shifting to the character, so that only the person who knows to decode
# only could it

shift = int(input("Enter the shift: "))                 # Enter the shift by which you want to shift the data

data = input("Enter the data: ")                        # Enter the data

for i in data:
    if i == ' ':
        print(' ', end='')                              # If space, leave space
    else:
        if i.isupper():                                 # If data is upper
            if (ord(i)-shift) > 64:                     # and ascii-shift is greater than 64
                print(chr(ord(i)-shift), end='')        # print ascii-shift
            elif (ord(i)-shift) <= 64:                  # else
                print(chr(ord(i)-shift+26), end='')     # print cyclically rotate character
        elif i.islower():
            if (ord(i)-shift) > 96:
                print(chr(ord(i)-shift), end='')
            elif (ord(i)-shift) <= 96:
                print(chr(ord(i)-shift+26), end='')

'''
----   --------   ----  ------ ------
---- - -------- - ----  ----- - -----
---- -- ------ -- ----  ---- --- ----
---- --- ---- --- ----  ---       ---
---- ---- -- ---- ----  -- ------  --
---- -----  ----- ----  - --------- -
'''