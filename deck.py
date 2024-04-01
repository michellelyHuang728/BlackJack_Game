from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, clubs), (2, diamonds), (2, hearts), (2, spades), (3, clubs)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, clubs), (Q, clubs), (10, clubs), (7, diamonds), (5, diamonds)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, clubs)
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        self.cards=[Card(i,j,visible=True) for i in [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] for j in ['clubs','diamonds','hearts','spades']]

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        # mongean_list=[]
        # for key,value in shuffle_and_count.items():
        #     if key==Shuffle.modified_overhand:
        #         self.cards=Shuffle.modified_overhand(self.cards, value)
        #     else:
        #         mongean_list.append(value)
        
        # for i in mongean_list:
        #     self.cards=Shuffle.mongean(self.cards)

        # modified_overhand_list=[]
        # mongean_list=[]
        # for key,value in shuffle_and_count.items():
        #     if key=='modified_overhand':
        #         modified_overhand_list.append(value)
        #     else:
        #         mongean_list.append(value)
        # for i in modified_overhand_list:
        #     self.cards=Shuffle.modified_overhand(self.cards, i)
        # for j in mongean_list:
        #     for k in range(j):
        #         self.cards=Shuffle.mongean(self.cards)


        # assert isinstance()
        modified_overhand_list=[]
        mongean_list=[]
        for key,value in shuffle_and_count.items():
            if key=='modified_overhand':
                modified_overhand_list.append((key,value))
            else:
                mongean_list.append((key,value))
        the_list=modified_overhand_list+mongean_list
        for i in the_list:
            if i[0]=='modified_overhand':
                self.cards=Shuffle.modified_overhand(self.cards, i[-1])
            # if i[0]=='mongean':
            else:
                for k in range(i[1]):
                    self.cards=Shuffle.mongean(self.cards)


        


    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert isinstance(hand,PlayerHand)
        first_card=self.cards[0]
        self.cards.remove(first_card)
        hand.add_card(first_card)
        #hand.sort_hand()

    def get_cards(self):
        return self.cards
