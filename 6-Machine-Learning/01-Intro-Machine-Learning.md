# 🤖 Introdução ao Machine Learning para Biologia

## 🎯 Objetivo da Lição

Aprender os **conceitos fundamentais de Machine Learning** e como aplicá-los em problemas de biologia e oceanografia.

**O que é Machine Learning?**
- Algoritmos que **aprendem padrões** a partir de dados
- Fazem **previsões** sem programação explícita
- Melhoram com **mais dados** e experiência

---

## 🧠 Tipos de Machine Learning

### 1. Aprendizado Supervisionado

**Definição:** Aprende a partir de exemplos rotulados.

```
Entrada (X) → Modelo → Saída (y)
```

**Exemplos em Biologia:**
- Classificar espécies a partir de características morfológicas
- Prever biomassa com base em temperatura e salinidade
- Identificar imagens de macroalgas

**Tipos:**
- **Classificação:** Saída categórica (espécie A, B ou C)
- **Regressão:** Saída numérica (biomassa em gramas)

---

### 2. Aprendizado Não-Supervisionado

**Definição:** Encontra padrões em dados sem rótulos.

**Exemplos:**
- Agrupar estações de coleta por similaridade (clustering)
- Reduzir dimensionalidade de dados genômicos (PCA)
- Detectar anomalias em séries temporais

---

### 3. Aprendizado por Reforço

**Definição:** Aprende por tentativa e erro com recompensas.

**Exemplo:** Otimizar estratégias de coleta para maximizar biodiversidade.

---

## 📊 Workflow de Machine Learning

```
1. COLETAR DADOS
   ↓
2. EXPLORAR E LIMPAR
   ↓
3. PREPARAR FEATURES (características)
   ↓
4. DIVIDIR: Treino (80%) | Teste (20%)
   ↓
5. ESCOLHER MODELO
   ↓
6. TREINAR MODELO
   ↓
7. AVALIAR DESEMPENHO
   ↓
8. AJUSTAR E MELHORAR
   ↓
9. USAR EM PRODUÇÃO
```

---

## 🔧 Bibliotecas Python para ML

```python
# Instalar
pip install scikit-learn pandas numpy matplotlib seaborn
```

```python
# Importar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
```

---

## 🎯 Exemplo 1: Classificação de Espécies

### Problema

Dado comprimento, largura e espessura de macroalgas, **prever a espécie**.

### Dataset

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Dados sintéticos de 3 espécies
dados = {
    'comprimento_cm': [12.5, 15.2, 18.7, 20.3, 25.1,  # Ulva
                       8.3, 9.5, 10.2, 11.8, 12.1,    # Gracilaria
                       30.5, 35.8, 40.2, 38.5, 42.1], # Sargassum
    'largura_cm': [8.2, 9.5, 11.3, 12.8, 15.2,
                   3.5, 4.1, 4.8, 5.2, 5.5,
                   10.5, 12.3, 15.8, 14.2, 16.5],
    'espessura_mm': [0.5, 0.6, 0.7, 0.8, 0.9,
                     1.2, 1.3, 1.5, 1.6, 1.7,
                     2.5, 2.8, 3.2, 3.0, 3.5],
    'especie': ['Ulva']*5 + ['Gracilaria']*5 + ['Sargassum']*5
}

df = pd.DataFrame(dados)

print("="*60)
print("🌿 CLASSIFICAÇÃO DE ESPÉCIES DE MACROALGAS")
print("="*60)
print("\n📊 Dataset:")
print(df.head(10))

# ====================
# PREPARAR DADOS
# ====================

# Features (X) e Target (y)
X = df[['comprimento_cm', 'largura_cm', 'espessura_mm']]
y = df['especie']

print(f"\n📏 Features (X): {X.shape}")
print(f"🎯 Target (y): {y.shape}")

# Dividir em treino e teste (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\n📚 Dados de treino: {len(X_train)} amostras")
print(f"🧪 Dados de teste: {len(X_test)} amostras")

# ====================
# TREINAR MODELO
# ====================

print("\n" + "="*60)
print("🤖 TREINANDO MODELO (DECISION TREE)")
print("="*60)

# Criar e treinar modelo
modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X_train, y_train)

print("✅ Modelo treinado!")

# ====================
# FAZER PREVISÕES
# ====================

print("\n" + "="*60)
print("🔮 FAZENDO PREVISÕES")
print("="*60)

# Prever no conjunto de teste
y_pred = modelo.predict(X_test)

print("\nPrevisões vs Real:")
print("-"*60)
for i, (real, pred) in enumerate(zip(y_test, y_pred)):
    correto = "✅" if real == pred else "❌"
    print(f"Amostra {i+1}: Real={real:12s} | Previsto={pred:12s} {correto}")

# ====================
# AVALIAR DESEMPENHO
# ====================

print("\n" + "="*60)
print("📊 AVALIAÇÃO DO MODELO")
print("="*60)

# Acurácia
acuracia = accuracy_score(y_test, y_pred)
print(f"\n🎯 Acurácia: {acuracia*100:.1f}%")

# Relatório detalhado
print("\n📋 Relatório de Classificação:")
print("-"*60)
print(classification_report(y_test, y_pred))

