# 🌿 Classificação Avançada de Espécies

## 🎯 Objetivo

Aprimorar a classificação de macroalgas com modelos mais robustos: **Random Forest**, **SVM** e boas práticas.

---

## 📦 Setup

Instalar dependências:

```bash
pip install scikit-learn pandas numpy matplotlib seaborn
```

---

## 🧪 Dataset Sintético

```python
import pandas as pd
import numpy as np

np.random.seed(42)

n = 150
especies = ['Ulva', 'Gracilaria', 'Sargassum']

df = pd.DataFrame({
    'comprimento_cm': np.concatenate([
        np.random.normal(20, 3, n//3),
        np.random.normal(11, 2, n//3),
        np.random.normal(35, 4, n//3)
    ]),
    'largura_cm': np.concatenate([
        np.random.normal(13, 2, n//3),
        np.random.normal(5, 1, n//3),
        np.random.normal(15, 2.5, n//3)
    ]),
    'espessura_mm': np.concatenate([
        np.random.normal(0.7, 0.15, n//3),
        np.random.normal(1.5, 0.2, n//3),
        np.random.normal(3.0, 0.3, n//3)
    ]),
    'especie': np.repeat(especies, n//3)
})
```

---

## 🔧 Preparação + Split

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = df[['comprimento_cm', 'largura_cm', 'espessura_mm']]
y = df['especie']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## 🌲 Random Forest

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

rf = RandomForestClassifier(n_estimators=200, max_depth=None, random_state=42)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)
print(f"Acurácia RF: {accuracy_score(y_test, y_pred_rf)*100:.1f}%")
print(classification_report(y_test, y_pred_rf))

# Importância das features
importancias = pd.Series(rf.feature_importances_, index=X.columns)
print("\nImportância das características:")
print(importancias.sort_values(ascending=False).round(3))
```

— Vantagens: robusto, pouco tuning.
— Interpretação: importância de variáveis.

---

## 🧭 SVM (Support Vector Machine)

```python
from sklearn.svm import SVC

svm = SVC(kernel='rbf', C=2.0, gamma='scale', probability=True, random_state=42)
svm.fit(X_train_scaled, y_train)

y_pred_svm = svm.predict(X_test_scaled)
print(f"Acurácia SVM: {accuracy_score(y_test, y_pred_svm)*100:.1f}%")
print(classification_report(y_test, y_pred_svm))
```

— Sensível à escala → usar StandardScaler.
— Kernel RBF captura não-linearidades.

---

## 🔄 Validação Cruzada

```python
from sklearn.model_selection import cross_val_score

scores_rf = cross_val_score(rf, X, y, cv=5)
scores_svm = cross_val_score(SVC(kernel='rbf', C=2.0, gamma='scale'), X, y, cv=5)

print(f"RF CV: {scores_rf.mean():.3f} ± {scores_rf.std():.3f}")
print(f"SVM CV: {scores_svm.mean():.3f} ± {scores_svm.std():.3f}")
```

---

## 🎯 Tuning (Grid Search)

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 4]
}

gs = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, n_jobs=-1)
gs.fit(X_train, y_train)
print(f"Melhor RF: {gs.best_params_}")
print(f"Score (val): {gs.best_score_:.3f}")
```

---

## 🧪 Matriz de Confusão

```python
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred_rf)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens',
            xticklabels=rf.classes_, yticklabels=rf.classes_)
plt.title('Random Forest - Matriz de Confusão')
plt.xlabel('Previsto'); plt.ylabel('Real')
plt.tight_layout(); plt.savefig('cm_rf.png', dpi=300); plt.show()
```

---

## ✅ Boas Práticas

- Padronizar escala para SVM
- Usar validação cruzada
- Evitar overfitting (regularização / limitar profundidade)
- Medir precisão, recall e F1 por classe
- Interpretar importância de variáveis

— Próxima: Agrupamento (K-Means) e redução de dimensionalidade (PCA).
