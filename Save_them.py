#Donte' Brown
# 11/26/24
# P5HW
# Using function to create a game

def create_character():
    name = input("Enter robot name: ")
    health = int(input(f"Enter {name}'s health: "))
    inventory = []
    metal_affinity = (input(f"What are you made of? "))
    
    

    character = {
        "Name":name,
        "Health":health,
        "Materials": weapons,
        "Tools": tools,
        "Durability": strength,
        }
    return character



def main():
    print("You're broken. Build yourself anew...")
    print()
    # Call create character
    char1 = create_character()
    print()
    print(char1)
    

if __name__ == "__main__":
    main()
