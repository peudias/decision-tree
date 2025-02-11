import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import graphviz
import os

# Carregar o dataset
file_path = "../dataset/dataCSV.csv"
data = pd.read_csv(file_path)

# Criar a variável alvo (Aprovado/Reprovado)
threshold = 60

data['Grade Category'] = data['Grades'].apply(lambda x: 'Aprovado' if x >= threshold else 'Reprovado')

# Preparar os dados
X = data[['Socioeconomic Score', 'Study Hours', 'Sleep Hours', 'Attendance (%)']]
y = data['Grade Category']

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar a árvore de decisão
tree_grades = DecisionTreeClassifier(criterion='entropy', random_state=42)
tree_grades.fit(X_train, y_train)

# Fazer previsões
y_pred = tree_grades.predict(X_test)

# Exibir resultados
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))
print("Acurácia:", accuracy_score(y_test, y_pred))

