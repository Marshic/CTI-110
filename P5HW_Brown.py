import random
import time
import threading

# Lock for thread-safe updates to player stats
player_lock = threading.Lock()

# Robot customization
def create_robot():
    print("You're broken... Get up...")
    name = input("Enter your robot's name: ")
    specialization = {
        "1": {
            "type": "Fighter", 
            "stability": 56, 
            "attack_power": 20,
            "abilities": {"Power Strike": "Deal double damage but lose 5 stability."}
        },
        "2": {
            "type": "Defender", 
            "stability": 56, 
            "attack_power": 15,
            "abilities": {"Shield Up": "Reduce incoming damage by half for 2 turns."}
        },
        "3": {
            "type": "Technician", 
            "stability": 56, 
            "attack_power": 10,
            "abilities": {"Overclock": "Increase attack power by 5 for 3 turns."}
        },
    }
    choice = input("Choose specialization (1: Fighter, 2: Defender, 3: Technician): ")
    return {"name": name, **specialization.get(choice, specialization["1"]), "scrap_collected": 0}

# Enemy and boss configurations
area_data = [
    {"name": "Scrap Field", "enemies": [{"name": "Weak Drone", "stability": 15, "attack_power": 8}], "boss": {"name": "Scrap Golem", "stability": 30, "attack_power": 12}},
    {"name": "Power Plant", "enemies": [{"name": "Zapper Bot", "stability": 20, "attack_power": 10}], "boss": {"name": "Shock Sentinel", "stability": 40, "attack_power": 15}},
    {"name": "Assembly Line", "enemies": [{"name": "Assembler Unit", "stability": 25, "attack_power": 12}], "boss": {"name": "Foreman Droid", "stability": 50, "attack_power": 18}},
    {"name": "Core Chamber", "enemies": [{"name": "Core Guardian", "stability": 30, "attack_power": 14}], "boss": {"name": "Final Guardian", "stability": 70, "attack_power": 20}},
]

# Scale enemies for difficulty
def scale_enemies(enemies, scale_factor):
    for enemy in enemies:
        enemy["stability"] += scale_factor * 5
        enemy["attack_power"] += scale_factor * 2
    return enemies

# Exploration choices
def explore_area():
    event = random.choice([
        "You find a repair station. Stability restored by 20.",
        "You discover an abandoned workshop. Attack power increased by 3.",
        "You fall into a trap! Stability reduced by 10.",
        "You collect some valuable scrap! Scrap increased by 15."
    ])

    print(f"\nExploration Event: {event}")
    with player_lock:
        if "repair station" in event:
            player["stability"] += 20
        elif "workshop" in event:
            player["attack_power"] += 3
        elif "trap" in event:
            player["stability"] -= 10
        elif "scrap" in event:
            player["scrap_collected"] += 15

# Stability depletion over time
def deplete_stability():
    while True:
        with player_lock:
            if player["stability"] > 0:
                player["stability"] -= 1
                print(f"\n{player['name']}'s stability is now {player['stability']}.")
            if player["stability"] <= 0:
                print(f"\n{player['name']} has lost all stability! GAME OVER.")
                exit()
        time.sleep(1)

# Battle system
def battle(enemy, final_battle=False):
    print(f"\nFighting {enemy['name']}!")
    turns_of_buff = 0
    buff_amount = 0

    while enemy["stability"] > 0 and player["stability"] > 0:
        # Handle active buffs
        if turns_of_buff > 0:
            turns_of_buff -= 1
        elif turns_of_buff == 0 and buff_amount != 0:
            player["attack_power"] -= buff_amount
            buff_amount = 0

        # Player's action
        choice = input("\n1. Attack\n2. Repair\n3. Use Ability\n4. Run\nChoose action: ")
        if choice == "1":
            damage = max(1, player["attack_power"] + random.randint(-3, 3))
            enemy["stability"] -= damage
            print(f"You dealt {damage} damage! Enemy stability: {max(enemy['stability'], 0)}")
        elif choice == "2":
            with player_lock:
                player["stability"] += 10
                print(f"You repaired your stability. Stability: {player['stability']}")
        elif choice == "3":
            ability = list(player["abilities"].keys())[0]
            print(f"You used {ability}!")
            if ability == "Power Strike":
                damage = player["attack_power"] * 2
                enemy["stability"] -= damage
                player["stability"] -= 5
                print(f"Dealt {damage} damage but lost 5 stability!")
            elif ability == "Shield Up":
                turns_of_buff = 2  # Halves damage for 2 turns
                print(f"Incoming damage halved for 2 turns!")
            elif ability == "Overclock":
                buff_amount = 5
                turns_of_buff = 3
                print(f"Attack power increased by 5 for 3 turns!")
        elif choice == "4":
            if not final_battle and random.random() > 0.5:
                print("\nYou escaped!")
                return False
            print("\nEscape failed!")

        # Enemy attacks
        enemy_attack = max(1, enemy["attack_power"] + random.randint(-2, 2))
        if turns_of_buff > 0:
            enemy_attack //= 2
        player["stability"] -= enemy_attack
        print(f"The enemy attacks you for {enemy_attack}. Your stability: {max(player['stability'], 0)}")

        if player["stability"] <= 0:
            print(f"\n{player['name']} has lost all stability! GAME OVER.")
            exit()

    print(f"\nYou defeated {enemy['name']}!")
    with player_lock:
        player["scrap_collected"] += 10
    return True

# Main game loop
def main():
    global player
    player = create_robot()

    # Start stability depletion thread
    deplete_thread = threading.Thread(target=deplete_stability, daemon=True)
    deplete_thread.start()

    for i, area in enumerate(area_data):
        print(f"\n--- AREA: {area['name']} ---")
        scaled_enemies = scale_enemies(area["enemies"], i + 1)
        for enemy in scaled_enemies:
            battle(enemy)
            explore_area()

    print("\nCongratulations! You got revenge!")

# Start the game
if __name__ == "__main__":
    main()
