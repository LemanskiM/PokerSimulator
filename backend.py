import random

poker = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"D":10,"J":11,"Q":12,"K":13,"A":14}
talia = []

Gracz1 = []
Gracz2 = []
Gracz3 = []
Gracz4 = []
Gracz5 = []
Gracz6 = []

karta1g1pocz = []
karta2g1pocz = []
karta3g1pocz = []
karta4g1pocz = []
karta5g1pocz = []

karta1g1kon = []
karta2g1kon = []
karta3g1kon = []
karta4g1kon = []
karta5g1kon = []

karta1g2pocz = []
karta2g2pocz = []
karta3g2pocz = []
karta4g2pocz = []
karta5g2pocz = []

karta1g2kon = []
karta2g2kon = []
karta3g2kon = []
karta4g2kon = []
karta5g2kon = []

karta1g3pocz = []
karta2g3pocz = []
karta3g3pocz = []
karta4g3pocz = []
karta5g3pocz = []

karta1g3kon = []
karta2g3kon = []
karta3g3kon = []
karta4g3kon = []
karta5g3kon = []

karta1g4pocz = []
karta2g4pocz = []
karta3g4pocz = []
karta4g4pocz = []
karta5g4pocz = []

karta1g4kon = []
karta2g4kon = []
karta3g4kon = []
karta4g4kon = []
karta5g4kon = []

karta1g5pocz = []
karta2g5pocz = []
karta3g5pocz = []
karta4g5pocz = []
karta5g5pocz = []

karta1g5kon = []
karta2g5kon = []
karta3g5kon = []
karta4g5kon = []
karta5g5kon = []


karta1g6pocz = []
karta2g6pocz = []
karta3g6pocz = []
karta4g6pocz = []
karta5g6pocz = []

karta1g6kon = []
karta2g6kon = []
karta3g6kon = []
karta4g6kon = []
karta5g6kon = []


def algoritm(g1):

    if g1 == Gracz1:
        x1 = g1[0]
        karta1g1pocz.append(x1[0])
        karta1g1kon.append(x1[-1])

        x2 = g1[1]
        karta2g1pocz.append(x2[0])
        karta2g1kon.append(x2[-1])

        x3 = g1[2]
        karta3g1pocz.append(x3[0])
        karta3g1kon.append(x3[-1])

        x4 = g1[3]
        karta4g1pocz.append(x4[0])
        karta4g1kon.append(x4[-1])

        x5 = g1[4]
        karta5g1pocz.append(x5[0])
        karta5g1kon.append(x5[-1])


    if g1 == Gracz2:
        x1 = g1[0]
        karta1g2pocz.append(x1[0])
        karta1g2kon.append(x1[-1])

        x2 = g1[1]
        karta2g2pocz.append(x2[0])
        karta2g2kon.append(x2[-1])

        x3 = g1[2]
        karta3g2pocz.append(x3[0])
        karta3g2kon.append(x3[-1])

        x4 = g1[3]
        karta4g2pocz.append(x4[0])
        karta4g2kon.append(x4[-1])

        x5 = g1[4]
        karta5g2pocz.append(x5[0])
        karta5g2kon.append(x5[-1])


    if g1 == Gracz3:
        x1 = g1[0]
        karta1g3pocz.append(x1[0])
        karta1g3kon.append(x1[-1])

        x2 = g1[1]
        karta2g3pocz.append(x2[0])
        karta2g3kon.append(x2[-1])

        x3 = g1[2]
        karta3g3pocz.append(x3[0])
        karta3g3kon.append(x3[-1])

        x4 = g1[3]
        karta4g3pocz.append(x4[0])
        karta4g3kon.append(x4[-1])

        x5 = g1[4]
        karta5g3pocz.append(x5[0])
        karta5g3kon.append(x5[-1])


    if g1 == Gracz4:
        x1 = g1[0]
        karta1g4pocz.append(x1[0])
        karta1g4kon.append(x1[-1])

        x2 = g1[1]
        karta2g4pocz.append(x2[0])
        karta2g4kon.append(x2[-1])

        x3 = g1[2]
        karta3g4pocz.append(x3[0])
        karta3g4kon.append(x3[-1])

        x4 = g1[3]
        karta4g4pocz.append(x4[0])
        karta4g4kon.append(x4[-1])

        x5 = g1[4]
        karta5g4pocz.append(x5[0])
        karta5g4kon.append(x5[-1])


    if g1 == Gracz5:
        x1 = g1[0]
        karta1g5pocz.append(x1[0])
        karta1g5kon.append(x1[-1])

        x2 = g1[1]
        karta2g5pocz.append(x2[0])
        karta2g5kon.append(x2[-1])

        x3 = g1[2]
        karta3g5pocz.append(x3[0])
        karta3g5kon.append(x3[-1])

        x4 = g1[3]
        karta4g5pocz.append(x4[0])
        karta4g5kon.append(x4[-1])

        x5 = g1[4]
        karta5g5pocz.append(x5[0])
        karta5g5kon.append(x5[-1])


    if g1 == Gracz6:
        x1 = g1[0]
        karta1g6pocz.append(x1[0])
        karta1g6kon.append(x1[-1])

        x2 = g1[1]
        karta2g6pocz.append(x2[0])
        karta2g6kon.append(x2[-1])

        x3 = g1[2]
        karta3g6pocz.append(x3[0])
        karta3g6kon.append(x3[-1])

        x4 = g1[3]
        karta4g6pocz.append(x4[0])
        karta4g6kon.append(x4[-1])

        x5 = g1[4]
        karta5g6pocz.append(x5[0])
        karta5g6kon.append(x5[-1])

