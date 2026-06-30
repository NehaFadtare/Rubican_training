# write a python prg to create a feature in a module and use it in your codes 
# function as a decorator and provide some feature to your function

from auth_module import login_required

@login_required
def login1(username):
    print(f"Welcome {username}")
    print("Accessing Dashboard...")

username = input("Enter Username: ")
password = input("Enter Password: ")

login1(username, password)