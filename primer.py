# Primeri uporabe
# -*- encoding: utf-8 -*-

from bool import *
from cnf import *

# Formula: x /\ not (not y \/ x) /\ z
formula1 = And([Atom("x"), Not(Or([Not(Atom("y")), Atom("x")])), Atom("z")])

# NNF oblika
formula2 = formula1.nnf()

# Primer CNF formule:
cnf1 = Cnf([
         Stavek([]),
         Stavek([Lit("x"), Lit("y"), Til("z")]),
         Stavek([Lit("z")]),
       ])
