import time

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself standing at the edge of a mysterious forest.")
    time.sleep(1)
    print("Your goal is to navigate through the forest and reach the hidden treasure.")
    time.sleep(1)

def make_choice(options):
    print("\nChoose your action:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path():
    print("\nYou enter the forest and come across a fork in the path.")
    time.sleep(1)
    print("Which path will you take?")

    options = ["Take the left path.", "Take the right path."]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou chose to take the left path.")
        time.sleep(1)
        print("As you walk, you encounter a friendly woodland creature.")
        time.sleep(1)
        print("It leads you to a shortcut, and you make good progress.")
    else:
        print("\nYou chose to take the right path.")
        time.sleep(1)
        print("The path becomes dense with thorns, and you get scratched.")
        time.sleep(1)
        print("However, you discover a hidden cave with a mysterious glow.")

def encounter_wild_animal():
    print("\nAs you continue your journey, you encounter a wild animal.")
    time.sleep(1)
    print("What will you do?")

    options = ["Try to scare it away.", "Stay still and remain calm."]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou attempt to scare the animal away, but it charges at you.")
        time.sleep(1)
        print("Luckily, you find a sturdy stick to defend yourself and manage to escape.")
    else:
        print("\nYou stay still and remain calm.")
        time.sleep(1)
        print("The animal loses interest and leaves you unharmed.")

def reach_treasure():
    print("\nAfter overcoming various challenges, you finally reach the hidden treasure!")
    time.sleep(1)
    print("Congratulations! You've completed the Text-Based Adventure Game.")

if __name__ == "__main__":
    introduction()
    forest_path()
    encounter_wild_animal()
    reach_treasure()
