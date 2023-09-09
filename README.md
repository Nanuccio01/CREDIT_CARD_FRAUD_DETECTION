# CREDIT_CARD_FRAUD_DETECTION
 
## Documentazione Caso di Studio Ingegneria della Conoscenza A.A. 2022/23

### Gruppo di lavoro:
- Dafne Spaccavento, d.spaccavento@studenti.uniba.it

- Gaetano Schiralli, g.schiralli5@studenti.uniba.it

### Repository GitHub:
https://github.com/Nanuccio01/CREDIT_CARD_FRAUD_DETECTION

### Indice:

#### 1. Definizione dell'Obiettivo e Comprensione dei Dati:
- L'obiettivo
- Analisi Esplorativa dei Dati

#### 2. Preparazione dei Dati e Creazione della Knowledge Base (KB)
- Preprocessing dei Dati  
- Creazione della Knowledge Base

#### 3. Overfitting
- Concetto e Tecniche utilizzate per mitigare l'Overfitting

#### 4. Classificazione Transazioni
Applicazione di Cross-Validation
Utilizzo degli Alberi di Decisione
Applicazione di Regressione e Classificazione Lineare
Valutazione delle Prestazioni dei Modelli
Apprendimento Probabilistico con Naive Bayes

#### 5. Introduzione al Modello Probabilistico Naive Bayes
Adattamento di Naive Bayes al Problema
Valutazione delle Prestazioni di Naive Bayes
Apprendimento Non Supervisionato con Clustering

#### 6. Concetto di Apprendimento Non Supervisionato e Clustering
Applicazione del Metodo di Clustering (es. K-Means)
Interpretazione dei Cluster Ottenuti
Conclusione

#### 7. Riassunto dei Risultati
Discussione delle Sfide e Prospettive Future

---------------------------------------------------------------------------------------------------------------------

### 1. Definizione dell'Obiettivo e Comprensione dei Dati
#### • L'obiettivo:
L'obiettivo di questo progetto è sviluppare un modello in grado di individuare le transazioni fraudolente all'interno di un dataset contenente transazioni effettuate con carte di credito. Il dataset in questione contiene transazioni effettuate da titolari di carte di credito europee nel mese di settembre 2013.

#### • Analisi Esplorativa dei Dati: 
Il dataset è composto da transazioni che si sono verificate in due giorni, con un totale di 284.807 transazioni. All'interno di queste transazioni, sono presenti 492 casi di frode. Le variabili di input sono tutte numeriche. Il dataset presenta uno sbilanciamento significativo tra le classi, poiché la classe positiva (frodi) costituisce lo 0.172% di tutte le transazioni.
![Grafico a torta](./Immagini/Grafico%20a%20torta.png)

- Le feature V1, V2, ..., V28 sono campi float e rappresentano le principali componenti ottenute come risultato di una trasformazione PCA (Principal Component Analysis), perchè a causa delle tutele privacy, il nome di questi campi è reso anonimo. Per implementare una trasformazione PCA, le feature devono essere preventivamente scalate. In questo caso, quindi, tutte le feature V1, V2, ..., V28 sono state scalate o almeno è ciò che assumiamo abbiano fatto gli sviluppatori del dataset.
 
- Le uniche feature che non sono state trasformate con PCA sono 'Time' e 'Amount', entrambe intere. La feature 'Time' rappresenta i secondi trascorsi tra ogni transazione e la prima transazione nel dataset, mentre la feature 'Amount' rappresenta l'importo della transazione. La feature 'Class' è la variabile di risposta e assume il valore 1 in caso di frode e 0 altrimenti.

Successivamente abbiamo scelto di analizzare e descrivere approfonditamente, solo le colonne 'Time', 'Amount' e 'Class' (tralasciando le feature V1, V2, ..., V28), per ottenere una visione dettagliata di alcune delle caratteristiche chiave dei dati che possono avere un impatto significativo sull'analisi delle frodi su carte di credito:

- "Amount" (Importo della Transazione):
Si analizza questa colonna per capire la distribuzione degli importi ed il totale delle transazioni nel dataset. L'importo delle transazioni potrebbe variare ampiamente e potrebbe essere utile comprendere se ci sono trend o pattern specifici nella distribuzione degli importi per le transazioni legittime o fraudolente.

