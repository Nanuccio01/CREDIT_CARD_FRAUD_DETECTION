# CREDIT_CARD_FRAUD_DETECTION
 
## Documentazione Caso di Studio Ingegneria della Conoscenza A.A. 2022/23

### Gruppo di lavoro:
•	Dafne Spaccavento, d.spaccavento@studenti.uniba.it

•	Gaetano Schiralli, g.schiralli5@studenti.uniba.it

### Repository GitHub:
https://github.com/Nanuccio01/CREDIT_CARD_FRAUD_DETECTION

### Definizione dell'Obiettivo e Comprensione dei Dati
#### • L'obiettivo:
L'obiettivo di questo progetto è sviluppare un modello in grado di individuare le transazioni fraudolente all'interno di un dataset contenente transazioni effettuate con carte di credito. Il dataset in questione contiene transazioni effettuate da titolari di carte di credito europee nel mese di settembre 2013.

#### • Comprensione dei Dati: 
Il dataset è composto da transazioni che si sono verificate in due giorni, con un totale di 284.807 transazioni. All'interno di queste transazioni, sono presenti 492 casi di frode. Le variabili di input sono tutte numeriche. Il dataset presenta uno sbilanciamento significativo tra le classi, poiché la classe positiva (frodi) costituisce lo 0.172% di tutte le transazioni.
![Grafico a torta](./Immagini/Grafico%20a%20torta.png)

-Le feature V1, V2, ..., V28 sono campi float e rappresentano le principali componenti ottenute come risultato di una trasformazione PCA (Principal Component Analysis), perchè a causa delle tutele privacy, il nome di questi campi è reso anonimo.
 
-Le uniche feature che non sono state trasformate con PCA sono 'Time' e 'Amount', entrambe intere. La feature 'Time' rappresenta i secondi trascorsi tra ogni transazione e la prima transazione nel dataset, mentre la feature 'Amount' rappresenta l'importo della transazione. La feature 'Class' è la variabile di risposta e assume il valore 1 in caso di frode e 0 altrimenti.

### Preparazione dei Dati e Creazione della Knowledge Base (KB)
#### 1.	Preprocessing dei Dati: 
Una volta caricato il dataset completo si analizza la sua struttura.
Si controlla la presenza di valori mancanti nel Dataset. In questo caso nessun problema vien creato, in quanto tutte le colonne presentano dei valori.
![Valori mancanti](./Immagini/Verifica%20valori%20mancanti.png)

Successivamente analizzando il dataset per la ricerca di valori nulli come importo, si è notato che:  
-Il numero delle transazioni fraudolente con importo nullo (Amount=0) è: 27   
-Il numero delle transazioni legittime con importo nullo (Amount=0) è: 1798   
Inizialmente si stava considerando l'eliminazione di questi campi poiché non sembrava esserci un motivo o uno scopo chiaro per la loro presenza, in quanto una transazione non si potrebbe definire valida con un ammontare pari a zero. Ricercando ulteriolmente però, si è appurato che esistono sia venditori che effettuano una transazione di prova per verificare gli estremi della carta bancaria, e sia siti web di lotterie o concorsi dove il vincitore effettua una transazione con ammontare pari a zero. Considerando codeste variabili reali quindi, tali righe sono state accettate come valide nel dataset.

#### 2. Creazione della Knowledge Base: 
Successivamente abbiamo scelto di analizzare e descrivere solo le colonne 'Time', 'Amount' e 'Class' (tralasciando le feature V1, V2, ..., V28)per ottenere una visione dettagliata di alcune delle caratteristiche chiave dei dati che possono avere un impatto significativo sull'analisi delle frodi su carte di credito:

-"Amount" (Importo della Transazione):
Si analizza questa colonna per capire la distribuzione degli importi ed il totale delle transazioni nel dataset. L'importo delle transazioni potrebbe variare ampiamente e potrebbe essere utile comprendere se ci sono trend o pattern specifici nella distribuzione degli importi per le transazioni legittime o fraudolente.

-"Time" (Tempo della Transazione):
Si esamina questa colonna per identificare qualsiasi modello temporale nei dati. Potrebbe esserci una correlazione tra i momenti delle transazioni e la probabilità di frode. Analizzando questa colonna, si potrebbero  individuare intervalli di tempo in cui si verificano più frodi o altre tendenze temporali interessanti, in quanto nel dataset sono presenti più transazioni per ogni secondo analizzato.
![Totale transazioni per ora](./Immagini/Totale%20transazioni%20per%20ora.png)
Da questo grafico possiamo notare che le transazioni fraudolente hanno una distribuzione più uniforme nel tempo rispetto alle transazioni legittime: esse sono distribuite in modo più uniforme nel tempo, al contrario delle transazioni legittime che subiscono un calo durante le ore notturne del fuso orario europeo.

-"Class" (Classe di Transazione - Legittima(0) o Fraudolenta(1)):
Si inserisce questa colonna perché rappresenta la variabile target dell'analisi delle frodi. Sebbene la si inserisce solo per capire la distribuzione delle classi nel dataset (già analizzate in precedenza), questo campo è nuovamente analizzato per completezza.

Qui troviamo riportate le statistiche descrittive delle tre features sopra descritte:
![Statistiche](./Immagini/Statistiche%20descrittive.png)
Guardando alla caratteristica "Time", possiamo confermare che i dati contengono 284807 transazioni, distribuite durante 2 giorni consecutivi (o 172792 secondi).

Dopo aver esplorato i dati, possiamo ora affermare che non c'è alcun pattern significativo tra i dati.



(Costruiamo una Knowledge Base (KB) che modelli le relazioni tra gli elementi nel dataset. Identifichiamo gli individui (transazioni) e le proprietà rilevanti, come le feature V1-V28, Time e Amount. Definiamo le relazioni tra queste proprietà, come ad esempio relazioni di sequenza temporale tra le transazioni.)








3.	Definizione delle Regole di Inferenza: Definiamo regole di inferenza nella KB che ci permettano di dedurre nuove informazioni o riconoscere pattern all'interno dei dati. Ad esempio, possiamo definire regole che catturino comportamenti anomali spesso associati alle transazioni fraudolente.
4.	Integrazione di Ontologie: Utilizziamo ontologie o conoscenza di dominio per arricchire la KB e consentire al modello di comprendere meglio le caratteristiche delle transazioni e le possibili relazioni tra di loro.
La fase di Preparazione dei Dati e Creazione della KB è fondamentale per costruire una base solida per il nostro modello di rilevamento delle frodi. Una volta completati questi passaggi, possiamo procedere con lo sviluppo e l'addestramento dei modelli di rilevamento delle transazioni fraudolente utilizzando modelli probabilistici relazionali e altre tecniche di apprendimento automatico.




Dato il disequilibrio tra le classi, si consiglia di misurare l'accuratezza utilizzando l'Area Under the Precision-Recall Curve (AUPRC), poiché la matrice di confusione non è significativa per la classificazione sbilanciata.
