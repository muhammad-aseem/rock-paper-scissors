import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("Please enter your pick (type 0 : rock, 1 : paper, 2 : scissors): "))

computer_choice = random.randint(0, 2)

print("Computer chose:")
print(game_images[computer_choice])

print(f"You chose: {user_choice}")

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

if user_choice > 2 or user_choice < 0:
    print("Invalid Number And You Have Lost the Game")

elif user_choice == 0 and computer_choice == 2:
    print("You Win!")

elif computer_choice == 0 and user_choice == 2:
    print("You Lose")

elif computer_choice > user_choice:
    print("You Lose")

elif user_choice > computer_choice:
    print("You Win")

elif computer_choice == user_choice:
    print("It's a Draw")
