import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}



class Game:
    
    def __init__(self):
        
        self.playing = True
        


class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    
    def __init__(self):
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) #build Card objects and add them to the list
                
    def __str__(self):
        deck_comp = ''
        
        for card in self.deck:
            deck_comp += '\n ' +card.__str__() #add each Card
            
        return 'The dack has:'+ deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop() #hit one card
        return single_card
    
class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry please provide an integer")
            
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips. You have: {}".format(chips.total))
            else:
                break

def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    #or hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    game.playing # to control an upcoming while loop
    
    while True:
        x = input("Hit or stand? Enter h or s ")
        
        if x[0].lower() == "h":
            hit(deck,hand)
            
        elif x[0].lower() == "s":
            print("Player Stands Dealer's Turn")
            game.playing = False
            
        else:
            print("Sorry. I did no unterstand that, Please enter h or s only")
            continue
        
        break

def show_some(player,dealer):

    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    print("\n Player's hand:")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    #show all the dealer's cards
    print("\n Dealer's hand:")
    for card in dealer.cards:
        print(card)

    print(f"Value of Dealer's hand is: {dealer.value}")

    print("\n Player's hand:")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")
    
def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player,dealer,chips):
    print("Player wins! dealer busted!")
    chips.win_bet()
    
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
    
def push(player,dealer):
    print("Dealer and player tie! PUSH!")
    
while True:
    #print an opening statement
    
    print("Welcome to Black Jack")
    #create & shuffle the deck, deal two cards to each player
    game = Game()
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    
    player_chips = Chips()

    
    take_bet(player_chips)

    show_some(player_hand,dealer_hand)
    
    
    while game.playing:

        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
 
        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
            
        else:
            push(player_hand,dealer_hand)

    print('\n Player total chips are at: {}'.format(player_chips.total))

    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        game.playing=True
        continue
    else:
        print("Thanks for playing!")
        game.playing = False
        break