def value_of_card(card):
    if card == "Q" or card == "J" or card== "K":
        return 10
    elif card == "A":
        return 1
    else :
        return int (card)
def higher_card(card_one, card_two):
    card_values = {"A": 1, "J": 10, "Q": 10, "K": 10}

    val_one = card_values[card_one] if card_one in card_values else int(card_one)
    val_two = card_values[card_two] if card_two in card_values else int(card_two)

    if val_one == val_two:
        return card_one,card_two

    return card_one if val_one > val_two else card_two

def value_of_ace(card_one, card_two):
    card_values = {"A":1 ,"Q":10 , "J":10 , "K":10 }

    first_value = card_values[card_one] if card_one in card_values else int(card_one)
    second_value = card_values[card_two] if card_two in card_values else int(card_two)

    sum = first_value + second_value

    if card_one == "A" or card_two == "A" or sum > 10:
        return 1
    elif  sum == 11 :
        return "Blackjack"
    else :
        return 11

def is_blackjack(card_one, card_two):
    card_value = {"A":1,"J":10,"K":10,"Q":10}

    value_one = card_value[card_one]if card_one in card_value else int(card_one)
    value_two = card_value[card_two]if card_two in card_value else int(card_two)

    sum = value_one + value_two

    if card_one != "A" and card_two != "A":
        return False
    elif sum == 11:
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    card_value = {"A":1,"J":10,"K":10,"Q":10}

    value_one = card_value[card_one]if card_one in card_value else int(card_one)
    value_two = card_value[card_two]if card_two in card_value else int(card_two)
    
    return True if value_one == value_two else False

def can_double_down(card_one, card_two):
    card_value = {"A":1,"J":10,"K":10,"Q":10}

    value_one = card_value[card_one]if card_one in card_value else int(card_one)
    value_two = card_value[card_two]if card_two in card_value else int(card_two)

    sum = value_one + value_two

    return True if sum == 9 or sum == 10 or sum ==11 else False
 
