# 🧠 Conceitos Básicos de Programação

## O que é Programação?

**Programação** é dar instruções ao computador em uma linguagem que ele entende.

### Analogia com a Vida Real

```
PESSOAS                          COMPUTADORES
├─ Entende português            ├─ Entende Python, JavaScript, etc
├─ Segue instruções              ├─ Executa código
├─ Toma decisões                 ├─ Segue lógica
└─ Usa ferramentas               └─ Usa bibliotecas
```

---

## 🔤 Linguagens de Programação

Assim como temos português, inglês, espanhol...
Temos linguagens de programação! 

### As principais para Biologia/Oceanografia:

```
🐍 Python      → Análise de dados (MELHOR PARA COMEÇAR)
🌐 JavaScript  → Mapas interativos web
📊 R           → Estatística avançada
🗺️ SQL         → Bancos de dados
```

**Você vai aprender:** Python → JavaScript → GeoJSON/SQL

---

## 💾 Informações Básicas (Bits & Bytes)

Antes de entender programação, você precisa entender como computadores armazenam dados.

### A Unidade Mais Pequena: Bit

```
1 bit = 0 ou 1
        Falso ou Verdadeiro
        Desligado ou Ligado
```

### Unidades de Armazenamento

```
1 Byte         = 8 bits                    (caractere)
1 Kilobyte     = 1.024 bytes              (~1 página)
1 Megabyte     = 1.024 KB                  (~música)
1 Gigabyte     = 1.024 MB                  (~filme)
1 Terabyte     = 1.024 GB                  (~biblioteca)
```

**Exemplo real:**
- Uma foto do microscópio: ~5 MB
- Datasets de pesquisa: 100 MB a 10 GB
- Seu computador: 256 GB a 1 TB

---

## 📊 Tipos de Dados (O Que o Computador Armazena)

### 1. Números Inteiros (int)
```python
idade = 25
quantidade = 1000
profundidade = -500  # negativo é permitido
```

### 2. Números Decimais (float)
```python
temperatura = 22.5
salinidade = 35.0
pH = 7.8
```

### 3. Texto (string)
```python
nome = "Caetano Ronan"
especie = "Ulva lactuca"
localizacao = "Praia dos Ingleses"
```

### 4. Verdadeiro/Falso (bool)
```python
coletado = True
analisado = False
valido = True
```

### 5. Listas (collections)
```python
especies = ["Ulva lactuca", "Gracilaria", "Sargassum"]
temperaturas = [22.5, 23.1, 22.8]
dados_mistos = [1, "espécie", True, 22.5]
```

### 6. Dicionários (dados com rótulo)
```python
amostra = {
    "id": 1,
    "especie": "Ulva lactuca",
    "profundidade": 5.2,
    "temperatura": 22.5,
    "valida": True
}
```

---

## 🔀 Estruturas de Controle

### 1. Sequência
Executar linhas uma por uma:

```python
# Linha 1
nome = "Oceanógrafo"

# Linha 2
print(nome)  # Printa: "Oceanógrafo"

# Linha 3
profissao = "Pesquisador"
```

### 2. Condição (if/else)
Tomar decisões:

```python
temperatura = 22.5

if temperatura > 25:
    print("🌞 Água quente")
elif temperatura > 20:
    print("🌤️ Temperatura ideal para coleta")
else:
    print("❄️ Água fria")
```

Resultado: "🌤️ Temperatura ideal para coleta"

### 3. Repetição (loops)
Fazer algo múltiplas vezes:

```python
especies = ["Ulva", "Gracilaria", "Sargassum"]

for especie in especies:
    print(f"Analisando: {especie}")
```

Resultado:
```
Analisando: Ulva
Analisando: Gracilaria
Analisando: Sargassum
```

---

## 🛠️ Funções (Reutilizar Código)

Função = bloco de código que pode ser usado várias vezes.

### Exemplo 1: Função Simples

```python
def saudar(nome):
    return f"Olá, {nome}! Bem-vindo à Oceanografia!"

# Usar a função
msg = saudar("Caetano")
print(msg)  # "Olá, Caetano! Bem-vindo à Oceanografia!"
```

### Exemplo 2: Função para Análise

```python
def calcular_media_temperatura(temperaturas):
    """Calcula a temperatura média"""
    total = sum(temperaturas)
    quantidade = len(temperaturas)
    return total / quantidade

# Dados de coleta
temps = [22.5, 23.1, 22.8, 23.4]
media = calcular_media_temperatura(temps)
print(f"Temperatura média: {media:.1f}°C")  # 22.95°C
```

### Exemplo 3: Função com Múltiplas Operações

