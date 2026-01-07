# 📖 Glossário - Machine Learning

## A

**Acurácia (Accuracy)**: Proporção de predições corretas (TP+TN / Total).

**Ajuste (Fitting)**: Processo de treinar modelo aos dados.

**Algoritmo**: Sequência de passos para resolver problema.

**Aprendizado Não-Supervisionado**: ML sem rótulos (clustering, PCA).

**Aprendizado Supervisionado**: ML com dados rotulados (classificação, regressão).

**Árvore de Decisão**: Modelo que toma decisões seguindo estrutura de árvore.

## B

**Bagging**: Técnica de ensemble que treina múltiplos modelos em subamostras.

**Baseline**: Modelo simples de referência para comparação.

**Batch**: Subconjunto de dados usado em uma iteração de treinamento.

**Bias (Viés)**: Tendência do modelo a sistematicamente errar em uma direção.

## C

**Centroide**: Centro de cluster em algoritmos de agrupamento.

**Classificação**: Tarefa de prever categoria/classe.

**Cluster**: Grupo de dados similares identificado por algoritmo.

**Clusterização**: Agrupamento de dados por similaridade.

**Coeficiente de Silhueta**: Métrica de qualidade de clustering (-1 a +1).

**Componente Principal**: Direção de máxima variância em PCA.

**Confusion Matrix (Matriz de Confusão)**: Tabela mostrando VP, VN, FP, FN.

**Cross-Validation (Validação Cruzada)**: Técnica para avaliar modelo dividindo dados em k-folds.

## D

**Dataset**: Conjunto de dados para treinar/testar modelo.

**Decision Boundary (Fronteira de Decisão)**: Limite que separa classes.

**Dendrograma**: Diagrama de árvore mostrando agrupamento hierárquico.

**Dimensionalidade**: Número de features em dataset.

## E

**Elbow Method (Método do Cotovelo)**: Técnica para escolher número de clusters.

**Ensemble**: Combinação de múltiplos modelos para melhorar predições.

**Epoch**: Uma passagem completa por todos dados de treino.

**Erro**: Diferença entre predição e valor real.

**Escala**: Intervalo de valores de variável.

**Especificidade**: Proporção de negativos corretamente identificados (VN / VN+FP).

**Estimador**: Algoritmo que aprende de dados (ex: RandomForest, KMeans).

## F

**F1-Score**: Média harmônica de precisão e recall (2×P×R / P+R).

**Falso Negativo (FN)**: Predizer negativo quando é positivo.

**Falso Positivo (FP)**: Predizer positivo quando é negativo.

**Feature (Característica)**: Atributo/variável de entrada no modelo.

**Feature Engineering**: Criação de novas features a partir das existentes.

**Feature Selection**: Escolha das features mais relevantes.

**Fit**: Treinar modelo com dados.

## G

**Generalização**: Capacidade de modelo performar bem em dados novos.

**Grid Search**: Busca exaustiva por melhores hiperparâmetros.

## H

**Hiperparâmetro**: Configuração externa ao modelo (ex: n_clusters, max_depth).

**Holdout**: Divisão simples de dados em treino e teste.

## I

**Inércia**: Soma das distâncias quadráticas de pontos aos centroides (KMeans).

**Iteração**: Repetição de processo de otimização.

## K

**K-Fold**: Técnica de cross-validation com k divisões.

**K-Means**: Algoritmo de clustering que agrupa em k grupos.

**KNN (K-Nearest Neighbors)**: Algoritmo que classifica baseado em k vizinhos mais próximos.

## L

**Label (Rótulo)**: Categoria/valor alvo que queremos prever.

**Learning Rate**: Taxa de atualização de parâmetros em otimização.

**Logistic Regression**: Modelo para classificação binária.

## M

**MAE (Mean Absolute Error)**: Média dos erros absolutos.

**Matriz de Confusão**: Ver Confusion Matrix.

**Métrica**: Medida de performance do modelo.

**Modelo**: Representação matemática aprendida dos dados.

**MSE (Mean Squared Error)**: Média dos erros quadráticos.

## N

**Normalização**: Ajuste de features para mesma escala (0 a 1).

**n_clusters**: Número de clusters desejado.

