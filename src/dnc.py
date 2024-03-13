import matplotlib.pyplot as plt
import time
from fungsi import *

def dnc(point_list):
#Fungsi yang menghitung dan menghasilkan bezier curve menggunakan formula

    bezier_point = [] 
    
    #Cari Koordinat dari setiap titik berdasarkan iterasi
    print('\t')
    iteration = int(input("How Many Iterations: "))
    if iteration >= 1:
        start = time.time()
        t = 1/(2**iteration)
        
        for i in range (2**(iteration)+1):
            b_t = bezier_rec(point_list, i*t)
            bezier_point.append(b_t)

        end = time.time()

        print(f"There're {len(bezier_point)} points created.")

        visualize(bezier_point)

        return end-start
    



def bezier_rec(point_list, t):

    if len(point_list) == 1:
        return point_list[0]
    else:
        q1 = bezier_rec(point_list[0:-1], t)
        q2 = bezier_rec(point_list[1:],t)
        return ((1-t)*q1[0]+t*q2[0], (1-t)*q1[1]+t*q2[1]) 


