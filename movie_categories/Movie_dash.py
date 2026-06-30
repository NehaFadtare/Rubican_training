from Movies import action, comedy, horror

def movies_dash():
    print("categories of movies")
    print("1. Action movies")
    print("2. Comedy movies")
    print("3. Horror movies")
    c1 = int(input("choose movie category"))
    if c1 == 1:
        return action.action()
    elif c1 ==2:
        return comedy.comedy()
    else:
        return horror.horror()
print(movies_dash())