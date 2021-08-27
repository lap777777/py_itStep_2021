"""
Verzovaci systemy - ukladaji postupne vsechny upravy - takze se muzu vracet v historii zmen.
Vetve - vice lidi v tymu - muzou se pak spojovat - a tak vice lidi muze delat na jednom programu

GIT - verzovaci system - https://git-scm.com

Github.com - server, kam se ukladaji soubory

- Repositories - prehled projektu, na kterych pracuji a pod nim jsou jednotlive soubory s kodem
Repozitar = projekt
- kazdy projekt by mel obsahovat soubor README.md - popis projektu, link na GitHubpages - pokud mam html stranku, tak ji muzu hostovat na Githubu
- jde pridavat popis i do About
- COMMITS - snimky historie projektu - jak jsem pridaval a upravoval soubory a menil jsem popisek - commit - update projektu - ukladam si kod
- kazdy commit - mel by mit svuj popis, co jsem updatoval/upravil apod. - dulezite je dobre popsat zmeny, abych vedel, co jsem delal
- kdyz rozkliknu modry znak vpravo, tak zelene oznaci nove radky a ukaze + pro nvoe radky, - pro vymazane radky cervene, bile, co tam bylo


struktura:
repozitar - projekt
commit - nahrani update projektu


Github - command line: - napoveda z Githubu na ovladani z prikazove radky:
#############################################################################################################

…or create a new repository on the command line
 echo "# python_itStep_2021" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/lap777777/python_itStep_2021.git
git push -u origin main


…or push an existing repository from the command line
 git remote add origin https://github.com/lap777777/python_itStep_2021.git
git branch -M main
git push -u origin main

…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.
#############################################################################################################

Pro praci s gitem muzu pouzivat separatni programy nebo pres terminal:

a) terminal
- musim se dostat do slozky, kde mam projekt

prikazy:
prikazy na zacatku - nastavni user a email - na novem pocitaci - globalni (pro cely pocitac = vsechny projekty) - konfigurace uzivatele a emailu
# git config --global user.name "FIRST_NAME LAST_NAME"
# git config --global user.email "MY_NAME@example.com"
verify your configuration by displaying config file:
cat .git/config
nebo se muzu zeptat jednotlive:
git config user.name
git config user.email

###### tady zacinaji prikazy pro projekty ######

# git init - tenhle adresar budu sledovat gitem - ve VS Code mi to zezelena

# git status
ukaze na jake jsem vetvy, kolik mam komitu a co se da komitovat, nesledovane soubory (cervene, zelene u ve VS code)
a rika mi pouzij git -add na pridani souboru 

GIT ma 3 plochy
- working directory - tady pracuji se soubory
- staging area - pridavam je tam pomoci git add a jsou pripravene na commit
- commit area

# git add jmeno_soubory.*
pridani souboru do staging arey, po pridani dam git status a mam zelene oznaceny pridany soubor a ve VS Code mam A misto U
# git add .   - prida vsechno (ne jenom jeden soubor)

# git rm jmeno_souboru.* - vyhodim soubor ze staging arey

# git commit -m "Prvni commit, hura" - commit musi mit commit message - popis, co se delo
(zmena ve VS code na "zlutou")
soubor je ted v commit area na mem disku a git si pamatuje jeho verzi
pokud zmenim, tak ve VS Code ukazuje 
U - untracked (dam add)
M - modified (uprava, dam add)
A - added (pripravene na commit)

# git log - vypise prehled commitu, ktere jsem spustil - zlute cislo je identifikator commitu

# git log --pretty=oneline --abbrev-commit
pusti log na jednu radku pro kazdy commit

# git config --global alias.lg "log --pretty=oneline --abbrev-commit"
tvorba aliasu - zkracenych prikazu
# git config --global alias.cm commit -m
alias pro commit git cm davam priste misto git commit -m

# git config --global alias.alias --get-regexp ^alias\.
nastavuji si alias pro aliasy

# git diff
prikaz, ktery ukazuje zmeny v souborech od posledniho commitu
vypis se strankuje
q ... pro quit
enter nebo jina libovolna klavesa pro pokracovani vypisu
prakticke pouziti pres komitem si projit zmeny, abych videl jestli to chci komitovat nebo ne - chci nahrat ulozene zmeny do gitu nebo ne

# git branch -M main
prejmenuji master vetev na main

# git remote add origin https://github.com/lap777777/python_itStep_2021.git
projim git s Githubem

# git push -u origin main (nebo master)
poslani commitovanych souboru na GitHub
druha varianta: 
# git push --set-upstream origin main
to davam poprve
dalsi nahravani davam uz jen:
# git push 


prijde novy kolega - vytvori si novy adresar a do nej si muze nakopirovat commity z jineho projektu
# git clone https:..... adresa puvodniho projektu
musim byt ve slozce, kde mi pak git vytvori podadresar se jmenem projektu a nemusim uz davat git init a propojovat, protoze mam udelano, pak staci jenom add commit a push jednoduse

Takze idealni postup:
1. zalozit si novou repozitory na GitHubu
2. zkopirovat si code HTTPS adresu repository
3. dat terminal a tam najet do slozky, ve ktere chci vytvorit repo u me v pocitaci
4. dat do terminalu git clone adresa z githubu
5. mam hotovo a muzu add, commit -m a push a vse je propojene

# git pull - tim si to nahraji do puvodni slozky, kde program vzniknul pred klonovanim - stahni ke mne vsechny zmeny zezhora (z GitHubu)
udelam si update praci kolegy
prvni vec rano pri tymovem projektu - dat si git pull a aktualizovat si tak vsechny zmeny ostatnich v teamu

prehled zakladnich prikazu
git init - zalozit novy projekt - nebo ho zalozit na githubu a odtup si ho naklonovat - git clone
git status  ... status
git add . pridava vsechny zmeny do staging area
git cm (commit -m) "popisek" ukladam zmeny
git push   nahravam na GitHub
git pull   nahravam si update od ostatnich
git clone https:....  vytvarim si novou slozku z githubu


### BRANCHES #####

pro vice verzi ruzneho kodu - napr mam funci v programu, ale chci ji rozsirit pro jine programy - tak si na to zalozim novou vetev
rozdeli cely projekt na dve separatni vetve
# git branch experiment
# git checkout experiment - prepnuti vetve
# git branch - ukazuje prehled vetsi

# git merge experiment - spojovani vetvi
pokud konflikt - git mi nabidne moznosti, co prijmout
kdyz se vetev zmerguje, tak zmizi

# nastaveni prijimani zmen ve VS Code v terminalu
# git config --global core.editor "code --wait"



"""