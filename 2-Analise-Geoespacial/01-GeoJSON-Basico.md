# 🗺️ GeoJSON - Dados Geográficos Básicos

## O que é GeoJSON?

**GeoJSON** = formato de arquivo para armazenar dados geográficos em JSON.

### Por que GeoJSON é importante?

```
Excel/CSV           GeoJSON
├─ Dados tabulares  ├─ Dados + Geografia
├─ Sem localização  ├─ Coordenadas incluídas
└─ Sem mapas        └─ Pronto para mapear
```

**Usado em:** Leaflet, Folium, QGIS, ArcGIS Online, Google Maps

---

## 📍 Coordenadas Geográficas

Antes de GeoJSON, você precisa entender coordenadas!

### Latitude e Longitude

```
Latitude  (Y) → Norte/Sul → -90° a +90°
Longitude (X) → Leste/Oeste → -180° a +180°

Brasil:
├─ Latitude: -33° a +5° (negativo = Sul)
└─ Longitude: -73° a -34° (negativo = Oeste)

Santa Catarina (exemplo):
├─ Florianópolis: -27.5969°, -48.5495°
├─ Praia dos Ingleses: -27.4374°, -48.3923°
└─ Laguna: -28.4833°, -48.7833°
```

**Formato padrão:** `[longitude, latitude]` ⚠️ **Longitude vem PRIMEIRO!**

---

## 📐 Tipos de Geometria

### 1. Point (Ponto)

Um único local.

```json
{
  "type": "Point",
  "coordinates": [-48.5495, -27.5969]
}
```

**Uso:** Estação de coleta, localização de espécie

### 2. LineString (Linha)

Sequência de pontos conectados.

```json
{
  "type": "LineString",
  "coordinates": [
    [-48.5495, -27.5969],
    [-48.5500, -27.6000],
    [-48.5505, -27.6030]
  ]
}
```

**Uso:** Transecto, rota de barco, corrente marinha

### 3. Polygon (Polígono)

Área fechada.

```json
{
  "type": "Polygon",
  "coordinates": [
    [
      [-48.5495, -27.5969],
      [-48.5500, -27.5969],
      [-48.5500, -27.6000],
      [-48.5495, -27.6000],
      [-48.5495, -27.5969]
    ]
  ]
}
```

⚠️ **Primeiro e último ponto devem ser iguais!**

**Uso:** Área de proteção, zona de coleta, habitat de espécie

---

## 🎯 Estrutura Completa de GeoJSON

### Feature (Um objeto geográfico)

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [-48.5495, -27.5969]
  },
  "properties": {
    "nome": "Praia dos Ingleses",
    "especie": "Ulva lactuca",
    "profundidade_m": 5.2,
    "temperatura_c": 22.5,
    "data_coleta": "2025-01-06"
  }
}
```

**Partes:**
- `geometry`: Localização geográfica
- `properties`: Dados descritivos (qualquer coisa!)

### FeatureCollection (Múltiplos objetos)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-48.5495, -27.5969]
      },
      "properties": {
        "id": 1,
        "especie": "Ulva lactuca",
        "profundidade_m": 5.2
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-48.3923, -27.4374]
      },
      "properties": {
        "id": 2,
        "especie": "Gracilaria",
        "profundidade_m": 7.8
      }
    }
  ]
}
```

---

## 🐍 Criar GeoJSON com Python

### Instalar Bibliotecas

```powershell
pip install geojson
```

### Exemplo 1: Criar Ponto Simples

```python
import json

# Criar Feature (ponto)
ponto_coleta = {
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [-48.5495, -27.5969]  # [lon, lat]
    },
    "properties": {
        "nome": "Estação 1 - Praia dos Ingleses",
        "especie": "Ulva lactuca",
        "profundidade_m": 5.2,
        "temperatura_c": 22.5,
        "salinidade_psu": 35.0
    }
}

# Salvar em arquivo
with open("ponto_coleta.geojson", "w", encoding="utf-8") as f:
    json.dump(ponto_coleta, f, indent=2, ensure_ascii=False)

print("✅ GeoJSON criado: ponto_coleta.geojson")
```

### Exemplo 2: Múltiplas Estações de Coleta

