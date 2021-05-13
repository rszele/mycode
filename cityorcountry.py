#!/usr/bin/env python3


city= ["smog", "crowds", "fantastic restaurants", "public transportation", "sightseeing"]

country= ["fresh air", "space", "bigger homes", "restaurants", "wild life", "stinky smells", "less hip dressers"]

print("How do you like your air?")
choice= input("""A. smog
                 B. clear  """)
print("How do you like your entertainment?")
choice2= input("""A. Variety
                 B. Basic  """)

print("How do you like your clothing?")
choice3= input("""A. Hip
                 B. Functional """)

cityscore= 0
countryscore= 0

if choice == "A":
    cityscore += 1
elif choice == "B":
    countryscore += 1
    
if choice2 == "A":
    cityscore += 1
elif choice2 == "B":
    countryscore += 1

if choice3 == "A":
    cityscore += 1
elif choice3 == "B":
    countryscore += 1

if cityscore > countryscore:
    print("you are a city person")

elif cityscore < countryscore:
    print("you are a country person")

else: 
    print("you are a suburbs person")

    