**n_components**: Número de componentes principais em PCA.

## O

**Outlier**: Ponto muito distante do padrão geral.

**Overfitting (Sobreajuste)**: Modelo muito ajustado aos dados de treino, ruim em generalizar.

## P

**Parâmetro**: Valor interno aprendido pelo modelo (pesos, coeficientes).

**PCA (Principal Component Analysis)**: Técnica de redução de dimensionalidade.

**Pipeline**: Sequência automatizada de transformações e modelo.

**Precisão (Precision)**: Proporção de positivos preditos que são realmente positivos (VP / VP+FP).

**Predição**: Saída do modelo para nova entrada.

**Predict**: Usar modelo treinado para fazer predições.

**Pre-processamento**: Preparação de dados antes do treino.

## R

**Random Forest**: Ensemble de árvores de decisão.

**Random State**: Semente para reprodutibilidade.

**Recall (Sensibilidade)**: Proporção de positivos corretamente identificados (VP / VP+FN).

**Redução de Dimensionalidade**: Diminuir número de features mantendo informação.

**Regressão**: Tarefa de prever valor numérico contínuo.

**RMSE (Root Mean Squared Error)**: Raiz quadrada de MSE.

**ROC Curve**: Gráfico de taxa VP vs FP para diferentes thresholds.

**R² (R-Squared)**: Coeficiente de determinação (0 a 1).

## S

**Scaler**: Transformador que ajusta escala de features.

**Score**: Métrica de avaliação do modelo.

**Sensibilidade**: Ver Recall.

**Silhouette Score**: Ver Coeficiente de Silhueta.

**StandardScaler**: Normalização usando média e desvio padrão (z-score).

**Supervisionado**: Aprendizado com dados rotulados.

## T

**Target**: Variável que queremos prever.

**Test Set (Conjunto de Teste)**: Dados não usados no treino para avaliar modelo.

**Threshold (Limiar)**: Valor de corte para decisão de classificação.

**Train Set (Conjunto de Treino)**: Dados usados para treinar modelo.

**Transformação**: Operação aplicada aos dados (normalização, PCA, etc).

**True Negative (TN - Verdadeiro Negativo)**: Predição negativa correta.

**True Positive (TP - Verdadeiro Positivo)**: Predição positiva correta.

## U

**Underfitting (Subajuste)**: Modelo muito simples que não captura padrões.

## V

**Validação**: Avaliação de performance do modelo.

**Variância Explicada**: Proporção de variância capturada por componentes principais.

**Viés-Variância**: Trade-off entre simplicidade e flexibilidade do modelo.

## Fórmulas Essenciais

### Métricas de Classificação
```
Acurácia = (VP + VN) / Total

Precisão = VP / (VP + FP)

Recall = VP / (VP + FN)

F1-Score = 2 × (Precisão × Recall) / (Precisão + Recall)

Especificidade = VN / (VN + FP)
```

### Métricas de Regressão
```
MAE = Σ|y_real - y_pred| / n

MSE = Σ(y_real - y_pred)² / n

RMSE = √MSE

R² = 1 - (SS_res / SS_tot)
```

### KMeans
```
Inércia = Σ min(||x - μⱼ||²)
onde μⱼ são os centroides

Silhueta = (b - a) / max(a, b)
a = distância média intra-cluster
b = distância média ao cluster mais próximo
```

## Exemplos Práticos

### Classificação Completa
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_csv('especies.csv')
X = df[['temperatura', 'salinidade', 'profundidade', 'ph']]
y = df['especie']

# Dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Normalizar
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Treinar modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train_scaled, y_train)

# Predizer
y_pred = modelo.predict(X_test_scaled)

# Avaliar
print("Acurácia:", modelo.score(X_test_scaled, y_test))
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

# Matriz de confusão
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Confusão')
plt.ylabel('Real')
plt.xlabel('Predito')
plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')

# Importância de features
importancias = pd.DataFrame({
    'feature': X.columns,
    'importancia': modelo.feature_importances_
}).sort_values('importancia', ascending=False)

