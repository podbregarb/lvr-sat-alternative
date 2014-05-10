#  SAT solver in primeri

##  Vsebina 

V mapi **Implementacija** so programi *bool.py*, *cnf.py* in *primeri.py*. 

V mapi **Prevedbe problemov na SAT - primeri** sta programa *barvanje_grafov.py* in *sudoku.py*.

V mapi **Dpll** sta programa *dpll.py* in *dpll_primeri.py*.

Program *demo.py* je glavni program, ki ga zaženemo.


##  Opis algoritmov in datotek 

### Implementacija

V programu *bool.py* implementiramo razrede za predstavitev formul. Hkrati podamo pravila za pretvorbo v nnf in cnf obliko.

V programu *cnf.py* podamo pravila za izpis formule v cnf obliki.

Program *primeri.py* izpiše primere uporabe cnf in nnf oblike ter primer izpisa formule.


### Prevedbe problemov na SAT - primeri

V programu *barvanje_grafov.py* je sprogramirana prevedba problema barvanja vozlišè grafa s k barvami v SAT obliko.

V programu *sudoku9x9.py* je sprogramirana prevedba 9x9 sudokuja, ki pa je dlpp ne reši, ker je formula predolga (že samo printanje formule primera na koncu je èasovno zahtevno).

V programu *sudoku4x4.py* je sprogramirana prevedba 4x4 sudokuja v SAT obliko.

V tekstovni datoteki *sudoku4.txt* je podan primer 4x4 sudokuja, ki ga program *demo.py* reši preko programa *dpll.py* in preko programa *sudoku4x4.py*, ki sestavi izjavno formulo.


### Dpll

V programu *dpll.py* je sprogramiran SAT solver. Le-ta pove, èe je dana izjavna formula izpolnljiva. V primeru da je, vrne tekst Formula je izpolnljiva in seznam spremenljivk s pripadajoèimi vrednostmi, za katere je formula izpolnljiva. V primeru, da kakim spremenljivkam ne pripiše vrednosti, lahko le-te zavzamejo poljubno vrednost. V primeru, da ni rešitve vrne tekst Ni rešitve in prazen seznam.

Program *dpll_testi.py* vsebuje testne primere, s katerimi smo preverili delovanje našega SAT solverja.


## Uporaba 

Zaženemo program **demo.py**. V Python Shell-u zaènemo pisati ukaze.

Ukaz *osnove()* izpiše primere uporabe cnf in nnf oblike ter primer izpisa formule.

Ukaz *test_dpll()* izpiše testne primere, s katerimi smo preverili delovanje našega SAT solverja.

Ukaz *sudoku4x4()* rešuje sudoku velikosti 4x4. Program nas sam vodi skozi cel proces. Ves èas nas sprašuje, èe želimo sami vpisati sudoku. 
Èe je naš odgovor 'y' (da), potem vpišemo želeni sudoku v formatu, ki ga program zahteva. 
Èe odgovorimo 'n' (ne), potem program reši sudoku iz tekstovne datoteke *Implementacija/sudoku4.txt* (naš sudoku lahko podamo tudi tam). 
Èe je naš odgovor karkoli drugega, se program konèa.
Trije primeri, ki pokažejo delovanje tega programa:
- Odgovorimo z 'y' in vpišemo 'primer0'. Program rešuje prazen sudoku. Vseeno ga reši in prikaže neko rešitev.
- Odgovorimo z 'y' in vpišemo 'primer1'. Program rešuje nerešljiv sudoku. Vrne 'Ni rešitve'.
- Odgovorimo z 'n'. Program rešuje enolièno rešljiv sudoku.

