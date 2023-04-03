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

#Write your code below this line 👇
import random

choice = input("What do you choose? Type 0 for Rock, 1 for Scissors, or 2 for Paper. ")
computer_choice = str(random.randint(0,2))

if choice == "0":
    print(rock)
elif choice == "1":
    print(scissors)
elif choice == "2":
    print(paper)
else:
    print("That is not a valid choice. Try again.")

print("Computer chose: ")

if computer_choice == "0":
    print(rock)
elif computer_choice == "1":
    print(scissors)
elif computer_choice == "2":
    print(paper)

if choice == "0" and computer_choice == "0" or choice == "1" and computer_choice == "1" or choice == "2" and computer_choice == "2":
    print("You tie.")
elif choice == "0" and computer_choice == "2" or choice == "1" and computer_choice == "0" or choice == "2" and computer_choice == "1":
    print("You lose.")
elif choice == "0" and computer_choice == "1" or choice == "1" and computer_choice == "2" or choice == "2" and computer_choice == "0":
    print("You win.")
