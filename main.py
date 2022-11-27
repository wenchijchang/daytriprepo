destinations = ["New York City", "Hudson Valley", "Long Island"]
transportation_options = ["train", "car", "ferry"]
NYC_restaurants = ["Chipotle", "Nougatine", "Keens"]
HV_restaurants = ["Cucina", "Hudson Brewing Company", "Le Bouchon"]
LI_restaurants = ["Peter Luger", "Sandbar", "Mosaic"]
NYC_entertainment_options = ["watch a Broadway show", "visit Moma", "check out Holiday markets"]
HV_entertainment_options = ["visit Angry Orchard", "hike Mohonk Mountain", "visit Fishkill Farms"]
LI_entertainment_options = ["visit Vanderbailt Museum", "visit Aquarium", "visit Caumsett State Park"]

import random

def greeting():
    print("""
    Hello and Welcome! This daily trip generator is here to help you put together a fun day exploring New York!
    """)

# greeting()

def select_destination(destination_list):
    confirm_bool = True
    while confirm_bool:
        random_dest = random.choice(destination_list)
        user_input = input(f"Would you like to spend a day in {random_dest}? Please enter y/n: ")
        if user_input == "n":
            print("Sorry you don't like this destination. Let's try again" )
            destination_list.remove(random_dest)
        else:
            confirm_bool = False
            print("Awsome! Glad that is decided. Let's move on!")
    return random_dest
    destination_winner = select_destination(destinations)



def select_transportation(transportation_list):
    confirm_bool = True
    while confirm_bool:
        random_transp = random.choice(transportation_list)
        user_input = input(f"Would you like to take the {random_transp} to your destination? Please enter y/n: ")
        if user_input == "n":
            print("Sorry you don't like this form of transportation. Let's try again")
            transportation_list.remove(random_transp)
        else:
            confirm_bool = False
            print("Awsome! Glad that is decided. Let's move on!")
    return random_transp
    transportation_winner = select_transportation(transportation_options)

def select_NYC_entertainment(NYC_enterta_list):
    confirm_bool = True
    while confirm_bool:
        random_entertainment = random.choice(NYC_enterta_list)
        user_input = input(f"Would you like to {random_entertainment}? Please enter y/n: ")
        if user_input == "n":
            print("Sorry you don't like this idea. Let's try again")
            NYC_enterta_list.remove(random_entertainment)
        else:
            confirm_bool = False
            print("Awsome! Glad that is decided. Let's move on!")
    return random_entertainment
    NYC_entertainment_winner = select_NYC_entertainment(NYC_entertainment_options)


def select_HV_entertainment(HV_enterta_list):
    confirm_bool = True
    while confirm_bool:
        random_entertainment = random.choice(HV_enterta_list)
        user_input = input(f"Would you like to {random_entertainment}? Please enter y/n: ")
        if user_input == "n":
            print("Sorry you don't like this idea. Let's try again")
            HV_enterta_list.remove(random_entertainment)
        else:
            confirm_bool = False
            print("Awsome! Glad that is decided. Let's move on!")
    return random_entertainment
    HV_entertainment_winner = select_HV_entertainment(HV_entertainment_options)


def select_LI_entertainment(LI_enterta_list):
    confirm_bool = True
    while confirm_bool:
        random_entertainment = random.choice(LI_enterta_list)
        user_input = input(f"Would you like to {random_entertainment}? Please enter y/n: ")
        if user_input == "n":
            print("Sorry you don't like this idea. Let's try again")
            LI_enterta_list.remove(random_entertainment)
        else:
            confirm_bool = False
            print("Awsome! Glad that is decided. Let's move on!")
    return random_entertainment
    LI_entertainment_winner = select_LI_entertainment(LI_entertainment_options)


def select_NYC_restaurants(NYC_rest_list):
    confirm_bool = True
    while confirm_bool:
        random_restaurant = random.choice(NYC_rest_list)
        user_input = input(f"Would you like to have dinner at {random_restaurant}? Please enter y/n: ")
        if user_input == "n":
            print("Sorry you don't like this restaurant. Let's try again")
            NYC_rest_list.remove(random_restaurant)
        else:
            confirm_bool = False
            print("Awsome! Glad that is decided. Let's move on!")
    return random_restaurant
    NYC_restaurant_winner = select_NYC_restaurants(NYC_restaurants)


def select_HV_restaurants(HV_rest_list):
    confirm_bool = True
    while confirm_bool:
        random_restaurant = random.choice(HV_rest_list)
        user_input = input(f"Would you like to have dinner at {random_restaurant}? Please enter y/n: ")
        if user_input == "n":
            print("Sorry you don't like this restaurant. Let's try again")
            HV_rest_list.remove(random_restaurant)
        else:
            confirm_bool = False
            print("Awsome! Glad that is decided. Let's move on!")
    return random_restaurant
    HV_restaurant_winner = select_HV_restaurants(HV_restaurants)


def select_LI_restaurants(LI_rest_list):
    confirm_bool = True
    while confirm_bool:
        random_restaurant = random.choice(LI_rest_list)
        user_input = input(f"Would you like to have dinner at {random_restaurant}? Please enter y/n: ")
        if user_input == "n":
            print("Sorry you don't like this restaurant. Let's try again")
            LI_rest_list.remove(random_restaurant)
        else:
            confirm_bool = False
            print("Awsome! Glad that is decided. Let's move on!")
    return random_restaurant
    LI_restaurant_winner = select_LI_restaurants(LI_restaurants)

def confirmation():
    destination_winner = select_destination(destinations)
    transportation_winner = select_transportation(transportation_options)
    if destination_winner == "New York City":
        NYC_entertainment_winner = select_NYC_entertainment(NYC_entertainment_options)
        NYC_restaurant_winner = select_NYC_restaurants(NYC_restaurants)
        print(f"We have now finished generating a day trip for you. \nDestination: {destination_winner} \nTransportation: {transportation_winner} \nEntertainment: {NYC_entertainment_winner} \nRestaurant: {NYC_restaurant_winner}")
        
    elif destination_winner == "Hudson Valley":
        HV_entertainment_winner = select_HV_entertainment(HV_entertainment_options)
        HV_restaurant_winner = select_HV_restaurants(HV_restaurants)
        print(f"We have now finished generating a day trip for you. \nDestination: {destination_winner} \nTransportation: {transportation_winner} \nEntertainment: {HV_entertainment_winner} \nRestaurant: {HV_entertainment_winner}")
        
    else:
        LI_entertainment_winner = select_LI_entertainment(LI_entertainment_options)
        LI_restaurant_winner = select_LI_restaurants(LI_restaurants)
        print(f"We have now finished generating a day trip for you. \nDestination: {destination_winner} \nTransportation: {transportation_winner} \nEntertainment: {LI_entertainment_winner} \nRestaurant: {LI_entertainment_winner}")


confirmation()

# def day_trip_generator():