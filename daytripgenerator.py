import random
from tkinter.messagebox import RETRY, YES
from unittest import result 

destinations_list = ["Kingston", "Honolulu", "Cancun", "California"]
restaurants_list  = ["Mcdonalds", "Dominos", "Applebees", "Burger King" ]
transportation_list = ["bicycle", "car", "train", "bus"]
entertainment_list = ["touring the city", "going to the beach", "scuba diving", "sky diving"]

print('Welcome to the day trip generator!')


def select_item (someArray, type):
    # setup a variable for while to track when user is satisifed
    notSatisfied = True

    while (notSatisfied):
        random_item_from_list = random.choice(someArray)

        print( f"We have selected {random_item_from_list} as your {type}, does this sound good? ")
        users_answer = input("Enter yes or no: ")
        if users_answer == "yes":
            print("Great choice lets move on")
            notSatisfied = False
            return random_item_from_list
        else:
            print("How about this destination?")


chosen_dest = select_item(destinations_list, "destination")
chosen_rest = select_item(restaurants_list, "restaurant")
chosen_transportation = select_item(transportation_list, "transportation")
chosen_entertainment = select_item(entertainment_list, "entertainment")

print("You will arrive in " + chosen_dest + " " + "where you will eat at" + " " + chosen_rest + " " + "and you will take a" + chosen_transportation  + "  and you will be " + chosen_entertainment)

print("Do you confirm your trip is complete?")
users_response = input("Enter yes: ")
if users_response == "yes":
    print("Have a wonderful vacation!")










