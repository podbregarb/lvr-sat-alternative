# uvozimo vse potrebne programe
import Implementacija.cnf as cnf
import Implementacija.bool as bool
import Dpll.dpll as dpll
import Dpll.dpll_testi as dpll_testi
import Prevedbe_problemov.barvanje_grafov as barvanje_grafov
import Prevedbe_problemov.sudoku4x4 as sudoku
import Implementacija.primer as primer
import copy
from tkinter import *
import time


# zažene funkcijo primer iz programa primer.py (iz mape Implementacija)
def osnove():
    primer.primer()

# za testiranje dpll
def test_dpll():
    dpll_testi.test()


############        BARVANJE GRAFOV        ############
# testi:
Test0=(2,[(1,2)],2) # graf na dveh točkah
Test1=(6,[(1,2),(2,3),(3,4),(4,5),(5,6)],2) # veriga šestih točk
Test2=(4,[(1,2),(2,3),(3,4),(4,1)],2) # kvadrat
Test3=(4,[(1,2),(2,3),(3,4),(4,1),(1,3),(2,4)],2)
def barvanje():
    resitev = dpll.dpll(barvanje_grafov.barvanje_grafov(Test3[0],Test3[1],Test3[2]))
    for i in resitev[1].copy():
        if resitev[1][i]==False:
            del resitev[1][i]
    return resitev



    
############             SUDOKU            ############
# uporaba dpll na sudokuju in barvanju grafov
# testi:
test0='0 0 0 0,0 0 0 0,0 0 0 0,0 0 0 0' # prazen
test1='1 1 2 3,0 0 0 0,0 0 0 0,0 0 0 0' # nerešljiv
test2='1 0 2 3,0 1 0 0,0 0 0 0,0 0 0 0' # nerešljiv
test3='1 0 2 3,0 0 0 0,1 0 0 0,0 0 0 0' # nerešljiv
test4='1 2 3 4,3 4 1 2,4 3 2 1,2 1 4 3' # poln
testi=[test0,test1,test2,test3,test4]
# primeri:
primer0='3 0 4 0,0 1 0 2,0 4 0 3,2 0 1 0' # zelo lahek
primer1='0 2 1 3,0 0 0 4,0 0 0 1,0 4 3 2' # lahek
primer2='0 1 3 0,0 0 0 4,0 0 0 1,0 2 4 0' # srednje težki
primer3='0 2 0 0,1 0 2 0,2 0 3 0,0 3 0 0' # težji
primeri=[primer0,primer1,primer2,primer3]
def sudoku4x4():
    print('Ta program resuje 4x4 sudoku.')
    
    # ponavljamo dokler uporabnik ne vpiše nekaj kar ni y/n
    while True:
        odlocitev=input('Ali zelis vpisati svoj sudoku? (y/n)  ')
        
        if odlocitev=='y' or odlocitev=='n':
            
            def risanje(resitev,besedilo=''):
                window=Tk()
                canvas=Canvas(window, width=280, height=300)
                canvas.pack()
                # besedilo na vrhu okenčka
                canvas.create_text(120,17,text=besedilo,font=('Arial',18))
                # vse ravne črte na platnu
                canvas.create_rectangle(20,40,260,280, width=3)
                canvas.create_line(80,40,80,280)
                canvas.create_line(140,40,140,280, width=3)
                canvas.create_line(200,40,200,280)
                canvas.create_line(20,100,260,100)
                canvas.create_line(20,220,260,220)
                canvas.create_line(20,160,260,160, width=3)
                # vstavimo cifre v sudoku
                for i in resitev.keys():
                    canvas.create_text(50+(i[1]-1)*60,70+(i[0]-1)*60,text='{0}'.format(i[2]),font=('Arial',30))  
                window.mainloop()
                
            # če uporabnik ne želi vpisati svojega sudokuja, mu program rešu sudoku iz datoteke Implementacija/sudoku4.txt
            if odlocitev=='n':
                f=open('Prevedbe_problemov/sudoku4.txt','r')
                f=f.readlines()
                # naredimo slovar 'narisi', s katerim narišemo sudoku, ki ga rešujemo in seznam 'seznam', tj. seznam znanih spremenljivk, ki jih vstavimo v program sudoku
                narisi={}
                seznam=[]
                for i in range(len(f)):
                    for j in range(0,7,2):
                        if f[i][j]!='0':
                            seznam.append((i+1,j//2+1,int(f[i][j])))
                            narisi[(i+1,j//2+1,int(f[i][j]))]=True
                risanje(narisi,'Rešujemo sudoku:')
                
            # če vpiše svoj sudoku ali želi rešitev dveh posebnih primerov zgoraj:
            if odlocitev=='y':
                print ('Sudoku naj bo oblike "1 2 0 0,0 3 4 0,...", kjer 0 pomeni, da je polje prazno.')
                sud=input('Vpisi svoj sudoku:  \n')
                if sud[:-1]=='test':
                    sud=testi[int(sud[-1])]
                if sud[:-1]=='primer':
                    sud=primeri[int(sud[-1])]
                sud=sud.split(',')
                narisi={}
                seznam=[]
                for i in range(len(sud)):
                    for j in range(0,7,2):
                        if sud[i][j]!='0':
                            seznam.append((i+1,j//2+1,int(sud[i][j])))
                            narisi[(i+1,j//2+1,int(sud[i][j]))]=True
                risanje(narisi,'Rešujemo sudoku:')
                
            # rešimo sudoku in vrnemo 'Ni rešitve' če ni rešljiv, oz. narišemo rešitev, če je rešljiv
            t1=time.clock()
            resitev=dpll.dpll(sudoku.sudoku4(seznam))
            t2=time.clock()
            print('Tvoj sudoku sem reševal {0} sekunde.'.format(t2-t1))
            if resitev[0]=='Ni rešitve':
                print ('Ta sudoku ni rešljiv.')
            
            else:
                for i in resitev[1].copy():
                    if resitev[1][i]==False:
                        del resitev[1][i]
                risanje(resitev[1],'Rešen sudoku:')
            
        else:
            break
            
                    
                
    
