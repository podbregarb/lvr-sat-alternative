from bool import *
from cnf import *



def dpll(formula):
    # v prvem delu formulo v CNF obliki pretvorimo v seznam seznamov
    # (zunanji je And, notranji so Or stavki)
    formula=formula.cnf()
    string_formula=[]
    for i in range(0,len(formula.stavki)):
        string_formula.append([])
    for i in range(0,len(formula.stavki)):
        for j in range(0,len(formula.stavki[i].literali)):
            spr=formula.stavki[i].literali[j]
            if isinstance(spr,Lit):
                string_formula[i].append(spr.ime)
            if isinstance(spr,Til):
                string_formula[i].append('~'+spr.ime)
    # poiščemo vse spremenljivke, ki nastopajo v naši formuli
    spr=[]
    for i in string_formula:
        for j in i:
            if len(j)==1 and j not in spr:
                spr.append(j)
            if len(j)==2 and j[1] not in spr:
                spr.append(j[1])
    znane_spr=list([])
    return vstavljanje(string_formula,znane_spr)
            
def dpll1(string_formula,znane_spr=[]):
    for i in string_formula[:]:
        if i==[]:
            return ['Ni rešitve.','Škoda.']
        if len(i)==1:
            # imamo samo eno spremenljivko v stavku, spremenljivka ni negirana
            if len(i[0])==1:
                if [i[0],Tru] not in znane_spr:
                    znane_spr.append([i[0],Tru])
                for k in string_formula[:]:
                    for j in k:
                        if j[0]==i[0] and k in string_formula:
                            string_formula.remove(k)
                        if len(j)>1 and j[1]==i[0]:
                            k.remove(j)
                            
            # imamo samo eno spremenljivko v stavku, spremenljivka je negirana
            if len(i[0])==2:
                if [i[0][1],Fls] not in znane_spr:
                    znane_spr.append([i[0][1],Fls])
                for k in string_formula[:]:
                    for j in k:
                        if len(j)>1 and j[1]==i[0][1]:
                            string_formula.remove(k)
                        if j[0]==i[0][1]:
                            k.remove(j)
    # tu se pokličemo rekurzivno, če med brisanjem elementov iz seznama
    # pridelamo seznam dolžine <=2
    for i in string_formula:
        if len(i)<=1:
            [string_formula,znane_spr]=dpll1(string_formula,znane_spr)   
    return [string_formula,znane_spr]
        
def dpll2(string_formula,znane_spr=[]):
    for i in string_formula:
        for j in i:
            if i.count(j)>1:
                i.remove(j)
    for i in string_formula:
        if string_formula.count(i)>1:
            string_formula.remove(i)
    for i in string_formula:
        for j in i:
            if len(j)==2:
                for k in i:
                    if k[0]==j[1]:
                        string_formula.remove(i)
                    
    return [string_formula,znane_spr]


def vstavljanje(string_formula,znane_spr=[]):
    while True:
        [string_formula0,znane_spr0]=dpll1(string_formula,znane_spr)
        if string_formula0=='Ni rešitve.':
            return ['Ni rešitve.','Škoda.']
        if string_formula0=='Formula je izvedljiva.':
            return ['Formula je izvedljiva.','Super.']
        else:
            [string_formula1,znane_spr1]=dpll2(string_formula0,znane_spr0)
            if string_formula==string_formula1:
                break
##  zdaj vemo, da so vsi stavki dolžine >=2.
##  to je to za ta denar :)
## iz preostanka formule na novo vzamemo neznane spremenljivke
    neznane_spr=[]
    for i in string_formula:
        for j in i:
            if len(j)==1 and j not in neznane_spr:
                neznane_spr.append(j)
            if len(j)==2 and j[1] not in neznane_spr:
                neznane_spr.append(j[1])
## na tem mestu bi uporabili rekurzivno funkcijo, ki poskusi vse
## vrednosti spremenljivk - nam ni še ratalo :P (glej dpll_poskusRekurzije)
    return [string_formula,neznane_spr]
        

##testne funkcije
f=And([Or([Atom('a')]),Or([Atom('b'),Atom('c'),Atom('a')]),Or([Atom('c'),Atom('d'),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Atom('a')])])
g=And([Or([Not(Atom('a'))]),Or([Atom('b'),Atom('c'),Atom('a')]),Or([Atom('c'),Atom('d'),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Not(Atom('a'))])])
h=And([Or([Atom('a')]),Or([Atom('b'),Atom('c'),Atom('d')]),Or([Atom('c'),Atom('a'),Atom('b')]),Or([Not(Atom('b'))])])
i=And([Or([Not(Atom('a'))]),Or([Atom('b'),Atom('c'),Atom('c')]),Or([Atom('c'),Atom('d'),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Not(Atom('a'))])])
j=And([Or([Atom('a'),Atom('b')]),Or([Atom('c'),Atom('d')]),Or([Not(Atom('a'))])])
test0=And([Or([Atom('a')]),Or([Not(Atom('a'))])])
test1=And([Or([Not(Atom('a')),Not(Atom('b')),Atom('c')]),Or([Not(Atom('a')),Atom('b')]),Or([Atom('a')])])
test2=And([Or([Atom('b'),Atom('c')]),Or([Atom('b'),Atom('c')]),Or([Atom('d'),Atom('e')])])
test3=And([Or([Atom('a'),Not(Atom('a')),Atom('b')])])

def test():
    print('f:  ', dpll(f))
    print('g:  ', dpll(g))
    print('h:  ', dpll(h))
    print('i:  ', dpll(i))
    print('j:  ', dpll(j))
    print('test0:  ', dpll(test0))
    print('test1:  ', dpll(test1))
    print('test2:  ', dpll(test2))
    print('test3:  ', dpll(test3))
