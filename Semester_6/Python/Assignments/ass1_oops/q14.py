import random
from dataclasses import dataclass

# Define the Card class using dataclass
@dataclass
class Card:
    suit: str
    rank: str

# Define the Deck class
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        hand = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]  # Remove dealt cards from the deck
        return hand

# Create a deck and shuffle it
deck = Deck()
deck.shuffle()

# Deal 5 cards to the player
player_hand = deck.deal(5)

# Display the player's hand
print("Player's hand:")
for card in player_hand:
    print(f"{card.rank} of {card.suit}")

# Display the number of remaining cards
print(f"\nCards remaining in deck: {len(deck.cards)}")
