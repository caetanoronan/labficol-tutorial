# 🐍 Sintaxe Básica de Python

## O que é Sintaxe?

**Sintaxe** = as "regras de escrita" da linguagem.

Assim como português tem regras (acentuação, pontuação), Python também tem.

---

## 🎯 Seu Primeiro Programa

### Executar o Básico

Abra VS Code, crie arquivo `hello.py`:

```python
print("🎉 Olá, Mundo!")
```

Execute:
```powershell
python hello.py
```

Resultado:
```
🎉 Olá, Mundo!
```

**Parabéns!** Você escreveu seu primeiro programa! 🚀

---

## 📝 Comentários (Notas no Código)

Comentários são anotações que **não são executadas**.

```python
# Isto é um comentário de linha única
# Python ignora tudo depois de #

print("Isto executa")  # Comentário depois do código

# Comentário de múltiplas linhas
# Você pode escrever quantas linhas quiser
# Python ignora tudo

"""
Isto é um docstring (comentário de documentação)
Usado para descrever funções e módulos
Pode ter múltiplas linhas
"""
```

**Boa prática:** Escreva comentários explicando O QUE o código faz, não COMO.

```python
# ❌ Ruim - explica óbvio
x = x + 1  # Adiciona 1 a x

# ✅ Bom - explica o contexto
profundidade_final = profundidade_inicial + incremento_coleta  # Soma profundidade de coleta
```

---

## 🔤 Print (Mostrar Resultados)

`print()` é a função mais básica. Mostra mensagens na tela.

```python
# Texto simples
print("Olá, Oceanógrafo!")

# Múltiplos valores
print("Temperatura:", 22.5)

# Vários argumentos separados por vírgula
print("Data", "Espécie", "Profundidade")

# Sem quebra de linha
print("Python", end=" ")
print("Oceanografia")  # Resultado: "Python Oceanografia"

# Com separador customizado
print("Ulva", "Gracilaria", "Sargassum", sep=" | ")
# Resultado: Ulva | Gracilaria | Sargassum
```

---

## 📥 Input (Receber Informações)

`input()` pede informação do usuário.

```python
# Solicitar nome
nome = input("Qual seu nome? ")
print(f"Bem-vindo, {nome}!")

# Solicitar número
# ⚠️ IMPORTANTE: input() sempre retorna TEXTO!
idade_texto = input("Qual sua idade? ")
idade = int(idade_texto)  # Converter para número

# Forma abreviada
idade = int(input("Qual sua idade? "))
```

**Exemplo Completo:**

Crie arquivo `coleta_dados.py`:

```python
# Sistema de cadastro de amostra
print("=" * 50)
print("📝 CADASTRO DE AMOSTRA DE COLETA")
print("=" * 50)

especie = input("Espécie coletada: ")
profundidade = float(input("Profundidade (m): "))
temperatura = float(input("Temperatura (°C): "))

print("\n✅ Amostra cadastrada:")
print(f"   Espécie: {especie}")
print(f"   Profundidade: {profundidade}m")
print(f"   Temperatura: {temperatura}°C")
```

Execute:
```powershell
python coleta_dados.py
```

Resultado:
```
==================================================
📝 CADASTRO DE AMOSTRA DE COLETA
==================================================
Espécie coletada: Ulva lactuca
Profundidade (m): 5.2
Temperatura (°C): 22.5

✅ Amostra cadastrada:
   Espécie: Ulva lactuca
   Profundidade: 5.2m
   Temperatura: 22.5°C
```

---

## 🔤 String (Texto) - Operações

### Concatenação (Juntar Strings)

```python
# Método 1: Usar + (mais antigo)
nome = "Caetano"
sobrenome = "Ronan"
completo = nome + " " + sobrenome
print(completo)  # Caetano Ronan

# Método 2: f-string (RECOMENDADO - Python 3.6+)
especie = "Ulva lactuca"
profundidade = 5.2
msg = f"Amostra de {especie} a {profundidade}m"
print(msg)  # Amostra de Ulva lactuca a 5.2m

# Dentro de f-string, você pode usar expressões!
temperatura = 22.5
print(f"Temperatura: {temperatura:.1f}°C")  # .1f = 1 casa decimal
print(f"Temperatura + 5: {temperatura + 5}°C")
```

### Propriedades de String

