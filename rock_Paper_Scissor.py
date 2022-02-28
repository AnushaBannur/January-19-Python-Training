#rock paper scissor

import random


def game(user_input,system_input):
           
                if(user_input == system_input):
                    return("Tie")
                elif(user_input == "rock" and system_input == "scissor"):
                    return("rock")
                elif(user_input == "rock" and system_input == "paper"):
                    return("paper")    
                elif(user_input == "paper" and system_input == "scissor"):
                    return("scissor")
                elif(user_input == "paper" and system_input == "rock"):
                    return("paper")
                elif(user_input == "scissor" and system_input == "rock"):
                    return("rock")
                elif(user_input == "scissor" and system_input == "paper"):
                    return("scissor")
                else:
                    return("Invalid Input")
           

#Number of games you want to play ? collect one integer

num_of_games = int(input(("Number of games you want to play ?")))

user_points = 0
system_points = 0

for i in range(num_of_games):

        #collect user input

        user_input = input("Enter user input : ")
        print("user input is : ", user_input)

        #collect system input

        Li1 = ["rock","paper","scissor"]
        system_input = random.choice(Li1)
        print("System input is : ", system_input)        
        game_Res = game(user_input,system_input)

        print("Result of the game : ", game_Res)

        if(game_Res == user_input):
            user_points = user_points + 1
        elif(game_Res == system_input):
            system_points = system_points + 1
            
        print("User points : ",user_points)
        print("System points : ",system_points)
    
if(user_points > system_points):
        print("The Winner is : User")
elif(user_points < system_points):
        print("The Winner is : System")
else:
        print("It's a Tie")  





