print("Select your pizza toppings by entering them below, enter \"quit\" when you no longer want any more toppings.")

while True:
 toppings = input("Enter the toppings you'd like to add. ")
 if toppings == 'quit':
    print("It seems you no longer want other toppings.")
    break
 else:
     print("I will add " + toppings + " to your pizza.")