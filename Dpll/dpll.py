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

    (list_formula, znane_spr)=dpll1(list_formula, {})
    return vstavljanje(list_formula, znane_spr)


            
def dpll1(list_formula, znane_spr={}):
    s=True
    while s:
        s=False
        for i in list_formula[:]:
            if i=={}:
                return ('Ni rešitve',{})
            
            if len(i)==1:
                # imamo samo en literal v stavku
                l,b=list(i.items())[0]
                if l in znane_spr and znane_spr[l]!=b:
                    return ('Ni rešitve',{})
                else:
                    znane_spr[l]=b
                    
                # zbrišemo literal not l ali stavek, v katerem nastopa literal l
                for k in list_formula[:]:
                    if l in k:
                        if k[l]==b:
                            list_formula.remove(k)                           
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
    return (string_formula,znane_spr) 


def vstavljanje(list_formula, znane_spr={}):
    if list_formula==[]:
        return ('Formula je izpolnljiva', znane_spr)
    
    elif list_formula=='Ni rešitve':
        return ('Ni rešitve',{})

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