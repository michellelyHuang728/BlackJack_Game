class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)
    #rank_dict={'hearts':'♥','spades':'♠','clubs':'♣','diamonds':'♦'}

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        self.suit=suit
        self.rank=rank 
        self.visible=visible
        

    def __lt__(self, other_card):
        rank_list=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        suit_list=['clubs','diamonds','hearts','spades']
        my_rank=rank_list.index(self.rank)
        your_rank=rank_list.index(other_card.rank)
        my_suit=suit_list.index(self.suit)
        your_suit=suit_list.index(other_card.suit)
        if my_rank<your_rank:
            return True
        elif my_rank>your_rank:
            return False
        else:
            if my_suit<your_suit:
                return True
            else:
                return False


    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        if self.visible==False:
            return '____'+'\n'+'|'+'?'+'  '+'|'+'\n'+'|'+' '+'?'+' '+'|'+'\n'+'|'+'__'+'?'+'|'
        else:
            return '____'+'\n'+'|'+str(self.get_rank())+'  '+'|'+'\n'+'|'+' '+self.get_suit()+' '+'|'+'\n'+'|'+'__'+str(self.get_rank())+'|'

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """
        if self.visible==True:
            return '('+str(self.rank)+', '+self.suit+')' 
        else:
            return '(?, ?)'
        

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        if self.suit=='hearts':
            return '♥'
        elif self.suit=='spades':
            return '♠'
        elif self.suit=='clubs':
            return '♣'
        else:
            return '♦'

    def set_visible(self, visible):
        assert isinstance(visible, bool)
        self.visible=visible
        

    