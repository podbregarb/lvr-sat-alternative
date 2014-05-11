# -*- encoding: utf-8 -*-

from . import dpll
import Implementacija.bool as bool
import Implementacija.cnf as cnf

##testne funkcije
test0=bool.And([])
test1=bool.And([bool.Or([])])
test2=bool.And([bool.Or([bool.Atom('a')])])
test3=bool.And([bool.Or([bool.Atom('a'),bool.Not(bool.Atom('a'))])])
test4=bool.And([bool.Or([bool.Atom('a')]),bool.Or([bool.Not(bool.Atom('a'))])])
test5=bool.And([bool.Or([bool.Atom('a')]),bool.Or([bool.Atom('b'),bool.Atom('c'),bool.Atom('a')]),bool.Or([bool.Atom('c'),bool.Atom('d'),bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Atom('a')])])
test6=bool.And([bool.Or([bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c'),bool.Atom('a')]),bool.Or([bool.Atom('c'),bool.Atom('d'),bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Not(bool.Atom('a'))])])
test7=bool.And([bool.Or([bool.Atom('a'),bool.Atom('d'),bool.Atom('g')]),bool.Or([bool.Not(bool.Atom('a')),bool.Not(bool.Atom('d')),bool.Not(bool.Atom('b'))]),bool.Or([bool.Atom('b'),bool.Atom('d'),bool.Not(bool.Atom('c'))]),bool.Or([bool.Atom('c'),bool.Not(bool.Atom('g'))])])
test8=bool.And([bool.Or([bool.Atom('a')]),bool.Or([bool.Atom('b'),bool.Atom('c'),bool.Atom('d')]),bool.Or([bool.Atom('c'),bool.Atom('a'),bool.Atom('b')]),bool.Or([bool.Not(bool.Atom('b'))])])
test9=bool.And([bool.Or([bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c'),bool.Atom('c')]),bool.Or([bool.Atom('c'),bool.Atom('d'),bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Not(bool.Atom('a'))])])
test10=bool.And([bool.Or([bool.Atom('a'),bool.Atom('b')]),bool.Or([bool.Atom('c'),bool.Atom('d')]),bool.Or([bool.Not(bool.Atom('a'))])])
test11=bool.And([bool.Or([bool.Not(bool.Atom('a')),bool.Not(bool.Atom('b')),bool.Atom('c')]),bool.Or([bool.Not(bool.Atom('a')),bool.Atom('b')]),bool.Or([bool.Atom('a')])])
test12=bool.And([bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Atom('d'),bool.Atom('e')])])
test13=bool.And([bool.Or([bool.Atom('a')]),bool.Or([bool.Atom('b'),bool.Not(bool.Atom('c')),bool.Atom('a')]),bool.Or([bool.Not(bool.Atom('c')),bool.Not(bool.Atom('d')),bool.Not(bool.Atom('a'))]),bool.Or([bool.Atom('b'),bool.Atom('c')]),bool.Or([bool.Atom('a')])])

TESTI=[test0,test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11,test12,test13]

def test(t):
    for i in range(t):
        print('test{0}:  '.format(i), TESTI[i], '\n', dpll.dpll(TESTI[i]), '\n')

