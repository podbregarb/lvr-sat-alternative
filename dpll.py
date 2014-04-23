from bool import *
from cnf import *

def dpll(formula):
    formula=formula.cnf()
    znane_spr={}
    neznane_spr=[]
    spr=[]
    for j in range(0,len(formula.stavki)):
        for k in range(0,len(formula.stavki[j].literali)):
            neznane_spr = neznane_spr + [str(formula.stavki[j].literali[k].ime)]
            if str(formula.stavki[j].literali[k].ime) not in spr:
                spr = spr + [str(formula.stavki[j].literali[k].ime)]
    # CS je seznam še neobdelanih stavkov
    CS1=formula.stavki
    CS=list(CS1)
    for i in CS1:
        if i.literali==[]:
            print ("Ni rešitve.")
            break
        if len(i.literali)==1:
            if isinstance(i.literali[0],Lit):
                znane_spr[i.literali[0].ime]=Tru
                neznane_spr.remove(i.literali[0].ime)
                for k in CS1:
                    for j in k.literali:
                        if j.ime==i.literali[0].ime and isinstance(j,Lit) and k in CS:
                            CS.remove(k)
                        if isinstance(j,Til) and j.ime==i.literali[0].ime and k in CS:
                            r=CS.index(k)
                            CS[r].literali.remove(j)
            else:
                znane_spr[i.literali[0].ime]=Fls
                neznane_spr.remove(i.literali[0].ime)
                for k in CS1:
                    for j in k.literali:
                        if isinstance(j,Til) and j.ime==i.literali[0].ime and k in CS:
                            CS.remove(k)
                        if j.ime==i.literali[0].ime and isinstance(j,Lit) and k in CS:
                            r=CS.index(k)
                            CS[r].literali.remove(j)
    print(znane_spr)
    return CS
    
f=And([Or([Atom('a')]),Or([Atom('b'),Atom('c'),Atom('a')]),Or([Atom('c'),Atom('d'),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Atom('a')])])
g=And([Or([Not(Atom('a'))]),Or([Atom('b'),Atom('c'),Atom('a')]),Or([Atom('c'),Atom('d'),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Not(Atom('a'))])])
h=And([Or([Atom('a')]),Or([Atom('b'),Atom('c'),Atom('d')]),Or([Atom('c'),Atom('a'),Atom('b')]),Or([Not(Atom('b'))])])
test=And([Or([Atom('a')]),Or([Not(Atom('a'))])])           
            
