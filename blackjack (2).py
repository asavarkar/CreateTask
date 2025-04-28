import random

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Club", "Diamond", "Heart", "Spade"]

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}

# Initialize game state
used_cards = {}
user_hand = []
user_total = 0
dealer_hand = []
dealer_total = 0


# Deal initial cards
def deal_card():
    while True:
        random_rank = random.randint(0, len(ranks) - 1)
        random_suit = random.randint(0, len(suits) - 1)
        card = (ranks[random_rank], suits[random_suit])

        # Check if card has been used already
        if card not in used_cards.values():
            used_cards[len(used_cards) + 1] = card
            return card


# Calculate hand total with Ace handling
def calculate_total(hand):
    total = 0
    aces = 0

    for card in hand:
        rank = card[0]
        if rank == "Ace":
            aces += 1
            total += 11
        else:
            total += card_values[rank]

    # Convert Aces from 11 to 1 as needed to avoid busting
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total

# Calculate visible dealer total (only first card)


def calculate_visible_dealer_total():
    rank = dealer_hand[0][0]
    if rank == "Ace":
        return 11
    else:
        return card_values[rank]


# Deal initial hands
# Deal 2 cards to player
user_hand.append(deal_card())
user_hand.append(deal_card())

# Deal 2 cards to dealer
dealer_hand.append(deal_card())
dealer_hand.append(deal_card())

# Calculate initial totals
user_total = calculate_total(user_hand)
dealer_total = calculate_total(dealer_hand)
visible_dealer_total = calculate_visible_dealer_total()

# Display initial hands
print("=== BLACKJACK ===")

# Display dealer's hand with second card hidden
print("\nDealer's hand:")
print(f"Card 1: {dealer_hand[0][0]} of {dealer_hand[0][1]}")
print(f"Card 2: [Face Down]")
print(f"Dealer's visible total: {visible_dealer_total}")

# Player's turn
while user_total < 21:
    # Display user's hand
    print("\nYour hand:")
    for i, card in enumerate(user_hand):
        print(f"Card {i+1}: {card[0]} of {card[1]}")
    print(f"Your current total: {user_total}")

    # Check for natural blackjack
    if len(user_hand) == 2 and user_total == 21:
        print("Blackjack! You have 21.")
        break

    # Ask for hit or stand
    decision = input("\nDo you want to hit or stand? ")

    if decision.lower() == "hit":
        new_card = deal_card()
        user_hand.append(new_card)
        user_total = calculate_total(user_hand)

        print(f"\nYou drew: {new_card[0]} of {new_card[1]}")

        # Display dealer's hand again with second card hidden
        print("\nDealer's hand:")
        print(f"Card 1: {dealer_hand[0][0]} of {dealer_hand[0][1]}")
        print(f"Card 2: [Face Down]")
        print(f"Dealer's visible total: {visible_dealer_total}")

        # Check for bust
        if user_total > 21:
            print(f"Bust! Your total is {user_total}.")
            break
    else:
        print(f"\nYou stand with a total of {user_total}.")
        break

# Reveal dealer's hidden card
print("\n=== Dealer reveals hidden card ===")
print(f"Hidden card was: {dealer_hand[1][0]} of {dealer_hand[1][1]}")
print("\nDealer's full hand:")
for i, card in enumerate(dealer_hand):
    print(f"Card {i+1}: {card[0]} of {card[1]}")
print(f"Dealer's actual total: {dealer_total}")

# Dealer's turn (if player didn't bust)
if user_total <= 21:
    print("\nDealer's turn:")

    # Dealer hits until reaching 17 or higher
    while dealer_total < 17:
        print("\nDealer hits...")
        new_card = deal_card()
        dealer_hand.append(new_card)
        dealer_total = calculate_total(dealer_hand)

        print(f"Dealer drew: {new_card[0]} of {new_card[1]}")

        # Display dealer's updated hand and total
        print("\nDealer's updated hand:")
        for i, card in enumerate(dealer_hand):
            print(f"Card {i+1}: {card[0]} of {card[1]}")
        print(f"Dealer's current total: {dealer_total}")

        # Check for dealer bust
        if dealer_total > 21:
            print(f"Dealer busts with {dealer_total}!")
            break

    if dealer_total <= 21:
        print(f"\nDealer stands with {dealer_total}.")

# Determine winner
print("\n=== GAME RESULT ===")
print("\nYour final hand:")
for i, card in enumerate(user_hand):
    print(f"Card {i+1}: {card[0]} of {card[1]}")
print(f"Your final total: {user_total}")

print("\nDealer's final hand:")
for i, card in enumerate(dealer_hand):
    print(f"Card {i+1}: {card[0]} of {card[1]}")
print(f"Dealer's final total: {dealer_total}")

if user_total > 21:
    print("\nYou bust! Dealer wins.")
elif dealer_total > 21:
    print("\nDealer busts! You win!")
elif user_total > dealer_total:
    print(f"\nYou win with {user_total} against dealer's {dealer_total}!")
elif dealer_total > user_total:
    print(f"\nDealer wins with {dealer_total} against your {user_total}.")
else:
    print(f"\nPush! Both you and the dealer have {user_total}.")
