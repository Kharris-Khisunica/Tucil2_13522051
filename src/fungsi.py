import matplotlib.pyplot as plt

def Menu_Choice():
    print("====================================")
    print("Choose your Order Restriction: ")
    print("1. Order/n = 2 (Quadratic)")
    print("2. No Restriction")
    print("====================================")
    

def Menu_Mode():
    print("====================================")
    print("Choose your method to make a Bezier Curve")
    print("1. Bruteforce Methode")
    print("2. Divide and Conquer Methode")
    print("3. Comparison Mode (Compare between Bruteforce and Divide and Conquer Methode)")
    print("====================================\n")



def Choice_Menu():
    # int Choice

    Choice = int(input("Please Input Your Choice (1/2): "))

    while (Choice != 1 and Choice != 2):
        print("You're inputing an invalid number. Please Retry.")
        Choice = int(input("Please Input Your Choice (1/2): "))

    return Choice


def Choice_Mode():
    # int Choice

    Choice = int(input("Please Input Your Choice (1/2/3): "))

    while (Choice != 1 and Choice != 2 and Choice != 3):
        print("You're inputing an invalid number. Please Retry.")
        Choice = int(input("Please Input Your Choice (1/2/3): "))

    return Choice
"""
def input_iteration():

    iteration = int(input("How Many Iterations (>=1): "))

    while (iteration < 1):
        print("You're inputing an invalid number. Please Retry.")
        iteration = int(input("How Many Iterations (>=1): "))

    return iteration
"""

def input_point_list_2():
#Meminta user untuk memasukkan point_listrmasi yang diperlukan, yaitu banyak titik kontrol, dan koordinat nya. 
    
    point_list = []
    n = 2
    print("\t")

    for i in range (n+1):
        while True:
            point = input(f"Enter the Coordinate (x,y) of Point-{i} Separated by Space: ").split()
            if len(point) != 2:
                print("Please enter exactly two real numbers seperated by space.")
                continue
            try:
                x,y = map(float, point)
                point = (x,y)
                point_list.append(point)
                break
            except ValueError:
                print("Please enter two real numbers only.")
        print('\t')
    return point_list

def input_point_list_n():
#Meminta user untuk memasukkan point_listrmasi yang diperlukan, yaitu banyak titik kontrol, dan koordinat nya. 
    
    point_list = []
    n = int(input("Please input your Bezier Curve's Order: "))    
    print("\t")

    for i in range (n+1):
        while True:
            point = input(f"Enter the Coordinate (x,y) of Point-{i} Separated by Space: ").split()
            if len(point) != 2:
                print("Please enter exactly two real numbers seperated by space.")
                continue
            try:
                x,y = map(float, point)
                point = (x,y)
                point_list.append(point)
                break
            except ValueError:
                print("Please enter two real numbers only.")
        print('\t')
    return point_list


def visualize (bezier_point, point_list):
    #Visualisasikan
    
    plt.title("Bezier Curve")
    bez_x = [x for x,_ in bezier_point]
    bez_y = [y for _,y in bezier_point]

    plt.plot(bez_x,bez_y, marker = "o")
    
    pl_x = [x for x,_ in point_list]
    pl_y = [y for _,y in point_list]

    plt.plot(pl_x,pl_y)

    plt.show()

def cek_visual(poin):

    
    x = [x for x,_ in poin]
    y = [y for _,y in poin]

    plt.plot (x,y)

    plt.show()