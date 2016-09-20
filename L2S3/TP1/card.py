# For details : https://github.com/tonythedealer/TP-info/tree/master/L2S3/TP1

### Defined constants for this TP
VALUES = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
COLORS = ["club", "diamond", "heart", "spade"]

### Card creation
def create(value, color):
    """
    Creates a card with value and color

    Paramètres: • value (element of card.VALUES) - value of the card
                • color (element of card.COLOR) - color of the card

    Exemple:
    >>> create('Ace', 'heart')
    ('Ace', 'heart')
    """
    assert value in VALUES and color in COLORS
    card = (value, color) # here we can use a tuple or a list.
    # to make a right desition let's check is there any
    # performance difference between tuples and lists when
    # it comes to instantiation and retrieval of elements;

    # we're going to use timeit
    # here's results for the tuple...
    
    # $ python -m timeit "x=(1,2,3,4,5,6,7,8)"
    # 10000000 loops, best of 3: 0.0388 usec per loop

    # ... and for the list

    # $ python -m timeit "x=[1,2,3,4,5,6,7,8]"
    # 1000000 loops, best of 3: 0.363 usec per loop

    # in this case, instantiation is almost an order
    # of magnitude faster for the tuple.

    # note : accessing an element is the same for list as for tuple.
    return card

### Get card value
def get_value(card):
    """
    Returns the value of the card

    Paramètres: • card (card) - the card
    Retourne: (element of card.VALUES) - the value of the card
    CU: none

    Exemple:
    >>> c = create('Ace', 'heart')
    >>> get_value(c)
    'Ace'
    """
    return card[0]

### Get card color
def get_color(card):
    """
    Returns the color of the card

    Paramètres: • card - the card
                • type - card

    Retourne: (element of card.COLORS) - the color of the card
    CU: none

    Example:
    >>> c = create('Ace', 'heart')
    >>> get_color(c)
    'heart'
    """
    if type(card) is tuple: # checking if type(card) is ok;
        # normally card represents a tuple of elements.
        return card[1]
    else:
        return AssertionError

### Representation of the card: to string
def to_string(card):
    """
    Returns a string representation of the card

    Paramètres: • card - the card
    Retourne: (string) - a string representation of the card
    CU: none

    Example:
    >>> c = create('Ace', 'heart')
    >>> to_string(c)
    'Ace of heart'
    """
    return card[0] + ' of ' + card[1]

### Create a random card
def random_card():
    """
    Create a card whose value and color are randomly chosen

    Retourne: (card) - a randomply chosen card

    Example:
    >>> random_card()
    ('Ace', 'heart')
    >>> c = random_card()
    >>> get_value(c) in VALUES
    True
    >>> get_color(c) in COLORS
    True
    """
    # the program should randomly take one element from the list
    # VALUES and from the list COLORS.
    # why we use 'random.choise';

    # we don't have to select more than one item from a list,
    # or select an item from a set
    # so we don't have to use 'random.select'.

    # we don't need the index
    # so we don' have to use 'randrange'.

    # importing random module
    import random
    value = random.choice(VALUES)
    color = random.choice(COLORS)
    card = (value, color)
    return card

### Print the card
def print(card, end='\n'):
    """
    Print the card

    Paramètres: • card(card) - the card
                • end(string) - [optional] separator (default is '\n')
    CU: none
    """
    return card

### Compare value
def compare_value(card1, card2):
    """
    Compares cards values, returns:
        • a positive number if card1's value is greater than card2's
        • a negative number if card1's value is lower than card2's
        • 0 if card1's value is the same greater than card2's

    Paramètres: • card1(card) - the first card
                • card2(card) - the second card

    Retourne: (int) -
        • a positive number if card1's value is greater than card2's
        • a negative number if card1's value is lower than card2's
        • 0 if card1's value is the same greater than card2's

    CU: none

    Example:
    >>> c1 = create('Ace','heart')
    >>> c2 = create('King','heart')
    >>> c3 = create('Ace','spade')
    >>> compare_value(c1,c2) > 0
    True
    >>> compare_value(c2,c1) < 0
    True
    >>> compare_value(c1,c3) == 0
    True
    """
    if card1[0] > card2[0]:
        return -1
    elif card1[0] < card2[0]:
        return 1
    elif card1[0] == card2[0]:
        return 0
    else:
        return AssertionError
    
### Compare color
def compare_color(card1, card2):
    """
    Compares cards colors, returns:
        • a positive number if card1's color is greater than card2's
        • a negative number if card1's color is lower than card2's
        • 0 if card1's color is the same greater than card2's

    Paramètres: • card1(card) - the first card
                • card2(card) - the second card

    Retourne: (int) -
        • a positive number if card1's color is greater than card2's
        • a negative number if card1's color is lower than card2's
        • 0 if card1's color is the same greater than card2's

    CU: none

    Example:
    >>> c1 = create('Ace','heart')
    >>> c2 = create('King','heart')
    >>> c3 = create('Ace','spade')   
    >>> compare_color(c1,c3) < 0
    True
    >>> compare_color(c3,c1) > 0
    True
    >>> compare_color(c1,c2) == 0
    True
    """
    if card1[1] > card2[1]:
        return -1
    elif card1[1] < card2[1]:
        return 1
    elif card1[1] == card2[1]:
        return 0
    else:
        return AssertionError

### Compare All
def compare(card1, card2):
    """
    Compares cards, first it compares
    cards values and if equal cards colors returns:
        • a positive number if card1 is greater than card2
        • a negative number if card1 is lower than card2
        • 0 if card1 is the same greater than card2

    Paramètres: • card1(card) - the first card
                • card2(card) - the second card

    Retourne: (int) -
        • a positive number if card1 is greater than card2
        • a negative number if card1 is lower than card2
        • 0 if card1 is the same greater than card2

    CU: none

    Example:
    >>> c1 = create('Ace','heart')
    >>> c2 = create('King','heart')
    >>> c3 = create('Ace','spade')
    >>> c1bis = create('Ace','heart')
    >>> compare(c1,c2) > 0
    True
    >>> compare(c2,c1) < 0
    True
    >>> compare(c1,c3) < 0
    True
    >>> compare(c1,c1bis) == 0
    True
    """
    if card1[0] > card2[0] and card1[1] > card2[1]:
        return 1
    elif card1[0] < card2[0] and card1[1] < card2[1]:
        return -1
    elif card1[0] < card2[0] and card1[1] > card2[1]:
        return -1
    elif card1[0] > card2[0] and card1[1] < card2[1]:
        return 1
    elif card1[0] > card2[0] and card1[1] == card2[1]:
        return -1
    elif card1[0] < card2[0] and card1[1] == card2[1]:
        return 1
    elif card1[0] == card2[0] and card1[1] > card2[1]:
        return 1
    elif card1[0] == card2[0] and card1[1] < card2[1]:
        return -1
    elif card1[0] == card2[0] and card1[1] == card2[1]:
        return 0
    else:
        return AssertionError
