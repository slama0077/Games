import random

suits = ('Heart', 'Clubs', 'Diamond', 'Spades')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'two': 2, 'three':3, 'four': 4, 'five': 5, 'six':6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck():
    def __init__(self):
        self.cardList = []

        for suit in suits:
            for rank in ranks:
                myCard = Card(suit, rank)
                self.cardList.append(myCard)
        
    
    def randomze(self):
        random.shuffle(self.cardList)

class Player():
    def __init__(self, name, indicator, origdeck):
        self.name = name
        self.deck = []
        if indicator == 1:
            self.deck = origdeck.cardList[0:53:2]
        else:
            self.deck = origdeck.cardList[1:53:2]
    

print("Welcome players to the WarZone! A new deck of card is being made ready for you!")
gameDeck = Deck()
gameDeck.randomze()
player1name = input("Player 1! Give me your name: ")
player1 = Player(player1name, 1, gameDeck)
player2name = input("Player 2! Give me your name: ")
player2 = Player(player2name, 2, gameDeck)
print(f"Thank you {player1name} and {player2name}! Your cards have been alternatively distributed starting from {player1name}")
smallDeck1 = []
smallDeck2 = []
tie = False
print(f"Game has been started!")
while True:
    if (player1.deck.__len__() == 0 or player2.deck.__len__() == 0) and tie == False:
        break
    
    gar1 = input(f"{player1name} press space bar to place your card(s): ")
    smallDeck1.append(player1.deck.pop())
    print(smallDeck1[0])
    gar2 = input(f"{player2name} press space bar to place your card(s): ")
    smallDeck2.append(player2.deck.pop())
    print(smallDeck2[0])

    print(f"{player1name}'s {smallDeck1[0]} vs {player2name}'s {smallDeck2[0]}")

    if smallDeck1[len(smallDeck1)-1].value > smallDeck2[len(smallDeck2)-1].value:
        print(f"{player1name} won the round")
        for card in smallDeck1:
            player1.deck.append(card)
        for card in smallDeck2:
            player1.deck.append(card)
        tie = False
        smallDeck1.clear()
        smallDeck2.clear()
        random.shuffle(player1.deck)

    elif smallDeck1[len(smallDeck1)-1].value < smallDeck2[len(smallDeck2)-1].value:
        print(f"{player2name} won the round")
        for card in smallDeck1:
            player2.deck.append(card)
        for card in smallDeck2:
            player2.deck.append(card)
        tie = False
        smallDeck1.clear()
        smallDeck2.clear()
        random.shuffle(player2.deck)

    else:
        print(f"It's a draw! War has been triggered. Both players, risk in 3 more cards!:")
        risk = 2
        if len(player1.deck) < 3 or len(player2.deck)< 3:
            if(len(player1.deck) < len(player2.deck)):
                print(f"It seems like {player1name} has less than 3 cards. So, we risk {len(player1.deck)} cards only")
                risk = len(player1.deck) - 1
            else:
                print(f"It seems like {player2name} has less than 3 cards. So, we risk {len(player2.deck)} cards only")
                risk = len(player2.deck) -1
        
        if risk < 0:
            if len(player1.deck) < len(player2.deck):
                print(f"{player1name}, you cant continue no more! You're out of cards")
            else:
                 print(f"{player2name}, you cant continue no more! You're out of cards")
            tie = False
        else:
            i = 0
            while i < risk:
                smallDeck1.append(player1.deck.pop())
                smallDeck2.append(player2.deck.pop())
            tie = True

if len(player1.deck) == 0:
    print(f"{player2name} won the battle")
else:
    print(f"{player1name} won the battle")
