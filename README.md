# Online-Payments-Fraud-Detection-Python-ML

Esta é uma analise de detecção de fraude de pagamentos online com Machine Learning.
Esse tipo de analise atualmente é feito por bancos para garantir que o pagamento é de fato autentico.
Usei o dataset que pode ser encontrado <a href="https://www.kaggle.com/datasets/ealaxi/paysim1?resource=download">neste link</a> 
que contém informações históricas sobre transações fraudulentas que podem ser usadas para detectar fraudes em pagamentos online.

Abaixo estão todas as colunas do conjunto de dados que estou usando aqui: 

<strong>step:</strong> representa uma unidade de tempo onde 1 step equivale a 1 hora

<strong>type:</strong> tipo de transação online

<strong>amount:</strong> o valor da transação

<strong>nameOrig:</strong> cliente iniciando a transação

<strong>oldbalanceOrg:</strong> saldo antes da transação

<strong>newbalanceOrig:</strong> saldo após a transação

<strong>nameDest:</strong> destinatário da transação

<strong>oldbalanceDest:</strong> saldo inicial do destinatário antes da transação

<strong>newbalanceDest:</strong> o novo saldo do destinatário após a transação

<strong>isFraud:</strong> transação fraudulenta


Agora que estão cientes da analise e do arquivo, acompanhe a analise no arquivo .py 
