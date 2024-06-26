#from selectors import EpollSelector
from deck import Deck
from hand import DealerHand, PlayerHand
from card import Card

# don't change these imports
from numpy.random import randint, seed
seed(20)

class Blackjack:
    """
    Game of blackjack!

    # Removes the game summaries from the previous doctest run
    >>> from os import remove, listdir
    >>> for f in listdir("game_summaries"):
    ...    remove("game_summaries/" + f)

    #######################################
    ### Doctests for calculate_score() ####
    #######################################
    >>> card_1 = Card("A", "diamonds")
    >>> card_2 = Card("J", "spades")
    >>> hand_1 = PlayerHand()
    >>> Blackjack.calculate_score(hand_1)
    0
    >>> hand_1.add_card(card_1)
    >>> Blackjack.calculate_score(hand_1) # (Ace)
    11
    >>> hand_1.add_card(card_2)
    >>> Blackjack.calculate_score(hand_1) # (Ace, Jack)
    21

    >>> card_3 = Card("A", "spades")
    >>> hand_2 = PlayerHand()
    >>> hand_2.add_card(card_1, card_3)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace)
    12
    >>> hand_2.add_card(card_2)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace, Jack)
    12

    >>> hand_3 = PlayerHand()
    >>> card_4 = Card(2, "spades")
    >>> card_5 = Card(4, "spades")
    >>> hand_3.add_card(card_4, card_5)
    >>> Blackjack.calculate_score(hand_3)
    6

    #######################################
    ### Doctests for determine_winner() ####
    #######################################
    >>> blackjack = Blackjack(10)
    >>> blackjack.determine_winner(10, 12)
    -1
    >>> blackjack.determine_winner(21, 21)
    0
    >>> blackjack.determine_winner(22, 23)
    0
    >>> blackjack.determine_winner(12, 2)
    1
    >>> blackjack.determine_winner(22, 2)
    -1
    >>> blackjack.determine_winner(2, 22)
    1
    >>> print(blackjack.get_log())
    Player lost with a score of 10. Dealer won with a score of 12.
    Player and Dealer tie.
    Player and Dealer tie.
    Player won with a score of 12. Dealer lost with a score of 2.
    Player lost with a score of 22. Dealer won with a score of 2.
    Player won with a score of 2. Dealer lost with a score of 22.
    <BLANKLINE>  
    >>> blackjack.reset_log()

    #######################################
    ### Doctests for play_round() #########
    #######################################
    >>> blackjack_2 = Blackjack(10)
    >>> blackjack_2.play_round(1, 15)
    >>> print(blackjack_2.get_log())
    Round 1 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (10, clubs) (A, clubs)
    Dealer Cards: (Q, clubs) (?, ?)
    Dealer Cards Revealed: (7, diamonds) (Q, clubs)
    Player won with a score of 21. Dealer lost with a score of 17.
    <BLANKLINE>
    >>> blackjack_2.reset_log()
   
    >>> blackjack_2.play_round(3, 21)
    >>> print(blackjack_2.get_log())
    Round 2 of Blackjack!
    wallet: 15
    bet: 5
    Player Cards: (4, clubs) (7, clubs)
    Dealer Cards: (A, hearts) (?, ?)
    Player pulled a (J, hearts)
    Dealer Cards Revealed: (5, clubs) (A, hearts)
    Dealer pulled a (6, clubs)
    Dealer pulled a (2, clubs)
    Dealer pulled a (8, clubs)
    Player won with a score of 21. Dealer lost with a score of 22.
    Round 3 of Blackjack!
    wallet: 20
    bet: 10
    Player Cards: (6, hearts) (9, diamonds)
    Dealer Cards: (K, hearts) (?, ?)
    Player pulled a (Q, hearts)
    Dealer Cards Revealed: (J, diamonds) (K, hearts)
    Player lost with a score of 25. Dealer won with a score of 20.
    Round 4 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (5, diamonds) (10, diamonds)
    Dealer Cards: (2, diamonds) (?, ?)
    Player pulled a (3, diamonds)
    Player pulled a (7, spades)
    Dealer Cards Revealed: (2, diamonds) (2, hearts)
    Dealer pulled a (K, spades)
    Dealer pulled a (3, spades)
    Player lost with a score of 25. Dealer won with a score of 17.
    <BLANKLINE>
    
    >>> with open("game_summaries/game_summary2.txt", encoding = 'utf-8') as f:
    ...     lines = f.readlines()
    ...     print("".join(lines[10:26]))
    Dealer Hand:
    ____
    |7  |
    | ♦ |
    |__7|
    ____
    |Q  |
    | ♣ |
    |__Q|
    Winner of ROUND 1: Player
    <BLANKLINE>
    ROUND 2:
    Player Hand:
    ____
    |4  |
    | ♣ |
    <BLANKLINE>

    >>> blackjack_3 = Blackjack(5)
    >>> blackjack_3.play_round(5, 21)
    >>> print(blackjack_3.get_log())
    Round 1 of Blackjack!
    wallet: 5
    bet: 5
    Player Cards: (2, clubs) (2, hearts)
    Dealer Cards: (2, diamonds) (?, ?)
    Player pulled a (3, clubs)
    Player pulled a (3, diamonds)
    Player pulled a (3, hearts)
    Player pulled a (3, spades)
    Player pulled a (4, clubs)
    Player pulled a (4, diamonds)
    Dealer Cards Revealed: (2, diamonds) (2, spades)
    Dealer pulled a (4, hearts)
    Dealer pulled a (4, spades)
    Dealer pulled a (5, clubs)
    Player lost with a score of 24. Dealer won with a score of 17.
    Wallet amount $0 is less than bet amount $5.

    >>> blackjack_4 = Blackjack(500)
    >>> blackjack_4.play_round(13, 21) # At least 52 cards will be dealt
    >>> blackjack_4.reset_log()
    >>> blackjack_4.play_round(1, 17)
    >>> print(blackjack_4.get_log())
    Not enough cards for a game.
    """
    # Class Attribute(s)
    game_number=0
    round_number=0

    def __init__(self, wallet):
        # Initialize instance attributes
        # auto-increment as needed

        # assert isinstance(self.deck, Deck)
        # assert isinstance(self.deck, int or float)
        # assert isinstance(self.game_number, int)
        # assert isinstance(self.log, str)
        # self.wallet=wallet
        # self.deck=Deck()
        # self.game_number=1
        # self.log=''
        self.wallet=wallet
        Blackjack.game_number+=1
        self.log=''
        #self.round_number=1
        self.deck=Deck()
        #self.player_hand=PlayerHand()
        #self.dealer_hand=DealerHand()
        
    
    def play_round(self, num_rounds, stand_threshold):
        """
        Plays `num_rounds` Blackjack rounds.

        Parameters:
            num_rounds (int): Number of rounds to play.
            stand_threshold (int): Score threshold for when the player
            will stand (ie player stands if they have a score >= 
            this threshold)
        """
        # This could get pretty long!
        assert isinstance(stand_threshold, int)
        assert isinstance(num_rounds, int)
        # version2
        bet=5
        for i in range(num_rounds):
            player_hand=PlayerHand()
            dealer_hand=DealerHand()
            if len(self.deck.cards)<4:
                self.log+="Not enough cards for a game."
                break
            else:
                if bet>self.wallet:
                    self.log+='Wallet amount '+'$'+str(self.wallet)+' is less than bet amount '+'$'+str(bet)+'.'
                    break
                else:
                    self.round_number+=1
                    self.log+='Round '+str(self.round_number)+' of Blackjack!'+'\n'
                    self.log+='wallet: '+str(self.wallet)+'\n'
                    self.log+='bet: '+str(bet)+'\n'

                    mongean_num=randint(0,6)
                    overhand_num=randint(0,6)
                    self.deck.shuffle(mongean=mongean_num, modified_overhand=overhand_num)

                    self.deck.deal_hand(player_hand)
                    self.deck.deal_hand(dealer_hand)
                    self.deck.deal_hand(player_hand)
                    self.deck.deal_hand(dealer_hand)

                    self.log+='Player Cards: '+player_hand.__repr__()+'\n'
                    self.log+='Dealer Cards: '+dealer_hand.__repr__()+'\n'
            
                    self.hit_or_stand(player_hand, stand_threshold)
                    dealer_hand.reveal_hand()
                    self.log+='Dealer Cards Revealed: '  +dealer_hand.__repr__()+'\n'
                    self.hit_or_stand(dealer_hand, 17)

                    # self.round_number+=1
                    win_or_not=Blackjack.determine_winner(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand))
                    if win_or_not==1:
                        self.wallet+=bet
                        bet+=5
                        # Blackjack.add_to_file(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand),1)
                    elif win_or_not==0:
                        self.wallet=self.wallet
                        bet=bet
                        # Blackjack.add_to_file(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand),0)
                    else:
                        self.wallet-=bet
                        bet-=5
                        if bet < 5:
                            bet = 5
                        # Blackjack.add_to_file(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand),-1)
                    
                    Blackjack.add_to_file(self, player_hand, dealer_hand,win_or_not)
                    


        #     if Blackjack.calculate_score(player_hand)>=stand_threshold:
        #         if Blackjack.determine_winner(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand))==1:
        #             self.wallet+=self.wallet
        #             self.bet+=5
        #             self.round_number+=1
        #             Blackjack.add_to_file(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand),1)
        #         elif Blackjack.determine_winner(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand))==0:
        #             self.wallet=self.wallet
        #             self.bet=self.bet
        #             self.round_number+=1
        #             Blackjack.add_to_file(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand),0)
        #         elif Blackjack.determine_winner(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(self.dealer_hand))==-1:
        #             self.wallet-=self.bet
        #             self.bet-=5
        #             self.round_number+=1
        #             Blackjack.add_to_file(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand),-1)
        #         continue
        #     dealer_hand.reveal_hand()
        #     self.log+='Dealer Cards Revealed: '+self.dealer_hand
        #     if Blackjack.calculate_score(dealer_hand)>=17:
        #         if Blackjack.determine_winner(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand))==1:
        #             self.wallet+=self.wallet
        #             self.bet+=5
        #             self.round_number+=1
        #             Blackjack.add_to_file(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand),1)
        #         elif Blackjack.determine_winner(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand))==0:
        #             self.wallet=self.wallet
        #             self.bet=self.bet
        #             self.round_number+=1
        #             Blackjack.add_to_file(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand),0)
        #         elif Blackjack.determine_winner(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand))==-1:
        #             self.wallet-=self.bet
        #             self.bet-=5
        #             self.round_number+=1
        #             Blackjack.add_to_file(self, Blackjack.calculate_score(player_hand), Blackjack.calculate_score(dealer_hand),-1)
        #         break
            
    def calculate_score(hand):
        """
        Calculates the score of a given hand. 

        Sums up the ranks of each card in a hand. Jacks, Queens, and Kings
        have a value of 10 and Aces have a value of 1 or 11. The value of each
        Ace card is dependent on which value would bring the score closer
        (but not over) 21. 

        Should be solved using list comprehension and map/filter. No explicit
        for loops.

        Parameters:
            hand: The hand to calculate the score of.
        Returns:
            The best score as an integer value.
        """
        # sum=0
        # ace_count=0
        # for i in hand.get_cards():
        #     if i.rank=='J' or i.rank=='Q' or i.rank=='K':
        #         sum+=10
        #     elif i.rank in [2,3,4,5,6,7,8,9]:
        #         sum+=i.rank
        #     elif i.rank=='A':
        #         ace_count+=1
        
        # if ace_count+sum>21:
        #     return sum+ace_count
        # else:
        #     while sum
        assert isinstance(hand,PlayerHand)
        rank_list=list(map(lambda x:x.rank,hand.get_cards()))
        list_A=list(filter(lambda x:x=='A',rank_list))
        sum_digit=sum([i for i in rank_list if type(i)==int])
        sum_JQK=sum([10 for i in rank_list if i=='J' or i=='Q' or i=='K'])
        if 'A' in rank_list:
            # before_A1=sum([i for i in rank_list[:rank_list.index('A')] if type(i)==int])
            # before_A2=sum([10 for i in rank_list[:rank_list.index('A')] if i=='J' or i=='Q' or i=='K'])
            if sum_digit+sum_JQK<=10 and len(list_A)==1:
                return sum_digit+sum_JQK+11+(len(list_A)-1)*1
            elif sum_digit+sum_JQK>10 and len(list_A)==1:
                return sum_digit+sum_JQK+len(list_A)
            elif sum_digit+sum_JQK<=9 and len(list_A)==2:
                return sum_digit+sum_JQK+11+(len(list_A)-1)*1
            elif sum_digit+sum_JQK>9 and len(list_A)==2:
                return sum_digit+sum_JQK+len(list_A)
            elif sum_digit+sum_JQK<=8 and len(list_A)==3:
                return sum_digit+sum_JQK+11+(len(list_A)-1)*1
            elif sum_digit+sum_JQK>8 and len(list_A)==3:
                return sum_digit+sum_JQK+len(list_A)
            elif sum_digit+sum_JQK<=7 and len(list_A)==4:
                return sum_digit+sum_JQK+11+(len(list_A)-1)*1
            elif sum_digit+sum_JQK>7 and len(list_A)==4:
                return sum_digit+sum_JQK+len(list_A)
        else:
            return sum_digit+sum_JQK
        # return sum_digit+sum_JQK+sum_A
        
        
        # if 'A' in rank_list:
        #     index_A=rank_list.index('A')
        # return index_A
        # sum=[]
        # for i in hand.get_cards():
        #     if i.rank=='J' or i.rank=='Q' or i.rank=='K':
        #         sum+=10
        #     elif i.rank=='A':
        #         index=hand.get_cards.index('A')
        #         if sum(list(filter(lambda x: <index)))
        # index=hand.get_cards.index('A')
        #return [hand.get_cards().index(i) for i in hand.get_cards()]
        
            
            

    def determine_winner(self, player_score, dealer_score):
        """
        Determine whether the Blackjack round ended with a tie, dealer winning, 
        or player winning. Update the log to include the winner and
        their scores before returning.

        Returns:
            1 if the player won, 0 if it is a tie, and -1 if the dealer won
        """


        if player_score<=21:
            if dealer_score>21:
                self.log+='Player won with a score of '+str(player_score)+'. '+'Dealer lost with a score of '+str(dealer_score)+'.\n'
                return 1
            else:
                if player_score>dealer_score:
                    self.log+='Player won with a score of '+str(player_score)+'. '+'Dealer lost with a score of '+str(dealer_score)+'.\n'
                    return 1
                elif player_score==dealer_score:
                    self.log+='Player and Dealer tie.\n'
                    return 0
                else:
                    self.log+='Player lost with a score of '+str(player_score)+'. '+'Dealer won with a score of '+str(dealer_score)+'.\n'
                    return -1
        else:
            if dealer_score>21:
                self.log+='Player and Dealer tie.\n'
                return 0
            else:
                self.log+='Player lost with a score of '+str(player_score)+'. '+'Dealer won with a score of '+str(dealer_score)+'.\n'
                return -1


                    

        # if dealer_score>21 or (abs(player_score-21)<abs(dealer_score-21)):
        #     self.log+='Player won with a score of'+str(player_score)+'.'+'Dealer lost with a score of '+str(dealer_score)+'.\n'
        #     return 1
        # if player_score>21 or (abs(player_score-21)>abs(dealer_score-21)):
        #     self.log+='Player lost with a score of '+str(player_score)+'.'+'Dealer won with a score of '+str(dealer_score)+'.\n'
        #     return -1
        # if player_score==dealer_score:
        #     self.log+='Player and Dealer tie.\n'
        #     return 0
        # if player_score>21 and dealer_score>21:
        #     self.log+='Player and Dealer tie.\n'
        #     return 0

        # if player_score>21 and dealer_score>21 or player_score==dealer_score:
        #     self.log+='Player and Dealer tie.\n'
        # if player_score<=21 and dealer_score>21:
        #     return 
        # elif player_score>21 and dealer_score<=21:
        # else:

        # if player_score>21 and dealer_score>21 or player_score==dealer_score:
        #     self.log+='Player and Dealer tie.\n'
        #     return 0
        # elif (dealer_score>21 and player_score<=21) or (player_score>dealer_score and player_score<21):
        #     self.log+='Player won with a score of '+str(player_score)+'. '+'Dealer lost with a score of '+str(dealer_score)+'.\n'
        #     return 1
        # else:
        #     self.log+='Player lost with a score of '+str(player_score)+'. '+'Dealer won with a score of '+str(dealer_score)+'.\n'
        #     return -1



        # if player_score>21 and dealer_score>21:
        #     self.log+='Player and Dealer tie.\n'
        #     return 0
        # elif player_score==dealer_score:
        #     self.log+='Player and Dealer tie.\n'
        #     return 0

        # elif dealer_score>21 and player_score<=21:
        #     self.log+='Player won with a score of '+str(player_score)+'. '+'Dealer lost with a score of '+str(dealer_score)+'.\n'
        #     return 1
        # elif player_score>21 and dealer_score<=21:
        #     self.log+='Player lost with a score of '+str(player_score)+'. '+'Dealer won with a score of '+str(dealer_score)+'.\n'
        #     return -1
        # elif player_score<=21 and dealer_score<=21:
        #     if (abs(player_score-21)<abs(dealer_score-21)):
        #         self.log+='Player won with a score of '+str(player_score)+'. '+'Dealer lost with a score of '+str(dealer_score)+'.\n'
        #         return 1
        #     elif (abs(player_score-21)>abs(dealer_score-21)):
        #         self.log+='Player lost with a score of '+str(player_score)+'. '+'Dealer won with a score of '+str(dealer_score)+'.\n'
        #         return -1

    def hit_or_stand(self, hand, stand_threshold):
        """
        Deals cards to hand until the hand score has reached or surpassed
        the `stand_threshold`. Updates the log everytime a card is pulled.

        Parameters:
            hand: The hand the deal the cards to depending on its score.
            stand_threshold: Score threshold for when the player
            will stand (ie player stands if they have a score >= 
            this threshold).
        """
        # score=Blackjack.calculate_score(hand)
        # if isinstance(hand, DealerHand):
        #     hand.reveal_hand()
        #     while len(self.deck.cards2)>0 and score<17:
        #         self.deck.deal_hand(hand)
        #         self.log+='Dealer pulled a '+repr(self.deck.get_cards[0])+'\n'
        #         score=Blackjack.calculate_score(hand)
        # else:
        #     while len(self.deck.cards2)>0 and score<stand_threshold:
        #         self.deck.deal_hand(hand)
        #         self.log+='Player pulled a '+repr(self.deck.get_cards[0])+'\n'
        #         score=Blackjack.calculate_score(hand)
        
        #no me
        # score=Blackjack.calculate_score(hand)
        # if isinstance(hand,DealerHand)==True:
        #     Name='Dealer'
        # else:
        #     Name='Player'
        # while score< stand_threshold and len(self.deckget_cards())>0:
        #     self.log+='{} pulled a {}\n'.format(Name, repr(self.deck.get_cards[0]))


        score=Blackjack.calculate_score(hand)
        if isinstance(hand,DealerHand)==True:
            while len(self.deck.cards)>0 and score<stand_threshold:
                self.log+='Dealer pulled a '+repr(self.deck.get_cards()[0])+'\n'
                self.deck.deal_hand(hand)
                score=Blackjack.calculate_score(hand)
        else:
            while len(self.deck.cards)>0 and score<stand_threshold:
                self.log+='Player pulled a '+repr(self.deck.get_cards()[0])+'\n'
                self.deck.deal_hand(hand)
                score=Blackjack.calculate_score(hand)


        # while len(self.deck)!=0 and self.calculate_score()<stand_threshold:
        #     if isinstance(hand, PlayerHand):
        #         self.log+=
        # while len(self.deck.cards)!=0 and self.calculate_score(hand)<stand_threshold:
        #     self.deck.deal_hand(hand)
        #     if isinstance(hand, PlayerHand):
        #         self.log+='Player pulled a '+'('+str()




        # for i in self.deck.cards2:
        #     self.deck.deal_hand(hand)
        #     if isinstance(hand, DealerHand):
        #         hand.reveal_hand()
        #         self.log+='Dealer pulled a '+hand.cards[-1].__repr__()+'\n'
        #         if self.deck.cards2==[] or Blackjack.calculate_score(hand)>=17:
        #             break
        #     else:
        #         self.log+='Player pulled a '+hand.cards[-1].__repr__()+'\n'
        #         if len(self.deck.cards2)==0 or Blackjack.calculate_score(hand)>stand_threshold:
        #             break

        # print("AAAA")
        # print(self.log)
        # print("AAA")

    def get_log(self):
        return self.log
    
    def reset_log(self):
        self.log=''
        
        
    def add_to_file(self, player_hand, dealer_hand, result):
        """
        Writes the summary and outcome of a round of Blackjack to the 
        corresponding .txt file. This file should be named game_summaryX.txt 
        where X is the game number and it should be in `game_summaries` 
        directory.
        """
        
        # Remember to use encoding = "utf-8" 
        # with open('./game_summaries/game_summary'+str(self.game_number)+'.txt','a', encoding='utf-8') as f:
        #     f.write('ROUND '+str(self.game_number)+':'+'\n'+'Player Hand:'+'\n'+player_hand.__str__()+'\n'+'Dealer Hand:'+'\n'+dealer_hand.__str__())
        #     if result==1:
        #         f.write('Winner of ROUND{}: Player'.format(self.round_number))
        #     if result==0:
        #         f.write('Winner of ROUND{}: Tied'.format(self.round_number))
        #     if result==-1:
        #         f.write('Winner of ROUND{}: Dealer'.format(self.round_number))

        # with open('./game_summaries/game_summary'+str(self.game_number)+'.txt','a+', encoding='utf-8') as f:
        #     # f.write('ROUND '+str(self.game_number)+':'+'\n'+'Player Hand:'+'\n'+player_hand.__str__()+'\n'+'Dealer Hand:'+'\n'+dealer_hand.__str__()+'\n')
        #     if result==1:
        #         f.write('ROUND '+str(self.round_number)+':'+'\n'+'Player Hand:\n'+player_hand.__str__()+'\n'+'Dealer Hand:'+'\n'+dealer_hand.__str__()+'\n'+'Winner of ROUND '+str(self.round_number)+': Player'+'\n'+'\n')
        #     if result==0:
        #         f.write('ROUND '+str(self.round_number)+':'+'\n'+'Player Hand:\n'+player_hand.__str__()+'\n'+'Dealer Hand:'+'\n'+dealer_hand.__str__()+'\n'+'Winner of ROUND '+str(self.round_number)+': Tied'+'\n'+'\n')
        #     if result==-1:
        #         f.write('ROUND '+str(self.round_number)+':'+'\n'+'Player Hand:\n'+player_hand.__str__()+'\n'+'Dealer Hand:'+'\n'+dealer_hand.__str__()+'\n'+'Winner of ROUND '+str(self.round_number)+': Dealer'+'\n'+'\n')

# blackjack_2 = Blackjack(10)
# blackjack_2.play_round(3, 15)
# blackjack_2.get_log()

blackjack_2 = Blackjack(10)
blackjack_2.play_round(1, 15)
blackjack_2.get_log()
blackjack_2.reset_log()
blackjack_2.play_round(3, 21)
blackjack_2.get_log()
