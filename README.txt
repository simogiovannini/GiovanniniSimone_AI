Istruzioni per l'utilizzo del codice scritto per l'esercizio

0. Tutti i pacchetti e le librerie necessarie ad eseguire questo codice
	sono salvate nel file requirements.txt. Evito quindi di salvare
	la cartella venv su Github.

1. Nel dataset German, gli spazi tra i vari attributi erano diversi: 
	ho dovuto, quindi, scaricare e riformattare il file.
	Il codice, perciò, utilizzerà i datasets riposti nella cartella
	datasets e non accederà a quelli del database UCI tramite link.

2. Tutti i dati presenti nella relazione sono stati ricavati ponendo
	qualsiasi seed o random_state al valore di 0 (zero).

3. Al termine dell'esecuzione verrano prodotti due file png, contenenti
	i punteggi ottenuti dai vari algloritmi.
	I file saranno salvati nella cartella contente il file main.py.

4. Gli altri file .py che sono importati in main.py, si trovano nella
	cartella source.

5. Il metodo con il quale stampo le tabelle è ispirato alla guida:
	https://towardsdatascience.com/simple-little-tables-with-matplotlib-9780ef5d0bc4
	Ho solamente adattato il codice alle mie esigenze.

Simone Giovannini
	
