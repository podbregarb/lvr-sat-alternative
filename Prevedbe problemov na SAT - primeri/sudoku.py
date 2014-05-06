from bool import *
from cnf import *

def sudoku(seznam):
    # seznam je seznam trojk (i,j,k) - na i,j - tem mestu je cifra k


    # znane predstavlja seznam znanih cifer
    znane=[]
    for i in seznam:
        znane.append(Atom((i)))


    # vsako polje ima vsaj eno cifro
    r=[]
    for i in range(1,10):
        for j in range(1,10):
            r2=[]
            for k in range(1,10):
                r2.append(Atom((i,j,k)))
            r.append(Or(r2))

            
    # nobeno polje nima več kot eno cifro
    s=[]
    for i in range(1,10):
        for j in range (1,10):
            for k in range(1,10):
                for l in range(1,k):
                    s.append(Not(And([Atom((i,j,k)),Atom((i,j,l))])))

                    
    # v nobeni vrstici/stolpcu ni istih cifer
    t=[]
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,j):
                for l in range(1,10):
                    t1=Not(Or([And([Atom((i,j,l)),Atom((i,k,l))]),And([Atom((j,i,l)),Atom((k,i,l))])]))
        t.append(t1)


    # v nobenem 3x3 kvadratku ni istih cifer
    v=[]
    for x in range(0,3):
        for y in range(0,3):
            for i in range(1,4):
                for j in range(1,4):            
                    for l in range(1,10):
                        w=Not(Or([And([Atom((i+x*3,j+y*3,l)),Atom((i+x*3,l+y*3,l))])]))
                    v.append(w)
                                  

    return And(r+s+t+v+znane)


primer=[(1,1,5),(1,2,3),(1,5,7),(2,1,6),(2,4,1),(2,5,9),(2,6,5),(3,2,9),(3,3,8),(3,8,6),(4,1,8),(4,5,6),(4,9,3),(5,1,4),(5,4,8),(5,6,3),(5,9,1),(6,1,7),(6,5,2),(6,9,6),(7,2,6),(7,7,2),(7,8,8),(8,4,4),(8,5,1),(8,6,9),(8,9,5),(9,5,8),(9,8,7),(9,9,9)]
