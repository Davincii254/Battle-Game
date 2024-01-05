# Declare variables in global scope
wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

# Choose a Character
while True:
    print("Choose your character:")
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")

    character_choice = input("Enter your Characters Number: ")

    if character_choice in ["1", "2", "3"]:
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")


# Check character choosen and assign respective values 
while True:
    character = ""
    my_hp = 0
    my_damage = 0

    if character_choice == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character_choice == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character_choice == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")

    print(f"You chose {character} with HP: {my_hp} and Damage: {my_damage}")


# Choosen character fights the dragon
while True:
    # Player attacks the dragon
    dragon_hp -= my_damage
    print(f"The {character} damaged the Dragon!")
    print(f"Dragon's HP: {dragon_hp}")

    # Check if the dragon has lost the battle
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break

    # Dragon attacks the player
    my_hp -= dragon_damage
    print(f"The Dragon strikes back {character}!")
    print(f"{character}'s HP: {my_hp}")

    # Check if the player has lost the battle
    if my_hp <= 0:
        print(f"Your {character} has lost the battle!")
        break
