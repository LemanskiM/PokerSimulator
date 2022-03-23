from backend import *
poker = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"D":10,"J":11,"Q":12,"K":13,"A":14}

def rozdanieGracz1():
    createTail()
    gaveCards(1)
    algoritm(Gracz1)
    change(Gracz1)
    pair(karta1g1pocz, karta2g1pocz, karta3g1pocz, karta4g1pocz, karta5g1pocz)
    kareta(karta1g1pocz, karta2g1pocz, karta3g1pocz, karta4g1pocz, karta5g1pocz)
    trio(Gracz1)
    strite(Gracz1)
    clear()

rozdanieGracz1()