```python
texto = "Oceanografia"

# Tamanho
print(len(texto))  # 12

# Maiúsculas
print(texto.upper())  # OCEANOGRAFIA

# Minúsculas
print(texto.lower())  # oceanografia

# Primeira letra maiúscula
print(texto.capitalize())  # Oceanografia

# Substituir texto
print(texto.replace("Oceano", "Bio"))  # Biorafia

# Dividir em partes
frase = "Ulva,Gracilaria,Sargassum"
especies = frase.split(",")
print(especies)  # ['Ulva', 'Gracilaria', 'Sargassum']

# Verificar se contém
if "Ulva" in frase:
    print("✅ Ulva encontrada!")
```

---

## 🔢 Números - Operações

### Inteiros (int)

```python
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333... (divisão com decimal)
print(a // b)   # 3 (divisão inteira)
print(a % b)    # 1 (resto da divisão)
print(a ** b)   # 1000 (10 elevado a 3)

# Operações com atribuição
numero = 5
numero += 3  # numero = numero + 3 → 8
numero -= 2  # numero = numero - 2 → 6
numero *= 2  # numero = numero * 2 → 12
numero //= 3 # numero = numero // 3 → 4
```

### Decimais (float)

```python
temperatura = 22.5
profundidade = 5.0
salinidade = 35.123456

# Arredondamento
print(round(salinidade, 2))  # 35.12 (2 casas decimais)
print(round(salinidade, 1))  # 35.1 (1 casa decimal)

# Função abs (valor absoluto)
print(abs(-5.2))  # 5.2

# Funções matemáticas
import math
print(math.sqrt(16))  # 4.0 (raiz quadrada)
print(math.pi)        # 3.14159...
print(math.ceil(5.2))  # 6 (arredonda para cima)
print(math.floor(5.8)) # 5 (arredonda para baixo)
```

---

## ✅ Booleanos (Verdadeiro/Falso)

```python
# Valores booleanos
verdade = True
falsidade = False

# Comparações retornam booleanos
print(5 > 3)      # True
print(5 < 3)      # False
print(5 == 5)     # True (igual)
print(5 != 3)     # True (diferente)
print(5 >= 5)     # True (maior ou igual)

# Operadores lógicos
print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Exemplos práticos
temperatura = 22.5
profundidade = 5.2

# Verificar se coleta foi válida
valida = (temperatura > 20) and (profundidade < 10)
print(f"Coleta válida: {valida}")  # True
```

---

## 📋 Conversão de Tipos

Às vezes você precisa converter um tipo para outro.

```python
# String para Número
texto_numero = "123"
numero = int(texto_numero)
print(tipo)  # <class 'int'>

# Número para String
numero = 42
texto = str(numero)
print(texto)  # "42"

# String para Decimal
texto_decimal = "3.14"
decimal = float(texto_decimal)
print(decimal)  # 3.14

# Número para Boolean
print(bool(0))     # False (0 é falso)
print(bool(1))     # True (número != 0 é verdadeiro)
print(bool(""))    # False (string vazia é falsa)
print(bool("Oi"))  # True (string não vazia é verdadeira)
```

---

## 🔍 Tipo de Dado (type)

Verificar que tipo é uma variável:

```python
print(type(5))              # <class 'int'>
print(type(5.0))            # <class 'float'>
print(type("Olá"))          # <class 'str'>
print(type(True))           # <class 'bool'>
print(type([1, 2, 3]))      # <class 'list'>

# Usar em condição
valor = "123"
if type(valor) == str:
    print("É uma string!")
```

---

## 🎯 Exemplo Prático: Sistema de Coleta

Crie arquivo `analise_coleta.py`:

```python
print("🌊 SISTEMA DE ANÁLISE DE COLETA")
print("-" * 50)

# Receber dados
especie = input("Espécie: ")
profundidade = float(input("Profundidade (m): "))
temperatura = float(input("Temperatura (°C): "))
salinidade = float(input("Salinidade (PSU): "))

# Validações
print("\n📊 ANÁLISE:")

# Verificar profundidade
if profundidade < 5:
    profundidade_status = "Rasa"
elif profundidade < 20:
    profundidade_status = "Intermediária"
else:
    profundidade_status = "Profunda"
print(f"Profundidade: {profundidade}m ({profundidade_status})")

# Verificar temperatura
if 20 <= temperatura <= 25:
    temp_status = "✅ Ideal"
else:
    temp_status = "⚠️ Fora do padrão"
print(f"Temperatura: {temperatura}°C {temp_status}")

# Verificar salinidade
salinidade_arredondada = round(salinidade, 1)
print(f"Salinidade: {salinidade_arredondada} PSU")

# Resumo
valida = (20 <= temperatura <= 25) and (profundidade < 50)
status_final = "✅ VÁLIDA" if valida else "❌ INVÁLIDA"
print(f"\nStatus da coleta: {status_final}")
```

