# 🔧 Funções e Módulos

## O que são Funções?

**Função** = bloco de código reutilizável.

### Analogia
```
Sem funções: Copiar e colar o mesmo código 100 vezes
Com funções: Escrever uma vez, usar 100 vezes
```

---

## 📝 Definir uma Função

### Sintaxe Básica

```python
def nome_funcao():
    """Descrição da função (docstring)"""
    # código aqui
    pass

# Chamar função
nome_funcao()
```

### Exemplo Simples

```python
def saudar():
    """Sauda o usuário"""
    print("Olá, bem-vindo ao LABFICOL!")

# Chamar
saudar()  # Printa: "Olá, bem-vindo ao LABFICOL!"
```

---

## 📥 Parâmetros (Receber Dados)

Funções podem receber dados para processar.

### Parâmetros Simples

```python
def saudar(nome):
    """Sauda uma pessoa específica"""
    print(f"Olá, {nome}!")

# Chamar com argumento
saudar("Caetano")      # Printa: "Olá, Caetano!"
saudar("Mariana")      # Printa: "Olá, Mariana!"

# Múltiplos parâmetros
def calcular_imc(peso, altura):
    """Calcula IMC"""
    imc = peso / (altura ** 2)
    return imc

resultado = calcular_imc(70, 1.75)
print(f"IMC: {resultado:.1f}")
```

### Parâmetros com Valores Padrão

```python
def saudar(nome, idioma="português"):
    """Sauda em um idioma"""
    if idioma == "português":
        print(f"Olá, {nome}!")
    elif idioma == "inglês":
        print(f"Hello, {nome}!")

# Chamar
saudar("Caetano")                    # Usa padrão português
saudar("Caetano", idioma="inglês")   # Especifica inglês
```

---

## 📤 Return (Retornar Valores)

Funções podem retornar resultados.

### Return Simples

```python
def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Usar retorno
temp_f = celsius_para_fahrenheit(22.5)
print(f"22.5°C = {temp_f:.1f}°F")  # 72.5°F

# Sem salvar
print(celsius_para_fahrenheit(25))  # 77.0
```

### Múltiplos Retornos

```python
def calcular_estatisticas(numeros):
    """Calcula média, mín e máx"""
    media = sum(numeros) / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return media, minimo, maximo

# Desempacotar retorno
temps = [22.5, 23.1, 22.8, 23.4]
media, minima, maxima = calcular_estatisticas(temps)
print(f"Média: {media:.1f}, Min: {minima}, Max: {maxima}")
# Média: 23.0, Min: 22.5, Max: 23.4
```

### Retornar Dicionário

```python
def analisar_amostra(especie, prof_m, temp_c):
    """Analisa uma amostra e retorna resultado"""
    
    valida = 20 <= temp_c <= 25 and prof_m < 10
    
    resultado = {
        "especie": especie,
        "profundidade_m": prof_m,
        "temperatura_c": temp_c,
        "valida": valida,
        "status": "✅ VÁLIDA" if valida else "❌ INVÁLIDA"
    }
    
    return resultado

# Usar
analise = analisar_amostra("Ulva lactuca", 5.2, 22.5)
print(analise["status"])  # ✅ VÁLIDA
```

---

## 🔍 Documentação (Docstrings)

Docstrings explicam o que a função faz.

```python
def processar_temperatura(celsius):
    """
    Converte temperatura de Celsius para Fahrenheit.
    
    Args:
        celsius (float): Temperatura em Celsius
    
    Returns:
        float: Temperatura em Fahrenheit
    
    Example:
        >>> processar_temperatura(0)
        32.0
        >>> processar_temperatura(100)
        212.0
    """
    return (celsius * 9/5) + 32

# Ver documentação
help(processar_temperatura)
# ou
print(processar_temperatura.__doc__)
```

---

## ⚙️ Exemplo: Sistema de Validação

