def check_delivery_area(func):
    def wrapper(location): 
        locations = ["pune", "mumbai", "delhi"]

        if location in locations:
            print("order placed!!")
            return func(location)
        else:
            print("sorry!! delivery is not available!!")

    return wrapper

# order_pizza()
# order_burger()
# order_pasta()

# @check_delivery_area