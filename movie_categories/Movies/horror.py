def horror():
    Horror = [
        "The Conjuring",
        "Insidious",
        "IT",
        "The Nun",
        "A Quiet Place"]
    print("\n")
    age = int(input("enter your age: "))
    if age >=18:
        for i in Horror:
            print(i)
    else:
        print("you are not eligible")