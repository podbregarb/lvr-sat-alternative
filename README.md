#  SAT solver in primeri

##  Vsebina 

V mapi **Implementacija** so programi *bool.py*, *cnf.py* in *primeri.py*. 

V mapi **Prevedbe problemov na SAT - primeri** sta programa *barvanje_grafov.py* in *sudoku.py*.

V mapi **Dpll** sta programa *dpll.py* in *dpll_primeri.py*.

Program *demo.py* je glavni program, ki ga za�enemo.


##  Opis algoritmov in datotek 

### Implementacija

V programu *bool.py* implementiramo razrede za predstavitev formul. Hkrati podamo pravila za pretvorbo v nnf in cnf obliko.

V programu *cnf.py* podamo pravila za izpis formule v cnf obliki.

Program *primeri.py* izpi�e primere uporabe cnf in nnf oblike ter primer izpisa formule.


### Prevedbe problemov na SAT - primeri

V programu *barvanje_grafov.py* je sprogramirana prevedba problema barvanja vozli�� grafa s k barvami v SAT obliko.

V programu *sudoku9x9.py* je sprogramirana prevedba 9x9 sudokuja, ki pa je dlpp ne re�i, ker je formula predolga (�e samo printanje formule primera na koncu je �asovno zahtevno).

V programu *sudoku4x4.py* je sprogramirana prevedba 4x4 sudokuja v SAT obliko.

V tekstovni datoteki *sudoku4.txt* je podan primer 4x4 sudokuja, ki ga program *demo.py* re�i preko programa *dpll.py* in preko programa *sudoku4x4.py*, ki sestavi izjavno formulo.


### Dpll

V programu *dpll.py* je sprogramiran SAT solver. Le-ta pove, �e je dana izjavna formula izpolnljiva. V primeru da je, vrne tekst Formula je izpolnljiva in seznam spremenljivk s pripadajo�imi vrednostmi, za katere je formula izpolnljiva. V primeru, da kakim spremenljivkam ne pripi�e vrednosti, lahko le-te zavzamejo poljubno vrednost. V primeru, da ni re�itve vrne tekst Ni re�itve in prazen seznam.

Program *dpll_testi.py* vsebuje testne primere, s katerimi smo preverili delovanje na�ega SAT solverja.


## Uporaba 

Za�enemo program **demo.py**. V Python Shell-u za�nemo pisati ukaze.

Ukaz *osnove()* izpi�e primere uporabe cnf in nnf oblike ter primer izpisa formule.

Ukaz *test_dpll()* izpi�e testne primere, s katerimi smo preverili delovanje na�ega SAT solverja.

Ukaz *sudoku4x4()* re�uje sudoku velikosti 4x4. Program nas sam vodi skozi cel proces. Ves �as nas spra�uje, �e �elimo sami vpisati sudoku. 
�e je na� odgovor 'y' (da), potem vpi�emo �eleni sudoku v formatu, ki ga program zahteva. 
�e odgovorimo 'n' (ne), potem program re�i sudoku iz tekstovne datoteke *Implementacija/sudoku4.txt* (na� sudoku lahko podamo tudi tam). 
�e je na� odgovor karkoli drugega, se program kon�a.
Trije primeri, ki poka�ejo delovanje tega programa:
- Odgovorimo z 'y' in vpi�emo 'primer0'. Program re�uje prazen sudoku. Vseeno ga re�i in prika�e neko re�itev.
- Odgovorimo z 'y' in vpi�emo 'primer1'. Program re�uje nere�ljiv sudoku. Vrne 'Ni re�itve'.
- Odgovorimo z 'n'. Program re�uje enoli�no re�ljiv sudoku.

