# -*- encoding: utf-8 -*-

# Osnovne podatkovne strukture za logicne formule

from cnf import *

# Razredi za predstavitev formul.
# POZOR: nikoli ne programiramo tako, da spremenimo objekte.
#        Vedno delamo nove.

class Tru():
    def __init__(self):
        pass

    def __repr__(self):
        return "Tru"

    def nnf(self, negiramo=False):
        if negiramo:
            return Fls()
        else:
            return self
        
    def cnf(self):
        return Cnf([])
        

class Fls():
    def __init__(self):
        pass

    def __repr__(self):
        return "Fls"

    def nnf(self, negiramo=False):
        if negiramo:
            return Tru()
        else:
            return self

    def cnf(self):
        return Cnf([Stavek([])])


class Atom():
    def __init__(self, x):
        self.ime = x

    def __repr__(self):
        return str(self.ime)

    def nnf(self, negiramo=False):
        """Vrni nnf obliko objekta self."""
        if negiramo:
            return Not(self)
        else:
            return self

    def cnf(self):
        """Vrni CNF obliko objekta self."""
        return Cnf([Stavek([Lit(self.ime)])])

class Not():
    def __init__(self, p):
        self.formula = p

    def __repr__(self):
        return "Not(" + str(self.formula) + ")"

    def nnf(self, negiramo=False):
        return self.formula.nnf(negiramo = not negiramo)
        # Ekvivalentno, a grdo, profiji ne delajo tako:
        # if negiramo:
        #     return self.formula.nnf(negiramo = false)
        # else:
        #     return self.formula.nnf(negiramo = true)

    def cnf(self):
        if isinstance(self.formula, Atom):
            return Cnf([Stavek([Til(self.formula.ime)])])
        else:
            return self.nnf().cnf()
        
class And():
    def __init__(self, lst):
        self.formule = lst

    def __repr__(self):
        return "And" + str(self.formule)

    def nnf(self, negiramo=False):
        lst = [p.nnf(negiramo) for p in self.formule]
        if negiramo:
            return Or(lst)
        else:
            return And(lst)

    def cnf(self):
        stavki = []
        for p in self.formule:
            stavki.extend(p.cnf().stavki)
        return Cnf(stavki)
        

class Or():
    def __init__(self, lst):
        self.formule = lst

    def __repr__(self):
        return "Or" + str(self.formule)

    def nnf(self, negiramo=False):
        lst = [p.nnf(negiramo) for p in self.formule]
        if negiramo:
            return And(lst)
        else:
            return Or(lst)

    def cnf(self):
        if len(self.formule) == 0:
            return Cnf([Stavek([])])
        elif len(self.formule) == 1:
            return self.formule[0].cnf()
        else:
            # Razbijemo disjunkcijo na dve podformuli in izracunamo CNF
            stavki = []
            for s1 in self.formule[0].cnf().stavki:
                for s2 in Or(self.formule[1:]).cnf().stavki:
                    stavki.append(Stavek(s1.literali + s2.literali))
            return Cnf(stavki)