def clear():

    global karta1g1pocz
    global karta2g1pocz
    global karta3g1pocz
    global karta4g1pocz
    global karta5g1pocz

    global karta1g2pocz
    global karta2g2pocz
    global karta3g2pocz
    global karta4g2pocz
    global karta5g2pocz

    global karta1g3pocz
    global karta2g3pocz
    global karta3g3pocz
    global karta4g3pocz
    global karta5g3pocz

    global karta1g4pocz
    global karta2g4pocz
    global karta3g4pocz
    global karta4g4pocz
    global karta5g4pocz

    global karta1g5pocz
    global karta2g5pocz
    global karta3g5pocz
    global karta4g5pocz
    global karta5g5pocz

    global karta1g6pocz
    global karta2g6pocz
    global karta3g6pocz
    global karta4g6pocz
    global karta5g6pocz

    global Gracz1
    global Gracz2
    global Gracz3
    global Gracz4
    global Gracz5
    global Gracz6

    global talia

    karta1g1pocz = []
    karta2g1pocz = []
    karta3g1pocz = []
    karta4g1pocz = []
    karta5g1pocz = []

    karta1g2pocz = []
    karta2g2pocz = []
    karta3g2pocz = []
    karta4g2pocz = []
    karta5g2pocz = []

    karta1g3pocz = []
    karta2g3pocz = []
    karta3g3pocz = []
    karta4g3pocz = []
    karta5g3pocz = []

    karta1g4pocz = []
    karta2g4pocz = []
    karta3g4pocz = []
    karta4g4pocz = []
    karta5g4pocz = []

    karta1g5pocz = []
    karta2g5pocz = []
    karta3g5pocz = []
    karta4g5pocz = []
    karta5g5pocz = []

    karta1g6pocz = []
    karta2g6pocz = []
    karta3g6pocz = []
    karta4g6pocz = []
    karta5g6pocz = []

    Gracz1 = []
    Gracz2 = []
    Gracz3 = []
    Gracz4 = []
    Gracz5 = []
    Gracz6 = []

    talia.clear()

def createTail():
    Poj_licz = ["2","3","4","5","6","7","8","9","D","J","Q","K","A"]
    Pok_kol =  ["Pik", "Trefl", "Kier", "Karo"]
    for i in range (0,len(Poj_licz)):
        x = Poj_licz.pop(0)
        a = x + Pok_kol[0]
        talia.append(a)
        b = x + Pok_kol[1]
        talia.append(b)
        c = x + Pok_kol[2]
        talia.append(c)
        d = x + Pok_kol[3]
        talia.append(d)

