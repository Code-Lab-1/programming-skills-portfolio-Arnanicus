sandwich_orders = ['ham','pepperoni','beef','chicken']
finished_sandwiches = []

while sandwich_orders:
    sandwichesmade = sandwich_orders.pop()
    print("Your "+ sandwichesmade + " sandwich has been made.")
    finished_sandwiches.append(sandwichesmade)
    if len(sandwich_orders) == 0:
        print("The following sandwiches were made:", *finished_sandwiches)
        break