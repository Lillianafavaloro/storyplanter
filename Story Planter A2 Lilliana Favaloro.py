import random
import time

prompts = {
    "Fantasy": [
        "A dragon offers to help you on a quest, but asks for a strange favour in return.",
        "You discover a hidden world inside an old library.",
        "A spell goes wrong and changes your world forever."
    ],
    "Romance": [
        "You bump into someone from your past on a rainy day.",
        "A love letter arrives, but you don't know who sent it.",
        "Two rivals find themselves stuck in a lift together."
    ],
    "Mystery": [
        "A mysterious note appears on your doorstep.",
        "Someone has been leaving cryptic messages in your diary.",
        "A locked room holds a secret no one expects."
    ]
}

print("Welcome to Word Planter! Your random writing prompt generator.\n")

while True:
    category = input("Choose a category (Fantasy, Romance, Mystery): ").title()

    if category in prompts:
        max_time = int(input("How long should the program run for in seconds? "))
        prompt = random.choice(prompts[category])
        print("\nHere's your writing prompt:\n" + prompt)

        print("\nWriting sprint starts now! You have", max_time, "seconds.")
        for i in range(max_time, 0, -1):
            print(i, "seconds remaining...")
            time.sleep(1)
        print("Time's up! Keep writing if you want to continue your story!")

    else:
        print("Sorry, that category doesn't exist. Try Fantasy, Romance, or Mystery.")

    continue_choice = input("\nDo you want another prompt? (yes/no): ").lower()
    if continue_choice != "yes":
        print("Thanks for using Word Planter! Happy writing!")
        break