def change(l):
    global karta1g1pocz
    global karta2g1pocz
    global karta3g1pocz
    global karta4g1pocz
    global karta5g1pocz

    global karta1g2pocz
    global karta2g2pocz
    global karta3g2pocz
    global karta4g2pocz
    global karta5g2pocz

    global karta1g3pocz
    global karta2g3pocz
    global karta3g3pocz
    global karta4g3pocz
    global karta5g3pocz

    global karta1g4pocz
    global karta2g4pocz
    global karta3g4pocz
    global karta4g4pocz
    global karta5g4pocz

    global karta1g5pocz
    global karta2g5pocz
    global karta3g5pocz
    global karta4g5pocz
    global karta5g5pocz

    global karta1g6pocz
    global karta2g6pocz
    global karta3g6pocz
    global karta4g6pocz
    global karta5g6pocz

    if l==Gracz1:
        karta1g1pocz = poker[karta1g1pocz[0]]
        karta2g1pocz = poker[karta2g1pocz[0]]
        karta3g1pocz = poker[karta3g1pocz[0]]
        karta4g1pocz = poker[karta4g1pocz[0]]
        karta5g1pocz = poker[karta5g1pocz[0]]

    if l==Gracz2:
        karta1g1pocz = poker[karta1g1pocz[0]]
        karta2g1pocz = poker[karta2g1pocz[0]]
        karta3g1pocz = poker[karta3g1pocz[0]]
        karta4g1pocz = poker[karta4g1pocz[0]]
        karta5g1pocz = poker[karta5g1pocz[0]]

        karta1g2pocz = poker[karta1g2pocz[0]]
        karta2g2pocz = poker[karta2g2pocz[0]]
        karta3g2pocz = poker[karta3g2pocz[0]]
        karta4g2pocz = poker[karta4g2pocz[0]]
        karta5g2pocz = poker[karta5g2pocz[0]]

    if l==Gracz3:
        karta1g1pocz = poker[karta1g1pocz[0]]
        karta2g1pocz = poker[karta2g1pocz[0]]
        karta3g1pocz = poker[karta3g1pocz[0]]
        karta4g1pocz = poker[karta4g1pocz[0]]
        karta5g1pocz = poker[karta5g1pocz[0]]

        karta1g2pocz = poker[karta1g2pocz[0]]
        karta2g2pocz = poker[karta2g2pocz[0]]
        karta3g2pocz = poker[karta3g2pocz[0]]
        karta4g2pocz = poker[karta4g2pocz[0]]
        karta5g2pocz = poker[karta5g2pocz[0]]

        karta1g3pocz = poker[karta1g3pocz[0]]
        karta2g3pocz = poker[karta2g3pocz[0]]
        karta3g3pocz = poker[karta3g3pocz[0]]
        karta4g3pocz = poker[karta4g3pocz[0]]
        karta5g3pocz = poker[karta5g3pocz[0]]

    if l==Gracz4:
        karta1g1pocz = poker[karta1g1pocz[0]]
        karta2g1pocz = poker[karta2g1pocz[0]]
        karta3g1pocz = poker[karta3g1pocz[0]]
        karta4g1pocz = poker[karta4g1pocz[0]]
        karta5g1pocz = poker[karta5g1pocz[0]]

        karta1g2pocz = poker[karta1g2pocz[0]]
        karta2g2pocz = poker[karta2g2pocz[0]]
        karta3g2pocz = poker[karta3g2pocz[0]]
        karta4g2pocz = poker[karta4g2pocz[0]]
        karta5g2pocz = poker[karta5g2pocz[0]]

        karta1g3pocz = poker[karta1g3pocz[0]]
        karta2g3pocz = poker[karta2g3pocz[0]]
        karta3g3pocz = poker[karta3g3pocz[0]]
        karta4g3pocz = poker[karta4g3pocz[0]]
        karta5g3pocz = poker[karta5g3pocz[0]]

        karta1g4pocz = poker[karta1g4pocz[0]]
        karta2g4pocz = poker[karta2g4pocz[0]]
        karta3g4pocz = poker[karta3g4pocz[0]]
        karta4g4pocz = poker[karta4g4pocz[0]]
        karta5g4pocz = poker[karta5g4pocz[0]]

    if l==Gracz5:
        karta1g1pocz = poker[karta1g1pocz[0]]
        karta2g1pocz = poker[karta2g1pocz[0]]
        karta3g1pocz = poker[karta3g1pocz[0]]
        karta4g1pocz = poker[karta4g1pocz[0]]
        karta5g1pocz = poker[karta5g1pocz[0]]

        karta1g2pocz = poker[karta1g2pocz[0]]
        karta2g2pocz = poker[karta2g2pocz[0]]
        karta3g2pocz = poker[karta3g2pocz[0]]
        karta4g2pocz = poker[karta4g2pocz[0]]
        karta5g2pocz = poker[karta5g2pocz[0]]

        karta1g3pocz = poker[karta1g3pocz[0]]
        karta2g3pocz = poker[karta2g3pocz[0]]
        karta3g3pocz = poker[karta3g3pocz[0]]
        karta4g3pocz = poker[karta4g3pocz[0]]
        karta5g3pocz = poker[karta5g3pocz[0]]

        karta1g4pocz = poker[karta1g4pocz[0]]
        karta2g4pocz = poker[karta2g4pocz[0]]
        karta3g4pocz = poker[karta3g4pocz[0]]
        karta4g4pocz = poker[karta4g4pocz[0]]
        karta5g4pocz = poker[karta5g4pocz[0]]

        karta1g5pocz = poker[karta1g5pocz[0]]
        karta2g5pocz = poker[karta2g5pocz[0]]
        karta3g5pocz = poker[karta3g5pocz[0]]
        karta4g5pocz = poker[karta4g5pocz[0]]
        karta5g5pocz = poker[karta5g5pocz[0]]


    if l==Gracz6:

        karta1g1pocz = poker[karta1g1pocz[0]]
        karta2g1pocz = poker[karta2g1pocz[0]]
        karta3g1pocz = poker[karta3g1pocz[0]]
        karta4g1pocz = poker[karta4g1pocz[0]]
        karta5g1pocz = poker[karta5g1pocz[0]]

        karta1g2pocz = poker[karta1g2pocz[0]]
        karta2g2pocz = poker[karta2g2pocz[0]]
        karta3g2pocz = poker[karta3g2pocz[0]]
        karta4g2pocz = poker[karta4g2pocz[0]]
        karta5g2pocz = poker[karta5g2pocz[0]]

        karta1g3pocz = poker[karta1g3pocz[0]]
        karta2g3pocz = poker[karta2g3pocz[0]]
        karta3g3pocz = poker[karta3g3pocz[0]]
        karta4g3pocz = poker[karta4g3pocz[0]]
        karta5g3pocz = poker[karta5g3pocz[0]]

        karta1g4pocz = poker[karta1g4pocz[0]]
        karta2g4pocz = poker[karta2g4pocz[0]]
        karta3g4pocz = poker[karta3g4pocz[0]]
        karta4g4pocz = poker[karta4g4pocz[0]]
        karta5g4pocz = poker[karta5g4pocz[0]]

        karta1g5pocz = poker[karta1g5pocz[0]]
        karta2g5pocz = poker[karta2g5pocz[0]]
        karta3g5pocz = poker[karta3g5pocz[0]]
        karta4g5pocz = poker[karta4g5pocz[0]]
        karta5g5pocz = poker[karta5g5pocz[0]]

        karta1g6pocz = poker[karta1g6pocz[0]]
        karta2g6pocz = poker[karta2g6pocz[0]]
        karta3g6pocz = poker[karta3g6pocz[0]]
        karta4g6pocz = poker[karta4g6pocz[0]]
        karta5g6pocz = poker[karta5g6pocz[0]]

