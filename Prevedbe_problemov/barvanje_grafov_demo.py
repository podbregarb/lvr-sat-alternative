# -*- encoding: utf-8 -*-

import Implementacija.bool as bool
import Implementacija.cnf as cnf
import Dpll.dpll as dpll
from . import barvanje_grafov

import copy
from tkinter import *
import time


# uporaba dpll na barvanju_grafov
# primeri:
pr0=(1,[],2)
pr1=(2,[(1,2)],3) # graf na dveh točkah
pr2=(6,[(1,2),(2,3),(3,4),(4,5),(5,6)],3) # veriga šestih točk
pr3=(4,[(1,2),(2,3),(3,4),(4,1)],3) # kvadrat
pr4=(4,[(1,2),(2,3),(3,4),(4,1),(1,3),(2,4)],5) # poln graf na 4 točkah
pr5=(12,[(1,3),(1,4),(1,10),(1,11),(1,2),(2,3),(2,6),(2,11),(2,12),(3,4),(3,5),(3,6),(4,5),(4,7),(4,10),(5,6),(5,7),(5,8),(6,8),(6,12),(7,8),(7,9),(7,10),(8,9),(8,12),(9,10),(9,11),(9,12),(11,10),(11,12)],4)
pr6=(10,[(1,5),(1,2),(1,3),(2,4),(2,9),(3,7),(3,8),(5,6),(5,10),(4,6),(4,8),(6,7),(7,9),(8,10),(9,10)],4) #Petersenov graf (ni 2, je 3-obarljiv)
pr7=(6,[(1,2),(1,3),(1,4),(1,6),(2,3),(2,6),(2,5),(3,5),(3,4),(4,6),(4,5),(5,6)],4) #(ni 2, je 3-obarljiv)
pr8=(8,[(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,1),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7)],5) # je 4-obarljiv
pr9=(20,[(1,2),(2,3),(3,4),(4,5),(5,1),(5,14),(1,6),(2,8),(3,10),(4,12),(14,15),(15,6),(6,7),(7,8),(8,9),(9,10),(10,11),(11,12),(12,13),(13,14),(15,20),(7,16),(9,17),(11,18),(13,19),(19,20),(20,16),(16,17),(17,18),(18,19)],4)
pr=[pr0,pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8,pr9]


def bedno_barvanje(V,E,k,risanje=0):
    
    # risanje
    def risanje(resitev,V,E,k):
        window=Tk()
        canvas=Canvas(window, width=50*V+20, height=50*V+20)
        canvas.configure(background="white")
        canvas.pack()
        xkoord=list(range(20,50*V,40))
        ykoord=[(50*V+20)/2]*V
        for i in range(0,len(ykoord),2):
            ykoord[i]+=(50*randint(0,V)+20)/3
        for i in range(1,len(ykoord),2):
            ykoord[i]-=(50*randint(0,V)+20)/3
        koordinate=[]
        for i in range(V):
            koordinate.append([i+1,[xkoord[i],ykoord[i]]])
        for (i,j) in E:
            koord=koordinate[:]
            x,y,u,v,a=koord[i-1][1][0],koord[i-1][1][1],koord[j-1][1][0],koord[j-1][1][1],5
            if x<u: x,u=x+a,u-a
            if x>u: x,u=x-a,u+a
            if y<v: y,v=y+a,v-a
            if y>v: y,v=y-a,v+a
            canvas.create_line(x,y,u,v,width=2)
        barve=[sample(range(0,255,40),3) for i in range(k)]
        for i in koordinate[:]:
            for (j,k) in list(resitev.keys()):
                if i[0]==j:
                    b=10
                    canvas.create_oval(i[1][0]-b,i[1][1]-b,i[1][0]+b,i[1][1]+b,fill='#%02x%02x%02x' % (barve[k-1][0],barve[k-1][1],barve[k-1][2]))
                    canvas.create_text(i[1][0],i[1][1],text='{0}'.format(i[0]),font=('Arial',12))
                    koordinate.remove(i)
        for i in koordinate:
            canvas.create_text(i[1][0],i[1][1],text='{0}'.format(i[0]),font=('Arial',14,'bold'))
        window.mainloop()

    #rešimo problem barvanja
    t1=time.clock()
    resitev = dpll.dpll(barvanje_grafov.barvanje_grafov(V,E,k))
    t2=time.clock()

    if resitev[0]=='Ni rešitve':
        print('  Ta graf ni {0} obarljiv. \n'.format(k))
        
    else:
        print('  Ta graf je {0} obarljiv.'.format(k))
        for i in resitev[1].copy():
            if resitev[1][i]==False:
                del resitev[1][i]
        izpis=[[] for i in range(k)]
        for (i,j) in list(resitev[1].keys()):
            izpis[j-1].append(i)
            izpis[j-1].sort()
        izpis.sort()
        for i in izpis[:]:
            if i==[]: izpis.remove(i)
        for i in range(len(izpis)):
            print('  Vozlišča {0} so pobarvana s/z {1}. barvo.'.format(izpis[i],i+1))
        print('  Tvoj graf sem barval {0} sekund. \n'.format(t2-t1))
        
        if risanje==1:
            risanje(resitev[1],V,E,k)
        
def primeri():
    for i in range(len(pr)):
        print('Primer{0}:'.format(i))
        for j in range(1,pr[i][2]+1):
            bedno_barvanje(pr[i][0],pr[i][1],j)
        print('--------------------------------------------------------------------------')