- "Time" (Tempo della Transazione):
Si esamina questa colonna per identificare qualsiasi modello temporale nei dati. Potrebbe esserci una correlazione tra i momenti delle transazioni e la probabilità di frode. Analizzando questa colonna, si potrebbero  individuare intervalli di tempo in cui si verificano più frodi o altre tendenze temporali interessanti, in quanto nel dataset sono presenti più transazioni per ogni secondo analizzato.
![Totale transazioni per ora](./Immagini/Totale%20transazioni%20per%20ora.png)
Da questo grafico possiamo notare che le transazioni fraudolente hanno una distribuzione più uniforme nel tempo rispetto alle transazioni legittime: esse sono distribuite in modo più uniforme nel tempo, al contrario delle transazioni legittime che subiscono un calo durante le ore notturne del fuso orario europeo.

- "Class" (Classe di Transazione - Legittima(0) o Fraudolenta(1)):
Si inserisce questa colonna perché rappresenta la variabile target dell'analisi delle frodi. Sebbene la si inserisce solo per capire la distribuzione delle classi nel dataset (già analizzate in precedenza), questo campo è nuovamente analizzato per completezza.

Qui troviamo riportate le statistiche descrittive delle tre features sopra descritte:
![Statistiche](./Immagini/Statistiche%20descrittive.png)
Guardando alla caratteristica "Time", possiamo confermare che i dati contengono 284807 transazioni, distribuite durante 2 giorni consecutivi (o 172792 secondi).

Dopo aver esplorato inizialmente i dati, possiamo affermare a colpo d'occhio di non aver notato nessuna ripetizione o comportamento significativo tra essi.

Per avere un quadro più generale delle correlazioni, quindi, si sono utilizzati i grafici KDE che mostrano la stima delle densità delle caratteristiche per due classi: Classe 0 (transazioni legittime) e Classe 1 (transazioni fraudolente): 
- I grafici servono a visualizzare come le distribuzioni delle caratteristiche differiscano tra le due classi, infatti consentono di vedere la forma approssimativa delle distribuzioni delle caratteristiche per entrambe le classi. Se ci sono differenze significative nelle distribuzioni tra le classi per una particolare caratteristica, potrebbe indicare che essa è utile per distinguere tra transazioni legittime e fraudolente.
![Densità](./Immagini/Densità%201.png)
![Densità2](./Immagini/Densità%202.png)

Per alcune delle caratteristiche possiamo osservare una buona selettività in termini di distribuzione per i due valori della classe: 
- V4 e V11 hanno distribuzioni chiaramente separate per i valori di Classe 0 e 1.
- V12 e V14 sono parzialmente separati.
- V1, V2, V3 e V10 hanno un profilo piuttosto distinto.
- V25, V26 e V28 hanno profili simili per i due valori della Classe.

In generale, con poche eccezioni (Tempo e Importo), la distribuzione delle caratteristiche per le transazioni legittime (valori di Classe = 0) è centrata intorno a 0, talvolta con una lunga coda su uno dei lati estremi. Allo stesso tempo, le transazioni fraudolente (valori di Classe = 1) hanno una distribuzione asimmetrica (sbilanciata).

Basandoci sui grafici KDE, potremmo fare delle scelte informate su quali feature includere nel modello successivamente. Se alcune caratteristiche hanno distribuzioni molto simili tra le due classi, potremmo decidere di escluderle dal modello, riducendo così la complessità e migliorando le prestazioni. 

### 2. Preparazione dei Dati e Creazione della Knowledge Base (KB)
#### Preprocessing dei Dati:

Gestione dei dati mancanti e non utilizzabili: 
Una volta caricato il dataset completo si analizza la sua struttura.
Si controlla la presenza di valori mancanti nel Dataset. In questo caso nessun problema vien creato, in quanto tutte le colonne presentano dei valori.
![Valori mancanti](./Immagini/Verifica%20valori%20mancanti.png)

Successivamente analizzando il dataset per la ricerca di valori nulli come importo, si è notato che:  
- Il numero delle transazioni fraudolente con importo nullo (Amount=0) è: 27   
- Il numero delle transazioni legittime con importo nullo (Amount=0) è: 1798

