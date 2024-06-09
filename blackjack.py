
import random

def countScore(cards):
    score = 0
    for card in cards:
        score += card
    return score


def gameStart():
    continue_game = True
    another_card = 'y'
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    round = 1
    player_cards = []
    pc_cards = []
    player_score = 0
    pc_score = 0
    answer = input("do you want to play a game of blackjack? Type 'y' or 'n': ")
    if answer == 'n':
        continue_game = False
        print('understood, have a nice day')
    
    while continue_game:
        if round == 1:
            for n in range(0,2):
                player_cards.append(random.choice(cards))
                pc_cards.append(random.choice(cards))
        elif another_card == 'y' and round > 1:
            player_cards.append(random.choice(cards))
        player_score = countScore(player_cards)
        print(f'your cards: {player_cards}, current score: {player_score}\n')
        print(f'pc first card: {pc_cards[0]}')
        another_card = input("Type 'y' to get another card, Type 'n' to pass: ")
        round+=1
        if player_score > 21 or another_card == 'n':
            pc_score = countScore(pc_cards)
            print(f'your final hand {player_cards}, final score: {[player_score]}')
            print(f'pc final hand {pc_cards}, final score: {[pc_score]}')
            if player_score > 21:
                print('"You went over. you lose.')
            elif player_score < pc_score and player_score < 21:
                print('you lose.')
            elif player_score == pc_score:
                print('its a tie.')
            elif player_score > pc_score and player_score <= 21:
                print('you win')
        
            gameStart()

gameStart()




        
        