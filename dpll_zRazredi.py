from bool import *
from cnf import *

def dpll1(formula,znane_spr={}):
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
            return "Ni rešitve."
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
                            [CS,znane_spr]=dpll1(Cnf(CS),znane_spr)
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
                            [CS,znane_spr]=dpll1(Cnf(CS),znane_spr)

    # 
    # 1. tocka na listu
##    for i in CS:
##        if CS.count(i)>1:
##            CS.remove(i)
##
##    # 2. tocka na listu
##    for i in CS:
##        for j in range(0,len(i.literali)):
##            if i.literali.count(i.literali[j])>1:
##                i.literali.remove(i.literali[j])

    return [CS,znane_spr]


    

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
    [CS,znane_spr]=dpll1(formula)
    se_nedolocene=list(spr)
    for i in znane_spr.keys():
        se_nedolocene.remove(i)
    print(se_nedolocene)
    
    if dpll1(formula)[0]==[]:
        print(dpll1(formula)[1])
        return 'Formula je izpolnljiva.'
    


f=And([Or([Atom('a')]),Or([Atom('b'),Atom('c'),Atom('a')]),Or([Atom('c'),Atom('d'),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Atom('a')])])
g=And([Or([Not(Atom('a'))]),Or([Atom('b'),Atom('c'),Atom('a')]),Or([Atom('c'),Atom('d'),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Not(Atom('a'))])])
h=And([Or([Atom('a')]),Or([Atom('b'),Atom('c'),Atom('d')]),Or([Atom('c'),Atom('a'),Atom('b')]),Or([Not(Atom('b'))])])
i=And([Or([Not(Atom('a'))]),Or([Atom('b'),Atom('c'),Atom('c')]),Or([Atom('c'),Atom('d'),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Not(Atom('a'))])])
j=And([Or([Atom('a'),Atom('b')]),Or([Atom('c'),Atom('d')]),Or([Not(Atom('a'))])])
test=And([Or([Atom('a')]),Or([Not(Atom('a'))])])
test1=And([Or([Not(Atom('a')),Not(Atom('b')),Atom('c')]),Or([Not(Atom('a')),Atom('b')]),Or([Atom('a')])])
test2=And([Or([Atom('b'),Atom('c')]),Or([Atom('b'),Atom('c')]),Or([Atom('d'),Atom('e')])])
