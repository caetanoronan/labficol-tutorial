# 📊 Estruturas de Dados em Python

## O que são Estruturas de Dados?

**Estrutura de dados** = forma de organizar múltiplos valores.

Analogia:
- Uma variável = uma caixa com um item
- Uma estrutura = uma caixa com vários itens organizados

---

## 📋 Listas (Arrays)

A estrutura mais usada em Python!

### Criar uma Lista

```python
# Lista vazia
lista_vazia = []

# Lista com valores
especies = ["Ulva", "Gracilaria", "Sargassum"]
temperaturas = [22.5, 23.1, 22.8, 23.4, 22.9]
dados_mistos = [1, "texto", 3.14, True, [1, 2, 3]]

# Usando list()
numeros = list(range(1, 6))  # [1, 2, 3, 4, 5]
```

### Acessar Elementos

```python
especies = ["Ulva", "Gracilaria", "Sargassum"]

# Índices começam em 0!
print(especies[0])   # "Ulva"
print(especies[1])   # "Gracilaria"
print(especies[2])   # "Sargassum"

# Índices negativos (do final para trás)
print(especies[-1])  # "Sargassum" (último)
print(especies[-2])  # "Gracilaria" (penúltimo)
```

### Modificar Lista

```python
especies = ["Ulva", "Gracilaria", "Sargassum"]

# Alterar elemento
especies[0] = "Ulva lactuca"

# Adicionar um elemento no final
especies.append("Laminaria")
print(especies)  # ["Ulva lactuca", "Gracilaria", "Sargassum", "Laminaria"]

# Inserir em posição específica
especies.insert(1, "Chondracanthus")
print(especies)  # ["Ulva lactuca", "Chondracanthus", ...]

# Remover elemento (por valor)
especies.remove("Sargassum")

# Remover elemento (por índice)
removida = especies.pop(0)  # Remove e retorna primeiro

# Remover tudo
especies.clear()
```

### Operações com Listas

```python
temperaturas = [22.5, 23.1, 22.8, 23.4, 22.9]

# Tamanho
print(len(temperaturas))  # 5

# Soma
print(sum(temperaturas))  # 114.7

# Máximo e mínimo
print(max(temperaturas))  # 23.4
print(min(temperaturas))  # 22.5

# Ordenar
ordenado = sorted(temperaturas)
print(ordenado)  # [22.5, 22.8, 22.9, 23.1, 23.4]

# Reverso
reverso = list(reversed(temperaturas))
print(reverso)  # [22.9, 23.4, 22.8, 23.1, 22.5]

# Verificar se contém
if 22.5 in temperaturas:
    print("✅ Encontrada")

# Contar ocorrências
amostras = ["Ulva", "Gracilaria", "Ulva", "Ulva", "Sargassum"]
print(amostras.count("Ulva"))  # 3

# Encontrar índice
print(amostras.index("Gracilaria"))  # 1
```

### Fatiar Lista (Slicing)

```python
especies = ["Ulva", "Gracilaria", "Sargassum", "Laminaria", "Chondracanthus"]

# [início:fim:passo] - fim é EXCLUSIVO!
print(especies[0:2])      # ["Ulva", "Gracilaria"]
print(especies[1:4])      # ["Gracilaria", "Sargassum", "Laminaria"]
print(especies[:3])       # ["Ulva", "Gracilaria", "Sargassum"] (começa do início)
print(especies[2:])       # ["Sargassum", "Laminaria", "Chondracanthus"] (até o fim)
print(especies[::2])      # ["Ulva", "Sargassum", "Chondracanthus"] (cada 2)
print(especies[::-1])     # Reverso! ["Chondracanthus", "Laminaria", ...]
```

### Juntar e Dividir Listas

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Juntar
combinada = lista1 + lista2
print(combinada)  # [1, 2, 3, 4, 5, 6]

# Repetir
repetida = [1, 2] * 3
print(repetida)  # [1, 2, 1, 2, 1, 2]

# Dividir (string para lista)
texto = "Ulva,Gracilaria,Sargassum"
especies = texto.split(",")
print(especies)  # ["Ulva", "Gracilaria", "Sargassum"]

# Juntar (lista para string)
resultado = " | ".join(especies)
print(resultado)  # "Ulva | Gracilaria | Sargassum"
```

---

## 🔑 Dicionários (Dicts)

Dados com rótulo/chave.

### Criar Dicionário

```python
# Dicionário vazio
vazio = {}

# Com dados
amostra = {
    "id": 1,
    "especie": "Ulva lactuca",
    "profundidade": 5.2,
    "temperatura": 22.5,
    "valida": True
}

# Usando dict()
dados = dict(nome="Caetano", profissao="Oceanógrafo")
```

### Acessar Valores

```python
amostra = {
    "especie": "Ulva lactuca",
    "profundidade": 5.2,
    "temperatura": 22.5
}

