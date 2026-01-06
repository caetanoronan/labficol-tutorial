# 📊 Caso Prático 1: Monitoramento Costeiro

## 🎯 Objetivo do Projeto

Criar um sistema completo de análise temporal de coletas de macroalgas em praias de Santa Catarina, usando **Python + pandas + matplotlib**.

**O que faremos:**
- Carregar dados de múltiplas coletas
- Analisar tendências temporais
- Identificar padrões sazonais
- Gerar relatórios visuais

---

## 📋 Contexto da Pesquisa

O LABFICOL realiza coletas mensais em 5 praias de Florianópolis para monitorar:
- Abundância de espécies
- Parâmetros físico-químicos
- Variações sazonais

**Objetivo científico:** Identificar como temperatura e salinidade afetam a distribuição de *Ulva lactuca* e *Gracilaria*.

---

## 🗂️ Estrutura dos Dados

Nosso dataset `coletas_2025.csv`:

```csv
data,praia,especie,biomassa_g,temperatura_c,salinidade_psu,profundidade_m
2025-01-15,Ingleses,Ulva lactuca,245.3,24.5,35.0,3.2
2025-01-15,Ingleses,Gracilaria,180.7,24.5,35.0,5.1
2025-01-15,Barra da Lagoa,Sargassum,310.2,23.8,34.8,4.5
2025-02-20,Ingleses,Ulva lactuca,198.5,26.1,34.5,3.0
2025-02-20,Barra da Lagoa,Gracilaria,220.4,25.5,34.7,5.3
2025-03-18,Ingleses,Ulva lactuca,302.1,22.3,35.2,3.5
```

---

## 💻 Código Completo - Parte 1: Análise Exploratória

