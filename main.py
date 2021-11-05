import random
##1)store destinations , restaurants, mode of transpo, and entertainment in sep list
    ##A)four sep list hold each information type

##2) randomize each list to return one vaule of each list. 
    #A) Find/import randomizer 
    #B)create a function with para = #of list
    #C)display each returned value 

##3)create a switch that allows the function to repeat until desired results come back (try using a bool to act the switch)

##4)if trip is completed(true) display(print) trip in consol

#********FUNCTION SHOULD HAVE ONE USE********

vaca_sites = ["Korea", "Romania", "Germany", "Rome", "Black Rock (burning man)", "Tahiti", "Racine", " Chicago"]
restaurants = ["Seafood Bob's", "Xtreme steakhouse" , "Fast burger", "KBBQ"]
transpo = ["Flight by plane", "Taxi", "Flight by helicopter", "Travel by sea"]
entertainment = ["Theatre", "Car shows", "Art exhibits", "Nightlife"]
#step 1 complete 

#2)A) radomizer *research online 
#2)B) function part remember build step by step 
def convert_adventure(some_list):
    list_index = random.randint(0, len(some_list)-1  )
    return some_list[list_index]

chosen_rest = convert_adventure(restaurants)
chosen_site = convert_adventure(vaca_sites)
chosen_tranpo = convert_adventure(transpo)
chosen_entertainment = convert_adventure(entertainment)
travel_trip = [chosen_rest,chosen_site,chosen_tranpo,chosen_entertainment]
print(travel_trip)

def does_this_work(chosen_trip, new_restaurants, new_vaca_sites, new_transpo, new_entertainment):
    print(chosen_trip)
    print("please enter 1 if youd like to change restaurants. 2 for location.3 for transportation. 4 for entertainment ")
    list_index = int (input ())
    if list_index == 1:
        return new_restaurants
    elif list_index == 2:
        return new_vaca_sites
    elif list_index == 3:
        return new_transpo
    elif list_index ==4:
        return new_entertainment


change_this = does_this_work (travel_trip,restaurants,vaca_sites,transpo,entertainment)
print(change_this)
convert_adventure(change_this)
print(travel_trip)








def confirm(chosen_type):
    print (chosen_type, "Please confirm choice by typing confirmed here:")
    affirmed = input()
    if affirmed == "confirmed":
        return("trip is confirmed")


confirm(travel_trip)
print (f"{travel_trip} is confirmed")