# Acessar por chave
print(amostra["especie"])      # "Ulva lactuca"
print(amostra["profundidade"]) # 5.2

# Usando .get() (mais seguro)
print(amostra.get("especie"))        # "Ulva lactuca"
print(amostra.get("salario", "N/A")) # "N/A" (não existe)
```

### Modificar Dicionário

```python
amostra = {"especie": "Ulva", "profundidade": 5.2}

# Adicionar chave
amostra["temperatura"] = 22.5

# Modificar existente
amostra["profundidade"] = 6.0

# Remover chave
del amostra["temperatura"]

# Remover e retornar
valor = amostra.pop("profundidade")  # Remove e retorna 6.0

# Limpar tudo
amostra.clear()
```

### Operações com Dicionários

```python
amostra = {
    "especie": "Ulva",
    "profundidade": 5.2,
    "temperatura": 22.5,
    "valida": True
}

# Tamanho
print(len(amostra))  # 4

# Chaves
print(amostra.keys())  # dict_keys(['especie', 'profundidade', ...])

# Valores
print(amostra.values())  # dict_values(['Ulva', 5.2, 22.5, True])

# Pares chave-valor
print(amostra.items())  # dict_items([('especie', 'Ulva'), ...])

# Verificar se chave existe
if "especie" in amostra:
    print("✅ Existe")

# Atualizar múltiplas chaves
amostra.update({"profundidade": 7.0, "salinidade": 35.0})
```

### Exemplo Prático: Registro de Amostra

```python
# Criar vários registros
amostras = [
    {"id": 1, "especie": "Ulva", "prof_m": 5.2, "temp_c": 22.5},
    {"id": 2, "especie": "Gracilaria", "prof_m": 7.8, "temp_c": 23.1},
    {"id": 3, "especie": "Sargassum", "prof_m": 3.1, "temp_c": 22.8}
]

# Acessar
print(amostras[0]["especie"])  # "Ulva"
print(amostras[1]["temp_c"])   # 23.1

# Iterar
for amostra in amostras:
    print(f"ID {amostra['id']}: {amostra['especie']} a {amostra['prof_m']}m")
```

---

## (Tuplas)

Listas imutáveis (não podem ser alteradas).

```python
# Tupla (com parênteses)
coordenadas = (27.5, -48.5)  # latitude, longitude

# Acessar
print(coordenadas[0])  # 27.5
print(coordenadas[1])  # -48.5

# Tuplas são imutáveis
coordenadas[0] = 28.0  # ❌ ERRO!

# Mas podem ser reatribuídas
coordenadas = (28.0, -48.5)  # ✅ OK

# Desempacotamento
lat, lon = coordenadas
print(f"Latitude: {lat}, Longitude: {lon}")

# Múltiplos retornos de função
def get_localizacao():
    return (27.5, -48.5, 15)  # lat, lon, profundidade

lat, lon, prof = get_localizacao()
```

**Quando usar:** Quando você quer garantir que dados não sejam alterados.

---

## ⚙️ Conjuntos (Sets)

Coleções sem duplicatas.

```python
# Criar conjunto
especies_unicas = {"Ulva", "Gracilaria", "Sargassum", "Ulva"}
print(especies_unicas)  # {'Ulva', 'Gracilaria', 'Sargassum'} - sem duplicata!

# Operações
especies_unicas.add("Laminaria")
especies_unicas.remove("Ulva")

# Interseção (elementos em comum)
grupo1 = {"Ulva", "Gracilaria", "Sargassum"}
grupo2 = {"Ulva", "Laminaria", "Codium"}
comuns = grupo1 & grupo2
print(comuns)  # {'Ulva'}

# União (tudo)
todos = grupo1 | grupo2
print(todos)  # {'Ulva', 'Gracilaria', 'Sargassum', 'Laminaria', 'Codium'}

# Diferença
so_em_grupo1 = grupo1 - grupo2
```

---

## 🔄 Loops com Estruturas

### For Loop com Listas

```python
especies = ["Ulva", "Gracilaria", "Sargassum"]

# Iterar valores
for especie in especies:
    print(f"Analisando: {especie}")

# Iterar com índice
for i, especie in enumerate(especies):
    print(f"{i}: {especie}")  # 0: Ulva, 1: Gracilaria, 2: Sargassum

# Iterar com range
for i in range(len(especies)):
    print(f"{i}: {especies[i]}")
```

### For Loop com Dicionários

```python
amostra = {"especie": "Ulva", "prof_m": 5.2, "temp_c": 22.5}

# Iterar chaves
for chave in amostra:
    print(chave)

# Iterar valores
for valor in amostra.values():
    print(valor)

# Iterar pares
for chave, valor in amostra.items():
    print(f"{chave}: {valor}")
```

### While Loop

```python
# Contar até 5
contador = 1
while contador <= 5:
    print(f"Contagem: {contador}")
    contador += 1

