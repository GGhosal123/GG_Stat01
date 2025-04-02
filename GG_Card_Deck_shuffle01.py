# Card Deck Shuffle - This Program shuffles a deck of cards and distributes within 4 players

def Card_Deck():

    import random
    All_deck=[]
    
    deck_Hearts = ('HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK')
    deck_Spades = ('SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK')
    deck_Clubs = ('CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK')
    deck_Diamonds = ('DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK')

    All_deck = list(deck_Hearts + deck_Spades + deck_Clubs + deck_Diamonds)
    Shuffled_deck=[]

    for _ in range(52):  
        choice = random.choice(All_deck)  # Pick a random element  
        Shuffled_deck.append(choice)  
        All_deck.remove(choice)  # Remove chosen element to prevent repetition  

    print("Card Shuffle completed...")
    print(Shuffled_deck)
    
    return Shuffled_deck

def main():
    import os
    import random
    
    # Clearing the Screen
    os.system('cls')

    my_Deck = Card_Deck()
 
   # print (my_Deck)

    playerA_deck=[]
    playerB_deck=[]
    playerC_deck=[]
    playerD_deck=[]
    
    for i in range(1,14):
        playerA_deck.append(my_Deck.pop())
        playerB_deck.append(my_Deck.pop())
        playerC_deck.append(my_Deck.pop())
        playerD_deck.append(my_Deck.pop())

    print("Distribution completed...",end=" ")
    print(my_Deck)
    
    ##for i in range(1,14):
    ## playerx_deck.append(my_Deck.pop())

    print ('Player A Deck : ',playerA_deck)
    print ('Player B Deck : ',playerB_deck)
    print ('Player C Deck : ',playerC_deck)
    print ('Player D Deck : ',playerD_deck)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()