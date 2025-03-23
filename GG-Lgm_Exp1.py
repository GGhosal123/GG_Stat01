def sep_char(c):
    print (c * 60)

def main():
    import os
    import math
    

     # Clearing the Screen
    os.system('cls')
    my_base = int(input("Enter Base: "))
    my_input = int(input("Enter Input: "))

    my_output = math.log(my_input,my_base)
         
    sep_char('=')
    print('Logarithm: Base ',my_base,'  Input: ',my_input , ' Output: ' , my_output)
    sep_char('=')
    print('Exponential e: Input ',my_output , ' Output: ' , math.exp(my_output))
    sep_char('=')
    print('Exponential: Rate: ',my_base,' Input: ',my_output , ' Output: ' , my_base**my_output)
    sep_char('=')

       
        
# Using the special variable 
# __name__
if __name__=="__main__":
    main()