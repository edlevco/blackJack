## author: Eddie Levcovich
## date: January 2
## Name: Black Jack Game
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
money = 100
lost = False

def getCard():
    return random.choice(cards)

def tellPlayerHand(allCards):
    line = "You have a "
    for cards in allCards["playerCardsTotal"]:
        line += (f"{cards}, ")
    print(line)

allCards = {
    "playerCardsTotal": [],
    "dealerCardsTotal": [],

}

playAgain = True;
while playAgain:
    for i in range(2):
        allCards["playerCardsTotal"].append(getCard())
        allCards["dealerCardsTotal"].append(getCard())
    
    print(f"The dealer has a {allCards["dealerCardsTotal"][0]}")
    print(f"You have a {allCards["playerCardsTotal"][0]} and a {allCards["playerCardsTotal"][1]}")
    makingMoves = True
    cardTotal = 0
    while makingMoves:
        for cards in allCards["playerCardsTotal"]:
            cardTotal += cards
        if cardTotal == 21:
            print("You have a total of 21 so you win!")
            lost = True
            break
        elif cardTotal > 21:
            print("Your total is greater than 21 so you lose!")
            lost = True
            break
        playerMove = input("Do you want to 'hit' or 'stand'? ")
        if playerMove == "hit":
            allCards["playerCardsTotal"].append(getCard())
            tellPlayerHand(allCards)
        elif playerMove == "stand":
            break
    playAgain = False
    
