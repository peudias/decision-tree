import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

# Treinar a Árvore de Decisão
tree_grades = DecisionTreeClassifier(criterion='entropy', random_state=42)
tree_grades.fit(X_train, y_train)
y_pred_tree = tree_grades.predict(X_test)
accuracy_tree = accuracy_score(y_test, y_pred_tree)

# Implementação do KNN
clf_knn = KNeighborsClassifier(n_neighbors=5)
clf_knn.fit(X_train, y_train)
y_pred_knn = clf_knn.predict(X_test)
accuracy_knn = accuracy_score(y_test, y_pred_knn)

# Implementação do SVM
clf_svm = SVC(kernel='linear', random_state=42)
clf_svm.fit(X_train, y_train)
y_pred_svm = clf_svm.predict(X_test)
accuracy_svm = accuracy_score(y_test, y_pred_svm)

# Exibir resultados
print("Acurácia dos modelos:")
print(f"Árvore de Decisão: {accuracy_tree:.4f}")
print(f"KNN: {accuracy_knn:.4f}")
print(f"SVM: {accuracy_svm:.4f}")

# Salvar a Árvore de Decisão como imagem no diretório ../dataset/
plt.figure(figsize=(12, 8))
plot_tree(tree_grades, feature_names=X.columns, class_names=tree_grades.classes_, filled=True)
plt.title("Árvore de Decisão")

output_path = "../dataset/decision_tree.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()  # Fecha a figura para liberar memória

print(f"Imagem da árvore de decisão salva em: {output_path}")
