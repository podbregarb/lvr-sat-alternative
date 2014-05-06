#  SAT solver in primeri

##  Vsebina 

V mapi **Implementacija** so programi *bool.py*, *cnf.py* in *primeri.py*. 

V mapi **Prevedbe problemov na SAT - primeri** sta programa *barvanje_grafov.py* in *sudoku.py*.

V mapi **Dpll* sta programa *dpll.py* in *dpll_primeri.py*.



##  Opis algoritmov in datotek 

### Implementacija

V programu *bool.py* implementiramo razrede za predstavitev formul. Hkrati podamo pravila za pretvorbo v nnf in cnf obliko.

V programu *cnf.py* podamo pravila za izpis formule v cnf obliki.

Program *primeri.py* izpi�e primere uporabe cnf in nnf oblike ter primer izpisa formule.


### Prevedbe problemov na SAT - primeri

V programu *barvanje_grafov.py* je sprogramirana prevedba problema barvanja vozli�� grafa s k barvami v SAT obliko.

V programu *sudoku.py* je sprogramirana prevedba 9x9 sudokuja, ki pa je dlpp ne re�i, ker je formula predolga (�e samo printanje formule primera na koncu je �asovno zahtevno).


### Dpll

V programu *dpll.py* je sprogramiran SAT solver. Le-ta pove, �e je dana izjavna formula izpolnljiva. V primeru da je, vrne tekst Formula je izpolnljiva in seznam spremenljivk s pripadajo�imi vrednostmi, za katere je formula izpolnljiva. V primeru, da kakim spremenljivkam ne pripi�e vrednosti, lahko le-te zavzamejo poljubno vrednost. V primeru, da ni re�itve vrne tekst Ni re�itve in prazen seznam.

Program *dpll_testi.py* vsebuje testne primere, s katerimi smo preverili delovanje na�ega SAT solverja.



## Uporaba 

�e �elimo videti izpisovanje formul in delovanje nnf in cnf oblike za�enemo datoteko *primeri.py* v mapi Implementacija.

�e �elimo videti testne primere in delovanje SAT solverja (oz. preveriti �e je kak problem izpolnljiv) za�enemo datoteko *dpll_testi.py* v mapi Dpll.

