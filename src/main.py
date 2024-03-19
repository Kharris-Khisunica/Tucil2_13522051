from bruteforce import *
from dnc import *
from fungsi import *
import matplotlib
import time

#Show Greeting
print("====================================")
print("Welcome to my Second STIMA's small project")
print("Kharris Khisunica - 13522051")
print("====================================")
print(""" 
 ____           _             __  __           _                     
| __ )  ___ ___(_) ___ _ __  |  \/  | __ _  __| |_ __   ___  ___ ___ 
|  _ \ / _ \_  / |/ _ \ '__| | |\/| |/ _` |/ _` | '_ \ / _ \/ __/ __|
| |_) |  __// /| |  __/ |    | |  | | (_| | (_| | | | |  __/\__ \__ |
|____/ \___/___|_|\___|_|    |_|  |_|\__,_|\__,_|_| |_|\___||___/___/
      
                                                                              
""")                                                                     

print("====================================\n")

#Mau Bruteforce atau DnC

#Menu Choice, Mau Orde 2 atau Orde >= 2 (bonus)

Menu_Choice()

print("\t")
#Choice Checker

Menu_Checker = Choice_Menu()

if Menu_Checker == 1:
    print("You've Chosen Order=2/Quadratic Mode.\t")
    print("\t")

    Menu_Mode()

    Mode_Checker = Choice_Mode()
    print("\t")

    if Mode_Checker == 1:
        print("You Choose Bruteforce Methode.\t")
        point_list = input_point_list_2()
        print(point_list)
    #    iteration = input_iteration()

        time = bf(point_list)

        print(f"Brute Force Methode took: {(time*1000):.5f} ms")
        #Clear Memory ?

        

    elif Mode_Checker == 2:
        print("You Choose Divide and Conquer Methode.\t")
        point_list = input_point_list_2()
    #    iteration = input_iteration()
        
        time = dnc_2(point_list)

        print(f"Divide and Conquer Methode took: {(time*1000):.5f} ms")

        #Clear Memory?

    else: #Choice == 3

        print("You Choose Comparison Mode.\t")
        point_list = input_point_list_2()
    #    iteration = input_iteration

        #DnC
        dnc_time = dnc_2(point_list)
        
        bf_time = bf(point_list)
        
        print(f"Divide and Conquer took {dnc_time*1000} ms")
        print(f"Brute force took {bf_time*1000} ms")
        
        if dnc_time > 0:
            time = (bf_time-dnc_time)/(dnc_time) * 100 
        else:
            time = 0

        print('\t')
        if time >= 0:
            print(f"Wow. Brute Force Methode is {time :.2f}% slower")
        else:
            print(f"Wow. Divide and Conquer Methode is {-time :.2f}% slower")
    


else: #Menu Choice == 2
    print("You've Chosen No Order Restriction Mode.")
    print("====================================")

    Menu_Mode()

    Mode_Checker = Choice_Mode()

    if Mode_Checker == 1:
        print("You Choose Bruteforce Methode.")
        point_list = input_point_list_n()
        print(point_list)
    #    iteration = input_iteration()

        time = bf(point_list)

        print(f"Brute Force Methode took: {(time*1000):.5f} ms")
        #Clear Memory ?

    elif Mode_Checker == 2:
        print("You Choose Divide and Conquer Methode.")
        point_list = input_point_list_n()
    #    iteration = input_iteration()
        
        dnc_n(point_list)

        print(f"Divide and Conquer Methode took: {(time*1000):.5f} ms")

        #Clear Memory?

    else: #Mode_Checker == 3

        print("You Choose Comparison Mode.")
        point_list = input_point_list_n()
    #    iteration = input_iteration

        #DnC
        dnc_time = dnc_n(point_list)
        
        bf_time = bf(point_list)
        
        if dnc_time!=0:
            time = (bf_time-dnc_time)/(dnc_time) * 100 
        else:
            time = 0

        print('\t')
        if time >= 0:
            print(f"Wow. Brute Force Methode is {time :.2f}% slower")
        else:
            print(f"Wow. Divide and Conquer Methode is {-time :.2f}% slower")