```python
def analisar_amostra(especie, profundidade, temperatura):
    """Analisa uma amostra de coleta"""
    
    # Verificação
    if profundidade < 0:
        return "❌ Profundidade inválida"
    
    # Análise
    if temperatura > 25:
        condicao = "quente"
    else:
        condicao = "fria"
    
    # Resultado
    resultado = {
        "especie": especie,
        "profundidade": profundidade,
        "condicao": condicao,
        "valida": True
    }
    
    return resultado

# Usar função
amostra = analisar_amostra("Ulva lactuca", 5.2, 22.5)
print(amostra)
# {'especie': 'Ulva lactuca', 'profundidade': 5.2, 
#  'condicao': 'fria', 'valida': True}
```

---

## 📚 Variáveis (Contêineres de Informação)

Variáveis são "caixas" que armazenam informações.

```python
# Criar variável
nome_pesquisador = "Caetano"
anos_experiencia = 5

# Modificar variável
anos_experiencia = 6

# Usar variável
print(f"{nome_pesquisador} tem {anos_experiencia} anos de experiência")
# Resultado: "Caetano tem 6 anos de experiência"
```

### Nomes de Variáveis (Regras)

✅ Bom:
```python
temperatura_media = 22.5
especie_coletada = "Ulva"
profundidade_m = 10
```

❌ Ruim:
```python
a = 22.5              # muito genérico
temperatura média = 10  # não use espaço
9temperatura = 5      # não comece com número
```

---

## 🔗 Operadores (Operações Matemáticas)

### Aritméticos
```python
a = 10
b = 3

soma = a + b        # 13
subtracao = a - b   # 7
multiplicacao = a * b  # 30
divisao = a / b     # 3.333...
inteira = a // b    # 3 (sem decimais)
resto = a % b       # 1 (10 dividido por 3 deixa resto 1)
potencia = a ** b   # 1000 (10 ao cubo)
```

### Comparação (resultado é True ou False)
```python
10 > 5      # True
10 < 5      # False
10 == 10    # True (igual)
10 != 5     # True (diferente)
10 >= 10    # True (maior ou igual)
```

### Lógicos
```python
temperatura = 22.5
profundidade = 5

# AND (e)
if temperatura > 20 and profundidade < 10:
    print("✅ Condições ideais de coleta")

# OR (ou)
if temperatura < 15 or temperatura > 28:
    print("❌ Temperatura fora do ideal")

# NOT (não)
if not profundidade > 100:
    print("✅ Profundidade aceitável")
```

---

## 📁 Importar Bibliotecas (Usar Ferramentas)

Bibliotecas são códigos prontos que outras pessoas criaram.

### O que é uma Biblioteca?
```
Imagine que programação é receita de bolo.
Uma biblioteca é um livro de receitas pronto!
```

### Importar Bibliotecas

```python
# Importar tudo
import numpy

# Usar função
dados = numpy.array([1, 2, 3, 4, 5])
print(numpy.mean(dados))  # 3.0

# Importar com apelido (mais prático)
import numpy as np
dados = np.array([1, 2, 3, 4, 5])
print(np.mean(dados))  # 3.0

# Importar função específica
from math import sqrt, pi
resultado = sqrt(16)  # 4.0
```

### Bibliotecas Que Você Usará

```python
# Análise de Dados
import pandas as pd      # Tabelas/DataFrames
import numpy as np       # Matrizes/Arrays

# Visualização
import matplotlib.pyplot as plt  # Gráficos
import folium                     # Mapas

# Geoespacial
import geopandas as gpd  # Dados com geografia
from shapely import Point, Polygon  # Geometrias

# Web
import requests  # Buscar dados na internet
```

---

## 💡 Pensamento Algorítmico

Um **algoritmo** é uma série de passos para resolver um problema.

### Exemplo: Como Fazer Uma Coleta de Dados?

```
ALGORITMO: Coleta de Fitoplâncton

PASSO 1: Chegar no local de coleta
PASSO 2: Verificar temperatura e salinidade
PASSO 3: SE temperatura < 15 OU > 30
           ENTÃO: Não coletar
           SENÃO: Continuar
PASSO 4: Coletar amostra com garrafa
PASSO 5: Armazenar em recipiente estéril
PASSO 6: Anotar hora, coordenadas, profundidade
PASSO 7: Enviar para laboratório
PASSO 8: FIM
```

---

## 🎯 Exemplo Completo: Sistema de Análise