def gaveCards(liczba_graczy):

    if liczba_graczy ==1:
        while len(Gracz1) != 5:
            x = talia.pop(random.choice(range(0,len(talia))))
            Gracz1.append(x)

    if liczba_graczy == 2:
        while len(Gracz1) != 5 and len(Gracz2)!=5:
            x = talia.pop(random.choice(range(0,len(talia))))
            Gracz1.append(x)
            y = talia.pop(random.choice(range(0,len(talia))))
            Gracz2.append(y)
    if liczba_graczy == 3:
        while len(Gracz1) != 5 and len(Gracz2)!=5 and len(Gracz3) !=5:
            x = talia.pop(random.choice(range(0,len(talia))))
            Gracz1.append(x)
            y = talia.pop(random.choice(range(0,len(talia))))
            Gracz2.append(y)
            z = talia.pop(random.choice(range(0,len(talia))))
            Gracz3.append(z)
    if liczba_graczy == 4:
        while len(Gracz1) != 5 and len(Gracz2)!=5 and len(Gracz3) !=5 and len(Gracz4) !=5:
            x1 = talia.pop(random.choice(range(0,len(talia))))
            Gracz1.append(x)
            x2 = talia.pop(random.choice(range(0,len(talia))))
            Gracz2.append(x2)
            x3 = talia.pop(random.choice(range(0,len(talia))))
            Gracz3.append(x3)
            x4 = talia.pop(random.choice(range(0,len(talia))))
            Gracz4.append(x4)
    if liczba_graczy == 5:
        while len(Gracz1) != 5 and len(Gracz2)!=5 and len(Gracz3) !=5 and len(Gracz4) !=5 and len(Gracz5) !=5:
            x1 = talia.pop(random.choice(range(0,len(talia))))
            Gracz1.append(x1)
            x2 = talia.pop(random.choice(range(0,len(talia))))
            Gracz2.append(x2)
            x3 = talia.pop(random.choice(range(0,len(talia))))
            Gracz3.append(x3)
            x4 = talia.pop(random.choice(range(0,len(talia))))
            Gracz4.append(x4)
            x5 = talia.pop(random.choice(range(0,len(talia))))
            Gracz4.append(x5)
    if liczba_graczy == 6:
        while len(Gracz1) != 5 and len(Gracz2)!=5 and len(Gracz3) !=5 and len(Gracz4) !=5 and len(Gracz5) !=5 and len(Gracz6) !=5:
            x1 = talia.pop(random.choice(range(0,len(talia))))
            Gracz1.append(x1)
            x2 = talia.pop(random.choice(range(0,len(talia))))
            Gracz2.append(x2)
            x3 = talia.pop(random.choice(range(0,len(talia))))
            Gracz3.append(x3)
            x4 = talia.pop(random.choice(range(0,len(talia))))
            Gracz4.append(x4)
            x5 = talia.pop(random.choice(range(0,len(talia))))
            Gracz5.append(x5)
            x6 = talia.pop(random.choice(range(0,len(talia))))
            Gracz6.append(x6)


