# -*- encoding: utf-8 -*-

# Osnovne podatkovne strukture za logicne formule

# Razredi za predstavitev formul.

# POZOR: nikoli ne programiramo tako, da spremenimo objekte.
#        Vedno delamo nove.

class Atom():
    def __init__(self, x):
        self.ime = x

    def __repr__(self):
        return self.ime

    def nnf(self, negiramo=False):
        """Vrni nnf obliko objekta self."""
        if negiramo:
            return Not(self)
        else:
            return self

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

        
class And():
    def __init__(self, lst):
        self.formulas = lst

    def __repr__(self):
        return "And" + str(self.formulas)

    def nnf(self, negiramo=False):
        lst = [p.nnf(negiramo) for p in self.formulas]
        if negiramo:
            return Or(lst)
        else:
            return And(lst)

class Or():
    def __init__(self, lst):
        self.formulas = lst

    def __repr__(self):
        return "Or" + str(self.formulas)

    def nnf(self, negiramo=False):
        lst = [p.nnf(negiramo) for p in self.formulas]
        if negiramo:
            return And(lst)
        else:
            return Or(lst)
