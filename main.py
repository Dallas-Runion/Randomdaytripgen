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







def does_this_work(chosen_trip):
    print(chosen_trip)
    print("please enter 1 if youd like to change restaurants. 2 for location.3 for transportation. 4 for entertainment ")
    list_index = int (input ())
    if list_index == 1:
        return chosen_trip[0]
    elif list_index == 2:
        return chosen_trip[1]
    elif list_index == 3:
        return chosen_trip[2]
    elif list_index ==4:
        return chosen_trip[3]
    else: 
        return chosen_trip

change_this = does_this_work (travel_trip)


def omit_item(list1, remove_this_item):
    # resouce = len(remove_this_item)-1
    for objects in list1:
        if objects == remove_this_item:
            list1.remove(objects) 
            return objects

        



jax = omit_item(travel_trip, change_this)





def remove_activity_type(list_rest, list_vacasite, list_trans, list_entertain, remove):
    for index  in  list_rest:
        if index == index in remove :
            list_rest.remove(index)
            return list_rest
    for index in list_vacasite:
        if index == index in remove:
            list_vacasite.remove(index)
            return list_vacasite
    for index in list_trans:
        if index == index in remove:
            list_trans.remove(index)
            return list_trans
    for index in list_entertain:
        if index == index in remove:
            list_entertain.remove(index)
            return list_entertain

yeet = remove_activity_type(restaurants, vaca_sites, transpo, entertainment, jax)


travel_trip_change = convert_adventure(yeet)
travel_trip.append(travel_trip_change)








def confirm(chosen_type):
    print (chosen_type, "Please confirm choice by typing confirmed here:")
    affirmed = input()
    if affirmed == "confirmed":
        return("trip is confirmed")
    else:
        return("trip is not confirmed")

yes_no = confirm(travel_trip)
print (travel_trip, yes_no)


            
            
            
            



            


