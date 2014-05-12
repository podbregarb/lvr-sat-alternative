#  SAT solver in primeri

##  Vsebina 

V mapi **Implementacija** so programi *bool.py*, *cnf.py* in *primeri.py*. 

V mapi **Prevedbe problemov na SAT - primeri** so programi *barvanje_grafov.py*, *sudoku9x9.py* in *sudoku4x4.py* ter tekstovna datoteka *sudoku4.txt*.

V mapi **Dpll** sta programa *dpll.py* in *dpll_primeri.py*.

Program **demo.py** je glavni program, ki ga za�enemo.


##  Opis algoritmov in datotek 

### Implementacija

V programu *bool.py* implementiramo razrede za predstavitev formul. Hkrati podamo pravila za pretvorbo v nnf in cnf obliko.

V programu *cnf.py* podamo pravila za izpis formule v cnf obliki.

Program *primeri.py* izpi�e primere uporabe cnf in nnf oblike ter primer izpisa formule.


### Prevedbe problemov na SAT - primeri

V programu *barvanje_grafov.py* je sprogramirana prevedba problema barvanja vozli�� grafa s k barvami v SAT obliko.

V programu *sudoku9x9.py* je sprogramirana prevedba 9x9 sudokuja, ki pa je dpll ne re�i, ker je formula predolga 
(�e samo printanje formule primera na koncu je �asovno zahtevno).

V tekstovni datoteki *sudoku9.txt* je podan primer 9x9 sudokuja, ki ga program *demo.py* re�i preko programa *dpll.py* in preko programa 
*sudoku9x9.py*, ki sestavi izjavno formulo.

V programu *sudoku4x4.py* je sprogramirana prevedba 4x4 sudokuja v SAT obliko.

Program *sudoku4x4_primeri.py* je namenjen predstavitvi testov in primerov za sudoku velikosti 4x4. Ta program uporablja *demo.py* za prikaz nere�enih in re�enih sudokujev.

V tekstovni datoteki *sudoku4.txt* je podan primer 4x4 sudokuja, ki ga program *demo.py* re�i preko programa *dpll.py* in preko programa 
*sudoku4x4.py*, ki sestavi izjavno formulo.


### Dpll

V programu *dpll.py* je sprogramiran SAT solver. Le-ta pove, �e je dana izjavna formula izpolnljiva. V primeru da je, vrne tekst 'Formula je izpolnljiva' 
in seznam spremenljivk s pripadajo�imi vrednostmi, za katere je formula izpolnljiva. V primeru da kakim spremenljivkam ne pripi�e vrednosti, lahko le-te 
zavzamejo poljubno vrednost. V primeru ko ni re�itve, vrne tekst 'Ni re�itve' in prazen seznam.

Program *dpll_testi.py* vsebuje testne primere, s katerimi smo preverili delovanje na�ega SAT solverja.


## Uporaba 

Za�enemo program **demo.py**. V Python Shell-u za�nemo pisati ukaze.

Ukaz **_osnove()_** izpi�e primere uporabe cnf in nnf oblike ter primer izpisa formule.

Ukaz **_test_dpll(t)_** izpi�e t testnih primerov, s katerimi smo preverili delovanje na�ega SAT solverja. Do t=5 so osnovni testi (prazen And, Or in podobni). 'test7' 
(zadnji za t=8) testira delovanje funkcije, ki na koncu za�ne preverjati vse mo�nosti (s �istimi pojavitvami in stavki dol�ine <=1 se formula �e ni re�ila). Najve�ji t je 14. 
Testi po t=8 so zraven le ker smo jih uporabljali za testiranje �e preden smo imeli sprogramirano funkcijo *vse_moznosti*, niso pa pomembni.

Ukaz **_sudoku4x4()_** re�uje sudoku velikosti 4x4. Program nas sam vodi skozi cel proces. Ves �as nas spra�uje, �e �elimo sami vpisati sudoku.  
�e odgovorimo 'n' (ne), potem program re�i sudoku iz tekstovne datoteke *Implementacija/sudoku4.txt* (na� sudoku lahko podamo tudi tam).  
�e je na� odgovor 'y' (da), potem imamo tri mo�nosti:
- Vpi�emo svoj sudoku v formatu, ki ga zahteva program.
- Vpi�emo tekst 'test0', 'test1', 'test2', 'test3' ali 'test4'. To so testni sudokuji. Program jih poka�e preden jih za�ne re�evati in nam nato prika�e �e re�en sudoku.
'test0' je prazen sudoku. Program ga vseeno re�i in prika�e neko re�itev. 'test1', 'test2' in 'test3' so nere�ljivi sudokuji. 'test4' je poln sudoku. 
- Vpi�emo tekst 'primer0', 'primer1', 'primer2' ali 'primer3'. Primeri so razvr��eni po te�avnosti od najla�jega ('primer0') do te�jega ('primer3').

Program za vsak re�en sudoku izpi�e tudi �as re�evanja.  
�e je na� odgovor karkoli drugega, se program kon�a.

Ukaz **_sudoku9x9()_** deluje enako kot *sudoku4x4()*, le da imamo tu 4 primere.


## Pomembna opomba

Razlog, da je ve�ino commitov narejenih iz mojega uporabni�kega imena (podbregarb) je v tem, da smo se ve�inoma dobili vsi skupaj pri nekomu doma in delali projekt na istem 
ra�unalniku. Vsak od nas je v projekt vlo�il veliko �asa in vsi smo se z njim veliko nau�ili.