# Coletar dados até digitar "sair"
temperaturas = []
while True:
    temp = input("Digite temperatura (ou 'sair'): ")
    if temp.lower() == "sair":
        break
    temperaturas.append(float(temp))

print(f"Temperaturas coletadas: {temperaturas}")
```

---

## 💡 Compreensão de Listas (List Comprehension)

Forma elegante de criar listas:

```python
# Forma tradicional
quadrados = []
for i in range(1, 6):
    quadrados.append(i ** 2)
print(quadrados)  # [1, 4, 9, 16, 25]

# Compreensão de lista (mais Pythônica)
quadrados = [i ** 2 for i in range(1, 6)]
print(quadrados)  # [1, 4, 9, 16, 25]

# Com condição
pares = [i for i in range(1, 11) if i % 2 == 0]
print(pares)  # [2, 4, 6, 8, 10]

# Exemplo oceanográfico
temperaturas_raw = [22.5, 23.1, 22.8, 23.4, 22.9]
# Arredondar todas para 1 casa decimal
temperaturas_limpas = [round(t, 1) for t in temperaturas_raw]
print(temperaturas_limpas)  # [22.5, 23.1, 22.8, 23.4, 22.9]

# Com transformação
especias_maiusculas = [sp.upper() for sp in ["Ulva", "Gracilaria"]]
print(especias_maiusculas)  # ['ULVA', 'GRACILARIA']
```

---

## 🎯 Exemplo Prático Completo

Crie arquivo `analise_amostras.py`:

```python
"""
Sistema de análise de amostras de ficologia
"""

# Banco de dados de amostras
amostras = [
    {"id": 1, "especie": "Ulva lactuca", "prof_m": 5.2, "temp_c": 22.5, "sal_psu": 35.0},
    {"id": 2, "especie": "Gracilaria", "prof_m": 7.8, "temp_c": 23.1, "sal_psu": 34.8},
    {"id": 3, "especie": "Sargassum", "prof_m": 3.1, "temp_c": 22.8, "sal_psu": 35.1},
    {"id": 4, "especie": "Ulva lactuca", "prof_m": 6.5, "temp_c": 23.4, "sal_psu": 35.0},
]

print("=" * 60)
print("📊 ANÁLISE DE AMOSTRAS - LABFICOL")
print("=" * 60)

# 1. Listar todas as amostras
print("\n📋 AMOSTRAS COLETADAS:")
for amostra in amostras:
    print(f"  #{amostra['id']}: {amostra['especie']} "
          f"({amostra['prof_m']}m, {amostra['temp_c']}°C)")

# 2. Encontrar espécie mais frequente
especies = [a["especie"] for a in amostras]
especie_freq = max(set(especies), key=especies.count)
print(f"\n🌿 Espécie mais frequente: {especie_freq}")

# 3. Média de profundidade
profundidades = [a["prof_m"] for a in amostras]
prof_media = sum(profundidades) / len(profundidades)
print(f"📏 Profundidade média: {prof_media:.1f}m")

# 4. Temperatura extrema
temp_minima = min(amostras, key=lambda x: x["temp_c"])
temp_maxima = max(amostras, key=lambda x: x["temp_c"])
print(f"🌡️ Temperatura: {temp_minima['temp_c']}°C (min) a {temp_maxima['temp_c']}°C (max)")

# 5. Filtrar amostras válidas
validas = [a for a in amostras if 20 <= a["temp_c"] <= 25]
print(f"\n✅ Amostras válidas: {len(validas)}/{len(amostras)}")

# 6. Relatório final
print("\n" + "=" * 60)
print("✓ Análise concluída com sucesso!")
```

Execute:
```powershell
python analise_amostras.py
```

---

## 🎓 Checklist desta Lição

- [ ] Entendo listas e operações básicas
- [ ] Sei usar dicionários
- [ ] Consigo usar loops com estruturas
- [ ] Entendo fatiar listas (slicing)
- [ ] Testei pelo menos 3 exemplos completos
- [ ] Conheço list comprehension

Se marcou tudo, você está pronto para **Funções**! 🎉

---

## ➡️ Próximo Tópico

**👉 [03-Funcoes-Modulos.md](03-Funcoes-Modulos.md)**

Lá você aprenderá:
- Definir funções
- Parâmetros e retornos
- Escopo de variáveis
- Importar módulos

---

## 📝 Resumo de Operações

| Estrutura | Exemplo | Mutável? |
|-----------|---------|----------|
| Lista | `[1, 2, 3]` | ✅ Sim |
| Dicionário | `{"a": 1}` | ✅ Sim |
| Tupla | `(1, 2, 3)` | ❌ Não |
| Conjunto | `{1, 2, 3}` | ✅ Sim |

---

**Você está aprendendo rápido!** Próximo: Funções! 🚀
