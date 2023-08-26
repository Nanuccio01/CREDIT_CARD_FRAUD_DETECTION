import numpy as np
import pandas as pd 
import seaborn as sns
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,f1_score
from sklearn.metrics import roc_curve, auc
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib import colors
import plotly.graph_objs as go
from plotly.offline import iplot
from plotly.subplots import make_subplots
from scipy import stats
from scipy.stats import norm, skew
import warnings
warnings.filterwarnings("ignore")

csv_path = '/Users/tanon/CREDIT_CARD_FRAUD_DETECTION/Dataset/creditcard.csv'
dataset = pd.read_csv(csv_path)

#Crea una copia del DataFrame
data=dataset.copy()

# Dato che la maggior parte dei nostri dati è già stata scalata, dovremmo scalare le colonne che sono rimaste da scalare (Importo e Tempo)
rob_scaler = RobustScaler()

# Creazione di nuove colonne con i dati scalati di Importo e Tempo
data['scaled_amount'] = rob_scaler.fit_transform(data['Amount'].values.reshape(-1,1))
data['scaled_time'] = rob_scaler.fit_transform(data['Time'].values.reshape(-1,1))

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

# Estrai le features (variabili indipendenti) dal dataframe escludendo la colonna "Class" e trasformale in un array
X = data.drop(["Class"], axis=1).values

# Estrai le etichette di classe dalla colonna "Class" del dataframe e trasformale in un array
y = data["Class"].values

# Suddividi i dati in training set e test set usando il metodo train_test_split
# X_train conterrà le features del training set, y_train conterrà le etichette di classe del training set
# X_test conterrà le features del test set, y_test conterrà le etichette di classe del test set
Original_X_train, Original_X_test, Original_y_train, Original_y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea un oggetto StandardScaler per la standardizzazione dei dati
# sc = StandardScaler()

# Applica la standardizzazione alle features del training set
# X_train = sc.fit_transform(X_train)

# Applica la standardizzazione alle features del test set usando la media e la deviazione standard calcolate dal training set
#X_test = sc.transform(X_test)

knn=KNeighborsClassifier()
dtc=DecisionTreeClassifier()
rfc=RandomForestClassifier()
gbc=GradientBoostingClassifier()
abc=AdaBoostClassifier()

models = [knn, dtc, rfc, gbc, abc]
model_names = ['KNN', 'Decision Tree', 'Random Forest', 'Gradient Boosting', 'AdaBoost']

for model in models:
    model.fit(Original_X_train, Original_y_train)
    Original_y_pred = model.predict(Original_X_test)
    print(type(model).__name__, "Model Test Accuracy Score is: ", accuracy_score(Original_y_test, Original_y_pred))
    print(type(model).__name__, "Model Test F1 Score is: ", f1_score(Original_y_test, Original_y_pred))
    print(type(model).__name__,"Mean_absolute_error: ",mean_absolute_error(Original_y_test, Original_y_pred))
    print(type(model).__name__,"Mean_squared_error: ",mean_squared_error(Original_y_test, Original_y_pred))
    print(type(model).__name__,"Root_mean_squared_error: ",np.sqrt(mean_squared_error(Original_y_test, Original_y_pred)))
    print(type(model).__name__,"R2_score: ",r2_score(Original_y_test, Original_y_pred))
    print(type(model).__name__,"Classification_report: \n",classification_report(Original_y_test, Original_y_pred))