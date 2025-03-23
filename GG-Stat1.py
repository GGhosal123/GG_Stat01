
############# Function for Calculation of Mean ########
def mean_calc():
    import statistics
    ctr = 0
    total = 0
    mean_val=0
    nos_list = []
    ans ="N"
        
    while True:
        nos = float(input ('Enter number to calculate Mean: ' ))
        nos_list.append(nos)

        total = total + nos
        ctr+=1
        ans = str(input('Exit now ? - Enter Y or y to Exit , Skip to continue '))
        
        if ans == "Y" or ans == "y":
            break
        
    #mean_val = total/ctr
    mean_val = statistics.mean(nos_list)

    return mean_val
    ###print("Mean value is ",str(mean_val))

############# Function for Calculation of Varaince ########
def variance_calc():
    import statistics
    import numpy as np
    ctr = 0
    total = 0
    ans ="N"
    nos_list = []
    mean_val=0
        
    while True:
        nos = float(input ('Enter numbers to calculate Variance : ' ))
        nos_list.append(nos)
        total = total + nos
        ctr+=1
        ans = str(input('Exit now ? - Enter Y or y to Exit , Skip to continue '))
        
        if ans == "Y" or ans == "y":
            break

    #mean_val = total/ctr    
    mean_val = statistics.mean(nos_list)

    print("The numbers entered are " ,nos_list[0:])

    n = len(nos_list)
    print("Total number of element entered is ", n )
    print("Mean:" , mean_val)

    tot_a = 0
    my_var1=0
    for i in range(n-1):
        a = nos_list[i]
        tot_a += (a - mean_val) ** 2
        print(f'{tot_a:>10.2f}')

    my_var1= tot_a/(n-0)

    my_variance = round(my_var1,3)


   # my_variance = round(np.sqrt(my_var1),3)

    #my_variance = statistics.variance(nos_list)

    return my_variance
    
############# Main starts Here########

if __name__== "__main__":

    import os
    os.system('cls')

    print("******************************************")
    print("1. Mean ")
    print("2. Variance ")
    print("******************************************")

    my_choice = int(input("Enter your Choice " ))

    if my_choice==1:
        my_mean = mean_calc()
        print("*********************")
        print("Mean value is: ",end=' ')
        print(f'{my_mean:>10.2f}')
        print("*********************")
    elif my_choice==2:
        my_variance = variance_calc()
        print("*********************")
        print("Variance is: ",end=' '),
        print(f'{my_variance:>10.2f}')
        print("*********************")
        

