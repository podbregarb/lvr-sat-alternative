# -*- encoding: utf-8 -*-

from bool import *
from cnf import *

def barvanje_grafov(V,E,k):
    # V je stevilo vozlisc
    # E je seznam parov (vozlisca, ki so med sabo povezana)
    # k je stevilo barv

    # vsako vozlisce ima vsaj eno barvo
    r=[]
    for i in range(1,V+1):
        r1=[]
        for j in range(1,k+1):
            r1.append(Atom((i,j)))
        r.append(Or(r1))

    # nobeno vozlisce ni pobarvano z dvema barvama
    s=[]
    for i in range(1,V+1):
        for l in range (1,k+1):
            for j in range(1,l):
                s.append(Not(And([Atom((i,j)),Atom((i,l))])))

    # sosednji vozlisci nista pobarvani z enako barvo
    t=[]
    for i in E:
        for j in range(1,k+1):
            t1=Not(And([Atom((i[0],j)),Atom((i[1],j))]))
        t.append(t1)
        
    return And(r+s+t)
                
