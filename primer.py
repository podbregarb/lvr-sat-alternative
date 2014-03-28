# Primeri uporabe
# -*- encoding: utf-8 -*-

from bool import *

# Formula: x /\ (not y \/ x) /\ z
formula1 = And([Atom("x"), Or([Not(Atom("y")), Atom("x")]), Atom("z")])
