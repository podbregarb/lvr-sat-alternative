# -*- encoding: utf-8 -*-

from . import dpll
import Implementacija.bool as bool
import Implementacija.cnf as cnf

##testne funkcije
f=bool.And([bool.Or([bool.Atom('a')]),bool.Or([bool.Atom('b'),bool.Atom('c'),bool.Atom('a')]),bool.Or([bool.Atom('c'),bool.Atom('d'),bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Atom('a')])])
g=bool.And([bool.Or([bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c'),bool.Atom('a')]),bool.Or([bool.Atom('c'),bool.Atom('d'),bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Not(bool.Atom('a'))])])
h=bool.And([bool.Or([bool.Atom('a')]),bool.Or([bool.Atom('b'),bool.Atom('c'),bool.Atom('d')]),bool.Or([bool.Atom('c'),bool.Atom('a'),bool.Atom('b')]),bool.Or([bool.Not(bool.Atom('b'))])])
i=bool.And([bool.Or([bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c'),bool.Atom('c')]),bool.Or([bool.Atom('c'),bool.Atom('d'),bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Not(bool.Atom('a'))])])
j=bool.And([bool.Or([bool.Atom('a'),bool.Atom('b')]),bool.Or([bool.Atom('c'),bool.Atom('d')]),bool.Or([bool.Not(bool.Atom('a'))])])
test0=bool.And([bool.Or([bool.Atom('a')]),bool.Or([bool.Not(bool.Atom('a'))])])
test1=bool.And([bool.Or([bool.Not(bool.Atom('a')),bool.Not(bool.Atom('b')),bool.Atom('c')]),bool.Or([bool.Not(bool.Atom('a')),bool.Atom('b')]),bool.Or([bool.Atom('a')])])
test2=bool.And([bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Atom('d'),bool.Atom('e')])])
test3=bool.And([bool.Or([bool.Atom('a'),bool.Not(bool.Atom('a')),bool.Atom('b')])])
test4=bool.And([bool.Or([bool.Atom('a')]),bool.Or([bool.Atom('b'),bool.Not(bool.Atom('c')),bool.Atom('a')]),bool.Or([bool.Not(bool.Atom('c')),bool.Not(bool.Atom('d')),bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Atom('a')])])

def test():
    print('f:  ', dpll.dpll(f))
    print('g:  ', dpll.dpll(g))
    print('h:  ', dpll.dpll(h))
    print('i:  ', dpll.dpll(i))
    print('j:  ', dpll.dpll(j))
    print('test0:  ', dpll.dpll(test0))
    print('test1:  ', dpll.dpll(test1))
    print('test2:  ', dpll.dpll(test2))
    print('test3:  ', dpll.dpll(test3))
    print('test4:', dpll.dpll(test4))
