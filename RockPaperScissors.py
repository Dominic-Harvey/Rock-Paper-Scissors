import random
players_throws = []
players_results = []

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

def play(players_results):
    player_choice = input("Rock Paper or Scissors? ").lower()
    bot_choice = throw_predictor(players_results, players_throws)
    print (f"{choices[player_choice]} VS {bot_choice}")
    if choices[player_choice] == bot_choice:
        print('Tie!')
        players_results.append('tie')    
    elif compare(choices[player_choice], bot_choice):
        print('Player Wins!')
        players_results.append('win')
    else:
        print('Computer Wins!')
        players_results.append('loss')
    print('=====================================================')
    return players_throws.append(choices[player_choice].lower())
   # players_results


def compare(playerChoice, botChoice):
    results = {('paper','rock') : True,
               ('paper','scissors') : False,
               ('rock','paper') : False,
               ('rock','scissors') : True,
               ('scissors','paper') : True,
               ('scissors','rock') : False}
    return results[(playerChoice, botChoice)]

def opposite_throw(last_throw):
    opposite_throw = {
        'paper': 'scissors',
        'rock': 'paper',
        'scissors': 'rock'       
    }
    return opposite_throw[last_throw]


def throw_predictor(players_results, players_throws):
    try:
        if players_results[-1] == 'loss' and players_results[-2] == 'loss':
            smart_bot_choice = players_throws[-1]
        elif players_results[-1] == 'win' or players_results[-2] == 'win' and players_results[-1] == 'win':
            smart_bot_choice = opposite_throw(players_throws[-1])
        return smart_bot_choice
    except:
        smart_bot_choice = choices[random.randint(1,3)]
        return smart_bot_choice


rounds = int(input("How many rounds would you like to play? "))
for _ in range(rounds):
    play(players_results)
   

final = input("Press enter to close")