```python
def validar_amostra(especie, profundidade, temperatura, salinidade):
    """
    Valida uma amostra de coleta.
    
    Returns:
        dict: Resultado da validação com status e mensagens
    """
    
    erros = []
    avisos = []
    
    # Validação de espécie
    especies_validas = ["Ulva", "Gracilaria", "Sargassum", "Laminaria"]
    if especie not in especies_validas:
        erros.append(f"Espécie '{especie}' não reconhecida")
    
    # Validação de profundidade
    if profundidade < 0:
        erros.append("Profundidade não pode ser negativa")
    elif profundidade > 100:
        avisos.append("Profundidade muito grande (>100m)")
    
    # Validação de temperatura
    if not (15 <= temperatura <= 30):
        erros.append(f"Temperatura {temperatura}°C fora do intervalo (15-30°C)")
    if temperatura < 20 or temperatura > 25:
        avisos.append("Temperatura não ideal (ideal: 20-25°C)")
    
    # Validação de salinidade
    if not (30 <= salinidade <= 40):
        erros.append(f"Salinidade {salinidade} PSU fora do intervalo (30-40)")
    
    # Resultado
    valida = len(erros) == 0
    
    return {
        "valida": valida,
        "status": "✅ VÁLIDA" if valida else "❌ INVÁLIDA",
        "erros": erros,
        "avisos": avisos
    }

# Teste
resultado = validar_amostra("Ulva", 5.2, 22.5, 35.0)
print(resultado["status"])      # ✅ VÁLIDA
print(resultado["erros"])       # []

resultado2 = validar_amostra("Alga desconhecida", -5, 35, 50)
print(resultado2["status"])     # ❌ INVÁLIDA
print(resultado2["erros"])      # Lista de erros
```

---

## 🔄 Escopo de Variáveis

Onde uma variável pode ser usada.

```python
# Variável global
mensagem_global = "LABFICOL"

def mostrar_mensagem():
    # Pode acessar global
    print(mensagem_global)
    
    # Variável local
    mensagem_local = "Oceanografia"
    print(mensagem_local)

mostrar_mensagem()
# Printa:
# LABFICOL
# Oceanografia

print(mensagem_global)  # ✅ Funciona
print(mensagem_local)   # ❌ ERRO - não existe fora da função
```

### Modificar Global

```python
contador = 0

def incrementar():
    global contador  # Autorizar modificação
    contador += 1

incrementar()
print(contador)  # 1
```

---

## 📚 Módulos (Reutilizar Código)

Módulos são arquivos Python com código reutilizável.

### Criar um Módulo

Crie arquivo `oceanografia.py`:

```python
"""
Módulo com funções oceanográficas
"""

def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit"""
    return (celsius * 9/5) + 32

def calcular_densidade_agua(salinidade, temperatura):
    """Calcula densidade aproximada da água"""
    # Fórmula simplificada
    densidade = 1000 + (salinidade - 35) * 0.78 - (temperatura - 15) * 0.2
    return densidade

def validar_coleta(temperatura, profundidade):
    """Verifica se coleta foi válida"""
    return 20 <= temperatura <= 25 and profundidade < 50
```

### Usar o Módulo

Crie arquivo `usar_modulo.py`:

```python
# Importar tudo
import oceanografia

# Usar funções
temp_f = oceanografia.celsius_para_fahrenheit(22.5)
print(f"22.5°C = {temp_f:.1f}°F")

# Importar funções específicas
from oceanografia import celsius_para_fahrenheit, calcular_densidade_agua

temp_f = celsius_para_fahrenheit(25)
densidade = calcular_densidade_agua(35.0, 22.5)
print(f"Densidade: {densidade:.2f} kg/m³")

# Importar com apelido
from oceanografia import validar_coleta as validar

if validar(22.5, 5.2):
    print("✅ Coleta válida!")
```

---

## 📦 Bibliotecas Padrão Úteis

### math (Matemática)

```python
import math

print(math.pi)              # 3.14159...
print(math.sqrt(16))        # 4.0
print(math.ceil(5.2))       # 6 (arredonda para cima)
print(math.floor(5.8))      # 5 (arredonda para baixo)
print(math.sin(math.pi/2))  # 1.0
```

### datetime (Data e Hora)

```python
from datetime import datetime, timedelta

agora = datetime.now()
print(agora)  # 2025-01-06 14:30:45.123456

# Formatar
print(agora.strftime("%d/%m/%Y"))  # 06/01/2025

# Adicionar dias
amanha = agora + timedelta(days=1)
print(amanha)
```

### random (Números Aleatórios)

