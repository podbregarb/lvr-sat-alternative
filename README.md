#  SAT solver in primeri

##  Vsebina 

V mapi **Implementacija** so programi *bool.py*, *cnf.py* in *primeri.py*. 

V mapi **Prevedbe problemov na SAT - primeri** so programi *barvanje_grafov.py*, *sudoku9x9.py* in *sudoku4x4.py* ter tekstovna datoteka *sudoku4.txt*.

V mapi **Dpll** sta programa *dpll.py* in *dpll_primeri.py*.

Program **demo.py** je glavni program, ki ga zaženemo.


##  Opis algoritmov in datotek 

### Implementacija

V programu *bool.py* implementiramo razrede za predstavitev formul. Hkrati podamo pravila za pretvorbo v nnf in cnf obliko.

V programu *cnf.py* podamo pravila za izpis formule v cnf obliki.

Program *primeri.py* izpiše primere uporabe cnf in nnf oblike ter primer izpisa formule.


### Prevedbe problemov na SAT - primeri

V programu *barvanje_grafov.py* je sprogramirana prevedba problema barvanja vozlišè grafa s k barvami v SAT obliko.

Program *barvanje_grafov_demo.py* je namenjen predstavitvi primerov barvanja grafov. Ta program uporablja *demo.py*.

V programu *sudoku9x9.py* je sprogramirana prevedba 9x9 sudokuja, ki pa je dpll ne reši, ker je formula predolga 
(že samo printanje formule primera na koncu je èasovno zahtevno).

V tekstovni datoteki *sudoku9.txt* je podan primer 9x9 sudokuja, ki ga program *demo.py* reši preko programa *dpll.py* in preko programa 
*sudoku9x9.py*, ki sestavi izjavno formulo.

V programu *sudoku4x4.py* je sprogramirana prevedba 4x4 sudokuja v SAT obliko.

V tekstovni datoteki *sudoku4.txt* je podan primer 4x4 sudokuja, ki ga program *demo.py* reši preko programa *dpll.py* in preko programa 
*sudoku4x4.py*, ki sestavi izjavno formulo.

Program *sudoku_demo.py* je namenjen predstavitvi testov in primerov za sudoku velikosti 4x4 in 9x9. Ta program uporablja *demo.py* za prikaz nerešenih in rešenih sudokujev.


### Dpll

V programu *dpll.py* je sprogramiran SAT solver. Le-ta pove, èe je dana izjavna formula izpolnljiva. V primeru da je, vrne tekst 'Formula je izpolnljiva' 
in seznam spremenljivk s pripadajoèimi vrednostmi, za katere je formula izpolnljiva. V primeru da kakim spremenljivkam ne pripiše vrednosti, lahko le-te 
zavzamejo poljubno vrednost. V primeru ko ni rešitve, vrne tekst 'Ni rešitve' in prazen seznam.

Program *dpll_testi.py* vsebuje testne primere, s katerimi smo preverili delovanje našega SAT solverja.


## Uporaba 

Zaženemo program **demo.py**. V Python Shell-u zaènemo pisati ukaze.

Ukaz **_osnove()_** izpiše primere uporabe cnf in nnf oblike ter primer izpisa formule.

Ukaz **_test_dpll(t)_** izpiše t testnih primerov, s katerimi smo preverili delovanje našega SAT solverja. Do t=5 so osnovni testi (prazen And, Or in podobni). 'test7' 
(zadnji za t=8) testira delovanje funkcije, ki na koncu zaène preverjati vse možnosti (s èistimi pojavitvami in stavki dolžine <=1 se formula še ni rešila). Najveèji t je 14. 
Testi po t=8 so zraven le ker smo jih uporabljali za testiranje še preden smo imeli sprogramirano funkcijo *vse_moznosti*, niso pa pomembni.

Ukaz **_barvanje()_** rešuje in izpiše 9 vnaprej podanih primerov grafov za razlièno število barv (od 1 do tam kjer postane obarljiv +1). 
Primer0 je ena toèka. Primer1 je graf na dveh toèkah z eno povezavo. Primer2 je veriga šestih toèk. Primer3 je kvadrat. Primer4 je poln graf na štirih toèkah.
Linki za ostale grafe: [Primer5](http://www.math.hmc.edu/~kindred/archive/spring11/math55/graphics/icosahedron-coloring.png), 
[Primer6](http://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Petersen_graph_3-coloring.svg/480px-Petersen_graph_3-coloring.svg.png), 
[Primer7](http://felix.abecassis.me/wp-content/uploads/2012/11/hexa.png), 
[Primer8](http://www.dharwadker.org/vertex_coloring/fig5a.jpg), 
[Primer9](http://www.dharwadker.org/vertex_coloring/fig9a.jpg).

Z ukazom **_barval_bi_sam(V,E,k)_** lahko podamo tudi svoj graf. V je število vozlišè, E je seznam povezav oblike [(e1,e2),(e3,e4),...], k pa število barv s katerimi 
želimo pobarvati vozlišèa grafa. Ukaz **_barval_bi_sam(V,E,k,1)_** graf tudi nariše. Ker nam to ni ravno najlepše uspelo, enke na koncu ne priporoèamo, oz. jo iz lepotnih
razlogov odsvetujemo.

Ukaz **_sudoku4x4()_** rešuje sudoku velikosti 4x4. Program nas sam vodi skozi cel proces. Ves èas nas sprašuje, èe želimo sami vpisati sudoku.  
Èe odgovorimo 'n' (ne), potem program reši sudoku iz tekstovne datoteke *Implementacija/sudoku4.txt* (naš sudoku lahko podamo tudi tam).  
Èe je naš odgovor 'y' (da), potem imamo tri možnosti:
- Vpišemo svoj sudoku v formatu, ki ga zahteva program.
- Vpišemo tekst 'test0', 'test1', 'test2', 'test3' ali 'test4'. To so testni sudokuji. Program jih pokaže preden jih zaène reševati in nam nato prikaže še rešen sudoku.
'test0' je prazen sudoku. Program ga vseeno reši in prikaže neko rešitev. 'test1', 'test2' in 'test3' so nerešljivi sudokuji. 'test4' je poln sudoku. 
- Vpišemo tekst 'primer0', 'primer1', 'primer2' ali 'primer3'. Primeri so razvršèeni po težavnosti od najlažjega ('primer0') do težjega ('primer3').

Program za vsak rešen sudoku izpiše tudi èas reševanja.  
Èe je naš odgovor karkoli drugega, se program konèa.

Ukaz **_sudoku9x9()_** deluje enako kot *sudoku4x4()*, le da imamo tu 4 primere. Tudi zadnjega, tj. 'primer4' ("World's hardest sudoku" :P) izraèuna, le èakati je treba 
(pri meni je trajalo pol minute).


## Pomembna opomba

Razlog, da je veèino commitov narejenih iz mojega uporabniškega imena (podbregarb) je v tem, da smo se veèinoma dobili vsi skupaj pri nekomu doma in delali projekt na istem 
raèunalniku. Vsak od nas je v projekt vložil veliko èasa in vsi smo se z njim veliko nauèili.