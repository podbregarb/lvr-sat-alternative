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
    print ('Lahko vpises svoj 4x4x sudoku v obliki [[1. vrstica],[2. vrstica],...]. Polja, ki so prazna naj vsebujejo stevilo 0. Ce ne zelis vpisati svojega sudokuja, bo program resil nekaj vnaprej dolocenih primerov, ki so v Prevedbe_problemov/sudoku4.txt.')
    odlocitev=input('Ali zelis vpisati svoj sudoku? (y/n)  ')
    if odlocitev=='n':
        f=open('Prevedbe_problemov/sudoku4.txt','r')
        f=f.readlines()
        seznam=[]
        for i in range(len(f)):
            for j in range(0,7,2):
                if f[i][j]!='0':
                    seznam.append((i+1,j//2+1,int(f[i][j])))
## to se delam: :D
##    else:
##        sud=input('Vpisi svoj sudoku:  \n')
##        sud=sud[1:-1].split('[')
##        print(sud)
    resitev=dpll.dpll(sudoku.sudoku4(seznam))[1]
    for i in resitev.copy():
        if resitev[i]==False:
            del resitev[i]
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
    return risanje(resitev)
            
                    
                
    