```python
import random

# Número aleatório
print(random.random())  # 0.123456... (0 a 1)

# Inteiro aleatório
print(random.randint(1, 10))  # Número de 1 a 10

# Escolher da lista
especies = ["Ulva", "Gracilaria", "Sargassum"]
escolhida = random.choice(especies)
print(escolhida)  # Aleatória

# Embaralhar
random.shuffle(especies)
print(especies)  # Embaralhada
```

---

## 🎯 Exemplo Completo: Processador de Dados

```python
"""
Processador de dados de coleta oceanográfica
"""

def carregar_dados():
    """Simula carregamento de dados"""
    return [
        {"especie": "Ulva", "prof_m": 5.2, "temp_c": 22.5, "sal_psu": 35.0},
        {"especie": "Gracilaria", "prof_m": 7.8, "temp_c": 23.1, "sal_psu": 34.8},
        {"especie": "Sargassum", "prof_m": 3.1, "temp_c": 22.8, "sal_psu": 35.1},
    ]

def validar_dados(amostras):
    """Valida todas as amostras"""
    validas = 0
    invalidas = 0
    
    for amostra in amostras:
        if 20 <= amostra["temp_c"] <= 25 and amostra["prof_m"] < 10:
            validas += 1
        else:
            invalidas += 1
    
    return validas, invalidas

def calcular_medias(amostras):
    """Calcula médias dos parâmetros"""
    temps = [a["temp_c"] for a in amostras]
    profs = [a["prof_m"] for a in amostras]
    sals = [a["sal_psu"] for a in amostras]
    
    return {
        "temp_media_c": sum(temps) / len(temps),
        "prof_media_m": sum(profs) / len(profs),
        "sal_media_psu": sum(sals) / len(sals)
    }

def gerar_relatorio(amostras):
    """Gera relatório completo"""
    print("=" * 60)
    print("🌊 RELATÓRIO DE COLETA - LABFICOL")
    print("=" * 60)
    
    # Total de amostras
    print(f"\n📊 Total de amostras: {len(amostras)}")
    
    # Validação
    validas, invalidas = validar_dados(amostras)
    print(f"✅ Válidas: {validas}")
    print(f"❌ Inválidas: {invalidas}")
    
    # Médias
    medias = calcular_medias(amostras)
    print(f"\n📈 Médias:")
    print(f"   Temperatura: {medias['temp_media_c']:.1f}°C")
    print(f"   Profundidade: {medias['prof_media_m']:.1f}m")
    print(f"   Salinidade: {medias['sal_media_psu']:.2f} PSU")
    
    # Espécies
    especies = [a["especie"] for a in amostras]
    print(f"\n🌿 Espécies coletadas: {', '.join(set(especies))}")
    
    print("\n" + "=" * 60)

# Executar
if __name__ == "__main__":
    dados = carregar_dados()
    gerar_relatorio(dados)
```

Execute:
```powershell
python processador_dados.py
```

---

## 🎓 Boas Práticas

✅ **Faça:**
- Use nomes descritivos para funções
- Escreva docstrings
- Mantenha funções simples (uma coisa por função)
- Use parâmetros em vez de variáveis globais

❌ **Evite:**
- Funções muito longas (>20 linhas)
- Variáveis globais
- Funções sem documentação
- Modificar parâmetros sem aviso

---

## 🎓 Checklist desta Lição

- [ ] Consigo definir uma função
- [ ] Entendo parâmetros e retornos
- [ ] Sei usar docstrings
- [ ] Consigo criar módulos
- [ ] Entendo escopo de variáveis
- [ ] Testei pelo menos 3 exemplos completos

Se marcou tudo, você completou **Python Essencial**! 🎉

---

## 📝 Resumo de Conceitos

| Conceito | Descrição |
|----------|-----------|
| **Função** | Bloco de código reutilizável |
| **Parâmetro** | Dados que função recebe |
| **Return** | Valor que função retorna |
| **Docstring** | Documentação da função |
| **Escopo** | Onde uma variável existe |
| **Módulo** | Arquivo com funções reutilizáveis |

---

## ➡️ Próximos Passos

Parabéns! Você completou **Python Essencial**! 🚀

**Próximos módulos:**
1. 📚 **Análise Geoespacial** (GeoPandas, Folium)
2. 🗺️ **Visualização Web** (JavaScript, HTML)
3. 📊 **Casos Práticos** (Oceanografia real)

---

**Você agora é um programador Python iniciante!** 🐍 Vamos para análises geoespaciais? 🗺️
