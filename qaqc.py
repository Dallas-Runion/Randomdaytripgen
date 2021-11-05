import random
vaca_sites = ["Korea", "Romania", "Germany", "Rome", "Black Rock (burning man)", "Tahiti", "Racine", " Chicago"]
restaurants = ["Seafood Bob's", "Xtreme steakhouse" , "Fast burger", "KBBQ"]
transpo = ["Flight by plane", "Taxi", "Flight by helicopter", "Travel by sea"]
entertainment = ["Theatre", "Car shows", "Art exhibits", "Nightlife"]
vaca_sites2 = ["Romania", "Rome", "Japan"]
def convert_adventure(some_list):
    list_index = random.randint(0, len(some_list)-1  )
    return some_list[list_index]

chosen_rest = convert_adventure(restaurants)
chosen_site = convert_adventure(vaca_sites)
chosen_tranpo = convert_adventure(transpo)
chosen_entertainment = convert_adventure(entertainment)
travel_trip = [chosen_rest,chosen_site,chosen_tranpo,chosen_entertainment]
print(travel_trip)


def does_this_work(chosen_trip):
    print(chosen_trip)
    print("please enter 1 if youd like to change restaurants. 2 for location.3 for transportation. 4 for entertainment ")
    list_index = int (input ())
    if list_index == 1:
        return chosen_trip[0]
    elif list_index == 2:
        return chosen_trip[1]
    elif list_index == 3:
        return chosen_trip[3]
    elif list_index ==4:
        return chosen_trip[4]
    else: 
        return chosen_trip

change_this = does_this_work (travel_trip)
print(change_this)

def omit_item(remove_this_item,list1):
    # resouce = len(remove_this_item)-1
    for elements in list1:
##use a for loop to seqence thru the list!
        for elements in remove_this_item:
            remove_this_item.remove(elements) 
        return remove_this_item 



jax = omit_item(travel_trip, change_this)
print(jax)

print(jax[2])
# def fill_in_new()
            







# def confirm(chosen_type):
#     print (chosen_type, "Please confirm choice by typing confirmed here:")
#     affirmed = input()
#     if affirmed == "confirmed":
#         return("trip is confirmed")

# confirm(travel_trip)
# print (f"{travel_trip} is confirmed")


            
            
            
            



            


