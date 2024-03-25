import random

choices = ['r','p','s']

while True:
   
    computer_choice = random.choice(choices)
    
    print("Rock Paper Scissors Game \n")
   
    print("Write r for rock \np for paper and \ns for scissors\nexit to quit the game \n")
    user_choice = input("Enter your choice : ")
   
    if user_choice == 'r' and computer_choice == 'p':
        print(f"\nYou lost your choice was {user_choice} and computer choice was {computer_choice}\n ")
    elif user_choice == 'p' and computer_choice == 'r':
        print(f"\nYou won your choice was {user_choice} and computer choice was {computer_choice} \n")
   
    if user_choice == 'p' and computer_choice == 's':
        print(f"\nYou lost your choice was {user_choice} and computer choice was {computer_choice}\n ")
    elif user_choice == 's' and computer_choice == 'p':
        print(f"\nYou won your choice was {user_choice} and computer choice was {computer_choice}\n ")
       
    if user_choice == 's' and computer_choice == 'r':
        print(f"\nYou lost your choice was {user_choice} and computer choice was {computer_choice}\n ")
    elif user_choice == 'r' and computer_choice == 's':
        print(f"\nYou won your choice was {user_choice} and computer choice was {computer_choice}\n ")
   
    if user_choice == computer_choice:
        print(f"\nThe game is a draw cause you picked {user_choice} and computer picked {computer_choice}\n")
       
    if user_choice == "exit":
        print("\nByeeeeeeeeeeeee")
        break