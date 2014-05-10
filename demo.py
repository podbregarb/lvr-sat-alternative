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



# zažene funkcijo primer iz programa primer.py (iz mape Implementacija)
def osnove():
    primer.primer()

# za testiranje dpll
def test_dpll():
    dpll_testi.test()

# uporaba dpll na sudokuju in barvanju grafov
def sudoku4x4():
    print('Ta program resuje 4x4 sudoku.')
    ven=True
    while ven:
        odlocitev=input('Ali zelis vpisati svoj sudoku? (y/n)  ')
        if odlocitev=='y' or odlocitev=='n':
            def risanje(resitev):
                window=Tk()
                canvas=Canvas(window, width=200, height=200)
                canvas.pack()
                canvas.create_rectangle(15,15,185,185, width=3)
                canvas.create_line(60,15,60,185)
                canvas.create_line(100,15,100,185, width=3)
                canvas.create_line(140,15,140,185)
                canvas.create_line(15,140,185,140)
                canvas.create_line(15,60,185,60)
                canvas.create_line(15,100,185,100, width=3)
                for i in resitev.keys():
                    canvas.create_text(i[1]*40,i[0]*40,text='{0}'.format(i[2]),font=('Arial',25))  
                window.mainloop()
            if odlocitev=='n':
                f=open('Prevedbe_problemov/sudoku4.txt','r')
                f=f.readlines()
                seznam=[]
                for i in range(len(f)):
                    for j in range(0,7,2):
                        if f[i][j]!='0':
                            seznam.append((i+1,j//2+1,int(f[i][j])))
        ## to se delam: :D
            if odlocitev=='y':
                print ('Sudoku naj bo oblike "1 2 0 0,0 3 4 0,...", kjer 0 pomeni, da je polje prazno.')
                sud=input('Vpisi svoj sudoku:  \n')
                sud=sud.split(',')
                seznam=[]
                for i in range(len(sud)):
                    for j in range(0,7,2):
                        if sud[i][j]!='0':
                            seznam.append((i+1,j//2+1,int(sud[i][j])))

            resitev=dpll.dpll(sudoku.sudoku4(seznam))[1]
            for i in resitev.copy():
                if resitev[i]==False:
                    del resitev[i]
            risanje(resitev)
        else:
            break
            
                    
                
    
