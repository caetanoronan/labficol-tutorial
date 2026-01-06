# 📊 Estatística Descritiva para Dados Biológicos

## 🎯 Objetivo da Lição

Aprender a calcular e interpretar **estatísticas descritivas** essenciais para análise de dados de pesquisa: médias, medianas, desvio padrão, quartis e muito mais.

**Por que é importante:**
- Resumir grandes conjuntos de dados
- Identificar padrões e anomalias
- Tomar decisões baseadas em evidências
- Comunicar resultados de forma clara

---

## 📐 Medidas de Tendência Central

### Média Aritmética

**Definição:** Soma de todos os valores dividido pela quantidade.

```python
import numpy as np

# Biomassas coletadas (gramas)
biomassas = [245.3, 180.7, 310.2, 198.5, 220.4, 302.1, 195.8, 275.4]

# Calcular média
media = np.mean(biomassas)
print(f"Média: {media:.2f}g")  # 241.05g

# Ou manualmente:
media_manual = sum(biomassas) / len(biomassas)
```

**Quando usar:** Dados simétricos sem outliers extremos.

---

### Mediana

**Definição:** Valor central quando os dados estão ordenados.

```python
# Calcular mediana
mediana = np.median(biomassas)
print(f"Mediana: {mediana:.2f}g")  # 233.75g

# Manualmente:
biomassas_ordenadas = sorted(biomassas)
meio = len(biomassas_ordenadas) // 2
if len(biomassas_ordenadas) % 2 == 0:
    mediana_manual = (biomassas_ordenadas[meio-1] + biomassas_ordenadas[meio]) / 2
else:
    mediana_manual = biomassas_ordenadas[meio]
```

**Quando usar:** Dados com outliers ou distribuição assimétrica.

---

### Moda

**Definição:** Valor que aparece com maior frequência.

```python
from scipy import stats

especies = ['Ulva lactuca', 'Gracilaria', 'Ulva lactuca', 'Sargassum', 
            'Ulva lactuca', 'Gracilaria', 'Ulva lactuca']

moda = stats.mode(especies, keepdims=True)
print(f"Espécie mais comum: {moda.mode[0]}")  # Ulva lactuca
print(f"Frequência: {moda.count[0]} vezes")   # 4 vezes
```

---

## 📏 Medidas de Dispersão

### Variância e Desvio Padrão

**Variância:** Média dos quadrados das diferenças em relação à média.  
**Desvio Padrão:** Raiz quadrada da variância (mesma unidade dos dados).

```python
# Temperaturas registradas (°C)
temperaturas = [24.5, 26.1, 22.3, 21.5, 19.8, 18.2, 17.5, 18.0, 19.5, 21.0]

# Variância
variancia = np.var(temperaturas, ddof=1)  # ddof=1 para amostra
print(f"Variância: {variancia:.2f} °C²")

# Desvio padrão
desvio_padrao = np.std(temperaturas, ddof=1)
print(f"Desvio padrão: {desvio_padrao:.2f} °C")

# Interpretação
media_temp = np.mean(temperaturas)
print(f"\nTemperatura: {media_temp:.1f} ± {desvio_padrao:.1f} °C")
```

**Interpretação:**
- Desvio padrão baixo → Dados concentrados perto da média
- Desvio padrão alto → Dados dispersos

---

### Coeficiente de Variação

**Definição:** Desvio padrão relativo à média (em %).

```python
cv = (desvio_padrao / media_temp) * 100
print(f"Coeficiente de Variação: {cv:.2f}%")

# Interpretação:
if cv < 10:
    print("Variabilidade: BAIXA")
elif cv < 30:
    print("Variabilidade: MODERADA")
else:
    print("Variabilidade: ALTA")
```

---

### Amplitude e Amplitude Interquartil

