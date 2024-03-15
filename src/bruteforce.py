#Metode BruteForce
#Bentuk Bernstein Polynomial
#Rumus => B(t_k) = sum(i=0,n)[binomial(n,i) * (1-t_k)**(n-i) * t_k**(n-1) * P_i], P_i = Titik-i, B(t_k) = Titik kurva bezier untuk iterasi ke-k
#Algoritma Kuadratik (order 2):
# 1. Pilih 2 titik jangka, lalu pilih 1 titik kontrol, Misal P0 dan P2 adalah titik jangka dan P1 adalah titik kontrol
# 2. Pilih berapa kali iterasi, semakin banyak iterasi, semakin mulus kurva nya. Misal banyak iterasi = t.
# 3. Buatlah titik pembentuk kurva dengan memasukkan nilai n=2, t_k = 1/t ke rumus B(t_k) di atas. 
# 4. Iterasi step ke-3, dengan setiap iterasi, t_k ditambah 1/t. Iterasi sampai didapat B(1).
# 5. Sambungkan setiap titik yang dibentuk oleh step 3 dan 4 untuk membentuk kurva bezier. 

import matplotlib.pyplot as plt
import time
from fungsi import *

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
def binomial (n, k):
    if k>n:
        return 0
    if k==n or k==0:
        return 1
    
    return binomial(n-1,k) + binomial(n-1,k-1)

def bf(point_list):

    bezier_point = []
    
     #Cari Koordinat dari setiap titik berdasarkan iterasi
    print('\t')
    iteration = int(input("How Many Iterations: "))
    if iteration >= 1:
        start = time.time()
        t = 1/(2**iteration)
        
        for i in range (2**(iteration)+1):
            b_t = bezier_bin(point_list, i*t)
            bezier_point.append(b_t)

        end = time.time()

        print(f"There're {len(bezier_point)} points created.")

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