```python
import json

# Dados de coleta (exemplo LABFICOL)
coletas = [
    {"nome": "Ingleses - Norte", "lon": -48.3923, "lat": -27.4374, 
     "especie": "Ulva lactuca", "prof": 5.2, "temp": 22.5},
    {"nome": "Ingleses - Sul", "lon": -48.3950, "lat": -27.4450, 
     "especie": "Gracilaria", "prof": 7.8, "temp": 23.1},
    {"nome": "Barra da Lagoa", "lon": -48.4200, "lat": -27.5750, 
     "especie": "Sargassum", "prof": 3.1, "temp": 22.8},
    {"nome": "Laguna", "lon": -48.7833, "lat": -28.4833, 
     "especie": "Laminaria", "prof": 10.5, "temp": 21.2}
]

# Criar FeatureCollection
features = []
for i, coleta in enumerate(coletas, start=1):
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [coleta["lon"], coleta["lat"]]
        },
        "properties": {
            "id": i,
            "nome": coleta["nome"],
            "especie": coleta["especie"],
            "profundidade_m": coleta["prof"],
            "temperatura_c": coleta["temp"]
        }
    }
    features.append(feature)

geojson_collection = {
    "type": "FeatureCollection",
    "features": features
}

# Salvar
with open("coletas_labficol.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson_collection, f, indent=2, ensure_ascii=False)

print(f"✅ GeoJSON criado com {len(features)} estações")
```

### Exemplo 3: Criar Polígono (Área de Estudo)

```python
import json

# Área de proteção marinha (exemplo)
area_protecao = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [[
            [-48.5495, -27.5969],  # Ponto 1
            [-48.5400, -27.5969],  # Ponto 2
            [-48.5400, -27.6100],  # Ponto 3
            [-48.5495, -27.6100],  # Ponto 4
            [-48.5495, -27.5969]   # Fecha (igual ao primeiro)
        ]]
    },
    "properties": {
        "nome": "Área de Proteção Marinha - Ingleses",
        "tipo": "Zona de coleta proibida",
        "area_km2": 12.5,
        "criacao": "2020-01-01"
    }
}

# Salvar
with open("area_protecao.geojson", "w", encoding="utf-8") as f:
    json.dump(area_protecao, f, indent=2, ensure_ascii=False)

print("✅ Área de proteção criada")
```

---

## 📊 Ler GeoJSON

### Exemplo: Carregar e Processar

```python
import json

# Carregar arquivo
with open("coletas_labficol.geojson", "r", encoding="utf-8") as f:
    dados = json.load(f)

# Acessar features
print(f"Total de pontos: {len(dados['features'])}")

# Iterar sobre features
for feature in dados["features"]:
    props = feature["properties"]
    coords = feature["geometry"]["coordinates"]
    
    print(f"\n📍 {props['nome']}")
    print(f"   Espécie: {props['especie']}")
    print(f"   Localização: {coords[1]:.4f}, {coords[0]:.4f}")
    print(f"   Profundidade: {props['profundidade_m']}m")

# Filtrar por espécie
ulvas = [f for f in dados["features"] 
         if f["properties"]["especie"] == "Ulva lactuca"]
print(f"\n🌿 Encontradas {len(ulvas)} amostras de Ulva lactuca")
```

---

## 🌐 Validar GeoJSON Online

Antes de usar em mapas, valide seu GeoJSON:

**Ferramentas:**
1. **geojson.io** - http://geojson.io
   - Cole seu GeoJSON
   - Visualize no mapa
   - Edite geometrias

2. **GeoJSONLint** - https://geojsonlint.com
   - Valida sintaxe
   - Mostra erros

---

## 🎯 Exemplo Prático: Sistema de Cadastro

Crie arquivo `cadastro_coletas.py`:

