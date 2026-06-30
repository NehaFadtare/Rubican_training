def login_required(func):
    def wrapper(username,password):
        registered ={
            "neha":"123",
            "abc":"456",
            "pqr":"789"
        }
        
        if username in registered and registered[username]==password:
            print("login successful!!")
            return func(username)
        else:
            print("access denied!!!")

    return wrapper
