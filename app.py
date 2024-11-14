favourite_foods = [] # Initialize empty List for favourite foods
while True:
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove foods")
    print("3. View favourite all foods")

    choice = input("Choose an option: ") # From taken user input

    if choice == "0":
        print("Thanks for using Favourite foods Manager")
        break

    elif choice == "1":
        food = input("Enter your Favourite Food Name: ")
        favourite_foods.append(food) # Add input to the Food List
        print(f"{food} added Successfully") # {food} shows user input

    elif choice == "2":
        food = input("Enter a food name which you want to remove: ")
        if food in favourite_foods: # Using Another if esle
            favourite_foods.remove(food) # Remove input from the Food List
            print(f"{food} removed Successfully") # {food} shows user input
        else:
            print(f"{food} does not exist in List")


    elif choice == "3":
        if favourite_foods:
            print("Your favourite foods:")
            for index, food in enumerate(favourite_foods, start=1):
                print(f"{index}.{food}") # For printing something dynamic, use {}
        else:
            print("Food List is empty or didn't added yet!")
        
    else:
        print("Invalid Choice!")