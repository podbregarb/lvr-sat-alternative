# -*- encoding: utf-8 -*-

from bool import *
from cnf import *
import copy



def dpll(formula):
    # v prvem delu formulo v CNF obliki pretvorimo v seznam slovarjev
    # slovarji predstavljajo stavke
    formula=formula.cnf()
    list_formula=[]
    for s in formula.stavki:
        d={}
        if len(s.literali)==0:
            return ('Ni rešitve', {})
        for l in s.literali:
            b=isinstance(l,Lit)
            if l.ime in d and d[l.ime]!=b:
                d={}
                break
            else:
                d[l.ime]=b
        if len(d)>0:
            list_formula.append(d)

    # na formuli najprej uporabimo dpll1, ki uporabi ciste_spremenljivke, zato vemo
    # da bomo imeli po tem koraku le stavke dolžine >=2 in nobenih čistih spremenljivk
    (list_formula, znane_spr)=dpll1(list_formula, {})
    # na tem mestu torej začnemo preverjati vse možne vrednosti za spremenljivke,
    # kar dela vstavljanje
    return vstavljanje(list_formula, znane_spr)


            
def dpll1(list_formula, znane_spr={}):
    # gleda stavke dolžine 0 ali 1
    s=True
    while s:
        s=False
        for i in list_formula[:]:
            # če imamo prazen stavek, potem dana formula ni izpolnljiva
            if i=={}:
                return ('Ni rešitve',{})
            
            if len(i)==1:
                # imamo samo eno spremenljivko v stavku
                l,b=list(i.items())[0]
                # če v znanih spremenljivkah že imamo spremenljivko z obratno vrednostjo, potem formula
                # ni izpolnljiva, sicer jo dodamo v znane spremenljivke in ji pripišemo vrednost
                if l in znane_spr and znane_spr[l]!=b:
                    return ('Ni rešitve',{})
                else:
                    znane_spr[l]=b

                # gremo po vseh stavkih v katerih nastopa spremenljivka l
                for k in list_formula[:]:
                    if l in k:
                        # če ima pripisano vrednost odstranimo stavek
                        if k[l]==b:
                            list_formula.remove(k)
                        # sicer odstranimo samo literal
                        else:
                            del k[l]                           
                            # tu se pokličemo rekurzivno, če med brisanjem elementov iz seznama
                            # pridelamo seznam dolžine <=1
                            s=s or len(k)<=1   
    return ciste_pojavitve(list_formula, znane_spr)



def ciste_pojavitve(string_formula,znane_spr={}):
    # odstranimo čiste pojavitve spremenljivk v naši formuli
    s=True
    while s:
        formula=list(string_formula)
        s=False
        # gremo čez vse stavke in vse spremenljivke in pogledamo ali so negirane ali ne, na koncu dobimo None
        # če spremenljivka ni čista
        pojavitve={}
        for i in formula:
            for k,l in i.items():
                if k not in pojavitve:
                    pojavitve[k]=l
                else:
                    if pojavitve[k]!=l:
                        pojavitve[k]=None
        # odstranimo stavke, ki vsebujejo čiste spremenljivke
        for j in formula:
            for m in j.keys():
                if m in pojavitve and pojavitve[m]!=None:
                    znane_spr[m]=pojavitve[m]
                    if j in string_formula:
                        string_formula.remove(j)
                        # če zbrišemo nek stavek, potem je možno, da se spremenljivka spet pojavi čisto
                        # in se pokličemo rekurzivno
                        s=True
    return (string_formula,znane_spr) 



def vstavljanje(list_formula, znane_spr={}):
    # preizkušamo možnosti za spremenljivke, ki so nam ostale
    if list_formula==[]:
        return ('Formula je izpolnljiva', znane_spr)
    
    elif list_formula=='Ni rešitve':
        return ('Ni rešitve',3)

    else:
        l = list_formula[0].keys()[0] 
        list_formula1=list_formula.copy()        
        znane_spr[l]=True
        for k in list_formula1[:]:
            if l in k:                        
                if k[l]==True:
                    list_formula1.remove(k)                           
                else:
                    del k[l]
        (list_formula1, znane_spr1)=dpll1(list_formula1, znane_spr)            
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
