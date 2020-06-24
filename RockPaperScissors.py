import random
players_throws = []
winner = [0]

choices={
       'r': 'rock',
       'p': 'paper',
       's':  'scissors',
       'rock': 'rock',
       'paper': 'paper',
       'scissors': 'scissors',
       1 : 'rock',
       2 : 'paper',
       3 : 'scissors'
    }

def play(winner):
    player_choice = input("Rock Paper or Scissors? ").lower()
    bot_choice = throw_predictor(winner[-1], players_throws)
    print (f"{choices[player_choice]} VS {bot_choice}")
    if choices[player_choice] == bot_choice:
        print('Tie!')
        winner.append(0)    
    elif compare(choices[player_choice], bot_choice):
        print('Player Wins!')
        winner.append(1)
    else:
        print('Computer Wins!')
        winner.append(-1)
    players_throws.append(choices[player_choice].lower())
    return winner


def compare(playerChoice, botChoice):
    results = {('paper','rock') : True,
               ('paper','scissors') : False,
               ('rock','paper') : False,
               ('rock','scissors') : True,
               ('scissors','paper') : True,
               ('scissors','rock') : False}
    return results[(playerChoice, botChoice)]

def opposite_throw(players_throws):
    opposite_throw = {
        'paper': 'scissors',
        'rock': 'paper',
        'scissors': 'rock'       
    }
    return opposite_throw[players_throws]


def throw_predictor(winner, players_throws):
    winner = str(winner)
    if int(winner[-1]) == 1: 
        smart_bot_choice = opposite_throw(players_throws[-1])
    elif int(winner[-1]) == -1:
        smart_bot_choice = players_throws[-1] 
    elif int(winner[-1]) == 0:
        smart_bot_choice = choices[random.randint(1,3)]
    return smart_bot_choice


rounds = int(input("How many rounds would you like to play? "))
for _ in range(rounds):
    play(winner)
    score = (sum(x > 0 for x in winner))
    
print (f"You won {score} out of {rounds}")
final = input("Press any key to close")