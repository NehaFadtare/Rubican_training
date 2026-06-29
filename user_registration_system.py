def create_account(**kwargs):
    print(f"Details:")
    mandatory = ["name", "email"]

    for field in mandatory:
        if not kwargs.get(field):
            print(f"{field.capitalize()} is mandatory!")
            return

    for key, value in kwargs.items():
        print(f"{key} = {value}")
 
create_account( name="Rahul",
    age=21,
    city="Pune",
    email="rahul@gmail.com")

# def mandatory(msg):
#     value = input(msg)
#     while value.strip() == "":
#         print("This field is mandatory!")
#         value = input(msg)
#     return value

# name = mandatory("Enter Name: ")
# email = mandatory("Enter email: ")

# print(name, email)