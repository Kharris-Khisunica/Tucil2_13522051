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

#Menu

Menu()

#Choice Checker

Choice = Choice()


if Choice == 1:
    print("You Choose Bruteforce Methode.")
    point_list = input_point_list()
    print(point_list)
#    iteration = input_iteration()

    time = bf(point_list)

    print(f"Brute Force Methode took: {(time*1000):.5f} ms")
    #Clear Memory ?

elif Choice == 2:
    print("You Choose Divide and Conquer Methode.")
    point_list = input_point_list()
#    iteration = input_iteration()
    
    time = dnc(point_list)

    print(f"Divide and Conquer Methode took: {(time*1000):.5f} ms")

    #Clear Memory?

else: #Choice == 3

    print("You Choose Comparison Mode.")
    point_list = input_point_list()
#    iteration = input_iteration

    #DnC
    dnc_time = dnc(point_list)
    
    bf_time = bf(point_list)
    
    time = (bf_time-dnc_time)/(dnc_time) * 100 

    print('\t')
    if time >= 0:
        print(f"Wow. Brute Force Methode is {time :.2f}% slower")
    else:
        print(f"Wow. Divide and Conquer Methode is {-time :.2f}% slower")


    



