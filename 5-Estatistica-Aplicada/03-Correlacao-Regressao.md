# 📈 Correlação e Regressão

## 🎯 Objetivo da Lição

Entender relações entre variáveis e criar modelos simples para previsão usando **correlação** e **regressão**.

— Quando duas variáveis variam juntas, há correlação.
— Regressão estima como uma variável explica outra.

---

## 🔗 Correlação (Pearson)

Mede relação linear entre duas variáveis (−1 a +1).

```python
import numpy as np
import pandas as pd

# Exemplo: biomassa vs temperatura
biomassa = np.array([245.3, 198.5, 302.1, 275.4, 310.8, 285.2, 320.5, 295.7, 260.8, 280.3])
temperatura = np.array([24.5, 26.1, 22.3, 21.5, 19.8, 18.2, 17.5, 18.0, 19.5, 21.0])

# Correlação de Pearson
corr = np.corrcoef(biomassa, temperatura)[0, 1]
print(f"Correlação (Pearson): {corr:.3f}")
```

Interpretação:
- |r| ≥ 0.7 → forte
- 0.4–0.7 → moderada
- 0.2–0.4 → fraca

---

## 📊 Matriz de Correlação

```python
# Dataset de exemplo
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
    'biomassa_g': biomassa,
    'temperatura_c': temperatura,
    'salinidade_psu': [35.0, 34.5, 35.2, 35.3, 35.4, 35.5, 35.6, 35.4, 35.2, 35.0],
    'profundidade_m': [3.2, 3.0, 3.5, 3.8, 3.6, 3.4, 3.9, 3.7, 3.5, 3.8]
}

df = pd.DataFrame(dados)

corr_mtx = df.corr(numeric_only=True)
print(corr_mtx.round(3))

plt.figure(figsize=(6, 5))
sns.heatmap(corr_mtx, annot=True, cmap='Blues', vmin=-1, vmax=1)
plt.title('Matriz de Correlação')
plt.tight_layout()
plt.savefig('matriz_correlacao.png', dpi=300)
plt.show()
```

---

## 📉 Regressão Linear Simples

Modelo: y = a + b·x

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

X = temperatura.reshape(-1, 1)
y = biomassa

modelo = LinearRegression()
modelo.fit(X, y)

# Coeficientes
intercepto = modelo.intercept_
coef = modelo.coef_[0]
print(f"Modelo: biomassa = {intercepto:.2f} + {coef:.2f}·temperatura")

# Avaliação
y_pred = modelo.predict(X)
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
print(f"R²: {r2:.3f} | RMSE: {rmse:.2f}g")
```

Visualização:

```python
plt.figure(figsize=(7,5))
plt.scatter(temperatura, biomassa, s=90, edgecolors='black', alpha=0.7)
plt.plot(temperatura, y_pred, 'r--', linewidth=2)
plt.xlabel('Temperatura (°C)')
plt.ylabel('Biomassa (g)')
plt.title('Regressão Linear: Biomassa vs Temperatura')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('regressao_simples.png', dpi=300)
plt.show()
```

---

## 📈 Regressão Múltipla

Várias variáveis explicam y.

```python
from sklearn.model_selection import train_test_split

X = df[['temperatura_c', 'salinidade_psu', 'profundidade_m']]
y = df['biomassa_g']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

coeficientes = pd.Series(modelo.coef_, index=X.columns)
print("Coeficientes:")
print(coeficientes.round(3))

# Avaliação
y_pred = modelo.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"R² (teste): {r2:.3f} | RMSE: {rmse:.2f}g")
```

---

## ⚠️ Cuidados Comuns

- Correlação ≠ causalidade
- Verificar outliers e não-linearidade
- Normalizar variáveis com escalas muito diferentes
- Usar validação (train/test ou cross-validation)

---

## 🎓 Checklist

- [ ] Calculei correlação entre variáveis
- [ ] Interpretei matriz de correlação
- [ ] Modelei regressão simples
- [ ] Modelei regressão múltipla
- [ ] Avaliei R² e RMSE

— Próxima: Visualização estatística com Seaborn e Matplotlib (opcional).
