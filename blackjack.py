import random
import os


def calc_hand(hand):
    sum = 0

    non_aces = [card for card in hand if card != "A"]
    aces = [card for card in hand if card == "A"]

    for card in non_aces:
        if card in "JQK":
            sum += 10
        else:
            sum += int(card)

    for card in aces:
        if sum <= 10:
            sum += 11
        else:
            sum += 1

    return sum


deck = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
]

random.shuffle(deck)

dealer_hand = []
player_hand = []

player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

stand = False
first_hand = True

while True:
    os.system("cls" if os.name == "nt" else "clear")

    dealer_score = calc_hand(dealer_hand)
    player_score = calc_hand(player_hand)

    if stand:
        print("Dealer Cards: [{}]({})".format("][".join(dealer_hand), dealer_score))
    else:
        print("Dealer Cards: [{}][?]".format(dealer_hand[0]))

    print("Your Cards: [{}] ({})".format("][".join(player_hand), player_score))
    print("")

    if stand:
        if dealer_score > 21:
            print("Dealer busted, you win!")
        elif player_score > dealer_score:
            print("You beat the dealer, you win!")
        elif player_score == dealer_score:
            print("Push, noboy wins or loses")
        else:
            print("You lose")

        break
    if player_score > 21:
        print("Busted!")
        break

    if first_hand and player_score == 21:
        print("***Blackjack!***")
        break

    first_hand = False

    print("What would you like to do?")
    print(" [1} Hit")
    print(" [2} Stand")

    print("")
    choice = input("Your choice:")
    print("")

    if choice == "1":
        player_hand.append(deck.pop())
    elif choice == "2":
        stand = True
    elif choice != "1" or "2":
        print('Enter a 1 or a 2 only')
        while calc_hand(dealer_hand) <= 16:
            dealer_hand.append(deck.pop())