def pair(k1,k2,k3,k4,k5):

    if k1 == k2 and k1 != k3 and k1 !=k4 and k1 !=k5:
        print("pair")
    if k1 == k3 and k1 != k2 and k1 !=k4 and k1 !=k5:
        print("pair")
    if k1 == k4 and k1 != k3 and k1 !=k2 and k1 !=k5:
        print("pair")
    if k1 == k5 and k1 != k3 and k1 !=k4 and k1 !=k2:
        print("pair")

    if k2 == k3 and k2 != k1 and k2 !=k4 and k2 !=k5:
        print("pair")
    if k2 == k4 and k2 != k1 and k2 !=k3 and k2 !=k5:
        print("pair")
    if k2 == k5 and k2 != k1 and k2 !=k3 and k2 !=k4:
        print("pair")

    if k3 == k4 and k3 != k1 and k3 !=k2 and k3 !=k5:
        print("pair")
    if k3 == k5 and k3 != k1 and k3 !=k2 and k2 !=k4:
        print("pair")

    if k4 == k5 and k4 != k1 and k5 !=k2 and k2 !=k3:
        print("pair")

    print("-----------------")

def kareta(k1,k2,k3,k4,k5):

    if k1==k2==k3==k4:
        print("kareta")
    if k1==k2==k3==k5:
        print("kareta")
    if k1==k2==k4==k5:
        print("kareta")
    if k1==k3==k4==k5:
        print("kareta")
    if k3==k2==k4==k5:
        print("kareta")

