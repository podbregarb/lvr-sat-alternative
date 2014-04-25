from bool import *
from cnf import *



def dpll(formula):
    # v prvem delu formulo v CNF obliki pretvorimo v seznam seznamov
    # (zunanji je And, notranji so Or stavki)
    formula=formula.cnf()
    string_formula=[]
    for f in formula.stavki:
        #D...slovar
        D={}
        if len(f.literali)==0:
            return 'Ni rešitve.'
        for spr in f.literali:
            b=isinstance(spr,Lit)
            if spr.ime in D and D[spr.ime]!=b:
                D={}
                break
            else:
                D[spr.ime]=b
        if len(D)>0:
            string_formula.append(D)
    # poiščemo vse spremenljivke, ki nastopajo v naši formuli
    spr=[]
    for i in string_formula:
        for j in i.keys():
            if j not in spr:
                spr.append(j)
    znane_spr={}
    return (string_formula,spr)
    return vstavljanje(string_formula,znane_spr)
            
def dpll1(string_formula,znane_spr={}):
    s=True
    while s:
        s=False
        for i in string_formula[:]:
            if i=={}:
                return ['Ni rešitve.','Škoda.']
            if len(i)==1:
                spr,b=i.items()[0]
                if spr in znane_spr and znane_spr[spr]!=b:
                    return 'Ni rešitve.'
                else:
                    znane_spr[spr]=b
                
                # imamo samo eno spremenljivko v stavku
                for k in string_formula[:]:
                    if spr in k:
                        if k[spr]==b:
                            string_formula.remove(k)
                        else:
                            # tu se pokličemo rekurzivno, če med brisanjem elementov iz seznama
                            # pridelamo seznam dolžine <=2
                            k.remove(spr)
                            s=s or len(k)<=1   
    return [string_formula,znane_spr]
        

################ do sem je narejeno :)  ####################

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
            if j[0]!='~' and j not in neznane_spr:
                neznane_spr.append(j)
            if j[0]=='~' and j[1:] not in neznane_spr:
                neznane_spr.append(j[1:])
## na tem mestu bi uporabili rekurzivno funkcijo, ki poskusi vse
## vrednosti spremenljivk - nam ni še ratalo :P (glej dpll_poskusRekurzije)
    return [string_formula,znane_spr]
        

##testne funkcije
f=And([Or([Atom('ananas')]),Or([Atom('b'),Atom('c'),Atom('ananas')]),Or([Atom('c'),Atom('d'),Not(Atom('ananas'))]),Or([Atom('b'),Atom('c')]),Or([Atom('ananas')])])
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