print("\nImportância de Features:")
print(importancias)
```

### Clusterização com K-Means
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Dados
df = pd.read_csv('locais_coleta.csv')
X = df[['latitude', 'longitude', 'temperatura', 'salinidade']]

# Normalizar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Método do cotovelo para escolher k
inercias = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inercias.append(kmeans.inertia_)

# Plotar cotovelo
plt.figure(figsize=(10, 6))
plt.plot(K_range, inercias, 'bo-')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Inércia')
plt.title('Método do Cotovelo')
plt.grid(True)
plt.savefig('elbow.png', dpi=300, bbox_inches='tight')

# Aplicar K-Means com k escolhido
k_ideal = 4
kmeans = KMeans(n_clusters=k_ideal, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Adicionar clusters ao DataFrame
df['cluster'] = clusters

# Avaliar silhueta
from sklearn.metrics import silhouette_score
silhueta = silhouette_score(X_scaled, clusters)
print(f"Coeficiente de Silhueta: {silhueta:.3f}")

# Plotar clusters
plt.figure(figsize=(12, 8))
scatter = plt.scatter(df['longitude'], df['latitude'], 
                     c=clusters, cmap='viridis', s=100, alpha=0.6)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title(f'Clusters Identificados (k={k_ideal})')
plt.colorbar(scatter, label='Cluster')
plt.savefig('clusters.png', dpi=300, bbox_inches='tight')
```

### PCA (Redução de Dimensionalidade)
```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Dados com muitas features
df = pd.read_csv('medicoes_complexas.csv')
X = df.drop('especie', axis=1)
y = df['especie']

# Normalizar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar PCA
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# Variância explicada
var_explicada = pca.explained_variance_ratio_
var_acumulada = var_explicada.cumsum()

# Plotar variância
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

ax1.bar(range(1, len(var_explicada)+1), var_explicada)
ax1.set_xlabel('Componente Principal')
ax1.set_ylabel('Variância Explicada')
ax1.set_title('Variância por Componente')

ax2.plot(range(1, len(var_acumulada)+1), var_acumulada, 'bo-')
ax2.axhline(y=0.95, color='r', linestyle='--', label='95%')
ax2.set_xlabel('Número de Componentes')
ax2.set_ylabel('Variância Acumulada')
ax2.set_title('Variância Acumulada')
ax2.legend()
ax2.grid(True)

plt.savefig('pca_variance.png', dpi=300, bbox_inches='tight')

# Reduzir para 2 componentes
pca_2d = PCA(n_components=2)
X_2d = pca_2d.fit_transform(X_scaled)

print(f"Variância explicada com 2 componentes: {pca_2d.explained_variance_ratio_.sum():.2%}")

# Plotar
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y.astype('category').cat.codes, 
                     cmap='viridis', s=100, alpha=0.6)
plt.xlabel(f'PC1 ({pca_2d.explained_variance_ratio_[0]:.1%})')
plt.ylabel(f'PC2 ({pca_2d.explained_variance_ratio_[1]:.1%})')
plt.title('Dados Projetados em 2 Componentes Principais')
plt.colorbar(scatter, label='Espécie')
plt.savefig('pca_2d.png', dpi=300, bbox_inches='tight')
```

### Pipeline Completo
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# Criar pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Definir grid de hiperparâmetros
param_grid = {
    'pca__n_components': [2, 3, 4, 5],
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [None, 10, 20]
}

# Grid search com validação cruzada
grid_search = GridSearchCV(pipeline, param_grid, cv=5, 
                           scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Melhores parâmetros
print("Melhores parâmetros:", grid_search.best_params_)
print("Melhor acurácia:", grid_search.best_score_)

# Avaliar no teste
y_pred = grid_search.predict(X_test)
print("\nAcurácia no teste:", accuracy_score(y_test, y_pred))
```

## Guia de Escolha de Algoritmo

| Tarefa | Algoritmo Recomendado |
|--------|----------------------|
| Classificação simples | Logistic Regression, KNN |
| Classificação complexa | Random Forest, XGBoost |
| Regressão simples | Linear Regression |
| Regressão complexa | Random Forest Regressor |
| Clustering | K-Means, DBSCAN |
| Redução de dimensionalidade | PCA, t-SNE |
| Dados desbalanceados | SMOTE + Classificador |

---

💡 **Dica**: Sempre normalize seus dados antes de aplicar KMeans ou PCA!
