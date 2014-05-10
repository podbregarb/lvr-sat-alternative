# -*- encoding: utf-8 -*-

import Implementacija.bool as bool
import Implementacija.cnf as cnf


def sudoku4(seznam):
    # seznam je seznam trojk (i,j,k) - na i,j - tem mestu je cifra k


    # znane predstavlja seznam znanih cifer
    znane=[]
    for i in seznam:
        znane.append(bool.Atom((i)))

    r=[]
    # vsako polje ima vsaj eno cifro
    for i in range(1,5):
        for j in range(1,5):
            r2=[]
            for k in range(1,5):
                r2.append(bool.Atom((i,j,k)))
            r.append(bool.Or(r2))

            
    # nobeno polje nima več kot eno cifro
    for i in range(1,5):
        for j in range (1,5):
            for k in range(1,5):
                for l in range(1,k):
                    r.append(bool.Not(bool.And([bool.Atom((i,j,k)),bool.Atom((i,j,l))])))

                    
    # v nobeni vrstici/stolpcu ni istih cifer
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,j):
                for l in range(1,5):
                    r.append(bool.Or([bool.Not(bool.Atom((i,j,l))),bool.Not(bool.Atom((i,k,l)))]))
                    r.append(bool.Or([bool.Not(bool.Atom((j,i,l))),bool.Not(bool.Atom((k,i,l)))]))


    # v nobenem 2x2 kvadratku ni istih cifer
    for x in range(0,2):
        for y in range(0,2):
                for l in range(1,5):
                    r.append(bool.Or([bool.Not(bool.Atom((1+x*2,1+y*2,l))),bool.Not(bool.Atom((1+x*2,2+y*2,l)))]))
                    r.append(bool.Or([bool.Not(bool.Atom((1+x*1,1+y*2,l))),bool.Not(bool.Atom((2+x*2,1+y*2,l)))]))
                    r.append(bool.Or([bool.Not(bool.Atom((1+x*2,1+y*2,l))),bool.Not(bool.Atom((2+x*2,2+y*2,l)))]))
                    r.append(bool.Or([bool.Not(bool.Atom((1+x*2,2+y*2,l))),bool.Not(bool.Atom((2+x*2,1+y*2,l)))]))
                    r.append(bool.Or([bool.Not(bool.Atom((1+x*2,2+y*2,l))),bool.Not(bool.Atom((2+x*2,2+y*2,l)))]))
                    r.append(bool.Or([bool.Not(bool.Atom((2+x*2,1+y*2,l))),bool.Not(bool.Atom((2+x*2,2+y*2,l)))]))

                                                          
    return bool.And(znane+r)
