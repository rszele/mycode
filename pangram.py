

# string is what we're checking to see if it's a pangram
string= "python can be really challenging but really rewarding to learn"

# we'll use alphabet to check it against
alphabet= "abcdefghijklmnopqrstuvwxyz"

# we'll return either a true or false if the string is an pangram
flag= True

# newstring will be the new string we make
newstring= ""
clear


string= "the brown fox jumps over the lazy dog"
alphabet= "abcdefghijklmnopqrstuvwxyz"
flag= True
newstring= ""

for everychar in string.lower():
    if everychar in alphabet:
        newstring += everychar

for letter in alphabet:
    if letter in newstring:
        print(letter)
    else:
        print(f"(letter)is not in (string)!")
        
:qw


chmod u+x forloop1.py
mkdir /home/student/mycode/netfunct01
exit
%
i

