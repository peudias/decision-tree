# 🌳 Árvores de Decisão em Python

## 🎯 Objetivo

Desenvolver uma árvore de decisão mais complexa com 10 perguntas e explorar datasets do Kaggle e do UCI Machine Learning Repository para criar novas aplições utilizando árvores de decisão.

---

## 1️⃣ [Parte 1: Desafio - Árvore de Decisão com 10 Perguntas](https://github.com/peudias/decision-tree/blob/main/src/parte1.py)

Implementação de uma árvore de decisão que ajuda uma pessoa a decidir entre diferentes esportes, com base nas respostas a 10 perguntas.

Utiliza-se uma estrutura de funções recursivas para simular uma árvore de decisão interativa. O programa faz perguntas baseadas nas preferências do usuário, como esportes individuais ou em equipe, intensidade, contato físico e ambiente, até chegar a uma sugestão personalizada de esportes. Essa abordagem permite direcionar as escolhas do usuário de forma dinâmica e intuitiva, garantindo recomendações adequadas.

---

## 2️⃣ [Parte 2: Exploração de Datasets no Kaggle e UCI](https://github.com/peudias/decision-tree/blob/main/src/parte2.py)

Explorando dados reais para aplicar árvores de decisão em problemas práticos.

Nesta parte, uma árvore de decisão é criada e treinada utilizando um [dataset](https://www.kaggle.com/datasets/rishidamarla/toughest-sports-by-skill) chamado **"The World’s Toughest Sports"** disponível no site da **Kaggle**. O dataset contém atributos físicos e habilidades, como força, agilidade e resistência, associados a diferentes esportes. Com o uso das bibliotecas `pandas`, `scikit-learn` e `graphviz`, o modelo identifica padrões nos dados e classifica os esportes de forma precisa. A visualização gerada em formato gráfico facilita a interpretação das decisões tomadas pelo modelo e oferece uma análise clara e detalhada dos resultados.

---

### 🛠️ Tecnologias e Ferramentas

- **Visual Studio Code**
- **Python 3.9+**
- **Bibliotecas Utilizadas**:
  - `pandas`: Manipulação de dados.
  - `scikit-learn`: Implementação do modelo de árvore de decisão.
  - `graphviz`: Visualização da árvore de decisão.
  - `openpyxl`: Leitura de arquivos Excel.

---

### 🔁 Compilação e Execução

Para tanto, temos as seguintes diretrizes de execução:

| Comando               | Função                                                               |
| --------------------- | -------------------------------------------------------------------- |
| `python3 filename.py` | Executa o arquivo — Substitua filename pelo nome do arquivo desejado |
