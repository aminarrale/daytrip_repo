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






random_item_from_list = random.choice(destinations_list)
print( f"We have selected {random_item_from_list} as your destination, does this sound good? ")
users_answer = input("Enter yes or no: ")
if users_answer == "yes":
    print("Great choice lets move on")
else:
    print("How about this destination?")
   


random_item_from_list = random.choice(restaurants_list)
print( f"We have selected {random_item_from_list} as your restaurant, does this sound good? ")
users_answer = input("Enter yes or no: ")
if users_answer == "yes":
    print("Great choice lets move on")
else:
    print("How about this restaurant?")

random_item_from_list = random.choice(transportation_list)
print( f"We have selected {random_item_from_list} as your form of transportation, does this sound good? ")
users_answer = input("Enter yes or no: ")
if users_answer == "yes":
    print("Great choice lets move on")
else:
    print("How about this form of transportation?")

random_item_from_list = random.choice(entertainment_list)
print( f"We have selected {random_item_from_list} as your entertainment, does this sound good? ")
users_answer = input("Enter yes or no: ")
if users_answer == "yes":
    print("Great choice lets move on")
else:
    print("How about this entertainment?")

print("Do you confirm this trip?")
users_answer = input("")
if users_answer == "yes":
    print("Have a wonderful vacation!") 








