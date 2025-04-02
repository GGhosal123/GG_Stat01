from GG_Code_Sep_01 import *

sep_char("#")
inp_chart_type = input(" Select Data Pattern (D-Discrete C-Continous) " )
sep_char("#")
    
if (inp_chart_type == "C" ) :
    sep_char("#")
    print(" Type selected is Continous ")
    inp_Mul_Sin = input(" Select M - Multiple Data Point S - Single Data Point " )
    if inp_Mul_Sin == "M":
        sep_char("#")
        print (" Chart Type is X-Bar or X Bar R ")
        sep_char("#")
        inp_XBR = input(" Display Range - Y/N ")
        if inp_XBR == "Y" :
            sep_char("#")
            print(" Chart Type is XBar R ")
            sep_char("#")
        else :
            sep_char("#")
            print(" Chart Type is XBar " )
            sep_char("#")
    else :
            sep_char("#")
            print ("Chart Type is IM-R " )
            sep_char("#")
else :
    sep_char("@")
    print (" Type selected is Discrete ")
    sep_char("@")
    inp_SinDef_MulDef = input (" Single Defect Per Unit S Multiple Defect per unit M ? ")
    if inp_SinDef_MulDef == "S" :
        inp_Con_Var = input("Sample Size Constant C or Variable V ? ")
        if inp_Con_Var == "C" :
            sep_char("@")
            print( " Chart is np " )
            sep_char("@")
        else :
            sep_char("@")
            print (" Chart is p ")
            sep_char("@")
    else :
        inp_Con_Var = input("Sample Size Constant C or Variable V ? ")
        if inp_Con_Var == "C" :
            sep_char("@")
            print( " Chart is c " )
            sep_char("@")
        else :
            sep_char("@")
            print (" Chart is u ")
            sep_char("@")

