

# string is what we're checking to see if it's a pangram
string= input("test a pangram")

# we'll use alphabet to check it against
alphabet= "abcdefghijklmnopqrstuvwxyz"

# we'll return either a true or false if the string is an pangram
flag= True

# newstring will be the new string we make
newstring= ""

for everychar in string.lower():
    if everychar in alphabet:
        newstring += everychar

for letter in alphabet:
    if letter in newstring:
        pass
    else:
        print(f"{letter} is not in {string}!")
