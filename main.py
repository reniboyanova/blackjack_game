import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = {
    'score': 0,
    'current_cards': [],
}
oponent_cards = {
    'score': 0,
    'current_cards': [],
}

have_winner = my_cards['score'] >= 21 or oponent_cards['score'] >= 21


def choose_two_cards(deck_of_cards, my_deck):
    first_card = random.choice(deck_of_cards)
    second_card = random.choice(deck_of_cards)

    my_deck['current_cards'].append(first_card)
    my_deck['current_cards'].append(second_card)
    my_deck['score'] += (first_card + second_card)

    return my_deck


def choose_one_card(deck_of_cards, deck):
    current_card = random.choice(deck_of_cards)

    if current_card == 11 and deck['score'] >= 21:
        current_card = 1

    deck['current_cards'].append(current_card)
    deck['score'] += current_card
    return deck


turns = 0

while not have_winner:

    first_question = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    print(first_question)

    if first_question == 'y':
        print(logo)
    else:
        break

    choose_two_cards(cards, my_cards)
    choose_two_cards(cards, oponent_cards)

    print(f"Your cards: {my_cards['current_cards']}, current score: {my_cards['score']}")

    computer_first_card = oponent_cards['current_cards'][0]

    print(f"Computer's first card: {computer_first_card}")

    if oponent_cards['score'] >= 21 or my_cards['score'] >= 21:
        have_winner = True
        print(f"")

    while not have_winner:

        second_question = input("Type 'y' to get another card, type 'n' to pass:")
        if second_question == 'y':
            choose_one_card(cards, my_cards)

            turns += 1
        else:
            choose_one_card(cards, oponent_cards)
            my_current_cards = my_cards['current_cards']
            print(f"Your cards: {my_current_cards}, current score: {my_cards['score']}")

        print(f"Computer's first card: {oponent_cards['current_cards']}")

        if oponent_cards['score'] >= 21 or my_cards['score'] >= 21:
            have_winner = True
            # print(f"Your last cards: {my_cards['current_cards']}, current score: {my_cards['score']}")
            # print(f"Computer's last cards: {oponent_cards['current_cards']}")

            if oponent_cards['score'] > my_cards['score']:
                print("You lose!")
            else:
                print("You win!")
                # da opravq printa
    if not have_winner:
        print(f"Your cards: {my_cards['current_cards']}, current score: {my_cards['score']}")
        print(f"Computer's first card: {oponent_cards['score']}")