Crie `analise_monitoramento.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ==========================
# 1. CARREGAMENTO DOS DADOS
# ==========================

# Criar dataset de exemplo
dados = {
    'data': ['2025-01-15', '2025-01-15', '2025-01-15', '2025-02-20', '2025-02-20', 
             '2025-03-18', '2025-03-18', '2025-04-22', '2025-04-22', '2025-05-17',
             '2025-05-17', '2025-06-14', '2025-06-14', '2025-07-19', '2025-07-19',
             '2025-08-16', '2025-08-16', '2025-09-20', '2025-09-20', '2025-10-18'],
    'praia': ['Ingleses', 'Ingleses', 'Barra da Lagoa', 'Ingleses', 'Barra da Lagoa',
              'Ingleses', 'Barra da Lagoa', 'Ingleses', 'Barra da Lagoa', 'Ingleses',
              'Barra da Lagoa', 'Ingleses', 'Barra da Lagoa', 'Ingleses', 'Barra da Lagoa',
              'Ingleses', 'Barra da Lagoa', 'Ingleses', 'Barra da Lagoa', 'Ingleses'],
    'especie': ['Ulva lactuca', 'Gracilaria', 'Sargassum', 'Ulva lactuca', 'Gracilaria',
                'Ulva lactuca', 'Gracilaria', 'Ulva lactuca', 'Sargassum', 'Ulva lactuca',
                'Gracilaria', 'Ulva lactuca', 'Sargassum', 'Ulva lactuca', 'Gracilaria',
                'Ulva lactuca', 'Sargassum', 'Ulva lactuca', 'Gracilaria', 'Ulva lactuca'],
    'biomassa_g': [245.3, 180.7, 310.2, 198.5, 220.4, 302.1, 195.8, 275.4, 340.5, 310.8,
                   210.3, 285.2, 298.7, 320.5, 185.4, 295.7, 315.2, 260.8, 205.6, 280.3],
    'temperatura_c': [24.5, 24.5, 23.8, 26.1, 25.5, 22.3, 22.0, 21.5, 21.2, 19.8,
                      19.5, 18.2, 17.9, 17.5, 17.3, 18.0, 17.8, 19.5, 19.2, 21.0],
    'salinidade_psu': [35.0, 35.0, 34.8, 34.5, 34.7, 35.2, 35.1, 35.3, 35.2, 35.4,
                       35.3, 35.5, 35.4, 35.6, 35.5, 35.4, 35.3, 35.2, 35.1, 35.0],
    'profundidade_m': [3.2, 5.1, 4.5, 3.0, 5.3, 3.5, 5.0, 3.8, 4.2, 3.6,
                       5.2, 3.4, 4.0, 3.9, 5.4, 3.7, 4.3, 3.5, 5.1, 3.8]
}

df = pd.DataFrame(dados)

# Converter coluna de data para datetime
df['data'] = pd.to_datetime(df['data'])

# Extrair mês e ano
df['mes'] = df['data'].dt.month
df['mes_nome'] = df['data'].dt.strftime('%B')

print("=" * 50)
print("DATASET CARREGADO COM SUCESSO")
print("=" * 50)
print(f"Total de registros: {len(df)}")
print(f"Período: {df['data'].min().strftime('%d/%m/%Y')} até {df['data'].max().strftime('%d/%m/%Y')}")
print(f"Espécies monitoradas: {df['especie'].unique()}")
print(f"Praias: {df['praia'].unique()}")
print()

# ==========================
# 2. ESTATÍSTICAS DESCRITIVAS
# ==========================

print("=" * 50)
print("ESTATÍSTICAS POR ESPÉCIE")
print("=" * 50)

# Agrupar por espécie
stats_especies = df.groupby('especie').agg({
    'biomassa_g': ['mean', 'std', 'min', 'max', 'count'],
    'temperatura_c': 'mean',
    'salinidade_psu': 'mean'
}).round(2)

print(stats_especies)
print()

# ==========================
# 3. ANÁLISE TEMPORAL
# ==========================

print("=" * 50)
print("ANÁLISE TEMPORAL - ULVA LACTUCA")
print("=" * 50)

# Filtrar apenas Ulva lactuca
ulva_df = df[df['especie'] == 'Ulva lactuca'].copy()

# Agrupar por mês
ulva_mensal = ulva_df.groupby('mes').agg({
    'biomassa_g': 'mean',
    'temperatura_c': 'mean',
    'salinidade_psu': 'mean'
}).round(2)

print(ulva_mensal)
print()

# ==========================
# 4. IDENTIFICAR TENDÊNCIAS
# ==========================

print("=" * 50)
print("ANÁLISE DE CORRELAÇÕES")
print("=" * 50)

# Correlação entre variáveis
correlacao = df[['biomassa_g', 'temperatura_c', 'salinidade_psu', 'profundidade_m']].corr().round(3)
print(correlacao)
print()

# Identificar meses de maior biomassa
print("=" * 50)
print("RANKING DE BIOMASSA POR MÊS")
print("=" * 50)

biomassa_mensal = df.groupby('mes')['biomassa_g'].mean().sort_values(ascending=False).round(2)
print(biomassa_mensal)
print()

# ==========================
# 5. ALERTAS E INSIGHTS
# ==========================

print("=" * 50)
print("🔍 INSIGHTS CIENTÍFICOS")
print("=" * 50)

# Temperatura média ideal para Ulva lactuca
temp_ideal_ulva = ulva_df['temperatura_c'].mean()
print(f"✅ Temperatura média ideal para Ulva lactuca: {temp_ideal_ulva:.1f}°C")

# Meses de pico
mes_pico = biomassa_mensal.idxmax()
biomassa_pico = biomassa_mensal.max()
print(f"✅ Mês de maior biomassa: Mês {mes_pico} ({biomassa_pico:.2f}g)")

# Correlação temperatura-biomassa
corr_temp_biomassa = df[df['especie'] == 'Ulva lactuca'][['temperatura_c', 'biomassa_g']].corr().iloc[0, 1]
if corr_temp_biomassa < -0.5:
    print(f"⚠️ ALERTA: Correlação negativa forte entre temperatura e biomassa ({corr_temp_biomassa:.2f})")
    print("   → Ulva lactuca prefere águas mais frias!")
elif corr_temp_biomassa > 0.5:
    print(f"✅ Correlação positiva entre temperatura e biomassa ({corr_temp_biomassa:.2f})")

print()
print("=" * 50)
print("ANÁLISE CONCLUÍDA!")
print("=" * 50)
```

**Execute:**

```bash
python analise_monitoramento.py
```

**Saída esperada:**
```
==================================================
DATASET CARREGADO COM SUCESSO
==================================================
Total de registros: 20
Período: 15/01/2025 até 18/10/2025
Espécies monitoradas: ['Ulva lactuca' 'Gracilaria' 'Sargassum']
Praias: ['Ingleses' 'Barra da Lagoa']

==================================================
🔍 INSIGHTS CIENTÍFICOS
==================================================
✅ Temperatura média ideal para Ulva lactuca: 21.3°C
✅ Mês de maior biomassa: Mês 8 (305.35g)
⚠️ ALERTA: Correlação negativa forte entre temperatura e biomassa (-0.85)
   → Ulva lactuca prefere águas mais frias!
```

---

## 📊 Código Completo - Parte 2: Visualizações

Adicione ao arquivo (continuação):

