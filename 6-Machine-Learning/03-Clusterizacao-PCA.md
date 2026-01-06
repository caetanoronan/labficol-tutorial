# 🧭 Clusterização (K-Means) e PCA

## 🎯 Objetivo

Agrupar coletas por similaridade e reduzir dimensionalidade para visualização e interpretação.

— K-Means: agrupa pontos em K clusters.
— PCA: projeta dados em componentes principais.

---

## 📦 Setup

```bash
pip install scikit-learn pandas numpy matplotlib seaborn
```

---

## 🔢 Dataset de Características

```python
import pandas as pd
import numpy as np
np.random.seed(42)

n = 120

df = pd.DataFrame({
    'biomassa_g': np.random.normal(280, 40, n),
    'temperatura_c': np.random.normal(20, 2.5, n),
    'salinidade_psu': np.random.normal(35.2, 0.4, n),
    'profundidade_m': np.random.normal(4.0, 1.0, n)
})

print(df.head())
```

---

## 🎛️ K-Means (Agrupamento)

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = df[['biomassa_g', 'temperatura_c', 'salinidade_psu', 'profundidade_m']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
kmeans.fit(X_scaled)

labels = kmeans.labels_
df['cluster'] = labels
print(df['cluster'].value_counts())
```

— Cada cluster agrupa coletas com padrões semelhantes.

### Visualização 2D (PCA)

```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(7,5))
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=df['cluster'], palette='Set2', s=80, edgecolor='black')
plt.title('K-Means clusters (PCA 2D)')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% var.)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% var.)')
plt.tight_layout(); plt.savefig('clusters_pca.png', dpi=300); plt.show()
```

---

## 📐 PCA: Componentes e Cargas

```python
componentes = pd.DataFrame(pca.components_, columns=X.columns, index=['PC1', 'PC2'])
print('\nCargas dos componentes:')
print(componentes.round(3))

print('\nVariância explicada:')
print(pca.explained_variance_ratio_.round(3))
```

Interpretação:
- Cargas altas (positivas/negativas) mostram variáveis que mais pesam em cada PC.

---

## 🔍 Escolha de K (Elbow Method)

```python
inertias = []
for k in range(2, 8):
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X_scaled)
    inertias.append(km.inertia_)

plt.figure(figsize=(6,4))
plt.plot(range(2,8), inertias, 'o--')
plt.xlabel('Número de clusters (K)')
plt.ylabel('Inércia')
plt.title('Elbow Method')
plt.tight_layout(); plt.savefig('elbow.png', dpi=300); plt.show()
```

— Ponto de inflexão sugere bom K.

---

## ✅ Boas Práticas

- Padronizar dados antes de K-Means
- Interpretar PCA com cargas das variáveis
- Validar clusters (silhouette score)
- Evitar inferências causais com clusters

— Com isso, você consegue agrupar e visualizar padrões em dados complexos.
