#Dice Game
def roll_Dice():
    import random
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    print(type(dice1))
    print(type(dice2))
    return(dice1,dice2)

def display_Dice(dice):
    print(type(dice))
    print(dice)
    dice1,dice2= dice   #Unpack the tuple
    print("First Dice: " , dice1)
    print("Second Dice: ", dice2)
    if dice1 > dice2:
        print("Player 1 Won")
    elif dice1 < dice2:
        print("Player 2 won")
    else:
        print("Draw")


def main():
    import os
    # Clearing the Screen
    os.system('cls')

    print("Rolling the Dice...")
    m_dice = roll_Dice() # Pack into a tuple
    print(type(m_dice))  
    print("Displaying the Dice")
    display_Dice(m_dice)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
     
     