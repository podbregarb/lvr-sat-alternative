# Primeri uporabe
# -*- encoding: utf-8 -*-

from bool import *
from cnf import *

# Formula: x /\ not (not y \/ x) /\ z
formula1 = And([Atom("x"), Not(Or([Not(Atom("y")), Atom("x")])), Atom("z")])
print('Primer izpisa formule: x /\ not (not y \/ x) /\ z \n', formula1)

# NNF oblika
formula2 = formula1.nnf()
print('Formulo postavimo v nnf obliko: \n', formula2, '\n')

# Primer CNF formule:
cnf0 = Cnf([
         Stavek([]),
         Stavek([Lit("x"), Lit("y"), Til("z")]),
         Stavek([Lit("z")]),
       ])
print('Primer izpisa formule  v cnf obliki: \n', cnf0)

# CNF oblika
cnf1 = formula1.cnf()
print('Formulo postavimo v cnf obliko: \n', formula2, '\n')

formula3 = Or([And([Atom("a"), Atom("b")]),
               And([Atom("x"), Atom("y")]),
               And([Atom("u"), Atom("v")])])
cnf3 = formula3.cnf()
print('Formulo \n', formula3, '\n postavimo v cnf obliko: \n', formula3, '\n')

formula4 = Not(And([Not(And([Atom("a"), Not(Atom("b"))])),
                    And([Atom("x"), Atom("y")]),
                    And([Atom("u"), Atom("v")])]))
cnf4 = formula4.cnf()
print('Formulo \n', formula4, '\n postavimo v cnf obliko: \n', formula4, '\n')
