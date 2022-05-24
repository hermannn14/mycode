#!/usr/bin/env python3

import pyfiglet

# Dictionary of countries

countries= {
            "Turkey": "Ankara",
            "Switzerland": "Bern",
            "Brazil": "Brasilia",
            "Morocco": "Rabat",
            "Canada": "Ottawa",
            "Ireland": "Dublin",
            "South-Africa": ["Pretoria", "Capetown", "Bloemfontein"]

           }
# Welcome message

print("Think you know the Capitals of these countries?")
print()
print("Let's Find out")
print()

# for loop over that dictionary to return each country:

for x in countries:
    print("What is the Capital of "+ x)
    correct = 0
    wrong = 0
    #input("Guess the capital>")

    while True: 

        # so before we give credit for a correct answer, they should answer first:
        response = input("Your guess is--> ")
        print()
        if response.lower() in  countries[x].lower(): # here we check the answer, and if it's correct:
             # we have to fetch the correct answer from the dictionary
             # as of line 25, x is equal to a key from our dictionary, the name of a country
             # so we can slice the dictionary "countries" using x as the key
             # correct = correct + 1 # give a point
             print( "You guessed it correctly, Congrats") # give an encouraging message :)
             print()
             correct += 1
             break
        elif response == "":
            print("Type in something foo")
            print()
            continue
       # elif wrong == 1:
        #    print("You got 1 more try my friend")
         #   continue
        elif wrong >= 2:
            print("Yikes..3 strikes. Let's get some geography lessons soon")
            print()
            break
        else:
            wrong += 1
            print("Wrong answer, Try again")
        

# take the input and checking if it matches the value of that key
# if it does match the key, then increase a counter by 1