# ====================
# TESTAR COM NOVA AMOSTRA
# ====================

print("\n" + "="*60)
print("🆕 PREVER ESPÉCIE DE NOVA AMOSTRA")
print("="*60)

# Nova amostra desconhecida
nova_amostra = pd.DataFrame({
    'comprimento_cm': [22.5],
    'largura_cm': [13.8],
    'espessura_mm': [0.75]
})

predicao = modelo.predict(nova_amostra)
probabilidades = modelo.predict_proba(nova_amostra)

print(f"\n📏 Características:")
print(f"   Comprimento: {nova_amostra['comprimento_cm'].values[0]} cm")
print(f"   Largura: {nova_amostra['largura_cm'].values[0]} cm")
print(f"   Espessura: {nova_amostra['espessura_mm'].values[0]} mm")

print(f"\n🔮 Previsão: {predicao[0]}")
print(f"\n📊 Probabilidades:")
for especie, prob in zip(modelo.classes_, probabilidades[0]):
    print(f"   {especie}: {prob*100:.1f}%")

print("\n" + "="*60)
print("✅ CLASSIFICAÇÃO CONCLUÍDA!")
print("="*60)
```

---

## 📈 Exemplo 2: Regressão - Prever Biomassa

### Problema

Prever **biomassa** com base em temperatura, salinidade e profundidade.

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Dataset
dados = {
    'temperatura_c': [24.5, 26.1, 22.3, 21.5, 19.8, 18.2, 17.5, 18.0, 19.5, 21.0],
    'salinidade_psu': [35.0, 34.5, 35.2, 35.3, 35.4, 35.5, 35.6, 35.4, 35.2, 35.0],
    'profundidade_m': [3.2, 3.0, 3.5, 3.8, 3.6, 3.4, 3.9, 3.7, 3.5, 3.8],
    'biomassa_g': [245.3, 198.5, 302.1, 275.4, 310.8, 285.2, 320.5, 295.7, 260.8, 280.3]
}

df = pd.DataFrame(dados)

print("="*60)
print("📊 REGRESSÃO: PREVER BIOMASSA")
print("="*60)

# Preparar dados
X = df[['temperatura_c', 'salinidade_psu', 'profundidade_m']]
y = df['biomassa_g']

# Normalizar features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Treinar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Prever
y_pred = modelo.predict(X_test)

# Avaliar
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\n📊 Desempenho do Modelo:")
print(f"   R² Score: {r2:.4f}")
print(f"   RMSE: {rmse:.2f}g")

print(f"\n🎯 Coeficientes:")
features = ['temperatura_c', 'salinidade_psu', 'profundidade_m']
for feature, coef in zip(features, modelo.coef_):
    print(f"   {feature}: {coef:.4f}")

# Prever nova amostra
nova_amostra = scaler.transform([[20.5, 35.1, 3.5]])
predicao = modelo.predict(nova_amostra)
print(f"\n🔮 Previsão para nova amostra: {predicao[0]:.2f}g")

print("\n" + "="*60)
print("✅ REGRESSÃO CONCLUÍDA!")
print("="*60)
```

---

## 🎨 Visualização de Modelos

### Árvore de Decisão

```python
from sklearn import tree
import matplotlib.pyplot as plt

# Visualizar árvore
plt.figure(figsize=(15, 10))
tree.plot_tree(modelo, 
               feature_names=['comprimento', 'largura', 'espessura'],
               class_names=modelo.classes_,
               filled=True, 
               rounded=True, 
               fontsize=10)
plt.title('Árvore de Decisão - Classificação de Espécies', fontsize=16)
plt.savefig('arvore_decisao.png', dpi=300, bbox_inches='tight')
plt.show()
```

### Matriz de Confusão

```python
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Calcular matriz de confusão
cm = confusion_matrix(y_test, y_pred)

# Plotar
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=modelo.classes_,
            yticklabels=modelo.classes_)
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.savefig('matriz_confusao.png', dpi=300)
plt.show()
```

---

## 🎓 Conceitos-Chave

### Overfitting vs Underfitting

```
UNDERFITTING (modelo simples demais)
   Treino: 60% | Teste: 62%
   → Adicionar complexidade

BONS RESULTADOS
   Treino: 95% | Teste: 92%
   → Modelo equilibrado ✅

OVERFITTING (modelo complexo demais)
   Treino: 99% | Teste: 75%
   → Simplificar modelo ou mais dados
```

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score

# Validação cruzada (k-fold)
scores = cross_val_score(modelo, X, y, cv=5)

print(f"Acurácia média: {scores.mean():.4f} ± {scores.std():.4f}")
```

---

## 🎓 Checklist desta Lição

- [ ] Entendi os tipos de ML (supervisionado/não-supervisionado)
- [ ] Criei modelo de classificação
- [ ] Treinei modelo de regressão
- [ ] Avaliei desempenho com métricas
- [ ] Fiz previsões em novos dados

---

## ➡️ Próxima Lição

- **02-Classificacao-Avancada.md** (Random Forest, SVM, Neural Networks)

---

**Você entrou no mundo do Machine Learning!** 🤖✨
