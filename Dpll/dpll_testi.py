# -*- encoding: utf-8 -*-

from dpll import *


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
test4=And([Or([Atom('a')]),Or([Atom('b'),Not(Atom('c')),Atom('a')]),Or([Not(Atom('c')),Not(Atom('d')),Not(Atom('a'))]),Or([Atom('b'),Atom('c')]),Or([Atom('a')])])

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
    print('test4:', dpll(test4))
