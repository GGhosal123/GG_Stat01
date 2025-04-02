# Guesssing Game

def gg_pick():
    import random
    m_pick = random.randint(1,10)
    #print(m_pick)
    return m_pick 

def main():
    import os
    
    # Clearing the Screen
    os.system('cls')
    v_pick = gg_pick()
    v_chances = 7

    v_guess_count = 0

    while v_guess_count <= v_chances :
        u_pick = int(input("Guess the number between 1 and 10 : "))
        if u_pick == v_pick:
            print ("Guess is correct.....")
            v_guess_count += 1
            break
            
        elif v_pick > u_pick:
            print("Your guess is Low ")
            v_guess_count += 1
        else:
            print("Your guess is High ")
            v_guess_count += 1

    if v_guess_count > v_chances :
       print("Exceeded the Allowed 7 Guesses")
       print("Better Luck next time...")
    else:
        print("No of Guess needed : ",v_guess_count )
            

# Using the special variable 
# __name__
if __name__=="__main__":
    main()