# -*- encoding: utf-8 -*-

# Osnovne podatkovne strukture za logicne formule

# Razredi za predstavitev formul

class Atom():
    def __init__(self, x):
        self.ime = x

    def __repr__(self):
        return self.ime

class Not():
    def __init__(self, p):
        self.formula = p

    def __repr__(self):
        return "Not(" + str(self.formula) + ")"

class And():
    def __init__(self, lst):
        self.formulas = lst

    def __repr__(self):
        return "And" + str(self.formulas)

class Or():
    def __init__(self, lst):
        self.formulas = lst

    def __repr__(self):
        return "Or" + str(self.formulas)
