# Review of functions
import random

def death_calculator(name, age):
    average_lifespan = 80
    years_left = average_lifespan - age
    print(f"Using an average lifespan of {average_lifespan}, {name} has {years_left} years left to live!")
    
    possible_deaths = ['choked on grapefruit', 'coughed on by space hobo', 'heart replaced by baked potato', 'played league of legends', 'attacked by rabid naked homelessman', 'sneezed really hard', 'smelled Nexas breath', 'car door', 'death by ligma']
    
    cause = random.choice(possible_deaths)
    return cause, random.randint(1596, 9999), random.randint(1596, 9999)

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    cause, birthyear, deathyear = death_calculator(name, age)
    
    print("💀💀💀💀💀💀💀💀💀")
    print(f"Cause of demise: {cause}")

    print("      ________       ")
    print("     /        \\      ")
    print("    /          \\     ")
    print("   /            \\    ")
    print(f"  |   RIP {name}  |   ")
    print(f"  | {birthyear} - {deathyear}  |   ")
    print("  |   Forever    |   ")
    print("  | Loved (probably)|   ")
    print("   \\            /    ")
    print("    \\__________/     ")
    print("       |  |          ")
    print("       |  |          ")

# Call the main
if __name__ == "__main__":
    main()
