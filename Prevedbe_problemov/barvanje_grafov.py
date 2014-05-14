# -*- encoding: utf-8 -*-

import Implementacija.cnf as cnf
import Implementacija.bool as bool

def barvanje_grafov(V,E,k):
    # V je stevilo vozlisc
    # E je seznam parov (vozlisca, ki so med sabo povezana)
    # k je stevilo barv

    # vsako vozlisce ima vsaj eno barvo
    r=[]
    for i in range(1,V+1):
        r1=[]
        for j in range(1,k+1):
            r1.append(bool.Atom((i,j)))
        r.append(bool.Or(r1))

    # nobeno vozlisce ni pobarvano z dvema barvama
    s=[]
    for i in range(1,V+1):
        for l in range (1,k+1):
            for j in range(1,l):
                s.append(bool.Not(bool.And([bool.Atom((i,j)),bool.Atom((i,l))])))

    # sosednji vozlisci nista pobarvani z enako barvo
    t=[]
    for i in E:
        for j in range(1,k+1):
            # t1=bool.Not(bool.And([bool.Atom((i[0],j)),bool.Atom((i[1],j))]))
            t.append(bool.Not(bool.And([bool.Atom((i[0],j)),bool.Atom((i[1],j))])))
        #t.append(t1)
        
    return bool.And(r+s+t)
                
