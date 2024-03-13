from dnc import *
from bruteforce import *
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

    start = time.time()
    bezier_point = bf(point_list)
    end = time.time()

    visualize(bezier_point)

    print(f"Brute Force Methode took: {((end-start)*1000):.2f} ms")
    #Clear Memory ?

elif Choice == 2:
    print("You Choose Divide and Conquer Methode.")
    point_list = input_point_list()
    
    start = time.time()
    bezier_point = dnc(point_list)
    end = time.time()

    visualize(bezier_point)

    print(f"Divide and Conquer Methode took: {((end-start)*1000):.2f} ms")
    #Clear Memory?

else: #Choice == 3

    print("You Choose Comparison Mode.")
    point_list = input_point_list()

    #DnC
    dnc_start = time.time()
    bezier_point = dnc(point_list)
    dnc_end = time.time()

    dnc_time = dnc_end - dnc_start
    print(f"Divide and Conquer Methode took: {(dnc_time*1000):.2f} ms")  

    #BruteForce
    bf_start = time.time()
    bezier_point = bf(point_list)
    bf_end = time.time()

    bf_time = bf_end - bf_start
    print(f"Brute Force Methode took: {(bf_time*1000):.2f} ms") 

    print(f"Wow. Brute Force Methode is {(bf_end-dnc_end)/(dnc_end) * 100 :.2f}% slower")



