from statistics import correlation
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#lê o arquivo das transações
df = pd.read_csv('cred_card_dataset.csv', 
                 dtype={'step': int, 
                        'type': str, 
                        'amount': float, 
                        'nameOrig': str,
                        'oldbalanceOrg':float,
                        "newbalanceOrig":float,
                        "nameDest":str,
                        "oldbalanceDest":float,
                        "newbalanceDest":float,
                        "isFraud":int,
                        "isFlaggedFraud":int})

df

# verifica se existe algum valor nulo 
df[df.isnull().sum(axis=1)>0]

# Explorando tipos de transação 
type = df['type'].value_counts()
transactions = type.index
quantity = type.values

#criando gráfico de trasações
figure = px.pie(df, values=quantity, names=transactions, title="Distribuição dos tipos de Transações")
figure.show()

# verificando correlação entre os dados e a coluna isFraud
correlation = df[['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFraud', 'isFlaggedFraud']].corr()
#correlation = df.corr()
correlation['isFraud'].sort_values(ascending=False)

# com a função map() altero 'type' de dados categoricos para dados numericos 
df['type'] = df['type'].map({'CASH_OUT': 1, 'PAYMENT': 2,
                             'CASH_IN': 3, 'TRANSFER': 4,
                             'DEBIT': 5})

# na coluna 'isFraud' faço o oposto
df['isFraud'] = df['isFraud'].map({0: 'No Fraud', 1: 'Fraud'})

df.head()

# separando os dados em dados de treino e dados de teste

x = np.array(df[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig']])
y = np.array(df[['isFraud']])

# treinando o modelo
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.10, random_state=42)
model = DecisionTreeClassifier()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)

#predição
#features = [type, amount, oldbalanceOrg, newbalanceOrig]
features = np.array([[2, 300.00, 9000.60, 8700.60]])
model.predict(features)