Inizialmente si stava considerando l'eliminazione di questi campi poiché non sembrava esserci un motivo o uno scopo chiaro per la loro presenza, in quanto una transazione non si potrebbe definire valida con un ammontare pari a zero. Ricercando ulteriolmente però, si è appurato che esistono sia venditori che effettuano una transazione di prova per verificare gli estremi della carta bancaria, e sia siti web di lotterie o concorsi dove il vincitore effettua una transazione con ammontare pari a zero. Considerando codeste variabili reali quindi, tali righe sono state accettate come valide nel dataset.

Inoltre in questa fase, andremo a scalare le colonne Time e Amount, per avere valori simili alle altre colonne precendentemente scalate in seguito alla trasformazione PCA. 
![Amount e tempo scalati](./Immagini/Amount%20e%20Tempo%20scalati.png)

#### Creazione della Knowledge Base: 

In questa fase di creazione della Knowledge Base, dopo aver esplorato il nostro dataset, a causa delle limitate informazioni da esso contenute e della mancanza di altri dataset rilevanti da accorpare, non siamo stati in grado di arricchire ulteriormente la nostra Knowledge Base. Ci siamo concentrati sull'analisi e l'interpretazione delle informazioni presenti nel dataset attuale, utilizzando strumenti di visualizzazione e tecniche di analisi per ottenere una comprensione più approfondita delle caratteristiche e dei modelli presenti nei dati.

### 3. Concetto di Overfitting
#### Concetto e Tecniche utilizzate per mitigare l'Overfitting:
 
Uno dei problemi che potrebbe creare lo sbilanciamento del nostro dataset originale è quello dell'overfitting.

L'overfitting è una condizione in cui un modello di apprendimento automatico si adatta troppo strettamente ai dati di addestramento. Questo significa che il modello cattura non solo i modelli sottostanti nei dati, ma anche il rumore o le variazioni casuali presenti nei dati di addestramento. Di conseguenza, il modello potrebbe avere una performance eccezionalmente buona sui dati di addestramento, ma si comporta in maniera pessima su nuovi dati che non ha mai elaborato prima.

Dunque, se utilizziamo questo dataframe come base per i nostri modelli predittivi e per le analisi, potremmo ottenere molti errori, in quanto gli algoritmi probabilmente "assumeranno" che la maggior parte delle transazioni non siano truffe(ricordiamo che sono solo lo 0.172% di tutte le transazioni). Siccome il nostro modello non è stato ideato per fare ipotesi, ma per essere sicuro di quando si verifichi una frode, andreamo ad utilizzare tecniche di regolarizzazione, limitando la complessità del modello. 

Un altro motivo per cui andremo ad utilizzare le varie tecniche di mitigazione delle problematiche è per le Correlazioni Errate: Siccome non sappiamo cosa rappresentano le feature "V", sarà comunque utile capire come ciascuna di queste feature influenzerà il risultato (Frode o Non Frode). Avendo un dataframe sbilanciato, quindi, non saremo in grado di vedere le vere correlazioni tra la classe e le feature.

Per questo andremo ad utilizzare le seguenti tecniche:
- Creare un sottocampionamento del dataset (sub-Sampling): In questo scenario, il nostro subsample sarà un dataframe con un rapporto 50/50 tra transazioni fraudolente e non fraudolente. Ciò significa che il nostro sottocampionamento avrà lo stesso numero di transazioni fraudolente e non fraudolente, aiutando i nostri algoritmi a comprendere meglio i pattern che determinano se una transazione è una frode o meno. Le transazioni non fraudolente saranno casuali e sempre diverse nelle varie ripetizioni.
- Utilizzare la Cross-validation: è una procedura di campionamento ripetuto utilizzata per valutare modelli di apprendimento automatico su un campione limitato di dati. La procedura ha un singolo parametro chiamato k che si riferisce al numero di fold o gruppi in cui un dato campione deve essere suddiviso. Pertanto, spesso la procedura è chiamata cross-validation k-fold. Lo scopo della cross-validation è testare la capacità di un modello di apprendimento automatico di prevedere nuovi dati. 

