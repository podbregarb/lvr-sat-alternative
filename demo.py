# uvozimo vse potrebne programe
import Implementacija.cnf as cnf
import Implementacija.bool as bool
import Implementacija.primer as primer

import Dpll.dpll as dpll
import Dpll.dpll_testi as dpll_testi

import Prevedbe_problemov.barvanje_grafov_demo as barvanje_grafov_demo
import Prevedbe_problemov.sudoku_demo as sudoku_demo

import copy
from tkinter import *
import time
from random import *

# zažene funkcijo primer iz programa primer.py (iz mape Implementacija)
def osnove():
    primer.primer()

# za testiranje dpll
def test_dpll(t):
    dpll_testi.test(t)


### BARVANJE GRAFOV ###
def barvanje():
    return barvanje_grafov_demo.primeri()

def barval_bi_sam(V,E,k):
    return barvanje_grafov_demo.bedno_barvanje(V,E,k)

    

###   SUDOKU   ###
def sudoku4x4():
    sudoku_demo.sudoku_demo(4,sudoku_demo.testi,sudoku_demo.primeri)
      
def sudoku9x9():
    sudoku_demo.sudoku_demo(9,sudoku_demo.TEsti,sudoku_demo.PRimeri)
    
