# uvozimo vse potrebne programe
import Implementacija.cnf as cnf
import Implementacija.bool as bool
import Implementacija.primer as primer

import Dpll.dpll as dpll
import Dpll.dpll_testi as dpll_testi

import Prevedbe_problemov.barvanje_grafov as barvanje_grafov
import Prevedbe_problemov.sudoku_demo as sudoku_demo

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



############        SUDOKU        ############
def sudoku4x4():
    sudoku_demo.sudoku_demo(4,sudoku_demo.testi,sudoku_demo.primeri)
      
def sudoku9x9():
    sudoku_demo.sudoku_demo(9,sudoku_demo.TEsti,sudoku_demo.PRimeri)
    
