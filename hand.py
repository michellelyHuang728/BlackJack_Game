from card import Card

class PlayerHand():
    """
    >>> card_1 = Card("A", "spades")
    >>> card_2 = Card(2, "diamonds")
    >>> card_3 = Card(3, "clubs")
    >>> card_4 = Card(4, "hearts")
    >>> card_5 = Card(5, "spades")
    >>> card_6 = Card("K", "diamonds")
    >>> card_7 = Card("J", "clubs")
    >>> card_8 = Card("Q", "hearts")
    
    >>> p_hand = PlayerHand()
    >>> p_hand.add_card(card_1, card_2)
    >>> p_hand
    (2, diamonds) (A, spades)
    >>> p_hand.add_card(card_3)
    >>> print(p_hand)
    ____
    |2  |
    | ♦ |
    |__2|
    ____
    |3  |
    | ♣ |
    |__3|
    ____
    |A  |
    | ♠ |
    |__A|
    
    >>> p_hand
    (2, diamonds) (3, clubs) (A, spades)

    >>> d_hand = DealerHand()
    >>> d_hand.add_card(card_4)
    >>> d_hand.add_card(card_5, card_6)
    >>> print(d_hand)
    ____
    |4  |
    | ♥ |
    |__4|
    ____
    |?  |
    | ? |
    |__?|
    ____
    |?  |
    | ? |
    |__?|
    >>> d_hand
    (4, hearts) (?, ?) (?, ?)
    >>> d_hand.reveal_hand()
    >>> print(d_hand)
    ____
    |4  |
    | ♥ |
    |__4|
    ____
    |5  |
    | ♠ |
    |__5|
    ____
    |K  |
    | ♦ |
    |__K|
    >>> d_hand
    (4, hearts) (5, spades) (K, diamonds)
    """
    
    def __init__(self):
        self.cards=[]
        
    def add_card(self, *cards):
        """
        Adds cards to the hand, then sorts
        them in ascending order.
        """
        assert all(isinstance(i, Card) for i in cards)
        
        for card in cards:
            self.cards.append(card)
        self.sort_hand()
        

    def get_cards(self):
        return self.cards           

    def __str__(self):
        """
        Returns the string representation of all cards
        in the hand, with each card on a new line.
        """
        string=''
        for i in self.get_cards():
            string+=str(i)+'\n'
        return string[:-1]
        
    
    def __repr__(self):
        """
        Returns the representation of all cards, with 
        each card separated by a space.
        """
        string=''
        for i in self.get_cards():
            string+=repr(i)+' '
        return string[:-1]
        

    def sort_hand(self):
        """
        Sorts the cards in ascending order.
        """
        rank_list=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        self.cards.sort(key=lambda x:rank_list.index(x.get_rank()),reverse=False)
        
    

class DealerHand(PlayerHand):
    
    def __init__(self):
        # This should inherit attributes from
        # the parent PlayerHand class.
        super().__init__()
        self.hand_visible=False



    def add_card(self, *cards):
        """
        Adds the cards to hand such that only the first card
        in the hand is visible (when the dealer's hand is not visible).
        If the dealer's hand is visible, then add cards to hand as 
        usual and sort them in ascending order.
        """
        assert all([isinstance(i,Card) for i in cards])
        if self.hand_visible==True:
            super().add_card(*cards)
        else:
            hi=[]
            for i in cards:
                hi.append(i)
            for x in hi:
                self.cards.append(x)
            self.cards[0].visible=True
            for i in self.cards[1:]:
                i.visible=False
            # for card in cards:
            #     self.cards.append(card)
            
            # for index,card in enumerate(self.cards):
            #     if index==0:
            #         card.set_visible(True)
            #     else:
            #         card.set_visible(False)



        

    
    def reveal_hand(self):
        """
        Makes all the cards in the hand visible
        and sorts them in ascending order.
        """
        for i in self.cards:
            i.visible=True
        super().sort_hand()
        
    
    
    