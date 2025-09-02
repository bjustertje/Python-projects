# helps calculate the chances of winning

def get_probabilities(deck, current_card):
    higher = sum(1 for card in deck if card > current_card)
    lower = sum(1 for card in deck if card < current_card)
    total = len(deck)
    if total == 0:
        return 0, 0
    return (higher / total * 100, lower / total * 100)