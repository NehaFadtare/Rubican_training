from food_delivery_App import check_delivery_area

def food():
    foods = {
            "pizza": 299,
            "burger": 149,
            "pasta": 249
    }
    print(foods,end="\n")
    choice = input("choose food item:")
    print("bill:")
    if choice in foods:
        print(foods[choice])
    else:
        print("item not available!!")

food()

        

@check_delivery_area
def delivery(location):
    return 0
    
name = input("Enter your name: ")
location = input("Enter your location: ")

delivery(location)