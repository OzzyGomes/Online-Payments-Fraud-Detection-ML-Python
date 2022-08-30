# Online-Payments-Fraud-Detection-Python-ML

Esta é uma analise de detecção de fraude de pagamentos online com Machine Learning.
Esse tipo de analise atualmente é feito por bancos para garantir que o pagamento é de fato autentico.
Usei o dataset que pode ser encontrado <a href="https://www.kaggle.com/datasets/ealaxi/paysim1?resource=download">neste link</a> 
que contém informações históricas sobre transações fraudulentas que podem ser usadas para detectar fraudes em pagamentos online.

Abaixo estão todas as colunas do conjunto de dados que estou usando aqui:

step: representa uma unidade de tempo onde 1 step equivale a 1 hora
type: tipo de transação online
amount: o valor da transação
nameOrig: cliente iniciando a transação
oldbalanceOrg: saldo antes da transação
newbalanceOrig: saldo após a transação
nameDest: destinatário da transação
oldbalanceDest: saldo inicial do destinatário antes da transação
newbalanceDest: o novo saldo do destinatário após a transação
isFraud: transação fraudulenta

Agora que estão ciente da analise e do arquivo, acompanhe a analise no arquivo .py 
