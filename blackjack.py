
import random
continue_game = True
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
round = 1
player_cards = []
pc_cards = []

while continue_game:
    answer = input("do you want to play? enter 'y' or 'n'\n")
    if answer == 'n':
        continue_game = False
        print('understood, have a nice day')
        break
    elif answer == 'y':
        if round == 1:
            for n in range(0,2):
                player_cards.append(random.choice(cards))
                pc_cards.append(random.choice(cards))
                print(f'your cards: {player_cards}\n')
                print(f'pc first card: {pc_cards[0]}')
        else:
            player_cards.append(random.choice(cards))
            pc_cards

        
        