# Applying Hierarchical Planning in going from one place to another.
options_for_travelling = [
    {
        "action": "Go by Bus"
    },
    {
        "action": "Go by Car"
    },
    {
        "action": "Go by Train"
    }
]

options_for_bus = [
    {
        "action": "Book tickets"
    },
    {
        "action": "Catch the Bus"
    }
]

options_for_car = [
    {
        "action": "Fill up the car at the gas Station"
    },
    {
        "action": "Get your car serviced"
    },
    {
        "action": "Grab snacks for the road"
    }
]

options_for_train = [
    {
        "action": "Book tickets"
    },
    {
        "action ": "Carry your luggage to the station"
    },
    {
        "action": "Board the train from the station"
    }
]
print("Travelling from source to destination\n Select any one from the following \n")
actions = ["Select Destination"]
print("1. Bus \n2. Car\n3. Train")

choice = int(input("Enter your choice : "))

# Choice for BUS
if choice == 1:
    actions.append(options_for_travelling[0]["action"])
    i = 0
    for options in options_for_bus:
        i = i + 1
        print(i, ".\t", options["action"], "\n")
    choice = int(input("Select either 1 or 2 : "))
    if choice == 1:
        actions.append(options_for_bus[0]["action"])
    if choice == 2:
        actions.append(options_for_bus[1]["action"])

# Choice for Car
elif choice == 2:
    actions.append(options_for_travelling[1]["action"])
    i = 0
    for options in options_for_car:
        i = i + 1
        print(i, ".\t", options["action"], "\n")
    choice = int(input("Select either 1 , 2  or 3 : "))
    if choice == 1:
        actions.append(options_for_car[0]["action"])
    elif choice == 2:
        actions.append(options_for_car[1]["action"])
    elif choice == 3:
        actions.append(options_for_car[2]["action"])

# Choice for train
elif choice == 3:
    actions.append(options_for_travelling[2]["action"])
    i = 0
    for options in options_for_train:
        i = i + 1
        print(i, ".\t", options["action"], "\n")
    choice = int(input("Select either 1 , 2  or 3 : "))
    if choice == 1:
        actions.append(options_for_train[0]["action"])
    elif choice == 2:
        actions.append(options_for_train[1]["action"])
    elif choice == 3:
        actions.append(options_for_train[2]["action"])
actions.append("Reach Destination")
print("Actions -> ", actions)
