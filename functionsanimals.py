# Value-returning functions
import random

def getHabitat(animal):
    if animal in ["turtle", "fish", "anemone", "urchin", "jellyfish", "blobfish"]:
        return "ocean"
    if animal in ["spider", "scorpion", "camel", "iguana", "fox", "snake", "emu"]:
        return "desert"
    if animal in ["lemur", "monkey", "tiger", "parrot", "panda", "panther", "lion"]:
        return "jungle"

def getFriends(habitat, numFriends):
    friends = []
    if habitat == "ocean":
        oceanList = [f"turtle", "fish", "anemone", "urchin", "jellyfish", "blobfish"]
        # Loop runs numFriends times
        for i in range(numFriends):
            # Adding a random oceanList item to the friends list
            friends.append(random.choice(oceanList))
        return friends

            
    if habitat == "desert":
        desertList = [f"spider", "scorpion", "camel", "iguana", "fox", "snake", "emu"]
        # Loop runs numFriends times
        for i in range(numFriends):
            # Adding a random desertList item to the friends list
            friends.append(random.choice(desertList))
        return friends
    
    if habitat == "jungle":
        jungleList = [f"lemur", "monkey", "tiger", "parrot", "panda", "panther", "lion"]
        # Loop runs numFriends times
        for i in range(numFriends):
            # Adding a random jungleList item to the friends list
            friends.append(random.choice(jungleList))
        return friends

# Define main
def main():
    run_again = "yes"
    while run_again.lower() == "yes":
        print("🦍🐅🐍🦘🐒")
        animal = input("Enter your favorite animal: ")
        habitat = getHabitat(animal.lower())
        print(f"{animal} lives in the {habitat}")
        print()
        numFriends = int(input(f"How many friends for the {animal}? "))
        # Call the getFriends function
        friendsList = getFriends(habitat, numFriends)
        print(f"The animal has the following friends: ")
        # Loop to display all items in friendsList
        for i in friendsList:
            print(i)
        print()
        
        run_again = input("Run again? Type 'yes' to run again or 'no' to stop: ")
    print("Program has ended...")
    
# Call the main
if __name__ == "__main__":
    main()
