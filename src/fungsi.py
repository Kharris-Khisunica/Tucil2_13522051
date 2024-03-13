import matplotlib.pyplot as plt

def Menu():
    print("====================================")
    print("Choose your method to make a Bezier Curve")
    print("1. Bruteforce Methode")
    print("2. Divide and Conquer Methode")
    print("3. Comparison Mode (Compare between Bruteforce and Divide and Conquer Methode)")
    print("====================================\n")

def Choice():
    # int Choice

    Choice = int(input("Please Input Your Choice (1/2/3): "))

    while (Choice != 1 and Choice != 2 and Choice != 3):
        print("You're inputing an invalid number. Please Retry.")
        Choice = int(input("Please Input Your Choice (1/2/3): "))

    return Choice
    
def input_point_list():
#Meminta user untuk memasukkan point_listrmasi yang diperlukan, yaitu banyak titik kontrol, dan koordinat nya. 
    
    point_list = []
    n = int(input("Please Input The Order of The Bezier Curve: "))
    print("\t")

    for i in range (n+1):
        while True:
            point = input(f"Enter the Coordinate (x,y) of Point-{i} Separated by Space: ").split()
            if len(point) != 2:
                print("Please enter exactly two integer seperated by space.")
                continue
            try:
                x,y = map(int, point)
                point = (x,y)
                point_list.append(point)
                break
            except ValueError:
                print("Please enter two integer only.")
        print('\t')
    return point_list

def visualize (bezier_point):
    #Visualisasikan
    
    x = [x for x,_ in bezier_point]
    y = [y for _,y in bezier_point]

    print(x)
    print(y)
    plt.plot(x,y)

    plt.show()