```python
import json
from datetime import datetime

def criar_ponto_coleta(nome, lon, lat, especie, profundidade, temperatura):
    """Cria um Feature GeoJSON para coleta"""
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [lon, lat]
        },
        "properties": {
            "nome": nome,
            "especie": especie,
            "profundidade_m": profundidade,
            "temperatura_c": temperatura,
            "data_cadastro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }

def adicionar_coleta(arquivo, nova_coleta):
    """Adiciona uma coleta ao GeoJSON existente"""
    try:
        # Tentar carregar arquivo existente
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        # Criar novo se não existe
        dados = {
            "type": "FeatureCollection",
            "features": []
        }
    
    # Adicionar nova coleta
    dados["features"].append(nova_coleta)
    
    # Salvar
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    
    return len(dados["features"])

def listar_coletas(arquivo):
    """Lista todas as coletas"""
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
        
        print("=" * 60)
        print("📊 COLETAS CADASTRADAS")
        print("=" * 60)
        
        for i, feature in enumerate(dados["features"], start=1):
            props = feature["properties"]
            coords = feature["geometry"]["coordinates"]
            
            print(f"\n{i}. {props['nome']}")
            print(f"   Espécie: {props['especie']}")
            print(f"   Coordenadas: {coords[1]:.4f}°, {coords[0]:.4f}°")
            print(f"   Profundidade: {props['profundidade_m']}m")
            print(f"   Temperatura: {props['temperatura_c']}°C")
        
        print("\n" + "=" * 60)
        print(f"Total: {len(dados['features'])} coletas")
        
    except FileNotFoundError:
        print("❌ Nenhum arquivo encontrado")

# Sistema interativo
def menu():
    arquivo = "minhas_coletas.geojson"
    
    while True:
        print("\n🌊 SISTEMA DE CADASTRO DE COLETAS")
        print("1 - Adicionar coleta")
        print("2 - Listar coletas")
        print("3 - Sair")
        
        opcao = input("\nEscolha: ")
        
        if opcao == "1":
            print("\n📝 Nova Coleta:")
            nome = input("Nome da estação: ")
            lat = float(input("Latitude: "))
            lon = float(input("Longitude: "))
            especie = input("Espécie: ")
            prof = float(input("Profundidade (m): "))
            temp = float(input("Temperatura (°C): "))
            
            coleta = criar_ponto_coleta(nome, lon, lat, especie, prof, temp)
            total = adicionar_coleta(arquivo, coleta)
            print(f"✅ Coleta adicionada! Total: {total}")
            
        elif opcao == "2":
            listar_coletas(arquivo)
            
        elif opcao == "3":
            print("👋 Até logo!")
            break

if __name__ == "__main__":
    menu()
```

Execute:
```powershell
python cadastro_coletas.py
```

---

## 🗺️ Visualizar no geojson.io

Depois de criar seus GeoJSON:

1. Abra: http://geojson.io
2. Arraste seu arquivo `.geojson`
3. Veja no mapa interativo! 🗺️

Ou cole o JSON diretamente no editor.

---

## 🎓 Boas Práticas

✅ **Faça:**
- Use `[longitude, latitude]` nesta ordem
- Feche polígonos (primeiro = último ponto)
- Valide GeoJSON antes de usar
- Use UTF-8 para acentos

❌ **Evite:**
- Coordenadas invertidas
- Polígonos não fechados
- Muitos decimais (4-6 é suficiente)
- Arquivos gigantes (use simplificação)

---

## 🎓 Checklist desta Lição

- [ ] Entendo o que é GeoJSON
- [ ] Sei a diferença entre Point, LineString e Polygon
- [ ] Consigo criar GeoJSON com Python
- [ ] Sei ler e processar arquivos GeoJSON
- [ ] Validei pelo menos um GeoJSON no geojson.io
- [ ] Criei um sistema de cadastro

Se marcou tudo, você está pronto para **GeoPandas**! 🎉

---

## ➡️ Próximo Tópico

**👉 [02-GeoPandas-Intro.md](02-GeoPandas-Intro.md)**

Lá você aprenderá:
- Usar GeoPandas para análise geoespacial
- Operações com geometrias
- Análise espacial
- Juntar dados geográficos

---

## 📝 Resumo de Tipos

| Tipo | Geometria | Uso |
|------|-----------|-----|
| **Point** | Um ponto | Estação de coleta |
| **LineString** | Linha | Transecto, rota |
| **Polygon** | Área | Zona de estudo |
| **MultiPoint** | Vários pontos | Cluster de coletas |

---

**Você agora domina GeoJSON básico!** 🗺️ Próximo: GeoPandas! 🐼