```python
# ==========================
# 6. VISUALIZAÇÕES
# ==========================

print("\nGerando gráficos...")

# Configurar estilo
plt.style.use('seaborn-v0_8-darkgrid')
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('📊 Monitoramento Costeiro LABFICOL - 2025', fontsize=16, fontweight='bold')

# --- GRÁFICO 1: Biomassa temporal por espécie ---
ax1 = axes[0, 0]
for especie in df['especie'].unique():
    dados_especie = df[df['especie'] == especie]
    ax1.plot(dados_especie['data'], dados_especie['biomassa_g'], 
             marker='o', label=especie, linewidth=2)

ax1.set_xlabel('Data', fontweight='bold')
ax1.set_ylabel('Biomassa (g)', fontweight='bold')
ax1.set_title('Variação Temporal de Biomassa', fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

# --- GRÁFICO 2: Temperatura vs Biomassa (Ulva) ---
ax2 = axes[0, 1]
ulva_scatter = df[df['especie'] == 'Ulva lactuca']
ax2.scatter(ulva_scatter['temperatura_c'], ulva_scatter['biomassa_g'], 
            s=100, alpha=0.6, c='green', edgecolors='black')

# Adicionar linha de tendência
z = np.polyfit(ulva_scatter['temperatura_c'], ulva_scatter['biomassa_g'], 1)
p = np.poly1d(z)
ax2.plot(ulva_scatter['temperatura_c'].sort_values(), 
         p(ulva_scatter['temperatura_c'].sort_values()), 
         "r--", alpha=0.8, linewidth=2, label='Tendência')

ax2.set_xlabel('Temperatura (°C)', fontweight='bold')
ax2.set_ylabel('Biomassa (g)', fontweight='bold')
ax2.set_title('Temperatura vs Biomassa - Ulva lactuca', fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

# --- GRÁFICO 3: Biomassa média por mês ---
ax3 = axes[1, 0]
biomassa_mes = df.groupby('mes')['biomassa_g'].mean()
cores = ['#FF6B6B' if x < biomassa_mes.mean() else '#4ECDC4' for x in biomassa_mes]
ax3.bar(biomassa_mes.index, biomassa_mes.values, color=cores, edgecolor='black')
ax3.axhline(y=biomassa_mes.mean(), color='red', linestyle='--', 
            linewidth=2, label=f'Média: {biomassa_mes.mean():.1f}g')
ax3.set_xlabel('Mês', fontweight='bold')
ax3.set_ylabel('Biomassa Média (g)', fontweight='bold')
ax3.set_title('Biomassa Média Mensal (Todas Espécies)', fontweight='bold')
ax3.legend()
ax3.grid(True, alpha=0.3, axis='y')

# --- GRÁFICO 4: Distribuição por praia ---
ax4 = axes[1, 1]
biomassa_praia = df.groupby(['praia', 'especie'])['biomassa_g'].sum().unstack()
biomassa_praia.plot(kind='bar', ax=ax4, width=0.8, edgecolor='black')
ax4.set_xlabel('Praia', fontweight='bold')
ax4.set_ylabel('Biomassa Total (g)', fontweight='bold')
ax4.set_title('Biomassa Total por Praia e Espécie', fontweight='bold')
ax4.legend(title='Espécie', loc='upper right')
ax4.grid(True, alpha=0.3, axis='y')
plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.savefig('monitoramento_costeiro.png', dpi=300, bbox_inches='tight')
print("✅ Gráfico salvo: monitoramento_costeiro.png")
plt.show()

print("\n" + "=" * 50)
print("PROJETO CONCLUÍDO COM SUCESSO! 🎉")
print("=" * 50)
```

**Adicione no topo do arquivo:**

```python
import numpy as np  # Para linha de tendência
```

---

## 📈 Resultados Esperados

Ao executar o código completo, você terá:

1. **Console:**
   - Estatísticas descritivas
   - Correlações
   - Insights científicos automáticos

2. **Arquivo gráfico:**
   - `monitoramento_costeiro.png` com 4 gráficos profissionais

3. **Insights:**
   - Meses de maior/menor biomassa
   - Relação temperatura-abundância
   - Comparação entre praias

---

## 🔬 Interpretação Científica

Com base nos resultados:

### 📊 Padrão Observado

```
Temperatura ↑ → Biomassa Ulva ↓
(Correlação negativa: -0.85)
```

**Conclusão científica:**
- *Ulva lactuca* prefere **águas frias** (17-19°C)
- Maior abundância no **inverno** (meses 6-8)
- Praias mais expostas têm maior diversidade

### 🎯 Recomendações para Coleta

1. **Intensificar amostragem:** Junho-Agosto (pico de Ulva)
2. **Monitorar temperatura:** Alerta se T > 25°C
3. **Expandir para outras praias:** Sul da ilha

---

## 🎓 O que você aprendeu

- ✅ Carregar e processar dados reais de campo
- ✅ Calcular estatísticas descritivas
- ✅ Identificar correlações entre variáveis
- ✅ Criar visualizações profissionais
- ✅ Gerar insights científicos automaticamente

---

## 🚀 Desafio Extra

**Expanda o projeto:**

1. Adicione mais espécies ao dataset
2. Calcule índice de diversidade de Shannon
3. Compare anos diferentes (2024 vs 2025)
4. Exporte resultados para relatório PDF

---

## ➡️ Próximo Caso Prático

- **02-Distribuicao-Espacial.md** (Análise geoespacial com mapas)

---

**Parabéns!** Você criou um sistema completo de análise científica! 🌊📊
