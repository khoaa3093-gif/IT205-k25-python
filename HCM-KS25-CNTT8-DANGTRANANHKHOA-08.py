fleet_list = []

while True:
    choice = input(""""
=============================================================
=== Managing delivery vehicles and fuel consmption levels ===
=============================================================
=== 1. Show fleet list                                    ===
=== 2. Adding new vehicles to the fleet.                  ===
=== 3. Update your travel log.                            ===
=== 4. Remove the vehicle from the management team.       ===
=== 5. Search for transportation                          ===
=== 6. Feet performance statistics                        ===
=== 7. Automatic performance classification               ===
=== 8. Exit program
=============================================================
Enter your choice (1-8): """)
    
    if choice == "8" :
        print("You have exited the program ! Thank you.")
        break
    
    if choice == "1" :
        print("You have selected function 1")
    elif choice == "2" :
        print("You have selected function 2")

    elif choice == "3" :
        print("You have selected function 3")
    elif choice == "4" :
        print("You have selected function 4")
    elif choice == "5" :
        print("You have selected function 5")
    elif choice == "6" :
        print("You have selected function 6")
    elif choice == "7" :
        print("You have selected function 7")
    else :
        print("Invalid selection! Please select again.")
        continue 