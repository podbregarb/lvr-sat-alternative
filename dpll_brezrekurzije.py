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
    [string_formula,znane_spr]=dpll1(string_formula,znane_spr)
    return vstavljanje(string_formula,spr)

            
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
    return ciste_pojavitve(string_formula,znane_spr)


def ciste_pojavitve(string_formula,znane_spr={}):
    # odstranimo čiste pojavitve spremenljivk v naši formuli
    s=True
    while s:
        formula=list(string_formula)
        s=False
        pojavitve={}
        for i in formula:
            for k,l in i.items():
                if k not in pojavitve:
                    pojavitve[k]=l
                else:
                    if pojavitve[k]!=l:
                        pojavitve[k]=None
        for j in formula:
            for m in j.keys():
                if m in pojavitve and pojavitve[m]!=None:
                    znane_spr[m]=pojavitve[m]
                    if j in string_formula:
                        string_formula.remove(j)
                        s=True
    return [string_formula,znane_spr]   

            
def vstavljanje(list_formula, znane_spr={}):
    if list_formula==[]:
        return ('Formula je izpolnljiva', znane_spr)
    
    elif list_formula=='Ni rešitve':
        return ('Ni rešitve',3)

    else:
        flag=False
        for i in list_formula:
            for j in i:
                if j not in znane_spr:
                    l=j
                    flag=True
                    break
                
        list_formula1=list_formula.copy()
        znane_spr1=znane_spr.copy()
               
        if flag:
            znane_spr1[l]=True
            for k in list_formula1[:]:
                if l in k:                        
                    if k[l]==True:
                        list_formula1.remove(k)                           
                    else:
                        del k[l]
            (list_formula1, znane_spr1)=dpll1(list_formula1, znane_spr1)            
            (list_formula1, znane_spr1)=vstavljanje(list_formula1, znane_spr1)
            if list_formula1=='Ni rešitve.':
                znane_spr[l]=False
                for k in list_formula[:]:
                    if l in k:                        
                        if k[l]==False:
                            list_formula.remove(k)                           
                        else:
                            del k[l]
                        (list_formula, znane_spr)=dpll1(list_formula, znane_spr)
                        return vstavljanje(list_formula, znane_spr)
            else:
                return (list_formula1, znane_spr1)  
        

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
