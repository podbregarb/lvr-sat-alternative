# -*- coding: utf-8 -*-

from bool import *
from cnf import *



def dpll(formula):
    # v prvem delu formulo v CNF obliki pretvorimo v seznam slovarjev
    # (zunanji seznam pomeni And, notranji slovarji so Or stavki)
    formula=formula.cnf()
    string_formula=[]
    for f in formula.stavki:
        # D...slovar
        D={}
        if len(f.literali)==0:
            return 'Ni rešitve.'
        for spr in f.literali:
            b=isinstance(spr,Lit)
            if spr.ime in D and D[spr.ime]!=b:
                D={}
                string_formula.append(D)
                break
            else:
                D[spr.ime]=b
        if len(D)>0:
            string_formula.append(D)
    # poiščemo vse spremenljivke, ki nastopajo v naši formuli
    znane_spr={}
    spr=[]
    for i in string_formula:
        for j in i.keys():
            if j not in spr:
                spr.append(j)
    return ciste_pojavitve(string_formula,znane_spr)
    return vse_moznosti(string_formula,spr)

            
def dpll1(string_formula,znane_spr={}):
    s=True
    while s:
        s=False
        for i in string_formula[:]:
            if i=={}:
                return ['Ni rešitve.', 'Škoda.']
            if len(i)==1:
                spremenljivka,b=list(i.items())[0]
                if spremenljivka in znane_spr and znane_spr[spremenljivka]!=b:
                    return ['Ni rešitve.', 'Škoda.']
                else:
                    znane_spr[spremenljivka]=b
                
                # imamo samo eno spremenljivko v stavku
                for k in string_formula[:]:
                    if spremenljivka in k:
                        if k[spremenljivka]==b:
                            string_formula.remove(k)
                        else:
                            # tu se pokličemo rekurzivno, če med brisanjem elementov iz seznama
                            # pridelamo seznam dolžine <=2
                            del k[spremenljivka]
                            s=s or len(k)<=1   
    return [string_formula,znane_spr]

## mislim, da dela prav::
def ciste_pojavitve(string_formula,znane_spr={}):
    # odstranimo čiste pojavitve spremenljivk v naši formuli
    s=True
    while s:
        formula=list(string_formula)
        s=False
        for i in formula:
            a,o=True,False
            for k,l in i.items():
                a,o=a and l, o or l
                for j in formula:
                    for m,n in j.items():
                        if k==m:
                            a,o=a and n, o or n
                if a==True and k not in znane_spr:
                    znane_spr[k]=True
                    s=True
                    for i1 in formula:
                        for k1 in i1.keys():
                            if k==k1 and i1 in string_formula:
                                string_formula.remove(i1)
                                
                if o==False and k not in znane_spr:
                    znane_spr[k]=False
                    s=True
                    for i2 in formula:
                        for k2 in i2.keys():
                            if k==k2 and i2 in string_formula:
                                string_formula.remove(i2)
    return dpll1(string_formula,znane_spr)



### TO ŠE NITI PRIBLIŽNO NE DELA!! ###
#                  |
#                  ˇ
# preverimo vse možnosti za preostale spremenljivke
def vse_moznosti(string_formula, neznane_spr):
    nastavljene_spr={}
    for i in [d.copy() for d in string_formula]:
        for j,l in i.items():
            if l==True:
                nastavljene_spr[j]=True
                for i1 in [d.copy() for d in string_formula]:
                    for j1,l1 in i1.items():
                        if j1==j and l1==l and i1 in string_formula:
                            string_formula.remove(i1)
                            string_formula=ciste_pojavitve(string_formula,nastavljene_spr)
                            if string_formula==[]:
                                znane_spr.update(nastavljene_spr)
                                return ['Formula je izvedljiva.', 'Super.']
                            else:
                                nastavljene_spr[j]=False
                                [string_formula,nastavljene_spr]=vse_moznosti(string_formula, neznane_spr)
                                           
    return [string_formula,nastavljene_spr]
            
            







        

##testne formule
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
    print('f:',f, '\n  ', dpll(f)[0], '\n  ',dpll(f)[1])
    print('g:',g, '\n  ', dpll(g)[0], '\n  ',dpll(g)[1])
    print('h:',h, '\n  ', dpll(h)[0], '\n  ',dpll(h)[1])
    print('i:',i, '\n  ', dpll(i)[0], '\n  ',dpll(i)[1])
    print('j:',j, '\n  ', dpll(j)[0], '\n  ',dpll(j)[1])
    print('test0:',test0, '\n  ', dpll(test0)[0], '\n  ',dpll(test0)[1])
    print('test1:',test1, '\n  ', dpll(test1)[0], '\n  ',dpll(test1)[1])
    print('test2:',test2, '\n  ', dpll(test2)[0], '\n  ',dpll(test2)[1])
    print('test3:',test3, '\n  ', dpll(test3)[0], '\n  ',dpll(test3)[1])
