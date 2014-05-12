# uvozimo vse potrebne programe
import Implementacija.cnf as cnf
import Implementacija.bool as bool
import Implementacija.primer as primer

import Dpll.dpll as dpll
import Dpll.dpll_testi as dpll_testi

import Prevedbe_problemov.barvanje_grafov as barvanje_grafov
import Prevedbe_problemov.sudoku4x4 as sudoku4
import Prevedbe_problemov.sudoku9x9 as sudoku9
import Prevedbe_problemov.sudoku4x4_primeri as sudoku4x4_primeri

import copy
from tkinter import *
import time


# zažene funkcijo primer iz programa primer.py (iz mape Implementacija)
def osnove():
    primer.primer()

# za testiranje dpll
def test_dpll(t):
    dpll_testi.test(t)


############        BARVANJE GRAFOV        ############
# testi:
Test0=(2,[(1,2)],2) # graf na dveh točkah
Test1=(6,[(1,2),(2,3),(3,4),(4,5),(5,6)],2) # veriga šestih točk
Test2=(4,[(1,2),(2,3),(3,4),(4,1)],2) # kvadrat
Test3=(4,[(1,2),(2,3),(3,4),(4,1),(1,3),(2,4)],2) # poln graf na 4 točkah
def barvanje():
    resitev = dpll.dpll(barvanje_grafov.barvanje_grafov(Test3[0],Test3[1],Test3[2]))
    for i in resitev[1].copy():
        if resitev[1][i]==False:
            del resitev[1][i]
    return resitev



# sudoku 4x4
def sudoku4x4():
    sudoku4x4_primeri.sudoku4x4_primeri()
    
            
