# -*- encoding: utf-8 -*-

# Osnovne podatkovne strukture za logicne formule

from . import cnf

# Razredi za predstavitev formul:
# za vsak razred, ki ga definiramo povemo kako ga predstavimo in kako ga
# pretvorimo v nnf in cnf obliko

# definiramo razred Tru
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
        return cnf.Cnf([])
        
# definiramo razred Fls
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
        return cnf.Cnf([cnf.Stavek([])])

# definiramo razred Atom
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
        return cnf.Cnf([cnf.Stavek([cnf.Lit(self.ime)])])

# definiramo razred Not
class Not():
    def __init__(self, p):
        self.formula = p

    def __repr__(self):
        return "Not(" + str(self.formula) + ")"

    def nnf(self, negiramo=False):
        return self.formula.nnf(negiramo = not negiramo)

    def cnf(self):
        if isinstance(self.formula, Atom):
            return cnf.Cnf([cnf.Stavek([cnf.Til(self.formula.ime)])])
        else:
            return self.nnf().cnf()

# definiramo razred And        
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
        return cnf.Cnf(stavki)
        
# definiramo razred Or
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
            return cnf.Cnf([cnf.Stavek([])])
        elif len(self.formule) == 1:
            return self.formule[0].cnf()
        else:
            # Razbijemo disjunkcijo na dve podformuli in izracunamo CNF
            stavki = []
            for s1 in self.formule[0].cnf().stavki:
                for s2 in Or(self.formule[1:]).cnf().stavki:
                    stavki.append(cnf.Stavek(s1.literali + s2.literali))
            return cnf.Cnf(stavki)


