import random
from chances import get_probabilities

# Create deck (Ace=1, Jack=11, Queen=12, King=13)
game_length = input("Do you want to play a (q)uick game, (n)ormal game or (l)ong game? ").strip().lower()
if game_length == 'q':
    deck = [value for value in range(1, 14)] # 1 suit
elif game_length == 'n':
    deck = [value for value in range(1, 14)] * 4  # 4 suits / full deck of cards
elif game_length == 'l':
    deck = [value for value in range(1, 14)] * 8  # 8 suits / 2 full decks of cards

def play_game():
    deck_copy = deck[:]
    random.shuffle(deck_copy)

    current_card = deck_copy.pop()
    streak = 0
    highest_streak = 0

    print(f"Starting card: {current_card}")

    while deck_copy:
        higher_prob, lower_prob = get_probabilities(deck_copy, current_card)
        print(f"\nChances → Higher: {higher_prob:.2f}% | Lower: {lower_prob:.2f}%")
        print(f"Current streak: {streak}")

        guess = input("Will the next card be (h)igher or (l)ower? ").strip().lower()
        next_card = deck_copy.pop()
        print(f"Next card: {next_card}")

        if guess == "h" and next_card > current_card:
            streak += 1
            if streak > highest_streak:
                highest_streak = streak
            print("Correct! It was higher.\n")
        elif guess == "l" and next_card < current_card:
            streak += 1
            if streak > highest_streak:
                highest_streak = streak
            print("Correct! It was lower.\n")
        elif next_card == current_card:
            print("It's a tie! No win or loss. Streak unchanged.\n")
        else:
            streak = 0
            print("Wrong guess. Streak reset.\n")

        current_card = next_card

    print("\nNo more cards left! Game over.")
    print(f"Final streak: {streak}")
    print(f"Highest streak: {highest_streak}")

play_game()