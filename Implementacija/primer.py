# Primeri uporabe
# -*- encoding: utf-8 -*-

from . import bool
from . import cnf

def primer():
    # Formula: x /\ not (not y \/ x) /\ z
    formula1 = bool.And([bool.Atom("x"), bool.Not(bool.Or([bool.Not(bool.Atom("y")), bool.Atom("x")])), bool.Atom("z")])
    print('Primer izpisa formule: x /\ not (not y \/ x) /\ z \n', formula1)

    # NNF oblika
    formula2 = formula1.nnf()
    print('Formulo postavimo v nnf obliko: \n', formula2, '\n')

    # Primer CNF formule:
    cnf0 = cnf.Cnf([
             cnf.Stavek([]),
             cnf.Stavek([cnf.Lit("x"), cnf.Lit("y"), cnf.Til("z")]),
             cnf.Stavek([cnf.Lit("z")]),
           ])
    print('Primer izpisa formule  v cnf obliki: \n', cnf0)

    # CNF oblika
    cnf1 = formula1.cnf()
    print('Formulo postavimo v cnf obliko: \n', formula2, '\n')

    formula3 = bool.Or([bool.And([bool.Atom("a"), bool.Atom("b")]),
                   bool.And([bool.Atom("x"), bool.Atom("y")]),
                   bool.And([bool.Atom("u"), bool.Atom("v")])])
    cnf3 = formula3.cnf()
    print('Formulo \n', formula3, '\n postavimo v cnf obliko: \n', formula3, '\n')

    formula4 = bool.Not(bool.And([bool.Not(bool.And([bool.Atom("a"), bool.Not(bool.Atom("b"))])),
                        bool.And([bool.Atom("x"), bool.Atom("y")]),
                        bool.And([bool.Atom("u"), bool.Atom("v")])]))
    cnf4 = formula4.cnf()
    print('Formulo \n', formula4, '\n postavimo v cnf obliko: \n', formula4, '\n')

