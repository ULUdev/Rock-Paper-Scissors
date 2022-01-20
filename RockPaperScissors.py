import random as r


# Valid Move-Options for Player & Computer
player_moves = ["rock", "paper", "scissors"]
bot_moves = ["rock", "paper", "scissors"]

# input for player
move_input = input("Please choose a valid move: ").lower()
player_ = move_input

# bot move
bot_move = r.choice(bot_moves)
bot_ = bot_move

# checks if the input is valid (player)
def input_checker():
    if move_input in player_moves:
        print(f" I choose... {bot_move}!")
    else:
        print("Please choose a valid move!")
        exit(1)

# shows the move of the bot with True or False
class bot_c:
    def rock(choice):
        return choice == "rock"

    def scissors(choice):
        return choice == "scissors"

    def paper(choice):
        return choice == "paper"



# game mechanics
class game:

    def draw_check(bot_input, player_input):
     if bot_input == player_input:
        print(f"Its a draw![{bot_move}|{move_input}]")
     else:
         return

    # Value list (notice)
    # 1r, 3p , 6s = (2), 4, (6), 7, 9, (12)

    def value_four(bot):
        if bot_c.rock(bot_) == True:
             print("The player has won the game![paper|rock]")
        elif bot_c.paper(bot_) == True:
             print("The computer has won the game![rock|paper]")
        else:
            return

    def value_seven(bot):
       if bot_c.scissors(bot_) == True:
           print("The player has won the game![rock|scissors]")
       elif bot_c.rock(bot_) == True:
           print("The computer has won the game![scissors|rock]")
       else:
           return



    def value_nine(bot):
       if bot_c.paper(bot_) == True:
         print("The player has won the game![scissors|paper]")
       elif bot_c.paper(bot_) == True:
           print("The computer has won the game![paper|scissors]")
       else:
           return


# Summary of the game and chooses a winner
class summay():

      # Recognizes if the player or bot choosed rock, paper or scissors
      def counts(player,bot):
        if player == "rock":
            player_count = 1
        elif player == "paper":
            player_count = 3
        elif player == "scissors":
            player_count = 6
        else:
            return


        if bot == "rock":
         bot_count = 1
        elif bot == "paper":
          bot_count = 3
        elif bot == "scissors":
          bot_count = 6
        else:
            return



        game_end_check = bot_count + player_count

        if game_end_check == 4:
            game.value_four(bot_)
        elif game_end_check == 7:
            game.value_seven(bot_)
        elif game_end_check == 9:
            game.value_nine(bot_)







# Driver Code
input_checker()
game.draw_check(bot_, player_)
summay.counts(player_,bot_)
