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
    entertainment_winner = select_NYC_entertainment(NYC_entertainment_options)


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
    entertainment_winner = select_HV_entertainment(HV_entertainment_options)


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
    entertainment_winner = select_LI_entertainment(LI_entertainment_options)


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
    restaurant_winner = select_NYC_restaurants(NYC_restaurants)


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
    restaurant_winner = select_HV_restaurants(HV_restaurants)


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
    restaurant_winner = select_LI_restaurants(LI_restaurants)

def trip_plan_confirmation():
    destination_winner = select_destination(destinations)
    transportation_winner = select_transportation(transportation_options)
    if destination_winner == "New York City":
        entertainment_winner = select_NYC_entertainment(NYC_entertainment_options)
        restaurant_winner = select_NYC_restaurants(NYC_restaurants)
        print(f"We have now finished generating a day trip for you. \nDestination: {destination_winner} \nTransportation: {transportation_winner} \nEntertainment: {entertainment_winner} \nRestaurant: {restaurant_winner}")
            
    elif destination_winner == "Hudson Valley":
        entertainment_winner = select_HV_entertainment(HV_entertainment_options)
        restaurant_winner = select_HV_restaurants(HV_restaurants)
        print(f"We have now finished generating a day trip for you. \nDestination: {destination_winner} \nTransportation: {transportation_winner} \nEntertainment: {entertainment_winner} \nRestaurant: {restaurant_winner}")

    else:
        entertainment_winner = select_LI_entertainment(LI_entertainment_options)
        restaurant_winner = select_LI_restaurants(LI_restaurants)
        print(f"We have now finished generating a day trip for you. \nDestination: {destination_winner} \nTransportation: {transportation_winner} \nEntertainment: {entertainment_winner} \nRestaurant: {restaurant_winner}")

    user_input = input("Now let's confirm do you like the trip that has planned for you? Please enter y/n: ")
    if user_input == "n":
        print("Sorry you don't like the plan. Let's start over")
        trip_plan_confirmation()
    else:
        print(f"Awsome! Please enjoy a day exploring {destination_winner} by {transportation_winner}, where you will also {entertainment_winner} and dine at {restaurant_winner}.")

# trip_plan_confirmation()


def day_trip_generator():
    greeting()
    trip_plan_confirmation()

day_trip_generator()