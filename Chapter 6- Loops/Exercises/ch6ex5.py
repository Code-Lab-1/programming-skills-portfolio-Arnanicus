print('UNFORTUNATELY WE\'RE OUT OF PASTRAMI!')
sandwich_orders = ['ham','pastrami','pepperoni','pastrami','beef','chicken','pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwichesmade = sandwich_orders.pop()
    print("Your "+ sandwichesmade + " sandwich has been made.")
    finished_sandwiches.append(sandwichesmade)
    if len(sandwich_orders) == 0:
        print("The following sandwiches were made:", *finished_sandwiches)
        break