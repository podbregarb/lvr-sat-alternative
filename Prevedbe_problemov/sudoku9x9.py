# -*- encoding: utf-8 -*-

import Implementacija.bool as bool
import Implementacija.cnf as cnf


def sudoku9(seznam):
    # seznam je seznam trojk (i,j,k) - na i,j - tem mestu je cifra k


    # znane predstavlja seznam znanih cifer
    znane=[]
    for i in seznam:
        znane.append(bool.Atom((i)))

    r=[]
    # vsako polje ima vsaj eno cifro
    for i in range(1,10):
        for j in range(1,10):
            r2=[]
            for k in range(1,10):
                r2.append(bool.Atom((i,j,k)))
            r.append(bool.Or(r2))

            
    # nobeno polje nima več kot eno cifro
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                for l in range(1,k):
                    r.append(bool.Or([bool.Not(bool.Atom((i,j,k))),bool.Not(bool.Atom((i,j,l)))]))

                    
    # v nobeni vrstici/stolpcu ni istih cifer
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,j):
                for l in range(1,10):
                    r.append(bool.Or([bool.Not(bool.Atom((i,j,l))),bool.Not(bool.Atom((i,k,l)))]))
                    r.append(bool.Or([bool.Not(bool.Atom((j,i,l))),bool.Not(bool.Atom((k,i,l)))]))


    # v nobenem 3x3 kvadratku ni istih cifer
    for x in range(0,3):
        for y in range(0,3):
            for i in range(1,4):
                for j in range(1,4):
                    for m in range(1,i+1):
                        if m<i:
                            for n in range(1,4):
                                for l in range(1,10):
                                    r.append(bool.Or([bool.Not(bool.Atom((i+x*3,j+y*3,l))),bool.Not(bool.Atom((m+x*3,n+y*3,l)))]))
                        if m==i:                            
                            for n in range(1,j):
                                for l in range(1,10):
                                    r.append(bool.Or([bool.Not(bool.Atom((i+x*3,j+y*3,l))),bool.Not(bool.Atom((m+x*3,n+y*3,l)))]))

                                  
    return bool.And(znane+r)
# primer=[(1,1,5),(1,2,3),(1,5,7),(2,1,6),(2,4,1),(2,5,9),(2,6,5),(3,2,9),(3,3,8),(3,8,6),(4,1,8),(4,5,6),(4,9,3),(5,1,4),(5,4,8),(5,6,3),(5,9,1),(6,1,7),(6,5,2),(6,9,6),(7,2,6),(7,7,2),(7,8,8),(8,4,4),(8,5,1),(8,6,9),(8,9,5),(9,5,8),(9,8,7),(9,9,9)]