def strite(Gracz):

    box = []
    if Gracz == Gracz1:
        box.append(karta1g1pocz)
        box.append(karta2g1pocz)
        box.append(karta3g1pocz)
        box.append(karta4g1pocz)
        box.append(karta5g1pocz)
    if Gracz == Gracz2:
        box.append(karta1g2pocz)
        box.append(karta2g2pocz)
        box.append(karta3g2pocz)
        box.append(karta4g2pocz)
        box.append(karta5g2pocz)
    if Gracz == Gracz3:
        box.append(karta1g3pocz)
        box.append(karta2g3pocz)
        box.append(karta3g3pocz)
        box.append(karta4g3pocz)
        box.append(karta5g3pocz)
    if Gracz == Gracz4:
        box.append(karta1g4pocz)
        box.append(karta2g4pocz)
        box.append(karta3g4pocz)
        box.append(karta4g4pocz)
        box.append(karta5g4pocz)
    if Gracz == Gracz5:
        box.append(karta1g5pocz)
        box.append(karta2g5pocz)
        box.append(karta3g5pocz)
        box.append(karta4g5pocz)
        box.append(karta5g5pocz)
    if Gracz == Gracz6:
        box.append(karta1g6pocz)
        box.append(karta2g6pocz)
        box.append(karta3g6pocz)
        box.append(karta4g6pocz)
        box.append(karta5g6pocz)
    box.sort()
    if box[0]+4 == box[1] +3 == box[2]+2 == box[3]+1 == box[4]:
        print(box[0],box[1],box[2],box[3],box[4])
        print ("Strite")
        box.clear()

def trio(Gracz):

    box = []
    if Gracz == Gracz1:
        box.append(karta1g1pocz)
        box.append(karta2g1pocz)
        box.append(karta3g1pocz)
        box.append(karta4g1pocz)
        box.append(karta5g1pocz)
    if Gracz == Gracz2:
        box.append(karta1g2pocz)
        box.append(karta2g2pocz)
        box.append(karta3g2pocz)
        box.append(karta4g2pocz)
        box.append(karta5g2pocz)
    if Gracz == Gracz3:
        box.append(karta1g3pocz)
        box.append(karta2g3pocz)
        box.append(karta3g3pocz)
        box.append(karta4g3pocz)
        box.append(karta5g3pocz)
    if Gracz == Gracz4:
        box.append(karta1g4pocz)
        box.append(karta2g4pocz)
        box.append(karta3g4pocz)
        box.append(karta4g4pocz)
        box.append(karta5g4pocz)
    if Gracz == Gracz5:
        box.append(karta1g5pocz)
        box.append(karta2g5pocz)
        box.append(karta3g5pocz)
        box.append(karta4g5pocz)
        box.append(karta5g5pocz)
    if Gracz == Gracz6:
        box.append(karta1g6pocz)
        box.append(karta2g6pocz)
        box.append(karta3g6pocz)
        box.append(karta4g6pocz)
        box.append(karta5g6pocz)
    box.sort()
    if box[0] == box[1] == box[2] and box[3] != box[4] or box[1] == box[2] == box[3] and box[0] != box[4] or box[2] == box[3] == box[4] and box[0] != box[1]:
        print(box[0],box[1],box[2],box[3],box[4])
        print ("3 cards ")
        box.clear()
