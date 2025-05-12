import random  # To shuffle the cards

# --------------------------
# 1. Card class
# --------------------------
class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # e.g., "Hearts"
        self.rank = rank  # e.g., "Queen"

    def __str__(self):
        return f"{self.rank} of {self.suit}"  # e.g., "Queen of Hearts"

# --------------------------
# 2. Deck class
# --------------------------
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "Jack", "Queen", "King", "Ace"]
        # Create all 52 cards using nested list comprehension
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)  # randomly shuffles the deck

    def deal(self, num_players, cards_each):
        hands = [[] for _ in range(num_players)]  # list of empty lists (one per player)
        for _ in range(cards_each):  # loop as many times as cards per player
            for hand in hands:       # go to each player's hand
                if self.cards:       # if deck still has cards
                    hand.append(self.cards.pop())  # give top card to player
        return hands  # return all hands

# --------------------------
# 3. Player class
# --------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        self.hand.extend(cards)  # add multiple cards to player's hand

    def show_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            print(f"  - {card}")
        print()

# --------------------------
# 4. Create players, shuffle and deal
# --------------------------
# Create 2 players
players = [Player("Alice"), Player("Bob")]

# Create a deck and shuffle it
deck = Deck()
deck.shuffle()

# Deal 5 cards to each player
hands = deck.deal(num_players=2, cards_each=5)

# Give cards to players
for player, hand in zip(players, hands):
    player.receive_cards(hand)
    player.show_hand()
