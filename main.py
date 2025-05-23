# Import the random library to use for the dice later
import random

# Import the sys library for error handling
import sys

# Put all the functions into another file and import them
import function

# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))  # Max combat strength is 6
big_dice_options = list(range(1, 21))  # Max health points is 20

# Define the number of stars to award the player
num_stars = 0
input_valid = False

# Loop to get valid input for Hero Combat Strength
i = 0
while not input_valid and i in range(5):
    # Lab 9: Question 1
    try:
        combat_strength = int(input("Enter your combat Strength (1-6): "))
    except ValueError as e:
        e_info = sys.exc_info()
        e_tb = e_info[2]
        print(e_tb.tb_lineno)
        print("Invalid input. Player needs to enter integer numbers for Combat Strength")
        i += 1
        continue

    # Note: combat_strength was safely converted to integer
    # Validate input: Check if the string inputted is between 1 and 6
    if combat_strength not in range(1, 7):
        print("Enter a valid integer between 1 and 6 only")
        i = i + 1

    else:
        input_valid = True

m_input_valid = False
i = 0
while not m_input_valid and i in range(5):
    # Lab 9: Question 1
    try:
        m_combat_strength = int(input("Enter the monster's combat Strength (1-6): "))
    except ValueError:
        print("Invalid input. Monster needs to enter integer numbers for Combat Strength")
        i += 1
        continue

    # Note: m_combat_strength was safely converted to integer
    # Validate input: Check if the string inputted is between 1 and 6
    if int(m_combat_strength) not in range(1, 7):
        print("Enter a valid integer between 1 and 6 only")
        i = i + 1
    else:
        m_input_valid = True

if input_valid and m_input_valid:
    # Input was valid - broke out of while loop
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for player health points
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("Player rolled " + str(health_points) + " health points")

# Roll for monster combat strength
input("Roll the dice for the monster's combat strength (Press enter)")
m_combat_strength = random.choice(small_dice_options)
print("Player rolled " + str(m_combat_strength) + " combat strength for the monster")

# Roll for monster health points
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(big_dice_options)
print("Player rolled " + str(m_health_points) + " health points for the monster")


# Lab 9: Question 2
try:
    health_points = function.monster_attacks("Somestring1", "Somestring2")
except TypeError:
    print("A TypeError occurred")


# Loop while the monster and the player are alive. Call fight sequence functions
while m_health_points > 0 and health_points > 0:
    # Fight Sequence
    # Who attacks first?
    input("Roll to see who attacks first (Press Enter)")
    attack_roll = random.choice(small_dice_options)
    if not (attack_roll % 2 == 0):
        input("You strike (Press enter)")
        # Hero Attacks First
        m_health_points = function.hero_attacks(combat_strength, m_health_points)
        if m_health_points != 0:
            input("The monster strikes (Press enter)!!!")
            # Monster Attacks Back
            health_points = function.monster_attacks(m_combat_strength, health_points)

    else:
        # Monster Attacks First
        input("The Monster strikes (Press enter)")
        health_points = function.monster_attacks(m_combat_strength, health_points)
        if health_points != 0:
            input("The hero strikes!! (Press enter)")
            # Hero Attacks Back
            m_health_points = function.hero_attacks(combat_strength, m_health_points)

