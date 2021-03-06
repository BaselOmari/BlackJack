
from random import *

turn = 0
wins = 0
draws = 0
losses = 0
cash = 0
bet = 0

def cashIn():
    globals()['cash'] = int(input("How much do you wish to cash in?\n"))


def blackJack():
    impot deckBuilder
    cards = deckBuilder.cards
    shuffle(cards)

    globals()['turn'] = 3
    pcards = [cards[0],cards[1]]
    dcards = [cards[2]]

    def bets():
        print("\n"*56)
        print(f"Money in the Bank: {globals()['cash']}$")
        globals()['bet'] = int(input("How much do you wish to bet?\n"))
        while globals()['bet'] > globals()['cash'] or globals()['bet']<=0:
            globals()['bet'] = int(input("Quit playin bruh ur broke. Put in a real amount:\n"))
        globals()['cash'] -= globals()['bet']

    def playerSumCalc():
        sum = 0
        n = 0
        ace = 0
        for i in pcards:
            card = pcards[n]
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
                sum += 10
            elif card[0] == 'A':
                ace += 1
                sum += 11
            else:
                ncard = card
                sum += int(ncard[0:2])
            n += 1

        while sum > 21 and ace != 0:
            sum -= 10
            ace -= 1
        return sum

    def dealerSumCalc():
        sum = 0
        n = 0
        ace = 0
        for i in dcards:
            card = dcards[n]
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
                sum += 10
            elif card[0] == 'A':
                ace += 1
                sum += 11
            else:
                ncard = card
                sum += int(ncard[0:2])
            n += 1
        while sum > 21 and ace != 0:
            sum -= 10
            ace -= 1
        return sum

    def interface():
        pSum = playerSumCalc()
        displayPSum = "Players Sum: " + str(pSum)
        dSum = dealerSumCalc()
        displayDSum = "Dealers Sum: " + str(dSum)
        gn = globals()['wins']+globals()['draws']+globals()['losses']+1

        print("\n"*26)
        print("Game Number:",gn)
        print("Wins: " + str(globals()['wins']))
        print("Draws: " + str(globals()['draws']))
        print("Losses: " + str(globals()['losses']))
        print()
        print("Players Cards:\n")
        for i in pcards:
            print(i)
        print("\n"+displayPSum)

        print("\n\nDealers Cards:\n")
        for i in dcards:
            print(i)
        print("\n"+displayDSum)

        print(f"\n\nMoney in the Bank: {globals()['cash']}$")
        print(f"Current Bet: {globals()['bet']}$")

    def choice():
        if playerSumCalc() > 21:
            print("\nPlayer Busts and loses the pot")
            globals()['losses'] += 1
        else:
            choice = input(f"\n\nDo you wish to stand or hit?\n1- Hit\n2- Stand\n\nSuggestion: {decision()}\n")
            if choice == "1":
                hit()
            elif choice == "2":
                stand()

    def doubChoice():
        choice = input(f"\n\nDo you wish to stand, hit or double?\n1- Hit\n2- Stand\n3- Double\n\nSuggestion: {doubDecision()}\n")
        if choice == "1":
            hit()
        elif choice == "2":
            stand()
        elif choice == "3":
            double()

    def hit():
        pcards.append(cards[globals()['turn']])
        globals()['turn'] += 1
        interface()
        choice()

    def double():
        globals()['cash'] -= globals()['bet']
        globals()['bet'] *= 2
        pcards.append(cards[globals()['turn']])
        globals()['turn'] += 1
        if playerSumCalc() > 21:
            print("\nPlayer Busts and loses the pot")
            globals()['losses'] += 1
        else:
            stand()

    def stand():
        while dealerSumCalc() < 17:
            dcards.append(cards[globals()['turn']])
            globals()['turn'] += 1
        interface()
        results()

    def results():
        if dealerSumCalc() > 21:
            print("\nDealer Busts and loses the pot")
            globals()['wins'] += 1
            globals()['cash'] += 2*globals()['bet']
        elif playerSumCalc() > dealerSumCalc():
            print("\nPLAYER WINSSSS")
            globals()['wins'] += 1
            globals()['cash'] += 2 * globals()['bet']
        elif dealerSumCalc() > playerSumCalc():
            print("\nDealer wins")
            globals()['losses'] += 1
        else:
            print("PUSH")
            globals()['draws'] += 1
            globals()['cash'] += globals()['bet']

    def decision():
        if playerSumCalc() >= 17:
            return "Stand"
        if playerSumCalc() <= 11:
            return "Hit"
        if playerSumCalc() <= 16 and playerSumCalc() >= 13 and dealerSumCalc() <= 6:
            return "Stand"
        if playerSumCalc() <= 16 and playerSumCalc() >= 12 and dealerSumCalc() >= 7:
            return "Hit"
        if playerSumCalc() == 12 and dealerSumCalc() <= 3:
            return "Hit"
        if playerSumCalc() == 12 and dealerSumCalc() >= 4 and dealerSumCalc() <= 6:
            return "Stand"

    def doubDecision():
        if playerSumCalc() >= 17:
            return "Stand"
        if playerSumCalc() <= 8:
            return "Hit"
        if playerSumCalc() <= 16 and playerSumCalc() >= 13 and dealerSumCalc() <= 6:
            return "Stand"
        if playerSumCalc() <= 16 and playerSumCalc() >= 12 and dealerSumCalc() >= 7:
            return "Hit"
        if playerSumCalc() == 12 and dealerSumCalc() <= 3:
            return "Hit"
        if playerSumCalc() == 12 and dealerSumCalc() >= 4 and dealerSumCalc() <= 6:
            return "Stand"
        if playerSumCalc() == 11:
            return "Double"
        if playerSumCalc() == 10 and dealerSumCalc() == 10:
            return "Hit"
        if playerSumCalc() == 10 and dealerSumCalc() < 10:
            return "Double"
        if playerSumCalc() == 9 and (dealerSumCalc() == 9 or dealerSumCalc() > 6):
            return "Hit"
        if playerSumCalc() == 9 and dealerSumCalc() >= 3 and dealerSumCalc() <= 6:
            return "Double"

    bets()
    interface()
    if globals()['bet']*2 <= globals()['cash']+globals()['bet']:
        doubChoice()
    else:
        choice()

def repeat():
    if globals()['cash'] == 0:
        print("DAMMNNNN BETTER NOT START BETTING AGAIN RIGHT, YOU BROKE BRUH")
    else:
        rep = input("\n\nDo you wish to restart?\n1- Yes\n2- No\n")
        if rep == '1':
            blackJack()
            repeat()
        else:
            print(f"\nAight see ya, enjoy your {globals()['cash']}$")

cashIn()
blackJack()
repeat()
