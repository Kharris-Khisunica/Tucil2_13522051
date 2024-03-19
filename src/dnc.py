import time
from fungsi import *

def dnc_2(point_list):
    
    bezier_dnc = []
    p1 = point_list[0]
    p2 = point_list[1]
    p3 = point_list[2]

    print('\t')
    t = int(input("How Many Iterations: "))
    print("\t")

    if t>=1:
        start = time.time()

        bezier_dnc.append(p1)
        dnc_2_point(p1, p2, p3, t, bezier_dnc)
        bezier_dnc.append(p3)

        end = time.time()

        print(f"There're {len(bezier_dnc)} points created.")
        print("\t")

        visualize(bezier_dnc, point_list)

        return end-start

def dnc_n(point_list):

    n = len(point_list)-1
    bezier_dnc = []
    p0 = point_list[0]
    pn = point_list[n]
    p_control_list = point_list[1:-1]

    print('\t')
    t = int(input("How Many Iterations: "))
    print("\t")

    if t>=1:
        start = time.time()

        bezier_dnc.append(p0)
        dnc_n_point(p0, p_control_list, pn, t, bezier_dnc)
        bezier_dnc.append(pn)

        end = time.time()

        print(f"There're {len(bezier_dnc)} points created.")
        print("\t")


        visualize(bezier_dnc, point_list)

        return end-start



def midpoint(p1, p2):
#p1, p2 = (x,y)
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def dnc_2_point(p1, p2, p3, t, bezier_dnc):

    if t>=1:
        mid1 = midpoint(p1,p2)
        mid3 = midpoint(p2,p3)
        mid2 = midpoint(mid1, mid3)

        dnc_2_point(p1, mid1, mid2, t-1, bezier_dnc)#Kiri
        bezier_dnc.append(mid2) #input
        dnc_2_point(mid2, mid3, p3, t-1, bezier_dnc)#Kanan



    return bezier_dnc

def dnc_n_point(p0, p_control_list, pn, t, n, bezier_dnc):

    if t>=1:


        #Pembuatan List Titik tengah dari tiap garis pembentuk kurva iterasi ke-t
        midpoint_list = []
        p1_list = [p0] + p_control_list #P0, P1, ... P(n-1)
        p2_list = p_control_list + [pn] #P1, P2, ... , Pn


        for i in range (len(p1_list)):
            midpoint_list.append(midpoint(p1_list[i], p2_list[i])) #P0+P1/2, P1+P2/2, ..., P(n-1)+Pn/2

        cek_visual(midpoint_list)

        print(f"midpoint {midpoint_list}")
        #Pembuatan list titik yang masuk ke dalam bezier.
        p3_list = []

        p3a_list = midpoint_list[:-1]
        p3b_list = midpoint_list[1:]

        for i in range (len(p3a_list)):
            p3_list.append(midpoint(p3a_list[i], p3b_list[i]))

        cek_visual(p3_list)

        print(f"p3 {p3_list}")

        pn_1 = p3_list[-1]
        p0_2 = p3_list[0]

        control_1 = [midpoint_list[0]] + p3_list[:-1]
        control_2 = p3_list[1:] + [midpoint_list[-1]]

        print(f"p0 = {p0}, c1 = {control_1}, pn1 = {pn_1}")
        print(f"p0_2 = {p0_2}, c2 = {control_2}, pn = {pn}")

        dnc_n_point(p0, control_1 , pn_1 , t-1, bezier_dnc)
        for x in p3_list:
            bezier_dnc.append(x)
        dnc_n_point(p0_2, control_2, pn, t-1, bezier_dnc)


    return bezier_dnc



def dnc_n_titik(p0, p_control_list, pn, t, n, bezier_point):

    if t>=1:

        if n==1: #Sisa 2 titik
            bezier_point = midpoint(p0,pn)
        else:
            midpoint_list = [midpoint(p0,p_control_list[0])]

            for i in range (n):
                midpoint_list.append(midpoint(p_control_list[i], p_control_list[i+1]))
            
            midpoint_list.append(midpoint(p_control_list[n],pn))

            p0 = midpoint_list[0]
            new_control_list = p_control_list[1:-1]
            pn = midpoint_list[-1]

            dnc_n_titik(p0,new_control_list,pn, t, n-1,bezier_point)

    return bezier_point

def dnc_n_real (p0,p_control_list,pn, t,n,bezier_dnc):



    return bezier_dnc

#Metode DnC
#Algoritma Midpoint
#Algoritma Wajib:
#bezier_dnc(pi, pj, t), t>0
#kasus t=1
#ambil titik2 tengah dari garis P0P1 dan P1P2 lalu ambil titik tengah dari titik2 tengah tersebut. Misal P3 
#Divide:
#Bagi menjadi sisi kanan dan sisi kiri dari titik tengah awal
#Conquer:
#bezier_dnc(p0,p3,t-1) Kiri
#bezier_dnc(p3,p2,t-1) Kanan
#Combine:
#

#Algoritma Orde-n
#Sadar Bezier bisa rekursif. B_p0p1...pn(t) = B_p0p1...pn-1(t)*(1-t) + B_p1p2...pn(t) * t
#Jika panjang larik = 1, maka pilih titik tersebut
#Jika panjang larik = 2, maka pilih titik tengah diantara kedua titik tersebut. 
 
#Divide:
#Bagi larik titik menjadi 2 larik, b1 dan b2, masing-masing berisi elemen

#b = b1*(1-t) + b2*t
#Conquer:
#b1 = bezier_dnc(point_list[0:-1], t)
#b2 = bezier_dnc(point_list[1:],t)
#Combine:
#
