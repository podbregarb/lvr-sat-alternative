# Primeri uporabe
# -*- encoding: utf-8 -*-

from bool import *

# Formula: x /\ not (not y \/ x) /\ z
formula1 = And([Atom("x"), Not(Or([Not(Atom("y")), Atom("x")])), Atom("z")])

formula2 = formula1.nnf()