############          SUDOKU  9x9          ############
# uporaba dpll na sudokuju 9x9
# testi:
TEst0='0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0' # prazen
TEst1='1 1 2 3 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0' # nerešljiv
TEst2='1 0 2 3 0 0 0 0 0,0 1 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0' # nerešljiv
TEst3='1 0 2 3 0 0 0 0 0,0 0 0 0 0 0 0 0 0,1 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0 0' # nerešljiv
TEst4='4 3 7 5 1 8 2 6 9,2 5 8 4 9 6 3 7 1,9 6 1 2 3 7 4 8 5,3 7 4 6 2 1 5 9 8,5 8 9 7 4 3 6 1 2,1 2 6 9 8 5 7 4 3,6 9 3 1 5 4 8 2 7,7 1 5 8 6 2 9 3 4,8 4 2 3 7 9 1 5 6' # poln sudoku
TEsti=[TEst0,TEst1,TEst2,TEst3,TEst4]
# primeri:
PRimer0='4 0 7 5 1 0 2 6 9,2 0 8 4 9 6 0 7 1,9 0 1 2 3 0 4 8 5,3 7 0 6 2 1 5 9 0,5 8 9 0 4 3 6 1 2,1 2 6 9 0 5 7 4 3,6 9 0 1 5 0 8 0 7,7 1 0 8 0 2 9 0 4,8 0 2 0 7 0 1 5 0' # "lahek"
PRimer1='4 0 7 5 0 0 2 6 0,2 0 8 0 9 6 0 7 1,9 0 1 0 3 0 4 8 5,0 7 0 6 2 1 5 9 0,5 0 9 0 4 3 0 1 2,1 0 6 9 0 5 7 4 3,0 9 0 1 5 0 8 0 7,0 1 0 8 0 2 9 0 4,8 0 2 0 7 0 1 0 0' # "srednja težavnost"
PRimer2='4 0 0 5 0 0 2 0 0,2 0 8 0 9 0 0 7 0,9 0 1 0 3 0 4 0 0,0 7 0 6 0 1 5 0 0,5 0 9 0 4 0 0 1 0,1 0 6 0 0 5 7 4 0,0 9 0 1 5 0 8 0 7,0 1 0 8 0 2 0 0 4,8 0 2 0 7 0 1 0 0' # "težek"
PRimer3='4 0 0 5 0 0 2 0 0,0 0 8 0 9 0 0 7 0,0 0 1 0 3 0 4 0 0,0 7 0 6 0 0 5 0 0,0 0 9 0 4 0 0 1 0,1 0 6 0 0 5 0 4 0,0 9 0 1 5 0 8 0 7,0 1 0 8 0 0 0 0 4,0 0 2 0 0 0 1 0 0' # "zelo težek"
PRimer4='8 0 0 0 0 0 0 0 0,0 0 3 6 0 0 0 0 0,0 7 0 0 9 0 2 0 0,0 5 0 0 0 7 0 0 0,0 0 0 0 4 5 7 0 0,0 0 0 1 0 0 0 3 0,0 0 1 0 0 0 0 6 8,0 0 8 5 0 0 0 1 0,0 9 0 0 0 0 4 0 0' # World's hardest sudoku (2012) :P
PRimeri=[PRimer0,PRimer1,PRimer2,PRimer3,PRimer4]
def sudoku9x9():
    print('Ta program resuje 9x9 sudoku.')
    
    # ponavljamo dokler uporabnik ne vpiše nekaj kar ni y/n
    while True:
        odlocitev=input('Ali zelis vpisati svoj sudoku? (y/n)  ')
        
        if odlocitev=='y' or odlocitev=='n':
            
            def risanje(resitev,besedilo=''):
                window=Tk()
                canvas=Canvas(window, width=580, height=600)
                canvas.pack()
                # besedilo na vrhu okenčka
                canvas.create_text(120,17,text=besedilo,font=('Arial',18))
                # vse ravne črte na platnu
                canvas.create_rectangle(20,40,560,580, width=3)
                canvas.create_line(80,40,80,580)
                canvas.create_line(140,40,140,580)
                canvas.create_line(260,40,260,580)
                canvas.create_line(320,40,320,580)
                canvas.create_line(440,40,440,580)
                canvas.create_line(500,40,500,580)
                canvas.create_line(200,40,200,580, width=3)
                canvas.create_line(380,40,380,580, width=3)
                canvas.create_line(20,100,560,100)
                canvas.create_line(20,160,560,160)
                canvas.create_line(20,280,560,280)
                canvas.create_line(20,340,560,340)
                canvas.create_line(20,460,560,460)
                canvas.create_line(20,520,560,520)
                canvas.create_line(20,220,560,220, width=3)
                canvas.create_line(20,400,560,400, width=3)
                # vstavimo cifre v sudoku
                for i in resitev.keys():
                    canvas.create_text(50+(i[1]-1)*60,70+(i[0]-1)*60,text='{0}'.format(i[2]),font=('Arial',30))  
                window.mainloop()
                
            # če uporabnik ne želi vpisati svojega sudokuja, mu program rešu sudoku iz datoteke Implementacija/sudoku4.txt
            if odlocitev=='n':
                f=open('Prevedbe_problemov/sudoku9.txt','r')
                f=f.readlines()
                # naredimo slovar 'narisi', s katerim narišemo sudoku, ki ga rešujemo in seznam 'seznam', tj. seznam znanih spremenljivk, ki jih vstavimo v program sudoku
                narisi={}
                seznam=[]
                for i in range(len(f)):
                    for j in range(0,17,2):
                        if f[i][j]!='0':
                            seznam.append((i+1,j//2+1,int(f[i][j])))
                            narisi[(i+1,j//2+1,int(f[i][j]))]=True
                risanje(narisi,'Rešujemo sudoku:')
                
            # če vpiše svoj sudoku ali želi rešitev dveh posebnih primerov zgoraj:
            if odlocitev=='y':
                print ('Sudoku naj bo oblike "1 2 0 0 0 0 0 0 0,0 0 0 3 4 0 0 0 0,...", kjer 0 pomeni, da je polje prazno.')
                sud=input('Vpisi svoj sudoku:  \n')
                if sud[:-1]=='test':
                    sud=TEsti[int(sud[-1])]
                if sud[:-1]=='primer':
                    sud=PRimeri[int(sud[-1])]
                sud=sud.split(',')
                narisi={}
                seznam=[]
                for i in range(len(sud)):
                    for j in range(0,17,2):
                        if sud[i][j]!='0':
                            seznam.append((i+1,j//2+1,int(sud[i][j])))
                            narisi[(i+1,j//2+1,int(sud[i][j]))]=True
                risanje(narisi,'Rešujemo sudoku:')
                
            # rešimo sudoku in vrnemo 'Ni rešitve' če ni rešljiv, oz. narišemo rešitev, če je rešljiv
            t1=time.clock()
            resitev=dpll.dpll(sudoku9.sudoku9(seznam))
            t2=time.clock()
            print('Tvoj sudoku sem reševal {0} sekund.'.format(t2-t1))
            if resitev[0]=='Ni rešitve':
                print ('Ta sudoku ni rešljiv.')
            
            else:
                for i in resitev[1].copy():
                    if resitev[1][i]==False:
                        del resitev[1][i]
                risanje(resitev[1],'Rešen sudoku:')
            
        else:
            break           
                
    
