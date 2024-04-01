class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25



    """    
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        assert isinstance(num,int)
        #assert all(isinstance(i, Card) for i in cards)
        if num==0:
            return cards
        else:
            if len(cards)%2==0:
                if num%2==0:
                    new_list1=cards[(len(cards)//2-num//2):(len(cards)//2+num//2)]
                    new_list2=cards[0:(len(cards)//2-num//2)]
                    new_list3=cards[(len(cards)//2+num//2):]
                    cards=new_list1+new_list2+new_list3
                    return Shuffle.modified_overhand(cards,num-1)
                else:
                    new_list1=cards[(len(cards)//2-(num+1)//2):(len(cards)//2+(num-1)//2)]
                    new_list2=cards[0:(len(cards)//2-(num+1)//2)]
                    new_list3=cards[(len(cards)//2+(num-1)//2):]
                    cards=new_list1+new_list2+new_list3
                    return Shuffle.modified_overhand(cards,num-1)

            else:
                if num%2==0:
                    new_list1=cards[(len(cards)-1)//2]
                    new_list2=cards[((len(cards)-1)//2-(num+1)//2):((len(cards)-1)//2)]
                    new_list3=cards[((len(cards)+1)//2):((len(cards)+1)//2+(num+1)//2-1)]
                    new_list4=cards[0:((len(cards)-1)//2-(num+1)//2)]
                    new_list5=cards[((len(cards)+1)//2+(num+1)//2)-1:]
                    cards=new_list2+[new_list1]+new_list3+new_list4+new_list5
                    return Shuffle.modified_overhand(cards,num-1)
                else:
                    #new_list1=cards[(len(cards)-1)//2]
                    new_list2=cards[((len(cards)-1)//2-num//2):((len(cards)-1)//2+num//2+1)]
                    new_list4=cards[0:((len(cards)-1)//2-num//2)]
                    new_list5=cards[((len(cards)+1)//2+(num//2-1)):]
                    cards=new_list2+new_list4+new_list5
                    return Shuffle.modified_overhand(cards,num-1)

        # if num==0:
        #     return cards
        # else:
        #     if len(cards)%2==0:
        #         if num%2==0:
        #             new_list1=cards[(len(cards)//2-num//2):(len(cards)//2+num//2)]
        #             new_list2=cards[0:(len(cards)//2-num//2)]
        #             new_list3=cards[(len(cards)//2+num//2):]
        #             return Shuffle.modified_overhand(new_list1+new_list2+new_list3,num-1)
        #         else:
        #             new_list1=cards[(len(cards)//2-(num+1)//2):(len(cards)//2+(num-1)//2)]
        #             new_list2=cards[0:(len(cards)//2-(num+1)//2)]
        #             new_list3=cards[(len(cards)//2+(num-1)//2):]
        #             return Shuffle.modified_overhand(new_list1+new_list2+new_list3,num-1)

        #     else:
        #         if num%2==0:
        #             new_list1=cards[(len(cards)-1)//2]
        #             new_list2=cards[(len(cards-1)//2-num//2):(len(cards-1)//2)]
        #             new_list3=cards[(len(cards+1)//2):(len(cards+1)//2+(num//2-1))]
        #             new_list4=cards[0:(len(cards-1)//2-num//2)]
        #             new_list5=cards[(len(cards+1)//2+(num/2-1)):]
        #             return Shuffle.modified_overhand(new_list1+new_list2+new_list3+new_list4+new_list5,num-1)
        #         else:
        #             new_list1=cards[(len(cards)-1)//2]
        #             new_list2=cards[(len(cards-1)//2-(num+1)//2):(len(cards-1)//2)]
        #             new_list3=cards[(len(cards+1)//2):(len(cards+1)//2+(num+1)//2)]
        #             new_list4=cards[0:(len(cards-1)//2-(num+1)//2)]
        #             new_list5=cards[(len(cards+1)//2+(num+1)//2):]
        #             return Shuffle.modified_overhand(new_list1+new_list2+new_list3+new_list4+new_list5,num-1)





        # if num==0:
        #     return cards
        # else:
        #     if len(cards)%2==0 and num%2!=0:
        #         the_index=int(len(cards)/2-1)
        #         if num==1:
        #             num_taken_top=round(num/2)
        #             num_taken_bottom=round(num/2)
        #             extracted=[cards[the_index]]
        #         else:
        #             num_taken_top=round(num/2)
        #             num_taken_bottom=round(num/2)-1
        #             extracted=cards[the_index-num_taken_top+1:the_index+1]+cards[the_index+1:the_index+num_taken_bottom+1]
        #         [cards.remove(i) for i in extracted]
        #         new_cards=extracted+cards
        #         return Shuffle.modified_overhand(new_cards, num-1)
        #     elif len(cards)%2==0 and num%2==0:
        #         x=int((len(cards)-num)/2)
        #         remainder3=cards[0:x]+cards[x+num:]
        #         extracted4=cards[x:x+num]
        #         new_cards_3=extracted4+remainder3
        #         return Shuffle.modified_overhand(new_cards_3,num-1)
        #     elif len(cards)%2!=0 and num%2!=0:
        #         y=int((len(cards)-num)/2)
        #         remainder4=cards[0:y]+cards[y+num:]
        #         extracted5=cards[y:y+num]
        #         new_cards_4=extracted5+remainder4
        #         return Shuffle.modified_overhand(new_cards_4,num-1)
        #     elif len(cards)%2!=0 and num%2==0:
        #         extracted2=[]
        #         median=round(len(cards)/2)
        #         extracted2.append(cards[median])
        #         cards.remove(cards[median])
        #         num=num-1
        #         new_median=int(len(cards)/2-1)
        #         extracted3=cards[new_median-(num-1):new_median+1]
        #         [cards.remove(i)for i in cards if i in extracted3 ]
        #         new_cards_2=extracted3+extracted2+cards
        #         return Shuffle.modified_overhand(new_cards_2, num)
                    
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        
        # list=[]
        # for i in enumerate(cards):
        #     if i[0]%2==0:
        #         list=list+[i]
        #     else:
        #         list=[i]+list
        # return [i[1] for i in list]

        # card_seq=enumerate(cards)
        # if len(card_seq)==0:
        #     return []
        # else:
        #     if len(cards)%2==0:
        #         return card_seq[0]+Shuffle.mongean(cards[::-1])
        #     else:
        #         return Shuffle.mongean(cards[:-1])+cards[-1]
        
        if len(cards)==0:
            return []
        if len(cards)==1:
            return [cards[0]]
        else:
            return [cards[-1]]+Shuffle.mongean(cards[:-2])+[cards[-2]]



        

        
            
        
    