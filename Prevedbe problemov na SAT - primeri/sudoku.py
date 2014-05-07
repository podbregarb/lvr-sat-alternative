# -*- encoding: utf-8 -*-

from bool import *
from cnf import *

def sudoku(seznam):
    # seznam je seznam trojk (i,j,k) - na i,j - tem mestu je cifra k


    # znane predstavlja seznam znanih cifer
    znane=[]
    for i in seznam:
        znane.append(Atom((i)))

    r=[]
    # vsako polje ima vsaj eno cifro
    for i in range(1,10):
        for j in range(1,10):
            r2=[]
            for k in range(1,10):
                r2.append(Atom((i,j,k)))
            r.append(Or(r2))

            
    # nobeno polje nima več kot eno cifro
    for i in range(1,10):
        for j in range (1,10):
            for k in range(1,10):
                for l in range(1,k):
                    r.append(Not(And([Atom((i,j,k)),Atom((i,j,l))])))

                    
    # v nobeni vrstici/stolpcu ni istih cifer
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,j):
                for l in range(1,10):
                    r.append(Or([Not(Atom((i,j,l))),Not(Atom((i,k,l)))]))
                    r.append(Or([Not(Atom((j,i,l))),Not(Atom((k,i,l)))]))


##    # v nobenem 3x3 kvadratku ni istih cifer
##    for x in range(0,3):
##        for y in range(0,3):
##            for i in range(1,4):
##                for j in range(1,4):            
##                    for l in range(1,10):
##                        w=Not(Or([And([Atom((i+x*3,j+y*3,l)),Atom((i+x*3,l+y*3,l))])]))
##                    v.append(w)
##                                  
##
##    return And(r+s+t+v+znane)
# primer=[(1,1,5),(1,2,3),(1,5,7),(2,1,6),(2,4,1),(2,5,9),(2,6,5),(3,2,9),(3,3,8),(3,8,6),(4,1,8),(4,5,6),(4,9,3),(5,1,4),(5,4,8),(5,6,3),(5,9,1),(6,1,7),(6,5,2),(6,9,6),(7,2,6),(7,7,2),(7,8,8),(8,4,4),(8,5,1),(8,6,9),(8,9,5),(9,5,8),(9,8,7),(9,9,9)]


def sudoku2(seznam):
    # seznam je seznam trojk (i,j,k) - na i,j - tem mestu je cifra k


    # znane predstavlja seznam znanih cifer
    znane=[]
    for i in seznam:
        znane.append(Atom((i)))

    r=[]
    # vsako polje ima vsaj eno cifro
    for i in range(1,5):
        for j in range(1,5):
            r2=[]
            for k in range(1,5):
                r2.append(Atom((i,j,k)))
            r.append(Or(r2))

            
    # nobeno polje nima več kot eno cifro
    for i in range(1,5):
        for j in range (1,5):
            for k in range(1,5):
                for l in range(1,k):
                    r.append(Not(And([Atom((i,j,k)),Atom((i,j,l))])))

                    
    # v nobeni vrstici/stolpcu ni istih cifer
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,j):
                for l in range(1,5):
                    r.append(Or([Not(Atom((i,j,l))),Not(Atom((i,k,l)))]))
                    r.append(Or([Not(Atom((j,i,l))),Not(Atom((k,i,l)))]))


    # v nobenem 2x2 kvadratku ni istih cifer
    for x in range(0,2):
        for y in range(0,2):
                for l in range(1,5):
                    r.append(Or([Not(Atom((1+x*2,1+y*2,l))),Not(Atom((1+x*2,2+y*2,l)))]))
                    r.append(Or([Not(Atom((1+x*1,1+y*2,l))),Not(Atom((2+x*2,1+y*2,l)))]))
                    r.append(Or([Not(Atom((1+x*2,1+y*2,l))),Not(Atom((2+x*2,2+y*2,l)))]))
                    r.append(Or([Not(Atom((1+x*2,2+y*2,l))),Not(Atom((2+x*2,1+y*2,l)))]))
                    r.append(Or([Not(Atom((1+x*2,2+y*2,l))),Not(Atom((2+x*2,2+y*2,l)))]))
                    r.append(Or([Not(Atom((2+x*2,1+y*2,l))),Not(Atom((2+x*2,2+y*2,l)))]))

                                                          
    return And(r+znane)
