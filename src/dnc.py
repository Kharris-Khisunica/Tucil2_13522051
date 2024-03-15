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

def midpoint(p1, p2):
#p1, p2 = (x,y)
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def dnc(point_list):


    return

