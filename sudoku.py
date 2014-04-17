from bool import *
from cnf import *

def sudoku(seznam):
    # seznam je seznam (i,j,k) - na i,j - tem mestu je stevilka k


    # banana predstavlja seznam vnaprej poznanih cifer/spremenljivk
    banana=[]
    for i in seznam:
        banana.append(Atom((i)))



    # vsako polje ima vsaj eno cifro
    r=[]
    for i in range(1,10):
        for j in range(1,10):
            r2=[]
            for k in range(1,10):
                r2.append(Atom((i,j,k)))
            r.append(Or(r2))

            
    # nima hkrati dveh cifer na istem mestu
    s=[]
    for i in range(1,10):
        for j in range (1,10):
            for k in range(1,10):
                for l in range(1,k):
                    s.append(Not(And([Atom((i,j,k)),Atom((i,j,l))])))

                    
    # v vrstici/stolpcu ni dveh istih cifer
    t=[]
    for i in range(1,10):
        for j in range(1,10):
            for l in range(1,10):
                for k in range(1,10):
                    t1=Not(Or([And([Atom((i,j,k)),Atom((i,l,k))]),And([Atom((i,j,k)),Atom((l,j,k))])]))
        t.append(t1)


    # v vsakem 3x3 kvadratku :) ni dveh dveh istih cifer
    luka=[]
    for alenka in range(0,3):
        for i in range(1,4):
            for j in range(1,4):
                for l in range(1,4):
                    for barbka in range(1,10):
                        luka1=Not(Or([And([Atom((i+alenka*3,j+alenka*3,barbka)),Atom((i+alenka*3,l+alenka*3,barbka))]),And([Atom((i+alenka*3,j+alenka*3,barbka)),Atom((l+alenka*3,j+alenka*3,barbka))])]))
        luka.append(luka1)
                                  

    return And(r+s+t+luka+banana)


primer=[(1,1,5),(1,2,3),(1,5,7),(2,1,6),(2,4,1),(2,5,9),(2,6,5),(3,2,9),(3,3,8),(3,8,6),(4,1,8),(4,5,6),(4,9,3),(5,1,4),(5,4,8),(5,6,3),(5,9,1),(6,1,7),(6,5,2),(6,9,6),(7,2,6),(7,7,2),(7,8,8),(8,4,4),(8,5,1),(8,6,9),(8,9,5),(9,5,8),(9,8,7),(9,9,9)]
