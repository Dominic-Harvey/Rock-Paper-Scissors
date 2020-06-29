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

def play():
    
    def ask_choice():
        player_choice = input("Rock Paper or Scissors?(r,p,s) ").lower()
        if not player_choice in choices:
            return ask_choice()
        return player_choice

    player_choice = ask_choice()
    if len(players_throws) > 5:
        bot_choice = pattern_matcher()
        compare_throws(choices[player_choice], bot_choice)
    else:
        bot_choice = throw_predictor(players_results, players_throws)
        compare_throws(choices[player_choice], bot_choice)
    players_throws.append(choices[player_choice])

def compare_throws(player_choice, bot_choice):
    results = {('paper','rock') : True,
               ('paper','scissors') : False,
               ('rock','paper') : False,
               ('rock','scissors') : True,
               ('scissors','paper') : True,
               ('scissors','rock') : False}
    print (f"{choices[player_choice]} VS {bot_choice}") 
    if player_choice == bot_choice:
        print('Tie!')
        players_results.append('tie')    
    elif results[(player_choice, bot_choice)]:
        print('Player Wins!')
        players_results.append('win')
    else:
        print('Computer Wins!')
        players_results.append('loss')   
    
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

def pattern_matcher():
    predicted_throws = []
    for i in range(len(players_throws)-1):
        len_of_pattern = ((len(players_throws)-i))
        if len_of_pattern <= len(players_throws)/2:
            for ix in range(len(players_throws)):
                start_of_slice = ix
                end_of_slice = start_of_slice+len_of_pattern
                if end_of_slice < len(players_throws):
                    players_throws_to_check_against = slice(start_of_slice, end_of_slice)
                    if (players_throws[players_throws_to_check_against]) == (players_throws[len(players_throws)-len_of_pattern:len(players_throws)]):
                        predicted_throws.append(players_throws[end_of_slice])
    if not predicted_throws:
        bot_choice = throw_predictor(players_results, players_throws) 
    else:
        rock = predicted_throws.count('rock')
        paper = predicted_throws.count('paper')
        scissors = predicted_throws.count('scissors')

        if rock > paper and rock > scissors:
            bot_choice = opposite_throw('rock')
        elif paper > rock and paper > scissors:
            bot_choice = opposite_throw('paper')
        else:
            bot_choice = opposite_throw('scissors')
    return bot_choice

rounds = int(input("How many rounds would you like to play? "))

for _ in range(rounds):
    play()
    win = players_results.count('win')
    loss = players_results.count('loss')
    tie = players_results.count('tie')
    print('=====================================================')
    print (f'Wins:{win} Losses:{loss} Ties: {tie}')
    print('=====================================================')

if loss > win:
    print ('Computer wins')
elif win > loss:
    print ('Player wins')
else:
    print ("It's a tie")

final = input("Press enter to close")