Il miglior modello non è quello che fornisce previsioni accurate sui dati di addestramento, ma quello che offre buone previsioni su nuovi dati e evita Overfitting e Underfitting.

















### 4. Classificazione Transazioni

Nelle transazioni, le features di input saranno le colonne numeriche, ad esempio "Time", "Amount" e le features "V1" a "V28".
La feature target sarà la colonna "Class", che indica se una transazione è fraudolenta o legittima.

Esempi di Training e Test:
Gli "esempi di training" saranno un sottoinsieme del dataset con tutte le colonne, inclusa la colonna "Class". Questi esempi verranno utilizzati per addestrare il modello.

Gli "esempi di test" saranno un altro sottoinsieme del dataset contenente solo le colonne numeriche (senza la colonna "Class"). Questi esempi verranno utilizzati per testare il modello addestrato e fare previsioni sulle classi delle transazioni.

Considerando le feature del dataset, abbiamo individuato un possibile target per un task di classificazione: IS_FRAUD per una data transazione è
    ● 0 se la transazione è legittima
    ● 1 altrimenti

Ovviamente utilizzando il metodo 10-fold Cross-Validation, non abbiamo bisogno di fare manualmente questa divisione.

# K-NN 
Considerando che il nostro dataset contiene una porzione significativa di dati privati i quali non possono essere selezionati o esclusi a causa della mancanza di conoscenza sul loro contenuto, potrebbe essere prudente utilizzare tutte le features disponibili nel contesto dell'algoritmo k-Nearest Neighbors (k-NN). Questo approccio ci permette di sfruttare tutte le informazioni disponibili per effettuare le previsioni, tenendo presente che alcune features potrebbero contenere informazioni utili.

Tuttavia, siamo consapevoli dei rischi associati all'utilizzo di tutte le features, specialmente quando il dataset contiene dati sensibili o potenzialmente rumorosi. L'aumento della dimensionalità dello spazio delle feature potrebbe comportare distorsioni nelle misure delle distanze tra le osservazioni, influenzando le prestazioni del modello k-NN.

Quindi, il K-NN è stato sostanzialmente eseguito sul dataset avente 31 features.
- Features di input: Time, "Amount e le features da "V1" a "V28".
- Features di output: la classe Class.

# Alberi di decisione
Gli alberi decisionali sono uno strumento potente per la classificazione e la regressione, in quanto dividono iterativamente il dataset in sottoinsiemi sempre più ristretti, utilizzando le feature disponibili per prendere decisioni. Tuttavia, possono essere soggetti all'overfitting, cioè adattarsi troppo bene ai dati di addestramento e non generalizzare bene ai nuovi dati.

Per superare questo problema, abbiamo esplorato l'uso di algoritmi ensemble, che combinano più alberi decisionali per ottenere risultati migliori e più stabili. Ecco alcuni dei principali algoritmi ensemble che abbiamo utilizzato:

- DecisionTreeClassifier: Abbiamo iniziato con il DecisionTreeClassifier, un algoritmo che costruisce un singolo albero decisionale. Questo ci ha permesso di esplorare le potenzialità di base degli alberi decisionali nel nostro caso di rilevamento delle transazioni fraudolente.
SPIEGARE GLI IPERPARAMETRI

- RandomForest: Successivamente, abbiamo implementato il RandomForest, un algoritmo ensemble che combina diversi alberi decisionali creati su sottoinsiemi casuali dei dati e delle feature. Questo ha migliorato la generalizzazione e la robustezza del nostro modello, riducendo l'overfitting.
SPIEGARE COME ABBIAMO SCELTO IL NUMERO DI ALBERI

- AdaBoost: Abbiamo anche esaminato l'AdaBoost, un algoritmo che assegna maggior peso agli esempi classificati erroneamente, permettendo agli alberi successivi di concentrarsi sulle aree difficili da classificare. Questo ha portato a un miglioramento delle prestazioni sui casi più complessi.

- GradientBoostingClassifier: Infine, abbiamo sperimentato il GradientBoostingClassifier, che costruisce gli alberi in modo sequenziale, ognuno correggendo gli errori dei precedenti. Questa metodologia ha permesso di ottenere previsioni sempre più accurate, affinando progressivamente il modello.

