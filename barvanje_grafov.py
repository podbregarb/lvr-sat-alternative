from bool import *
from cnf import *

def barvanje_grafov(V,E,k):
    #V je stevilo vozlisc
    #E je seznam parov (vozlisca, ki so med sabo povezana)
    #k je stevilo barv
    r=[]
    for i in range(1,V+1):
        r1=[]
        for j in range(1,k+1):
            r1.append(Atom((i,j)))
        r.append(Or(r1))
    
    s=[]
    for i in range(1,V+1):
        for l in range (1,k+1):
            for j in range(1,l):
                s.append(Not(And([Atom((i,j)),Atom((i,l))])))

    t=[]
    for i in E:
        t1=[]
        for j in range(1,k+1):
            t1=And([Atom((i[0],j)),Atom((i[1],j))])
        t.append(Not(t1))
        
    return And(r+s+t)
                