```python
# Amplitude total (range)
amplitude = max(temperaturas) - min(temperaturas)
print(f"Amplitude: {amplitude:.1f} °C")

# Quartis
q1 = np.percentile(temperaturas, 25)  # 1º quartil (25%)
q2 = np.percentile(temperaturas, 50)  # 2º quartil (mediana)
q3 = np.percentile(temperaturas, 75)  # 3º quartil (75%)

# Amplitude interquartil (IQR)
iqr = q3 - q1
print(f"\nQ1 (25%): {q1:.1f} °C")
print(f"Q2 (50%): {q2:.1f} °C")
print(f"Q3 (75%): {q3:.1f} °C")
print(f"IQR: {iqr:.1f} °C")
```

**IQR:** Contém os 50% centrais dos dados (menos sensível a outliers).

---

## 📊 Exemplo Completo: Análise de Coletas

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Dataset de coletas
dados = {
    'praia': ['Ingleses', 'Ingleses', 'Barra', 'Barra', 'Armação', 
              'Armação', 'Garopaba', 'Garopaba', 'Laguna', 'Laguna'],
    'especie': ['Ulva', 'Gracilaria', 'Ulva', 'Sargassum', 'Ulva', 
                'Gracilaria', 'Ulva', 'Laminaria', 'Ulva', 'Gracilaria'],
    'biomassa_g': [245.3, 180.7, 302.1, 310.2, 275.4, 195.8, 310.8, 425.8, 295.7, 205.6],
    'temperatura_c': [24.5, 24.5, 22.3, 23.8, 21.5, 21.5, 19.8, 21.0, 18.0, 18.0],
    'profundidade_m': [3.2, 5.1, 3.5, 4.5, 3.8, 5.0, 3.6, 10.5, 3.7, 5.4]
}

df = pd.DataFrame(dados)

# ====================
# ESTATÍSTICAS GERAIS
# ====================

print("="*60)
print("📊 ESTATÍSTICAS DESCRITIVAS - BIOMASSA")
print("="*60)

biomassas = df['biomassa_g']

print(f"\n📏 Tendência Central:")
print(f"   Média: {biomassas.mean():.2f}g")
print(f"   Mediana: {biomassas.median():.2f}g")

print(f"\n📐 Dispersão:")
print(f"   Desvio Padrão: {biomassas.std():.2f}g")
print(f"   Variância: {biomassas.var():.2f}g²")
print(f"   CV: {(biomassas.std() / biomassas.mean() * 100):.2f}%")

print(f"\n📊 Valores Extremos:")
print(f"   Mínimo: {biomassas.min():.2f}g")
print(f"   Máximo: {biomassas.max():.2f}g")
print(f"   Amplitude: {biomassas.max() - biomassas.min():.2f}g")

print(f"\n🎯 Quartis:")
print(f"   Q1 (25%): {biomassas.quantile(0.25):.2f}g")
print(f"   Q2 (50%): {biomassas.quantile(0.50):.2f}g")
print(f"   Q3 (75%): {biomassas.quantile(0.75):.2f}g")
print(f"   IQR: {biomassas.quantile(0.75) - biomassas.quantile(0.25):.2f}g")

# ====================
# POR ESPÉCIE
# ====================

print("\n" + "="*60)
print("🌿 ESTATÍSTICAS POR ESPÉCIE")
print("="*60)

for especie in df['especie'].unique():
    dados_especie = df[df['especie'] == especie]['biomassa_g']
    
    print(f"\n📌 {especie}")
    print(f"   n = {len(dados_especie)}")
    print(f"   Média: {dados_especie.mean():.2f}g ± {dados_especie.std():.2f}g")
    print(f"   Mediana: {dados_especie.median():.2f}g")
    print(f"   Range: [{dados_especie.min():.2f}, {dados_especie.max():.2f}]g")

# ====================
# VISUALIZAÇÕES
# ====================

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('📊 Análise Estatística de Coletas', fontsize=16, fontweight='bold')

# 1. Histograma
ax1 = axes[0, 0]
ax1.hist(biomassas, bins=6, edgecolor='black', alpha=0.7, color='skyblue')
ax1.axvline(biomassas.mean(), color='red', linestyle='--', linewidth=2, label=f'Média: {biomassas.mean():.1f}g')
ax1.axvline(biomassas.median(), color='green', linestyle='--', linewidth=2, label=f'Mediana: {biomassas.median():.1f}g')
ax1.set_xlabel('Biomassa (g)')
ax1.set_ylabel('Frequência')
ax1.set_title('Histograma de Biomassa')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 2. Boxplot
ax2 = axes[0, 1]
ax2.boxplot(biomassas, vert=True)
ax2.set_ylabel('Biomassa (g)')
ax2.set_title('Boxplot de Biomassa')
ax2.grid(True, alpha=0.3)