```python
# Bibliotecas
import pandas as pd

# Dados de coleta
amostras = {
    'data': ['2025-01-01', '2025-01-02', '2025-01-03'],
    'especie': ['Ulva', 'Gracilaria', 'Sargassum'],
    'profundidade_m': [5.2, 7.8, 3.1],
    'temperatura_c': [22.5, 23.1, 22.8],
    'densidade_cells_ml': [150, 230, 180]
}

# Criar tabela
df = pd.DataFrame(amostras)

# Funções de análise
def validar_amostra(temp, prof):
    """Verifica se amostra é válida"""
    if 20 <= temp <= 25 and prof < 10:
        return "✅ Válida"
    else:
        return "❌ Inválida"

def densidade_media(densidade_list):
    """Calcula densidade média"""
    return sum(densidade_list) / len(densidade_list)

# Análises
print("=" * 60)
print("📊 RELATÓRIO DE ANÁLISE DE FITOPLÂNCTON")
print("=" * 60)

# Mostrar dados
print("\n📋 Dados Coletados:")
print(df.to_string())

# Validação
print("\n✓ Validação:")
for idx, row in df.iterrows():
    validacao = validar_amostra(row['temperatura_c'], row['profundidade_m'])
    print(f"  Amostra {idx+1}: {validacao}")

# Estatísticas
print("\n📈 Estatísticas:")
print(f"  Temperatura média: {df['temperatura_c'].mean():.1f}°C")
print(f"  Profundidade média: {df['profundidade_m'].mean():.1f}m")
print(f"  Densidade média: {densidade_media(df['densidade_cells_ml']):.0f} células/mL")
print(f"  Espécie mais frequente: {df['especie'].mode()[0]}")

print("\n" + "=" * 60)
```

**Resultado:**
```
============================================================
📊 RELATÓRIO DE ANÁLISE DE FITOPLÂNCTON
============================================================

📋 Dados Coletados:
        data       especie  profundidade_m  temperatura_c  densidade_cells_ml
0 2025-01-01          Ulva             5.2           22.5                 150
1 2025-01-02    Gracilaria             7.8           23.1                 230
2 2025-01-03     Sargassum             3.1           22.8                 180

✓ Validação:
  Amostra 1: ✅ Válida
  Amostra 2: ✅ Válida
  Amostra 3: ✅ Válida

📈 Estatísticas:
  Temperatura média: 22.8°C
  Profundidade média: 5.4m
  Densidade média: 187 células/mL
  Espécie mais frequente: Gracilaria

============================================================
```

---

## 🔄 Ciclo de Desenvolvimento

```
         ┌─────────────────────┐
         │  Problema Real      │
         │  (Ex: Mapear algas) │
         └──────────┬──────────┘
                    │
                    ↓
         ┌─────────────────────┐
         │  Planejar Solution  │
         │  (Algoritmo)        │
         └──────────┬──────────┘
                    │
                    ↓
         ┌─────────────────────┐
         │  Escrever Código    │
         │  (Implementação)    │
         └──────────┬──────────┘
                    │
                    ↓
         ┌─────────────────────┐
         │  Testar            │
         │  (Debug)           │
         └──────────┬──────────┘
                    │
              Funciona?
             /       \
           NÃO       SIM
            │         │
            └─────────┘
            ↓
         ┌─────────────────────┐
         │  Publicar           │
         │  (GitHub/web)       │
         └─────────────────────┘
```

---

## 📝 Checklist de Aprendizado

- [ ] Entendo o que é programação
- [ ] Conheço os tipos de dados básicos
- [ ] Entendo condições (if/else)
- [ ] Entendo repetições (loops)
- [ ] Consegui escrever uma função
- [ ] Importei uma biblioteca com sucesso
- [ ] Rodei um programa Python

Se marcou tudo, você está pronto para **Python Essencial**! 🎉

---

## 🎓 Conceitos-Chave para Lembrar

| Conceito | Definição |
|----------|-----------|
| **Variável** | Contêiner que armazena dados |
| **Tipo de Dado** | Categoria do dado (int, float, string, etc) |
| **Função** | Bloco de código reutilizável |
| **Algoritmo** | Série de passos para resolver problema |
| **Biblioteca** | Código pronto para usar |
| **Sequência** | Executar linhas uma por uma |
| **Condição** | Tomar decisão (if/else) |
| **Loop** | Repetir ações |

---

## ➡️ Próximo Passo

Agora que você entende os conceitos, vamos para:

**👉 Módulo 1: [PYTHON ESSENCIAL](../1-Python-Essencial/)**

Lá você aprenderá na prática:
- Sintaxe Python
- Estruturas de dados avançadas
- Funções profissionais
- Processamento de arquivos

---

## 🚀 Seu Progresso

```
0-FUNDAMENTOS
├── 01-Introducao ✅
├── 02-Configurar-Ambiente ✅
└── 03-Conceitos-Basicos ✅ (VOCÊ ESTÁ AQUI!)

Pronto para Python! 🐍
```

---

**Parabéns por completar o módulo Fundamentos!** 🎊

Você agora tem a base teórica. Vamos botar a mão na massa com Python? 🐍
