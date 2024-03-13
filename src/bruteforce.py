import matplotlib.pyplot as plt

def bf(point_list):
#Fungsi yang menghitung dan menghasilkan bezier curve menggunakan formula

    bezier_point = [] 
    
    #Cari Koordinat dari setiap titik berdasarkan iterasi
    print('\t')
    iteration = int(input("How Many Iterations: "))
    if iteration >= 1:
        t = 1/(2**iteration)
        
        for i in range (2**(iteration)+1):
            b_t = bezier_rec(point_list, i*t)
            bezier_point.append(b_t)
    
    #Get bezier_points
    
    print(f"There're {len(bezier_point)} points created.")
    print(bezier_point)

    return bezier_point


def bezier_rec(point_list, t):

    if len(point_list) == 1:
        return point_list[0]
    else:
        q1 = bezier_rec(point_list[0:-1], t)
        q2 = bezier_rec(point_list[1:],t)
        return ((1-t)*q1[0]+t*q2[0], (1-t)*q1[1]+t*q2[1]) 


