import random
from art import logo

#cards list
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def final_result(score_result):
    print(f"user cards: {score_result["user"][0]}, user score: {score_result["user"][1]} \ncomputer cards: {score_result["computer"][0]}, computer Score: {score_result["computer"][1]}")
    user_score=score_result["user"][1]
    computer_score=score_result["computer"][1]
    if user_score > 21 and computer_score>21:
        print(f"both of you lose!")
    elif user_score > 21 and computer_score<=21:
        print("Computer Wins")
    elif computer_score > 21 and user_score<=21:
        print("You Win")
    elif computer_score > user_score:
        print("Computer Wins")
    elif user_score > computer_score:
        print("You Win")
    elif user_score==computer_score and user_score<=21 and computer_score<=21:
        print(f"it's a draw!")

def final_cards(total_cards):
    total_cards["user"][1] = sum(total_cards["user"][0])
    total_cards["computer"][1] = sum(total_cards["computer"][0])
    for key in total_cards:
        card_list=total_cards[key][0]

        for i in range(len(card_list)):
            if card_list[i]==11:

                if sum(card_list) >21:
                    card_list[i]=1

        total_cards[key][1] = sum(total_cards[key][0])


    return final_result(total_cards)

def computer_calc(dictionary):

    if sum(dictionary["computer"][0]) < 17:
        dictionary["computer"][0].append(random.choice(cards))
        return dictionary
    else:
        return dictionary

def start_game():
    print("\n" * 20)
    print(logo)
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards=[random.choice(cards), random.choice(cards)]
    cards_choice={
        "user":[user_cards,sum(user_cards)],
        "computer":[computer_cards,sum(computer_cards)]
    }

    computer_first_card=cards_choice["computer"][0][0]
    print(f"Your cards: {user_cards}, current score: {cards_choice["user"][1]}")
    print(f"computer's first card: {computer_first_card}")

    other_card_option=str(input("Type 'y' to get another card, type 'n' to pass: "))
    if other_card_option=="y":
        user_cards.append(random.choice(cards))
        final_cards(computer_calc(cards_choice))
    elif other_card_option=="n":
        final_cards(computer_calc(cards_choice))

# Start of the program:
end_program=False
while not end_program:
    play_game=str(input("Do you want to play a game of Blackjack? Type 'y' or 'n':"))
    if play_game=='n':
        end_program=True
    elif play_game == "y":
        start_game()
    else:
        print("You selected an invalid option: ")