import time
from fungsi import *

def binomial (n, k):
    if k>n:
        return 0
    if k==n or k==0:
        return 1
    
    return binomial(n-1,k) + binomial(n-1,k-1)

def bf(point_list):

    bezier_point = []
    n = len(point_list) - 1
    
     #Cari Koordinat dari setiap titik berdasarkan iterasi
    print('\t')
    iteration = int(input("How Many Iterations: "))
    print("\t")
    if iteration >= 1:

        bezier_point = []
        start = time.time()
        t = 1/(2**iteration)
            
        for i in range ((2**iteration)+1):
            b_t = bezier_bin(point_list, i*t)
            bezier_point.append(b_t)

        end = time.time()
        
        print(f"There're {len(bezier_point)} points created.")
        print("\t")



        visualize(bezier_point, point_list)

        return end-start
    
def bezier_bin(point_list, t):
    n = len(point_list)-1

    x_bt = 0
    y_bt = 0
    
    for i in range (n+1):
        x_bt += binomial(n,i)*(1-t)**(n-i)*t**(i)*point_list[i][0]
        y_bt += binomial(n,i)*(1-t)**(n-i)*t**(i)*point_list[i][1]

    return (x_bt, y_bt)



"""
def bf_rec(point_list):
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



"""
