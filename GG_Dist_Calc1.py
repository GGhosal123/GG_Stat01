from GG_Code_Sep_01 import *

from math import *
from decimal import Decimal
from GG_List_Entry_01 import *

import numpy as np
import os

def show_list():
        # Clearing the Screen
    os.system('cls')

    sep_char("=")
    print (" DISTANCE CALCULATION METHODS " )
    sep_char("=")
    print (" 1. Minkowski Distance " )
    print (" 2. Manhattan Distance " )
    print (" 3. Euclidean Distance " )
    print (" 4. Chebyshev Distance " )
    print (" 5. Hamming Distance " )
    sep_char("=")

def p_root(value, root):
     
    root_value = 1 / float(root)
    return round (Decimal(value) **
             Decimal(root_value), 3)

def Minkowski_Calc_GG(x, y, p_value):
    #show_list()
    
    print (" (d(x,y) = |x1-y1|^p + |x2-y2|^p +....+|xn-yn|^p)^1/p ) " )
    sep_char("*")
    return (p_root(sum(pow(abs(a-b), p_value)
            for a, b in zip(x, y)), p_value))
 
        
def Manhatten_Calc_GG(point1,point2):
    #show_list()

    print(" the taxicab distance between two point (X1, Y1) and (X2,Y2) is" )
    print(" |x1-x2| + |y1-y2|" )
    sep_char("*")
    dist_manhatten = 0
    for x1, x2 in zip(point1, point2):
        difference = x2 - x1
        absolute_difference = abs(difference)
        dist_manhatten += absolute_difference
    return dist_manhatten
    
def Euclidian_Calc_GG(point1,point2):
    #show_list()

    print (" (d(x,y) = (|x1-y1|^2 + |x2-y2|^2 +....+|xn-yn|^2)^1/2 " )
    sep_char("*")    
    # finding sum of squares
    sum_sq = np.sum(np.square(point1 - point2))

    # Doing squareroot and
    # printing Euclidean distance
    dist_euclid = round(np.sqrt(sum_sq),3)
    return dist_euclid
   
def Chebyshev_Calc_GG(list1,list2):
    #show_list()

    print (" (d(x,y) = max{|x1-y1| + |x2-y2| +....+|xn-yn|})" )
    sep_char("*")

    from scipy.spatial import distance
    dist_Chebyshev = distance.chebyshev(list1,  list2)
    return(dist_Chebyshev)


def Hamming_Calc_GG(arr1,arr2):
    #show_list()

    print (" This method is used to obtain distance between two ")
    print( "strings of the same length. " )
    sep_char("*")

    from scipy.spatial.distance import hamming

    #calculate Hamming distance between the two arrays
    dist_hamming =(hamming(arr1, arr2) * len(arr1))
    return(dist_hamming)

def main():
    
    show_list()
    
    inp_distance_type = 0
    while int(inp_distance_type) < 6:
        sep_char("=")
        inp_distance_type = input(" Choose 1-5 for Choice of Distance Method- 9 to Exit " )
        sep_char("=")
            
        if (inp_distance_type == '1' ) :

            p=0
            print(" In Minkowski_Calc_GG ")
        # Get the number of elements
            n = int(input("Enter the number of elements: "))
            # Enter elements of list 1
            vector1 = gg_list_entry_int(n)
        # Enter elements of list 2
            vector2 = gg_list_entry_int(n)

            p = int(input(" Enter the Power " ))

            dist_Minkowski = Minkowski_Calc_GG(vector1, vector2, p)
            print("Minkowski Distance is : ",dist_Minkowski)
            
        elif (inp_distance_type == '2' ) :
            print(" In Manhatten_Calc_GG ")
        # Get the number of elements
            n = int(input("Enter the number of elements: "))
        # Enter elements of list 1
            list1 = gg_list_entry_int(n)

        # Enter elements of list 2
            list2 = gg_list_entry_int(n)

            man_dist = Manhatten_Calc_GG(list1,list2)
            print("Manhatten Distance is : ",man_dist)
        elif (inp_distance_type == '3' ) :
            print(" In Euclidian_Calc_GG ")
            import numpy as np
            # initializing points in
            # numpy arrays
            arr1 = np.array((1, 2, 3))
            arr2 = np.array((1, 1, 1))
            print("First array : ",arr1)
            print("Second array : ",arr2)
            euclid_dist = Euclidian_Calc_GG(arr1,arr2)
            print("Euclidian Distance is : ",euclid_dist)
        elif (inp_distance_type == '4' ) :
            print(" In Chebyshev_Calc_GG ")
          
        # Get the number of elements
            n = int(input("Enter the number of elements: "))
        # Enter elements of list 1
            list1 = gg_list_entry_int(n)

        # Enter elements of list 2
            list2 = gg_list_entry_int(n)

            chebyshev_dist = Chebyshev_Calc_GG(list1,list2)
            print("Chebyshev Distance is : ",chebyshev_dist)

        elif (inp_distance_type == '5' ) :
            print(" In Hamming_Calc_GG ")
           
            # Get the number of elements
            n = int(input("Enter the number of elements: "))
            list1 = gg_list_entry_char(n)
            list2 = gg_list_entry_char(n)
            hamm_dist = Hamming_Calc_GG(list1,list2)
            print("Hamming Distance is : ",hamm_dist)
        else :
            sep_char("*")
            print("Exiting Program.....")
            sep_char("*")
            exit

# Using the special variable 
# __name__
if __name__=="__main__":
    main()

    
