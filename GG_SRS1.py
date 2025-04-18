#Simple Random Sampling

from GG_List_Entry_01 import *

from GG_Code_Sep_01 import *

def srswor(m_list,m_sample_size):
    # Import permutations from itertools
    from itertools import permutations
    # Import combinations from itertools
    from itertools import combinations
    #from math import comb
    
    print("Simple Random Sampling without Replacement")

    m_element_count =len(m_list)**m_sample_size
    
    # Get all permutations of length 2 
    perm = permutations(m_list, m_sample_size) 
    comb = combinations(m_list, m_sample_size) 

 
    # Print the obtained permutations 
    sep_char('=')
    print ("Replacement=No - Ordered=Yes")
    print("Total number of elements:" ,m_element_count - len(m_list) )
    sep_char('=')
    cnt = 0
    for i in list(perm): 
        cnt +=1
        print (cnt,end=' ')
        print (i) 

        # Print the obtained permutations 
    sep_char('=')
    print ("Replacement=No - Ordered=No")
    print("Total number of elements:" ,m_element_count )
    sep_char('=')
    cnt = 0
    for j in list(comb): 
        x,y= j
       # print(x)
        #print(y)
        if x != y:
            cnt +=1
            print (cnt,end=' ')
            print (j) 
        

    
def main():
    import os
    from GG_List_Entry_01 import gg_list_entry_str
    
     # Clearing the Screen
    os.system('cls')
    n = int(input("Enter the number of elements: "))
     
    population_str = gg_list_entry_str(n)
    sep_char('=')
    print("List:", population_str)
    sep_char('=')

    sample_size = int(input("Enter Sample Size: "))
    srswor(population_str,sample_size)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()