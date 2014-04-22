from bool import *
from cnf import *

def dpll(formula):
    formula=formula.cnf()
    znane_spr={}
    neznane_spr=[]
    for j in range(0,len(formula.stavki)):
        for k in range(0,len(formula.stavki[j].literali)):
            if str(formula.stavki[j].literali[k].ime) not in neznane_spr:
                neznane_spr = neznane_spr + [str(formula.stavki[j].literali[k].ime)]
    print (neznane_spr)
    # CS je seznam še neobdelanih stavkov
    CS1=formula.stavki
    CS=CS1
    print(CS1)
    for i in CS1:
        print(CS1)
        if i.literali==[]:
            print ("Ni rešitve.")
            break
        if len(i.literali)==1:
            if isinstance(i.literali[0],Lit):
                znane_spr[i.literali[0].ime]=Tru
                neznane_spr.remove(i.literali[0].ime)
                for k in CS1:
                    for j in k.literali:
                        if j.ime==i.literali[0].ime and isinstance(j,Lit):
                            CS.remove(k)
                        if isinstance(j,Til) and j.ime==i.literali[0].ime:
                            r=CS.index(k)
                            CS[r].literali.remove(j)
            else:
                znane_spr[i.literali[0].ime]=Fls
                neznane_spr.remove(i.literali[0].ime)
                for k in CS1:
                    for j in k.literali:
                        if isinstance(j,Til) and j.ime==i.literali[0].ime:
                            CS.remove(k)
                        if j.ime==i.literali[0].ime and isinstance(j,Lit):
                            r=CS.index(k)
                            CS[r].literali.remove(j)
            

    print(neznane_spr)
    print(CS)
    return znane_spr
    
    
            
            
            