# 3. Boxplot por espécie
ax3 = axes[1, 0]
especies_ordenadas = df.groupby('especie')['biomassa_g'].median().sort_values().index
df_plot = df.set_index('especie').loc[especies_ordenadas]
df_plot.boxplot(column='biomassa_g', by='especie', ax=ax3)
ax3.set_xlabel('Espécie')
ax3.set_ylabel('Biomassa (g)')
ax3.set_title('Biomassa por Espécie')
plt.sca(ax3)
plt.xticks(rotation=45, ha='right')

# 4. Scatter com tendência
ax4 = axes[1, 1]
ax4.scatter(df['temperatura_c'], df['biomassa_g'], s=100, alpha=0.6, edgecolors='black')
ax4.set_xlabel('Temperatura (°C)')
ax4.set_ylabel('Biomassa (g)')
ax4.set_title('Biomassa vs Temperatura')
ax4.grid(True, alpha=0.3)

# Linha de tendência
z = np.polyfit(df['temperatura_c'], df['biomassa_g'], 1)
p = np.poly1d(z)
ax4.plot(df['temperatura_c'], p(df['temperatura_c']), 
         "r--", alpha=0.8, linewidth=2, label='Tendência')
ax4.legend()

plt.tight_layout()
plt.savefig('estatisticas_descritivas.png', dpi=300)
print("\n✅ Gráfico salvo: estatisticas_descritivas.png")
plt.show()

print("\n" + "="*60)
print("✅ ANÁLISE CONCLUÍDA!")
print("="*60)
```

---

## 📈 Resumo dos 5 Números

**Five-number summary:** Resumo completo da distribuição.

```python
def resumo_cinco_numeros(dados):
    """Calcula e exibe o resumo de 5 números"""
    minimo = np.min(dados)
    q1 = np.percentile(dados, 25)
    mediana = np.median(dados)
    q3 = np.percentile(dados, 75)
    maximo = np.max(dados)
    
    print("\n📊 RESUMO DOS 5 NÚMEROS:")
    print(f"   Mínimo:   {minimo:.2f}")
    print(f"   Q1 (25%): {q1:.2f}")
    print(f"   Mediana:  {mediana:.2f}")
    print(f"   Q3 (75%): {q3:.2f}")
    print(f"   Máximo:   {maximo:.2f}")
    
    return minimo, q1, mediana, q3, maximo

resumo_cinco_numeros(biomassas)
```

---

## 🔍 Identificação de Outliers

**Método IQR:** Valores fora de 1.5 × IQR são considerados outliers.

```python
def identificar_outliers(dados):
    """Identifica outliers usando método IQR"""
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    iqr = q3 - q1
    
    # Limites
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    
    # Identificar outliers
    outliers = [x for x in dados if x < limite_inferior or x > limite_superior]
    
    print(f"\n🔍 DETECÇÃO DE OUTLIERS:")
    print(f"   Limite inferior: {limite_inferior:.2f}")
    print(f"   Limite superior: {limite_superior:.2f}")
    
    if outliers:
        print(f"   ⚠️ {len(outliers)} outlier(s) detectado(s): {outliers}")
    else:
        print(f"   ✅ Nenhum outlier detectado")
    
    return outliers

identificar_outliers(df['biomassa_g'])
```

---

## 🎓 Checklist desta Lição

- [ ] Calculei média, mediana e moda
- [ ] Entendi desvio padrão e variância
- [ ] Criei boxplots para visualizar distribuição
- [ ] Identifiquei outliers usando IQR
- [ ] Comparei estatísticas entre grupos

---

## ➡️ Próxima Lição

- **02-Testes-Hipotese.md** (Testes estatísticos: t-test, ANOVA, etc.)

---

**Você domina estatística descritiva!** 📊✨
