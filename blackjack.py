print(""" 
+----------------------------+
|      Blackjack Project     |
+----------------------------+
""")

import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]

def blackjack_game():
    user_hand = []
    comp_hand = []
    game_over = False

    def deal_card():
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, comp_score):
        if user_score == comp_score:
            return "DRAW"
        elif comp_score == 0:
            return "Lost, Opponent has Blackjack"
        elif user_score == 0:
            return "Won, You have Blackjack"
        elif user_score > 21:
            return "You went over score, YOU LOST"
        elif comp_score > 21:
            return "Opponent went over score, YOU WIN"
        elif user_score > comp_score:
            return "YOU WIN"
        else:
            return "YOU LOST"

    for i in range(2):
        user_card = deal_card()
        user_hand.append(user_card)

        comp_card = deal_card()
        comp_hand.append(comp_card)

    while not game_over:
        user_score = calculate_score(user_hand)
        comp_score = calculate_score(comp_hand)
        print("USER HAND = ", user_hand,"USER SCORE = ", user_score)
        print("COMP FIRST CARD = ", comp_hand[0])        
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:        
                user_choice = input("Do You Want To Draw Another Card - Yes OR No: ")
                if user_choice.lower() == "yes":
                    user_hand.append(deal_card())
                else:
                    game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_hand.append(deal_card())
        comp_score = calculate_score(comp_hand)

    print("USER HAND = ", user_hand,"USER SCORE = ", user_score)
    print("COMPUTER HAND = ", comp_hand,"COMPUTER SCORE = ", comp_score)
    print(compare(user_score, comp_score))
   
while input("START BLACKJACK GAME, 'Y' OR 'N'").lower() == "y":
    blackjack_game()


            