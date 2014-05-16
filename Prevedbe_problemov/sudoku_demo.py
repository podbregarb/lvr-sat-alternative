# -*- encoding: utf-8 -*-

import Implementacija.bool as bool
import Implementacija.cnf as cnf
import Dpll.dpll as dpll
from . import sudoku4x4
from . import sudoku9x9

import copy
from tkinter import *
import time

# uporaba dpll na sudokuju 4x4
# testi:
test0='0 0 0 0,0 0 0 0,0 0 0 0,0 0 0 0' # prazen
test1='1 1 2 3,0 0 0 0,0 0 0 0,0 0 0 0' # nerešljiv
test2='1 0 2 3,0 1 0 0,0 0 0 0,0 0 0 0' # nerešljiv
test3='1 0 2 3,0 0 0 0,1 0 0 0,0 0 0 0' # nerešljiv
test4='1 2 3 4,3 4 1 2,4 3 2 1,2 1 4 3' # poln
testi=[test0,test1,test2,test3,test4]

# primeri:
primer0='1 2 0 4,3 4 0 2,4 3 2 1,0 1 4 3' # zelo lahek
primer1='1 2 0 4,3 4 0 2,4 0 2 1,0 1 4 0' # lahek
primer2='0 2 0 4,0 4 0 2,4 0 2 1,0 1 4 0' # srednje težki
primer3='0 2 0 4,0 4 0 2,4 0 2 0,0 1 0 0' # težji
primeri=[primer0,primer1,primer2,primer3]


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

def sudoku_demo(s,testi,primeri):
    # s=4 ali 9: določa ali želimo reševati 9x9 ali 4x4 sudoku
    print('Ta program resuje {0}x{0} sudoku.'.format(s))
    
    # ponavljamo dokler uporabnik ne vpiše nekaj kar ni y/n
    while True:
        odlocitev=input('Ali zelis vpisati svoj sudoku? (y/n)  ')
        
        if odlocitev=='y' or odlocitev=='n':
            
            def risanje(s,resitev,besedilo=''):
                window=Tk()
                if s==4:
                    canvas=Canvas(window, width=280, height=300)
                if s==9:
                    canvas=Canvas(window, width=580, height=600)
                canvas.pack()
                # besedilo na vrhu okenčka
                canvas.create_text(120,17,text=besedilo,font=('Arial',18))
                if s==4:
                    # vse ravne črte na platnu
                    canvas.create_rectangle(20,40,260,280, width=3)
                    canvas.create_line(140,40,140,280, width=3)
                    canvas.create_line(20,160,260,160, width=3)
                    for i in range(2):   
                        canvas.create_line(80+i*120,40,80+i*120,280)
                        canvas.create_line(20,100+i*120,260,100+i*120)
                if s==9:
                    # vse ravne črte na platnu
                    canvas.create_rectangle(20,40,560,580, width=3)
                    for i in [0,1,3,4,6,7]:
                        canvas.create_line(80+i*60,40,80+i*60,580)
                        canvas.create_line(20,100+i*60,560,100+i*60)
                    for j in range(2):
                        canvas.create_line(200+j*180,40,200+j*180,580, width=3)
                        canvas.create_line(20,220+j*180,560,220+j*180, width=3)
                # vstavimo cifre v narisana polja
                for i in resitev.keys():
                    canvas.create_text(50+(i[1]-1)*60,70+(i[0]-1)*60,text='{0}'.format(i[2]),font=('Arial',30))  
                window.mainloop()
                
            # če uporabnik ne želi vpisati svojega sudokuja, mu program rešu sudoku iz datoteke Implementacija/sudoku4.txt
            if odlocitev=='n':
                if s==4:
                    f=open('Prevedbe_problemov/sudoku4.txt','r')
                if s==9:
                    f=open('Prevedbe_problemov/sudoku9.txt','r')
                f=f.readlines()
                # naredimo slovar 'narisi', s katerim narišemo sudoku, ki ga rešujemo in seznam 'seznam', tj. seznam znanih spremenljivk, ki jih vstavimo v program sudoku
                narisi={}
                seznam=[]
                for i in range(len(f)):
                    for j in range(0,2*s-1,2):
                        if f[i][j]!='0':
                            seznam.append((i+1,j//2+1,int(f[i][j])))
                            narisi[(i+1,j//2+1,int(f[i][j]))]=True
                risanje(s,narisi,'Rešujemo sudoku:')
                
            # če vpiše svoj sudoku ali želi rešitev dveh posebnih primerov zgoraj:
            if odlocitev=='y':
                if s==4:
                    print ('Sudoku naj bo oblike "1 2 0 0,0 3 4 0,...", kjer 0 pomeni, da je polje prazno.')
                if s==9:
                    print ('Sudoku naj bo oblike "1 2 0 0 0 0 0 0 0,0 0 0 3 4 0 0 0 0,...", kjer 0 pomeni, da je polje prazno.')
                sud=input('Vpisi svoj sudoku:  \n')
                if sud[:-1]=='test':
                        sud=testi[int(sud[-1])]
                if sud[:-1]=='primer':
                        sud=primeri[int(sud[-1])]
                sud=sud.split(',')
                narisi={}
                seznam=[]
                for i in range(len(sud)):
                    for j in range(0,2*s-1,2):
                        if sud[i][j]!='0':
                            seznam.append((i+1,j//2+1,int(sud[i][j])))
                            narisi[(i+1,j//2+1,int(sud[i][j]))]=True
                risanje(s,narisi,'Rešujemo sudoku:')
                
            # rešimo sudoku in vrnemo 'Ni rešitve' če ni rešljiv, oz. narišemo rešitev, če je rešljiv
            t1=time.clock()
            if s==4:
                resitev=dpll.dpll(sudoku4x4.sudoku4(seznam))
            if s==9:
                resitev=dpll.dpll(sudoku9x9.sudoku9(seznam))
            t2=time.clock() 

            if resitev[0]=='Ni rešitve':
                print ('Ta sudoku ni rešljiv. \n')
            
            else:
                for i in resitev[1].copy():
                    if resitev[1][i]==False:
                        del resitev[1][i]
                print('Tvoj sudoku sem reševal {0} sekund. \n'.format(t2-t1))
                risanje(s,resitev[1],'Rešen sudoku:')
            
        else:
            break       
