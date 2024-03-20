import random
user_score = 0
computer_score = 0
#determine_winner=(user_choice= 0, computer_choice = 0)
while True:
    user_choice = (input("Enter your choice: rock, paper or scissors ")).lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("You Entered an invalid choice, check and choose again ")
        continue
   

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer Choose: {computer_choice}")
    #print(f"computer_choice: {computer_choice}")
    
    #result = determine_winner(user_choice, computer_choice)
    #print(result)
    #computer_choice += 1

    if computer_choice == user_choice:
        print("It's a Tie")
    elif computer_choice == 'rock' and user_choice == 'scissors':
        print("You Lose!")
        computer_score += 1
        
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print("You Won!")
        user_score += 1
    elif computer_choice > user_choice:
        print("You Lose. ")
        computer_score += 1
    elif user_choice > computer_choice:
        print("You Won. ")
        user_score += 1
        
    print(F"Your Score:{user_score}, computer Score {computer_score} ")
        
    play_again = input("Do you want to play again? (yes/no): ").lower()  
    if play_again != 'yes':
        print("Thanks for playing! ")
        break
   
        