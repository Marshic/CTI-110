import random
import time
import threading

# Robot customization
def create_robot():
    print("Welcome to the Robot Customization Lab!")
    name = input("Enter your robot's name: ")
    specialization = {
        "1": {"type": "Fighter", "health": 100, "stability": 50, "attack_power": 20},
        "2": {"type": "Defender", "health": 150, "stability": 40, "attack_power": 15},
        "3": {"type": "Technician", "health": 80, "stability": 70, "attack_power": 10},
    }
    choice = input("Choose specialization (1: Fighter, 2: Defender, 3: Technician): ")
    return {"name": name, **specialization.get(choice, specialization["1"]), "scrap_collected": 0}

# Enemy and boss configurations
area_data = [
    {"name": "Scrap Field", "enemies": [{"name": "Weak Drone", "health": 40, "attack_power": 8}], "boss": {"name": "Scrap Golem", "health": 70, "attack_power": 12}},
    {"name": "Power Plant", "enemies": [{"name": "Zapper Bot", "health": 50, "attack_power": 10}], "boss": {"name": "Shock Sentinel", "health": 90, "attack_power": 15}},
    {"name": "Assembly Line", "enemies": [{"name": "Assembler Unit", "health": 60, "attack_power": 12}], "boss": {"name": "Foreman Droid", "health": 110, "attack_power": 18}},
    {"name": "Core Chamber", "enemies": [{"name": "Core Guardian", "health": 70, "attack_power": 14}], "boss": {"name": "You", "health": 150, "attack_power": 20}},
]

# Deplete stability over time
def deplete_stability():
    while player["health"] > 0 and player["stability"] > 0:
        time.sleep(1)
        player["stability"] -= 1
        if player["stability"] <= 0:
            print(f"\n{player['name']} has lost all stability! GAME OVER.")
            exit()

# Display player status
def display_status():
    print(f"\n--- {player['name']}'s Status ---")
    print(f"Type: {player['type']}\nHealth: {player['health']}\nStability: {player['stability']}\nScrap Collected: {player['scrap_collected']}")
    print("-----------------------------")

# Battle system
def battle(enemy, final_battle=False):
    print(f"\nFighting {enemy['name']}!")
    while enemy["health"] > 0 and player["health"] > 0:
        choice = input("\n1. Attack\n2. Repair\n3. Run\nChoose action: ")
        
        if choice == "1":
            damage = player["attack_power"] + random.randint(-3, 3)
            enemy["health"] -= damage
            print(f"You dealt {damage} damage! Enemy health: {max(enemy['health'], 0)}")
        elif choice == "2":
            player["stability"] += 20
            print(f"You repaired your stability. Stability: {player['stability']}")
        elif choice == "3":
            if not final_battle and random.random() > 0.5:
                print("\nYou escaped!")
                return False
            print("\nEscape failed!")
        
        # Enemy attacks
        enemy_attack = enemy["attack_power"] + random.randint(-2, 2)
        player["health"] -= enemy_attack
        print(f"The enemy attacks you for {enemy_attack}. Your health: {max(player['health'], 0)}")

        if player["health"] <= 0:
            print(f"\n{player['name']} was destroyed! GAME OVER.")
            exit()
    
    print(f"\nYou defeated {enemy['name']}!")
    player["stability"] += random.randint(15, 30)
    player["scrap_collected"] += 10
    return True

# Secret level
def secret_level():
    print("\n--- SECRET LEVEL ---")
    print("The Last Human stands before you.")
    battle({"name": "The Last Human", "health": 200, "attack_power": 25}, final_battle=True)

# Main game loop
def main():
    global player
    player = create_robot()
    
    # Start the stability depletion thread after player initialization
    deplete_thread = threading.Thread(target=deplete_stability, daemon=True)
    deplete_thread.start()
    
    for area in area_data:
        print(f"\n--- AREA: {area['name']} ---")
        display_status()
        
        for enemy in area["enemies"]:
            battle(enemy)
        
        print(f"\nThe boss is {area['boss']['name']}!")
        if area["boss"]["name"] == "You" and player["name"].lower() == "me":
            print("\nRiddle: What is something lost but never forgotten?")
            if input("Your answer: ").lower() == "i remember":
                secret_level()
        else:
            battle(area["boss"], final_battle=True)
        display_status()
    
    print("\nCongratulations! You completed the game!")

if __name__ == "__main__":
    deplete_thread = threading.Thread(target=deplete_stability, daemon=True)
    deplete_thread.start()
    main()
