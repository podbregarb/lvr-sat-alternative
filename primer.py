# Primeri uporabe
# -*- encoding: utf-8 -*-

from bool import *
from cnf import *

# Formula: x /\ not (not y \/ x) /\ z
formula1 = And([Atom("x"), Not(Or([Not(Atom("y")), Atom("x")])), Atom("z")])

# NNF oblika
formula2 = formula1.nnf()

# Primer CNF formule:
cnf0 = Cnf([
         Stavek([]),
         Stavek([Lit("x"), Lit("y"), Til("z")]),
         Stavek([Lit("z")]),
       ])

# CNF oblika
cnf1 = formula1.cnf()

formula3 = Or([And([Atom("a"), Atom("b")]),
               And([Atom("x"), Atom("y")]),
               And([Atom("u"), Atom("v")])])
cnf3 = formula3.cnf()

formula4 = Not(And([Not(And([Atom("a"), Not(Atom("b"))])),
                    And([Atom("x"), Atom("y")]),
                    And([Atom("u"), Atom("v")])]))
cnf4 = formula4.cnf()
