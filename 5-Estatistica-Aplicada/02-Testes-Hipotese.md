# 🧪 Testes de Hipótese para Dados Biológicos

## 🎯 Objetivo da Lição

Aprender a realizar **testes estatísticos** para comparar grupos e testar hipóteses científicas usando Python.

**O que faremos:**
- Teste t (Student's t-test)
- ANOVA (Analysis of Variance)
- Testes não-paramétricos
- Interpretar p-valores
- Tomar decisões estatísticas

---

## 🔬 Conceitos Fundamentais

### Hipótese Nula (H₀) vs Alternativa (H₁)

```
H₀: Não há diferença entre os grupos
H₁: Há diferença entre os grupos
```

### P-valor

**Definição:** Probabilidade de obter os resultados observados se H₀ for verdadeira.

```python
if p_valor < 0.05:
    print("✅ Rejeitamos H₀ (diferença significativa)")
else:
    print("❌ Não rejeitamos H₀ (sem diferença significativa)")
```

**Níveis de significância comuns:**
- α = 0.05 (5%) → padrão
- α = 0.01 (1%) → mais rigoroso
- α = 0.10 (10%) → exploratório

---

## 📊 Teste t de Student

### Teste t para Uma Amostra

**Objetivo:** Comparar média da amostra com valor de referência.

**Exemplo:** Biomassa média é diferente de 250g?

```python
from scipy import stats
import numpy as np

# Dados de biomassa (g)
biomassas = [245.3, 180.7, 310.2, 198.5, 220.4, 302.1, 195.8, 275.4]

# Valor de referência (hipotético)
valor_referencia = 250

# Realizar teste t para uma amostra
t_stat, p_valor = stats.ttest_1samp(biomassas, valor_referencia)

print("="*60)
print("🧪 TESTE T PARA UMA AMOSTRA")
print("="*60)
print(f"\nH₀: μ = {valor_referencia}g")
print(f"H₁: μ ≠ {valor_referencia}g")
print(f"\nMédia observada: {np.mean(biomassas):.2f}g")
print(f"Estatística t: {t_stat:.4f}")
print(f"P-valor: {p_valor:.4f}")

if p_valor < 0.05:
    print("\n✅ Resultado: SIGNIFICATIVO (p < 0.05)")
    print("   Rejeitamos H₀: A média é diferente de 250g")
else:
    print("\n❌ Resultado: NÃO SIGNIFICATIVO (p ≥ 0.05)")
    print("   Não rejeitamos H₀: A média pode ser 250g")
```

---

### Teste t para Amostras Independentes

**Objetivo:** Comparar médias de dois grupos diferentes.

**Exemplo:** Biomassa de *Ulva* vs *Gracilaria* é diferente?

```python
import pandas as pd

# Dados de duas espécies
dados = {
    'especie': ['Ulva', 'Ulva', 'Ulva', 'Ulva', 'Ulva',
                'Gracilaria', 'Gracilaria', 'Gracilaria', 'Gracilaria'],
    'biomassa_g': [245.3, 302.1, 275.4, 310.8, 295.7,
                   180.7, 195.8, 205.6, 220.4]
}

df = pd.DataFrame(dados)

# Separar grupos
ulva = df[df['especie'] == 'Ulva']['biomassa_g']
gracilaria = df[df['especie'] == 'Gracilaria']['biomassa_g']

# Teste t independente
t_stat, p_valor = stats.ttest_ind(ulva, gracilaria)

print("\n" + "="*60)
print("🧪 TESTE T PARA AMOSTRAS INDEPENDENTES")
print("="*60)
print(f"\nH₀: μ₁ = μ₂ (médias iguais)")
print(f"H₁: μ₁ ≠ μ₂ (médias diferentes)")

print(f"\n📊 Estatísticas descritivas:")
print(f"   Ulva:       n={len(ulva)}, média={ulva.mean():.2f}g ± {ulva.std():.2f}g")
print(f"   Gracilaria: n={len(gracilaria)}, média={gracilaria.mean():.2f}g ± {gracilaria.std():.2f}g")

print(f"\n🔬 Resultado do teste:")
print(f"   Estatística t: {t_stat:.4f}")
print(f"   P-valor: {p_valor:.4f}")

if p_valor < 0.05:
    print("\n✅ Conclusão: Há diferença significativa entre as espécies (p < 0.05)")
    diferenca = ulva.mean() - gracilaria.mean()
    print(f"   Ulva tem {abs(diferenca):.2f}g {'a mais' if diferenca > 0 else 'a menos'} que Gracilaria")
else:
    print("\n❌ Conclusão: Não há diferença significativa (p ≥ 0.05)")
```

---

### Teste t Pareado

**Objetivo:** Comparar médias de duas medições no mesmo indivíduo/local.

**Exemplo:** Biomassa antes vs depois de tratamento.

```python
# Biomassa antes e depois de experimento (mesmos locais)
antes = [245.3, 180.7, 310.2, 198.5, 220.4]
depois = [280.1, 195.3, 335.8, 210.2, 245.7]

# Teste t pareado
t_stat, p_valor = stats.ttest_rel(antes, depois)

print("\n" + "="*60)
print("🧪 TESTE T PAREADO")
print("="*60)
print(f"\nH₀: μ_diferença = 0 (sem mudança)")
print(f"H₁: μ_diferença ≠ 0 (houve mudança)")

diferencas = [d - a for d, a in zip(depois, antes)]
print(f"\n📊 Diferenças: {[f'{d:.1f}' for d in diferencas]}")
print(f"   Média das diferenças: {np.mean(diferencas):.2f}g")

print(f"\n🔬 Resultado do teste:")
print(f"   Estatística t: {t_stat:.4f}")
print(f"   P-valor: {p_valor:.4f}")

if p_valor < 0.05:
    print("\n✅ Conclusão: Houve mudança significativa (p < 0.05)")
else:
    print("\n❌ Conclusão: Não houve mudança significativa (p ≥ 0.05)")
```

---

## 📊 ANOVA (Analysis of Variance)

**Objetivo:** Comparar médias de 3 ou mais grupos.

**Exemplo:** Biomassa difere entre 4 praias?

```python
# Dados de 4 praias
praia1 = [245.3, 302.1, 275.4]  # Ingleses
praia2 = [180.7, 195.8, 205.6]  # Barra
praia3 = [310.2, 340.5, 315.2]  # Armação
praia4 = [198.5, 220.4, 210.8]  # Garopaba

# ANOVA one-way
f_stat, p_valor = stats.f_oneway(praia1, praia2, praia3, praia4)

print("\n" + "="*60)
print("🧪 ANOVA (ONE-WAY)")
print("="*60)
print(f"\nH₀: μ₁ = μ₂ = μ₃ = μ₄ (todas as médias iguais)")
print(f"H₁: Pelo menos uma média é diferente")

print(f"\n📊 Estatísticas por praia:")
praias = [praia1, praia2, praia3, praia4]
nomes = ['Ingleses', 'Barra', 'Armação', 'Garopaba']

for nome, dados in zip(nomes, praias):
    print(f"   {nome}: média={np.mean(dados):.2f}g ± {np.std(dados, ddof=1):.2f}g")

print(f"\n🔬 Resultado do ANOVA:")
print(f"   Estatística F: {f_stat:.4f}")
print(f"   P-valor: {p_valor:.4f}")

if p_valor < 0.05:
    print("\n✅ Conclusão: Há diferença significativa entre as praias (p < 0.05)")
    print("   💡 Use teste post-hoc (Tukey) para ver quais praias diferem")
else:
    print("\n❌ Conclusão: Não há diferença significativa (p ≥ 0.05)")
```

### Teste Post-Hoc (Tukey HSD)

```python
from scipy.stats import tukey_hsd

# Após ANOVA significativo, identificar diferenças
result = tukey_hsd(praia1, praia2, praia3, praia4)

print("\n" + "="*60)
print("📊 TESTE POST-HOC (TUKEY HSD)")
print("="*60)
print("\nComparações pareadas:")
print(result)
```

---

## 🔄 Testes Não-Paramétricos

### Quando usar?

- Dados **não seguem distribuição normal**
- Amostras **pequenas** (n < 30)
- Dados **ordinais** (rankings)
- Presença de **outliers**

### Mann-Whitney U (alternativa ao teste t)

```python
# Comparar dois grupos (não-paramétrico)
grupo1 = [245, 180, 310, 198, 220]
grupo2 = [302, 195, 275, 310, 295]

u_stat, p_valor = stats.mannwhitneyu(grupo1, grupo2, alternative='two-sided')

print("\n" + "="*60)
print("🧪 MANN-WHITNEY U TEST")
print("="*60)
print(f"Estatística U: {u_stat:.4f}")
print(f"P-valor: {p_valor:.4f}")

if p_valor < 0.05:
    print("✅ Diferença significativa (p < 0.05)")
else:
    print("❌ Sem diferença significativa (p ≥ 0.05)")
```

### Kruskal-Wallis (alternativa ao ANOVA)

```python
# Comparar 3+ grupos (não-paramétrico)
h_stat, p_valor = stats.kruskal(praia1, praia2, praia3, praia4)

print("\n" + "="*60)
print("🧪 KRUSKAL-WALLIS TEST")
print("="*60)
print(f"Estatística H: {h_stat:.4f}")
print(f"P-valor: {p_valor:.4f}")
```

---

## 📈 Exemplo Completo: Análise Comparativa

```python
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Dataset completo
dados = {
    'praia': ['Ingleses']*5 + ['Barra']*5 + ['Armação']*5,
    'biomassa_g': [245.3, 302.1, 275.4, 310.8, 295.7,  # Ingleses
                   180.7, 195.8, 205.6, 220.4, 198.5,  # Barra
                   310.2, 340.5, 315.2, 325.8, 330.1]  # Armação
}

df = pd.DataFrame(dados)

print("="*70)
print("🔬 ANÁLISE COMPARATIVA COMPLETA")
print("="*70)

# ====================
# 1. ESTATÍSTICAS DESCRITIVAS
# ====================

print("\n📊 ESTATÍSTICAS POR PRAIA:")
print("-"*70)

for praia in df['praia'].unique():
    dados_praia = df[df['praia'] == praia]['biomassa_g']
    print(f"\n{praia}:")
    print(f"   n = {len(dados_praia)}")
    print(f"   Média = {dados_praia.mean():.2f}g ± {dados_praia.std():.2f}g")
    print(f"   Mediana = {dados_praia.median():.2f}g")
    print(f"   Range = [{dados_praia.min():.2f}, {dados_praia.max():.2f}]g")

# ====================
# 2. TESTE DE NORMALIDADE
# ====================

print("\n" + "="*70)
print("🔍 TESTE DE NORMALIDADE (SHAPIRO-WILK)")
print("="*70)

for praia in df['praia'].unique():
    dados_praia = df[df['praia'] == praia]['biomassa_g']
    stat, p_valor = stats.shapiro(dados_praia)
    
    normal = "SIM ✅" if p_valor > 0.05 else "NÃO ❌"
    print(f"\n{praia}: p={p_valor:.4f} → Distribução normal? {normal}")

# ====================
# 3. ANOVA
# ====================

print("\n" + "="*70)
print("🧪 ANOVA ONE-WAY")
print("="*70)

ingleses = df[df['praia'] == 'Ingleses']['biomassa_g']
barra = df[df['praia'] == 'Barra']['biomassa_g']
armacao = df[df['praia'] == 'Armação']['biomassa_g']

f_stat, p_valor = stats.f_oneway(ingleses, barra, armacao)

print(f"\nH₀: μ₁ = μ₂ = μ₃")
print(f"Estatística F: {f_stat:.4f}")
print(f"P-valor: {p_valor:.6f}")

if p_valor < 0.05:
    print("\n✅ RESULTADO: Há diferença significativa entre praias (p < 0.05)")
else:
    print("\n❌ RESULTADO: Não há diferença significativa (p ≥ 0.05)")

# ====================
# 4. COMPARAÇÕES PAREADAS (Post-hoc)
# ====================

if p_valor < 0.05:
    print("\n" + "="*70)
    print("📊 COMPARAÇÕES PAREADAS (TESTE T)")
    print("="*70)
    
    comparacoes = [
        ('Ingleses', ingleses, 'Barra', barra),
        ('Ingleses', ingleses, 'Armação', armacao),
        ('Barra', barra, 'Armação', armacao)
    ]
    
    for nome1, dados1, nome2, dados2 in comparacoes:
        t_stat, p = stats.ttest_ind(dados1, dados2)
        
        # Correção de Bonferroni
        p_corrigido = p * 3  # 3 comparações
        
        sig = "✅ SIG" if p_corrigido < 0.05 else "❌ NS"
        print(f"\n{nome1} vs {nome2}:")
        print(f"   p-valor: {p:.4f} (corrigido: {p_corrigido:.4f}) {sig}")

# ====================
# 5. VISUALIZAÇÃO
# ====================

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Boxplot
ax1 = axes[0]
df.boxplot(column='biomassa_g', by='praia', ax=ax1)
ax1.set_xlabel('Praia', fontweight='bold')
ax1.set_ylabel('Biomassa (g)', fontweight='bold')
ax1.set_title('Distribuição de Biomassa por Praia')
plt.sca(ax1)
plt.xticks(rotation=0)

# Barplot com erro
ax2 = axes[1]
medias = df.groupby('praia')['biomassa_g'].mean()
erros = df.groupby('praia')['biomassa_g'].std()

ax2.bar(range(len(medias)), medias, yerr=erros, 
        capsize=5, alpha=0.7, edgecolor='black', color=['skyblue', 'lightcoral', 'lightgreen'])
ax2.set_xticks(range(len(medias)))
ax2.set_xticklabels(medias.index, rotation=0)
ax2.set_xlabel('Praia', fontweight='bold')
ax2.set_ylabel('Biomassa Média (g)', fontweight='bold')
ax2.set_title('Biomassa Média (± DP)')
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('analise_comparativa.png', dpi=300)
print("\n✅ Gráfico salvo: analise_comparativa.png")

plt.show()

print("\n" + "="*70)
print("✅ ANÁLISE CONCLUÍDA!")
print("="*70)
```

---

## 🎓 Checklist desta Lição

- [ ] Entendi hipótese nula e alternativa
- [ ] Realizei teste t para comparar 2 grupos
- [ ] Usei ANOVA para comparar 3+ grupos
- [ ] Interpretei p-valores corretamente
- [ ] Apliquei testes não-paramétricos quando necessário

---

## ➡️ Próxima Lição

- **03-Correlacao-Regressao.md** (Análise de relações entre variáveis)

---

**Você domina testes de hipótese!** 🧪✨
