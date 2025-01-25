import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz

# Carregar o arquivo Excel
file_path = "../dataset/toughestsport.xlsx"
data = pd.read_excel(file_path)

# Preparar os dados
X = data[['END', 'STR', 'PWR', 'SPD', 'AGI', 'FLX', 'NER', 'DUR', 'HAN', 'ANA']]
y_sports = data['SPORT']

# Dividir os dados em treinamento e teste
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y_sports, test_size=0.2, random_state=42)

# Treinar a árvore de decisão
tree_sports = DecisionTreeClassifier(criterion='entropy', random_state=42)
tree_sports.fit(X_train, y_train)

# Exportar a árvore para o formato DOT
dot_data = export_graphviz(
    tree_sports, 
    out_file=None, 
    feature_names=X.columns, 
    class_names=tree_sports.classes_, 
    filled=True, 
    rounded=True, 
    special_characters=True, 
    impurity=False,
    proportion=False
)

# Criar o gráfico da árvore com o Graphviz
graph = graphviz.Source(dot_data)

# Caminho de saída do arquivo
output_dot_path = "../dataset/arvore_decisao_esportes_simplificada.dot"
output_png_path = "../dataset/arvore_decisao_esportes_simplificada_final.png"

# Salvar a árvore simplificada como PNG
graph.render(filename=output_dot_path, format='png', cleanup=True)

# Informar onde o arquivo PNG foi salvo
print(f"Imagem da árvore salva em: {output_png_path}")
