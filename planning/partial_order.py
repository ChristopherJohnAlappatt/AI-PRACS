print("Welcome to Partial order planning program !!!")
actions = []

left = [
    "Left-sock-on",
    "Left-shoe-on"
]
right = [
    "Right-sock-on",
    "Right-shoe-on"
]

print("Wear a shoe !!!")
print("Start from \n1. Left-sock-on\n2. Right-sock-on")
choice = int(input("Select any one from above -> "))

if choice == 1:
    actions.append(left[0])
    print("\n1. Left-shoe-on\n2. Right-sock-on")
    choice = int(input("Select any one from above -> "))
    if choice == 1:
        actions.append(left[1])
        print("Wear right sock followed by right shoe ")
        actions.append(right[0])
        actions.append(right[1])
    elif choice == 2:
        actions.append(right[0])
        print("\n1. Left-shoe-on\n2. Right-shoe-on")
        choice = int(input("Select any one from above -> "))
        if choice == 1:
            actions.append(left[1])
            print("\nWear right shoe ")
            actions.append(right[1])
        elif choice == 2:
            actions.append(right[1])
            print("\nWear right shoe ")
            actions.append(left[1])


elif choice == 2:
    actions.append(right[0])
    print("\n1. Right-shoe-on\n2. Left-sock-on")
    choice = int(input("Select any one from above -> "))
    if choice == 1:
        actions.append(right[1])
        print("Wear left sock followed by right shoe ")
        actions.append(left[0])
        actions.append(left[1])
    elif choice == 2:
        actions.append(left[0])
        print("\n1. Left-shoe-on\n2. Right-shoe-on")
        choice = int(input("Select any one from above -> "))
        if choice == 1:
            actions.append(left[1])
            print("\nWear right shoe ")
            actions.append(right[1])
        elif choice == 2:
            actions.append(right[1])
            print("\nWear left shoe ")
            actions.append(left[1])

actions.append("Both shoe on")
print("ACTIONS => ", actions)
