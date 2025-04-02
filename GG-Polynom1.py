from GG_Code_Sep_01 import *

from GG_List_Entry_01 import *

def main():
    import os
    import numpy as np
    import matplotlib.pyplot as plt

     # Clearing the Screen
    os.system('cls')
    n = int(input("Enter the number of elements: "))
     
    coefficients = gg_list_entry_int(n)
    sep_char('=')
    print("List:", coefficients)
    sep_char('=')

    # Create a polynomial object
    p = np.poly1d(coefficients)
    x_value = int(input("Enter x value: "))
    
    sep_char('=')
    print('Value of polynomial is: ', p(x_value))
    sep_char('=')

    plt.plot(coefficients)
    plt.show()
        
        
# Using the special variable 
# __name__
if __name__=="__main__":
    main()