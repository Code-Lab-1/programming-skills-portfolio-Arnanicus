while True:
    age = int(input("Welcome to the movie theater. Ticket price will vary depending on your age. How old are you? "))
    if age < 3:
        print("Your ticket will be free of charge.")
    elif age < 12:
        print("Your ticket will be 10$.")
    else:
        print("Your ticket will be 15$.")