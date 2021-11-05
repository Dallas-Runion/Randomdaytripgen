import random
vaca_sites = ["Korea", "Romania", "Germany", "Rome", "Black Rock (burning man)", "Tahiti", "Racine", " Chicago"]
restaurants = ["Seafood Bob's", "Xtreme steakhouse" , "Fast burger", "KBBQ"]
transpo = ["Flight by plane", "Taxi", "Flight by helicopter", "Travel by sea"]
entertainment = ["Theatre", "Car shows", "Art exhibits", "Nightlife"]

def convert_adventure(some_list):
    list_index = random.randint(0, len(some_list)-1  )
    return some_list[list_index]

chosen_rest = convert_adventure(restaurants)
chosen_site = convert_adventure(vaca_sites)
chosen_tranpo = convert_adventure(transpo)
chosen_entertainment = convert_adventure(entertainment)
travel_trip = [convert_adventure(restaurants), convert_adventure(vaca_sites),convert_adventure(transpo),convert_adventure(entertainment)]
print(travel_trip)