In sintesi, attraverso l'applicazione di alberi decisionali e degli algoritmi ensemble sopra menzionati, siamo stati in grado di creare modelli che possono  individuare transazioni fraudolente all'interno del nostro dataset.  

# Logistic Regression
La regressione logistica è computazionalmente efficiente, il che significa che può essere addestrata su grandi dataset in tempi relativamente brevi. Questo è vantaggioso quando si hanno dataset con molte transazioni, come nel nostro caso.
PARLARE DELLA REGOLARIZZAZIONE

(da inserire nel codice e Assicurati di sostituire X e y con le tue features e il tuo target, rispettivamente. Questo esempio ti fornirà una stima delle prestazioni del modello di regressione logistica utilizzando la cross-validation.)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Supponiamo che tu abbia già preparato i tuoi dati come X (features) e y (target).

# Creazione di un modello di regressione logistica
logistic_model = LogisticRegression()

# Eseguire la 10-fold cross-validation e calcolare le metriche di valutazione
accuracy_scores = cross_val_score(logistic_model, X, y, cv=10, scoring='accuracy')
precision_scores = cross_val_score(logistic_model, X, y, cv=10, scoring='precision')
recall_scores = cross_val_score(logistic_model, X, y, cv=10, scoring='recall')
f1_scores = cross_val_score(logistic_model, X, y, cv=10, scoring='f1')

# Calcolare le medie delle metriche
mean_accuracy = accuracy_scores.mean()
mean_precision = precision_scores.mean()
mean_recall = recall_scores.mean()
mean_f1 = f1_scores.mean()

# Stampare i risultati
print("Mean Accuracy:", mean_accuracy)
print("Mean Precision:", mean_precision)
print("Mean Recall:", mean_recall)
print("Mean F1-score:", mean_f1)

#### 5. Concetto di Apprendimento Non Supervisionato e Clustering
Il clustering può suddividere il Nostro dataset in gruppi omogenei in base a determinate caratteristiche o pattern. Questa segmentazione può aiutare a identificare se ci sono gruppi di transazioni legittime o gruppi di transazioni fraudolente con caratteristiche comuni. Questo potrebbe rivelare insight sul comportamento dei truffatori o dei clienti legittimi.







Per garantire una valutazione accurata e affidabile delle capacità predittive dei nostri modelli, adotteremo il metodo "10-fold Cross-Validation", che ci consentirà di valutare le prestazioni dei nostri classificatori in modo robusto e accurato.

Durante ciascuna iterazione, il classificatore verrà addestrato sui dati di addestramento e valutato sui dati di test. Le metriche di valutazione, come l'accuratezza, la precisione, il richiamo e l'F1-score, verranno calcolate per ogni iterazione. Alla fine delle 10 iterazioni, calcoleremo le medie di queste metriche per ottenere una stima complessiva delle prestazioni del classificatore.
La "10-fold Cross-Validation" è un caso specifico della k-fold Cross-Validation in cui il valore di "k" è impostato a 10. Ciò significa che il dataset verrà diviso in 10 parti uguali, e il processo di addestramento e valutazione verrà ripetuto 10 volte.
Le ragioni per preferire la "10-fold Cross-Validation" includono:

Bilanciamento tra varianza e bias: Utilizzare un numero maggiore di fold (come nel caso della 10-fold) può fornire una stima più accurata delle prestazioni del modello, poiché il processo di addestramento e valutazione viene eseguito su un maggior numero di partizioni dei dati.

Robustezza: L'uso di più fold rende la valutazione più robusta rispetto alle fluttuazioni casuali nei dati di training e test.

Precisione della stima: Maggiore è il numero di iterazioni, maggiore sarà la precisione delle stime delle metriche di valutazione, come l'accuratezza, la precisione e il richiamo.

Rappresentatività: Utilizzando più fold, possiamo avere un'idea migliore di come il modello generalizza su diverse parti del dataset, riducendo il rischio di ottenere una valutazione distorta da una singola divisione casuale dei dati.

Tuttavia, è importante notare che utilizzare un valore elevato di "k" (ad esempio 10) potrebbe richiedere più tempo di calcolo rispetto a valori più bassi, poiché richiede più iterazioni.