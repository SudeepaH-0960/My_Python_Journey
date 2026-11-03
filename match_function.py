# A simple function using match structure
name = input("Enter the cricketer name: ")
match name:
    case "Dhoni":
        print("CSK")
    case "Virat":
        print("RCB")
    case "Rohit":
        print("MI")
    case _:                          # same as else in if...else structure
        print("Unknown identity")  

# Using conditional operators in match structure
name = input("Enter the cricketer name: ")
match name:
    case "Dhoni" | "Jadeja" | "Brewis" | "Ruturaj" | "Urvil":
        print("CSK")
    case "Virat" | "Patidar" | "Padikal" | "Bhuvaneshwar" | "Krunal":
        print("RCB")
    case "Rohit" | "Tilak" | "Ishan" | "Naman" | "Boult":
        print("MI")
    case _:
        print("Identity not found")