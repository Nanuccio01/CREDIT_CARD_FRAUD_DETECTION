# CREDIT_CARD_FRAUD_DETECTION
 
## Documentazione Caso di Studio Ingegneria della Conoscenza A.A. 2022/23

### Gruppo di lavoro:
•	Dafne Spaccavento, d.spaccavento@studenti.uniba.it 

•	Gaetano Schiralli, g.schiralli5@studenti.uniba.it

### Repository GitHub:
https://github.com/Nanuccio01/CREDIT_CARD_FRAUD_DETECTION

### Definizione dell'Obiettivo e Comprensione dei Dati
##### • L'obiettivo:
L'obiettivo di questo progetto è sviluppare un modello in grado di individuare le transazioni fraudolente all'interno di un dataset contenente transazioni effettuate con carte di credito. Il dataset in questione contiene transazioni effettuate da titolari di carte di credito europee nel mese di settembre 2013.

##### • Comprensione dei Dati: 
Il dataset è composto da transazioni che si sono verificate in due giorni, con un totale di 284.807 transazioni. All'interno di queste transazioni, sono presenti 492 casi di frode. Il dataset presenta uno sbilanciamento significativo tra le classi, poiché la classe positiva (frodi) costituisce lo 0.172% di tutte le transazioni.
Le variabili di input sono numeriche e sono il risultato di una trasformazione PCA (Principal Component Analysis). Le feature V1, V2, ..., V28 rappresentano le principali componenti ottenute con PCA. Le uniche feature che non sono state trasformate con PCA sono 'Time' e 'Amount'. La feature 'Time' rappresenta i secondi trascorsi tra ogni transazione e la prima transazione nel dataset, mentre la feature 'Amount' rappresenta l'importo della transazione. La feature 'Class' è la variabile di risposta e assume il valore 1 in caso di frode e 0 altrimenti.

Dato il disequilibrio tra le classi, si consiglia di misurare l'accuratezza utilizzando l'Area Under the Precision-Recall Curve (AUPRC), poiché la matrice di confusione non è significativa per la classificazione sbilanciata.

### Preparazione dei Dati e Creazione della Knowledge Base (KB)
In questo passo, eseguiremo le seguenti attività:
1.	Preprocessing dei Dati: Carichiamo il dataset e analizziamo la sua struttura. Effettuiamo eventuali operazioni di pulizia dei dati, gestione dei valori mancanti e normalizzazione delle feature numeriche.
2.	Creazione della KB: Costruiamo una Knowledge Base (KB) che modelli le relazioni tra gli elementi nel dataset. Identifichiamo gli individui (transazioni) e le proprietà rilevanti, come le feature V1-V28, Time e Amount. Definiamo le relazioni tra queste proprietà, come ad esempio relazioni di sequenza temporale tra le transazioni.
3.	Definizione delle Regole di Inferenza: Definiamo regole di inferenza nella KB che ci permettano di dedurre nuove informazioni o riconoscere pattern all'interno dei dati. Ad esempio, possiamo definire regole che catturino comportamenti anomali spesso associati alle transazioni fraudolente.
4.	Integrazione di Ontologie: Utilizziamo ontologie o conoscenza di dominio per arricchire la KB e consentire al modello di comprendere meglio le caratteristiche delle transazioni e le possibili relazioni tra di loro.
La fase di Preparazione dei Dati e Creazione della KB è fondamentale per costruire una base solida per il nostro modello di rilevamento delle frodi. Una volta completati questi passaggi, possiamo procedere con lo sviluppo e l'addestramento dei modelli di rilevamento delle transazioni fraudolente utilizzando modelli probabilistici relazionali e altre tecniche di apprendimento automatico.