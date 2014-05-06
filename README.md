#  SAT solver in primeri

##  Vsebina 

V mapi **Implementacija** so programi *bool.py*, *cnf.py* in *primeri.py*. 

V mapi **Prevedbe problemov na SAT - primeri** sta programa *barvanje_grafov.py* in *sudoku.py*.

V mapi **Dpll* sta programa *dpll.py* in *dpll_primeri.py*.



##  Opis algoritmov in datotek 

### Implementacija

V programu *bool.py* implementiramo razrede za predstavitev formul. Hkrati podamo pravila za pretvorbo v nnf in cnf obliko.

V programu *cnf.py* podamo pravila za izpis formule v cnf obliki.

Program *primeri.py* izpiše primere uporabe cnf in nnf oblike ter primer izpisa formule.


### Prevedbe problemov na SAT - primeri

V programu *barvanje_grafov.py* je sprogramirana prevedba problema barvanja vozlišè grafa s k barvami v SAT obliko.

V programu *sudoku.py* je sprogramirana prevedba 9x9 sudokuja, ki pa je dlpp ne reši, ker je formula predolga (že samo printanje formule primera na koncu je èasovno zahtevno).


### Dpll

V programu *dpll.py* je sprogramiran SAT solver. Le-ta pove, èe je dana izjavna formula izpolnljiva. V primeru da je, vrne tekst Formula je izpolnljiva in seznam spremenljivk s pripadajoèimi vrednostmi, za katere je formula izpolnljiva. V primeru, da kakim spremenljivkam ne pripiše vrednosti, lahko le-te zavzamejo poljubno vrednost. V primeru, da ni rešitve vrne tekst Ni rešitve in prazen seznam.

Program *dpll_testi.py* vsebuje testne primere, s katerimi smo preverili delovanje našega SAT solverja.



## Uporaba 

Èe želimo videti izpisovanje formul in delovanje nnf in cnf oblike zaženemo datoteko *primeri.py* v mapi Implementacija.

Èe želimo videti testne primere in delovanje SAT solverja (oz. preveriti èe je kak problem izpolnljiv) zaženemo datoteko *dpll_testi.py* v mapi Dpll.