Execute:
```powershell
python analise_coleta.py
```

---

## 💾 Variáveis - Boas Práticas

### Nomes de Variáveis em Python

```python
# ✅ BOM - Descritivo, em inglês ou português claro
temperatura_media = 22.5
profundidade_coleta_m = 5.2
especie_coletada = "Ulva lactuca"
numero_amostras = 10

# ❌ RUIM - Genérico ou confuso
t = 22.5
x = 5.2
s = "Ulva lactuca"
n = 10

# ✅ BOM - Constantes em MAIÚSCULA
PI = 3.14159
PROFUNDIDADE_MAXIMA = 100
TEMPERATURA_IDEAL_MINIMA = 20
TEMPERATURA_IDEAL_MAXIMA = 25

# ❌ EVITAR
meu_valor_muito_longo_que_ninguem_entende = 42
_variavel = 10  # Convenção: começa com _ = privada
```

### Escopo de Variáveis

```python
# Variável global
mensagem_global = "Oceanografia UFSC"

if True:
    # Variável local
    mensagem_local = "LAFIC"
    print(mensagem_global)  # ✅ Funciona
    print(mensagem_local)   # ✅ Funciona

print(mensagem_global)  # ✅ Funciona
print(mensagem_local)   # ❌ ERRO - não existe fora do bloco
```

---

## 🎓 Exemplo Completo: Calculadora Oceanográfica

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculadora Oceanográfica
Calcula propriedades de água marinha
"""

print("=" * 60)
print("🌊 CALCULADORA OCEANOGRÁFICA")
print("=" * 60)

# Constantes
SALINIDADE_PADRAO = 35.0
DENSIDADE_AGUA_DOCE = 1.0
DENSIDADE_AGUA_SALGADA_COEF = 0.8

# Entrada de dados
print("\n📥 Digite os parâmetros:")
profundidade = float(input("Profundidade (m): "))
temperatura = float(input("Temperatura (°C): "))
salinidade = float(input("Salinidade (PSU): "))

# Cálculos
print("\n📊 RESULTADOS:\n")

# Densidade aproximada
densidade = 1000 + (salinidade - SALINIDADE_PADRAO) * 0.78
print(f"Densidade da água: {densidade:.2f} kg/m³")

# Pressão aproximada (1 atm por 10m)
pressao_atm = 1 + (profundidade / 10)
print(f"Pressão: {pressao_atm:.2f} atm")

# Luz solar (50% em ~5m, ~1% em ~30m)
penetracao_luz = 100 * (0.7 ** (profundidade / 10))
print(f"Penetração de luz: {penetracao_luz:.1f}%")

# Status da coleta
print("\n✓ STATUS DA COLETA:")
if 20 <= temperatura <= 28:
    print("✅ Temperatura adequada")
else:
    print("⚠️ Temperatura fora do ideal")

if 34 <= salinidade <= 36:
    print("✅ Salinidade adequada")
else:
    print("⚠️ Salinidade fora do ideal")

if profundidade < 50:
    print("✅ Profundidade acessível")
else:
    print("⚠️ Profundidade muito grande")

print("\n" + "=" * 60)
```

---

## 🎓 Checklist desta Lição

- [ ] Entendo o que é print() e input()
- [ ] Consigo fazer concatenação de strings
- [ ] Entendo operações com números
- [ ] Sou capaz de converter tipos (int, float, str)
- [ ] Testei pelo menos 3 exemplos
- [ ] Sei o que são variáveis e boas práticas de nomes

Se marcou tudo, você está pronto para **Estruturas de Dados**! 🎉

---

## ➡️ Próximo Tópico

**👉 [02-Estruturas-Dados.md](02-Estruturas-Dados.md)**

Lá você aprenderá:
- Listas (arrays)
- Dicionários
- Tuplas
- Conjuntos
- Operações com coleções

---

## 📝 Resumo de Funções Básicas

| Função | Uso | Exemplo |
|--------|-----|---------|
| `print()` | Mostrar na tela | `print("Olá")` |
| `input()` | Receber do usuário | `nome = input("Nome: ")` |
| `int()` | Converter para inteiro | `int("5")` → 5 |
| `float()` | Converter para decimal | `float("3.14")` → 3.14 |
| `str()` | Converter para string | `str(42)` → "42" |
| `len()` | Tamanho | `len("Olá")` → 3 |
| `type()` | Ver tipo | `type(5)` → `<class 'int'>` |
| `round()` | Arredondar | `round(3.7)` → 4 |

---

**Você está progredindo rápido!** 🚀 Próximo: Estruturas de Dados!
