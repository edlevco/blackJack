## author: Eddie Levcovich
## date: January 2
## Name: Black Jack Game
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
money = 100

def getCard():
    return random.choice(cards)

def tellPlayerHand(allCards):
    line = "You have a "
    total = 0
    for card in allCards["playerCardsTotal"]:
        line += (f"{card}, ")
        total += card
    line += (f"totaling to {total}")
    print(line)

def playerTotal(allCards):
    total = 0
    for card in allCards["playerCardsTotal"]:
        total += card
    return total

def tellDealerHand(allCards):
    line = "The dealer has a "
    total = 0
    for card in allCards["dealerCardsTotal"]:
        line += (f"{card}, ")
        total += card
    line += (f"totaling to {total}")
    print(line)

def dealerTotal(allCards):
    total = 0
    for card in allCards["dealerCardsTotal"]:
        total += card
    return total

playAgain = True
print("Starting money: $100")
while playAgain:
    dealerLessThan17 = True
    end = False
    betProcessing = True
    allCards = {
    "playerCardsTotal": [],
    "dealerCardsTotal": [],   
}   
    while betProcessing:
        bet = int(input("How much money do you want to bet: "))
        if bet <= money:
            betProcessing = False
        else:
            print(f"You only have ${money} so you can not bet ${bet}")
    money -= bet
    for i in range(2):
        allCards["playerCardsTotal"].append(getCard())
        allCards["dealerCardsTotal"].append(getCard())
    
    print(f"The dealer's known card is a {allCards['dealerCardsTotal'][0]}")
    tellPlayerHand(allCards)
    makingMoves = True
    while makingMoves:
        userTotal = playerTotal(allCards)
        if userTotal == 21 and 11 in allCards["playerCardsTotal"] and 10 in allCards["playerCardsTotal"]:
            print("You have a total of 21 so you win!")
            end = True
            money += bet*2
            break
        elif userTotal > 21:
            print("Your total is greater than 21 so you lose!")
            end = True
            break
        playerMove = input("Do you want to 'hit' or 'stand'? ")
        if playerMove == "hit":
            allCards["playerCardsTotal"].append(getCard())
            tellPlayerHand(allCards)
        elif playerMove == "stand":
            makingMoves = False
    if not end:
        while dealerLessThan17:
            computerTotal = dealerTotal(allCards)
            if not computerTotal < 17:
                dealerLessThan17 = False
                if computerTotal > 21:
                    tellDealerHand(allCards)
                    print("The dealers total is more than 21 so you win!")
                    money += bet*2
                elif computerTotal > 16:
                    tellDealerHand(allCards)
                    print(f"You have a total of {userTotal} and the dealer has a total of {computerTotal}")
                    if userTotal > computerTotal:
                        print("You Win!")
                        money += bet*2
                    elif userTotal < computerTotal:
                        print("The dealer wins")
                    else:
                        print("It's a tie!")
                        dealerLessThan17 = False
            else:
                allCards["dealerCardsTotal"].append(getCard())
    if money == 0:
        print("You have $0, Thanks for playing!")
        break
    else:
        print(f"You now have ${money}")
    rerun = input("Do you want to play again? (y/n to quit)")
    if rerun == "n":
        print("Thanks for playing!")
        break
        
    

