import pandas as pd
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split


csv_path = '/Users/tanon/CREDIT_CARD_FRAUD_DETECTION/Dataset/creditcard.csv'
dataset = pd.read_csv(csv_path)

#Crea una copia del DataFrame
data=dataset.copy()

# Dato che la maggior parte dei nostri dati è già stata scalata, dovremmo scalare le colonne che sono rimaste da scalare (Importo e Tempo)
rob_scaler = RobustScaler()

# Creazione di nuove colonne con i dati scalati di Importo e Tempo
data['scaled_amount'] = rob_scaler.fit_transform(df['Amount'].values.reshape(-1,1))
data['scaled_time'] = rob_scaler.fit_transform(df['Time'].values.reshape(-1,1))

# Rimozione delle colonne originali di Importo e Tempo
data.drop(['Time','Amount'], axis=1, inplace=True)

# Conserva le colonne scalate 'scaled_amount' e 'scaled_time' in nuove variabili
scaled_amount = data['scaled_amount']
scaled_time = data['scaled_time']

# Rimuovi le colonne 'scaled_amount' e 'scaled_time' dal dataframe
data.drop(['scaled_amount', 'scaled_time'], axis=1, inplace=True)

# Inserisci nuovamente le colonne scalate 'scaled_amount' e 'scaled_time' come prime due colonne nel dataframe
data.insert(0, 'scaled_amount', scaled_amount)
data.insert(1, 'scaled_time', scaled_time)

# Divide le transazioni in legittime e fraudolente
legitimate_transactions = data[data['Class'] == 0]
fraudulent_transactions = data[data['Class'] == 1]

# Sottocampiona il numero di transazioni legittime per farlo corrispondere al numero di transazioni fraudolente
legitimate_subsample = resample(legitimate_transactions, replace=False, n_samples=len(fraudulent_transactions), random_state=42)

# Combina le transazioni legittime sottocampionate con quelle fraudolente
balanced_subsample = pd.concat([legitimate_subsample, fraudulent_transactions])

# Mischia il sottocampionamento 
balanced_subsample = balanced_subsample.sample(frac=1, random_state=42)

# Divide le features (X) dalla variabile target (y)
X = balanced_subsample.drop('Class', axis=1)  # Features
y = balanced_subsample['Class']  # Target

# Dividi il dataset in training set e test set (80% per il training e 20% per il test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ora hai i tuoi training set e test set pronti per essere utilizzati con i modelli di apprendimento