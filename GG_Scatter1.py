def sep_char(c):
    print (c * 60)

def main():
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    os.system('cls')
    # read by default 1st sheet of an excel file
    df = pd.read_excel('Python-Test-Excel1.xlsx','BP-Age')
    df.fillna(value='')
   
    sep_char('=')
    print(df)
    sep_char('=')

    my_age = pd.read_excel('Python-Test-Excel1.xlsx','BP-Age',usecols=['Age'])
    my_Systolic_BP = pd.read_excel('Python-Test-Excel1.xlsx','BP-Age',usecols=['Systolic BP'])

    plt.xlabel('Age')
    plt.ylabel('Systolic BP')
    plt.title('Comparison of Age vs Systolic BP')

    plt.scatter(my_age, my_Systolic_BP,edgecolors='b',linewidths=2)
    
    plt.show()

    df = pd.read_excel('Python-Test-Excel1.xlsx','Walk-BP')
    df.fillna(value='')
   
    sep_char('=')
    print(df)
    sep_char('=')


    my_BP = pd.read_excel('Python-Test-Excel1.xlsx','Walk-BP',usecols=['BP'])
    my_walk = pd.read_excel('Python-Test-Excel1.xlsx','Walk-BP',usecols=['Duration of Walk'])

    plt.xlabel('Duration of Walk')
    plt.ylabel('Systolic BP')
    plt.title('Comparison of BP vs Duration of Walk')

    plt.scatter(my_walk, my_BP,edgecolors='b',linewidths=2)
    
    plt.show()

# Using the special variable 
# __name__
if __name__=="__main__":
    main()