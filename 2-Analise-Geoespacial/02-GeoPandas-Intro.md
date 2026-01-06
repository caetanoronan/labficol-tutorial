# 🐼 GeoPandas - Análise Geoespacial com Python

## O que é GeoPandas?

**GeoPandas** = Pandas + Geografia

```
Pandas              GeoPandas
├─ DataFrames       ├─ GeoDataFrames (DataFrames + geometria)
├─ Tabelas          ├─ Tabelas + mapas
└─ Análise dados    └─ Análise espacial
```

**Por que usar:** Análise geoespacial com sintaxe familiar de Pandas!

---

## 🚀 Instalação

```powershell
pip install geopandas
pip install matplotlib  # Para gráficos
pip install folium      # Para mapas interativos (próxima lição)
```

---

## 📊 GeoDataFrame - A Base

### Criar GeoDataFrame Simples

```python
import geopandas as gpd
from shapely.geometry import Point

# Dados de coleta
dados = {
    'nome': ['Ingleses Norte', 'Ingleses Sul', 'Barra da Lagoa'],
    'especie': ['Ulva lactuca', 'Gracilaria', 'Sargassum'],
    'profundidade_m': [5.2, 7.8, 3.1],
    'temperatura_c': [22.5, 23.1, 22.8]
}

# Criar pontos (geometria)
geometrias = [
    Point(-48.3923, -27.4374),  # Ingleses Norte
    Point(-48.3950, -27.4450),  # Ingleses Sul
    Point(-48.4200, -27.5750)   # Barra da Lagoa
]

# Criar GeoDataFrame
gdf = gpd.GeoDataFrame(dados, geometry=geometrias, crs="EPSG:4326")

print(gdf)
```

Resultado:
```
              nome       especie  profundidade_m  temperatura_c                    geometry
0   Ingleses Norte  Ulva lactuca             5.2           22.5  POINT (-48.3923 -27.4374)
1    Ingleses Sul    Gracilaria             7.8           23.1  POINT (-48.3950 -27.4450)
2  Barra da Lagoa     Sargassum             3.1           22.8  POINT (-48.4200 -27.5750)
```

### O que é CRS?

**CRS (Coordinate Reference System)** = sistema de coordenadas.

```
EPSG:4326  → WGS84 (GPS padrão - graus decimais)
EPSG:3857  → Web Mercator (Google Maps, Leaflet)
EPSG:31982 → SIRGAS 2000 / UTM 22S (Brasil Sul)
```

**Sempre use EPSG:4326** para dados geográficos básicos!

---

## 📥 Carregar Dados Geoespaciais

### De GeoJSON

```python
import geopandas as gpd

# Carregar GeoJSON
gdf = gpd.read_file("coletas_labficol.geojson")

# Informações
print(gdf.info())
print(gdf.head())

# Ver CRS
print(gdf.crs)
```

### De Shapefile

```python
# Shapefile (formato antigo mas comum)
gdf = gpd.read_file("municipios_sc.shp")
```

### De CSV com Coordenadas

```python
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Carregar CSV
df = pd.read_csv("coletas.csv")
# Colunas: nome, latitude, longitude, especie

# Converter para GeoDataFrame
geometry = [Point(lon, lat) for lon, lat in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
```

---

## 🗺️ Visualizar Dados

### Plot Simples

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Criar dados
gdf = gpd.read_file("coletas_labficol.geojson")

# Plot básico
gdf.plot(figsize=(10, 6), marker='o', color='blue', markersize=50)
plt.title("Estações de Coleta - LABFICOL")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()
```

### Plot com Cores por Categoria

```python
# Colorir por espécie
gdf.plot(column='especie', 
         figsize=(10, 6), 
         legend=True,
         markersize=100,
         cmap='Set1')  # Esquema de cores
plt.title("Distribuição de Espécies")
plt.show()
```

### Plot com Tamanho Variável

```python
# Tamanho proporcional à profundidade
gdf.plot(column='profundidade_m',
         figsize=(10, 6),
         legend=True,
         markersize=gdf['profundidade_m'] * 20,  # Multiplicar para visualizar
         cmap='YlOrRd')  # Amarelo a Vermelho
plt.title("Profundidade das Coletas")
plt.show()
```

---

## 🔧 Operações Básicas

### Filtrar Dados

```python
# Filtrar por espécie
ulvas = gdf[gdf['especie'] == 'Ulva lactuca']
print(f"Total de Ulva lactuca: {len(ulvas)}")

# Filtrar por profundidade
rasas = gdf[gdf['profundidade_m'] < 5]
print(f"Coletas rasas (<5m): {len(rasas)}")

# Múltiplas condições
validas = gdf[(gdf['temperatura_c'] >= 20) & 
              (gdf['temperatura_c'] <= 25) & 
              (gdf['profundidade_m'] < 10)]
```

### Adicionar Coluna

```python
# Classificar profundidade
def classificar_profundidade(prof):
    if prof < 5:
        return "Rasa"
    elif prof < 20:
        return "Intermediária"
    else:
        return "Profunda"

gdf['classificacao'] = gdf['profundidade_m'].apply(classificar_profundidade)
```

---

## 📐 Operações Geométricas

### Calcular Distâncias

```python
from shapely.geometry import Point

# Ponto de referência (LABFICOL - UFSC)
labficol = Point(-48.5495, -27.5969)

# Calcular distância de cada coleta ao LABFICOL
# Nota: distância em graus (aproximação!)
gdf['distancia_graus'] = gdf.geometry.distance(labficol)

# Converter para km (1 grau ≈ 111 km)
gdf['distancia_km'] = gdf['distancia_graus'] * 111

print(gdf[['nome', 'distancia_km']])
```

### Criar Buffer (Área ao Redor)

```python
# Criar buffer de 5km ao redor de cada ponto
# Primeiro converter para sistema métrico
gdf_utm = gdf.to_crs("EPSG:31982")  # UTM para Santa Catarina

# Buffer de 5000 metros (5km)
gdf_utm['buffer_5km'] = gdf_utm.geometry.buffer(5000)

# Plotar
fig, ax = plt.subplots(figsize=(10, 6))
gdf_utm.plot(ax=ax, color='red', markersize=50)
gdf_utm['buffer_5km'].plot(ax=ax, alpha=0.3, color='blue')
plt.title("Áreas de Influência (5km)")
plt.show()
```

### Verificar se Ponto está Dentro de Polígono

```python
from shapely.geometry import Polygon

# Criar área de estudo (polígono)
area_estudo = Polygon([
    (-48.6, -27.4),
    (-48.3, -27.4),
    (-48.3, -27.7),
    (-48.6, -27.7)
])

# Verificar quais pontos estão dentro
gdf['dentro_area'] = gdf.geometry.within(area_estudo)

# Filtrar
dentro = gdf[gdf['dentro_area']]
print(f"Coletas dentro da área: {len(dentro)}")
```

---

## 🎯 Análise Espacial

### Encontrar Vizinhos Mais Próximos

```python
import numpy as np

def encontrar_mais_proximo(gdf, idx):
    """Encontra ponto mais próximo a um dado índice"""
    ponto = gdf.loc[idx, 'geometry']
    
    # Calcular distâncias
    distancias = gdf.geometry.distance(ponto)
    
    # Remover próprio ponto
    distancias[idx] = np.inf
    
    # Encontrar mínimo
    idx_proximo = distancias.idxmin()
    dist_km = distancias[idx_proximo] * 111
    
    return gdf.loc[idx_proximo, 'nome'], dist_km

# Testar
nome, dist = encontrar_mais_proximo(gdf, 0)
print(f"Ponto mais próximo: {nome} ({dist:.2f} km)")
```

### Agrupar por Região

```python
# Dividir em regiões por latitude
gdf['regiao'] = pd.cut(gdf.geometry.y, 
                       bins=3, 
                       labels=['Norte', 'Centro', 'Sul'])

# Estatísticas por região
resumo = gdf.groupby('regiao').agg({
    'profundidade_m': 'mean',
    'temperatura_c': 'mean',
    'especie': 'count'
})
resumo.columns = ['Prof. Média (m)', 'Temp. Média (°C)', 'Num. Coletas']
print(resumo)
```

---

## 💾 Salvar Dados

### Para GeoJSON

```python
# Salvar como GeoJSON
gdf.to_file("resultado_analise.geojson", driver="GeoJSON")
```

### Para Shapefile

```python
# Salvar como Shapefile
gdf.to_file("resultado_analise.shp")
```

### Para CSV (sem geometria)

```python
# Adicionar colunas de coordenadas
gdf['longitude'] = gdf.geometry.x
gdf['latitude'] = gdf.geometry.y

# Salvar só os dados
gdf.drop(columns=['geometry']).to_csv("resultado.csv", index=False)
```

---

## 🌍 Exemplo Completo: Análise de Distribuição de Espécies

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point

# 1. CRIAR DADOS DE EXEMPLO (LABFICOL)
dados = {
    'id': range(1, 11),
    'local': [
        'Ingleses N', 'Ingleses S', 'Barra Lagoa', 'Laguna', 
        'Garopaba', 'Armação', 'Campeche', 'Pântano Sul',
        'Joaquina', 'Mole'
    ],
    'especie': [
        'Ulva lactuca', 'Gracilaria', 'Sargassum', 'Ulva lactuca',
        'Gracilaria', 'Ulva lactuca', 'Sargassum', 'Laminaria',
        'Ulva lactuca', 'Gracilaria'
    ],
    'profundidade_m': [5.2, 7.8, 3.1, 10.5, 6.0, 4.5, 8.2, 12.0, 5.5, 7.0],
    'temperatura_c': [22.5, 23.1, 22.8, 21.2, 22.0, 23.5, 22.9, 20.5, 23.0, 22.7],
    'longitude': [-48.39, -48.40, -48.42, -48.78, -48.62, -48.51, -48.48, -48.50, -48.44, -48.43],
    'latitude': [-27.44, -27.45, -27.58, -28.48, -28.02, -27.75, -27.67, -27.78, -27.63, -27.58]
}

df = pd.DataFrame(dados)

# 2. CRIAR GEODATAFRAME
geometry = [Point(lon, lat) for lon, lat in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

print("=" * 70)
print("🌊 ANÁLISE DE DISTRIBUIÇÃO DE MACROALGAS - LABFICOL/UFSC")
print("=" * 70)

# 3. ESTATÍSTICAS GERAIS
print(f"\n📊 Dados Gerais:")
print(f"   Total de coletas: {len(gdf)}")
print(f"   Espécies únicas: {gdf['especie'].nunique()}")
print(f"   Profundidade média: {gdf['profundidade_m'].mean():.1f}m")
print(f"   Temperatura média: {gdf['temperatura_c'].mean():.1f}°C")

# 4. ANÁLISE POR ESPÉCIE
print(f"\n🌿 Distribuição por Espécie:")
especies_count = gdf['especie'].value_counts()
for especie, count in especies_count.items():
    print(f"   {especie}: {count} coletas")

# 5. CALCULAR CENTROIDE (centro geográfico)
centroide = gdf.geometry.unary_union.centroid
print(f"\n📍 Centro Geográfico das Coletas:")
print(f"   Latitude: {centroide.y:.4f}°")
print(f"   Longitude: {centroide.x:.4f}°")

# 6. FILTRAR E ANALISAR
print(f"\n✓ Coletas Validadas (20-25°C, <10m):")
validas = gdf[(gdf['temperatura_c'] >= 20) & 
              (gdf['temperatura_c'] <= 25) & 
              (gdf['profundidade_m'] < 10)]
print(f"   {len(validas)}/{len(gdf)} coletas válidas ({len(validas)/len(gdf)*100:.0f}%)")

# 7. VISUALIZAÇÃO
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Subplot 1: Todas as coletas
gdf.plot(ax=axes[0], marker='o', color='blue', markersize=100, alpha=0.6)
axes[0].set_title("Todas as Estações de Coleta", fontsize=12)
axes[0].set_xlabel("Longitude")
axes[0].set_ylabel("Latitude")
axes[0].grid(True, alpha=0.3)

# Subplot 2: Por espécie
gdf.plot(ax=axes[1], column='especie', legend=True, 
         markersize=100, cmap='Set1', alpha=0.7)
axes[1].set_title("Distribuição por Espécie", fontsize=12)
axes[1].set_xlabel("Longitude")
axes[1].grid(True, alpha=0.3)

# Subplot 3: Por profundidade
gdf.plot(ax=axes[2], column='profundidade_m', legend=True,
         markersize=100, cmap='YlOrRd', alpha=0.7)
axes[2].set_title("Profundidade das Coletas", fontsize=12)
axes[2].set_xlabel("Longitude")
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("analise_distribuicao.png", dpi=300, bbox_inches='tight')
print(f"\n💾 Gráfico salvo: analise_distribuicao.png")

# 8. SALVAR RESULTADOS
gdf.to_file("coletas_analisadas.geojson", driver="GeoJSON")
print(f"💾 GeoJSON salvo: coletas_analisadas.geojson")

print("\n" + "=" * 70)
print("✅ Análise concluída com sucesso!")
```

---

## 🎓 Checklist desta Lição

- [ ] Entendo o que é GeoDataFrame
- [ ] Consigo criar GeoDataFrame de dados
- [ ] Sei carregar e salvar GeoJSON
- [ ] Posso fazer operações geométricas (buffer, distância)
- [ ] Consigo visualizar dados em mapas
- [ ] Realizei análise espacial completa

Se marcou tudo, você está pronto para **Mapas Interativos**! 🎉

---

## ➡️ Próximo Tópico

**👉 [03-Mapas-Folium.md](03-Mapas-Folium.md)**

Lá você aprenderá:
- Criar mapas interativos com Folium
- Adicionar marcadores e popups
- Camadas e clusters
- Publicar mapas online

---

## 📝 Resumo de Funções

| Função | Uso |
|--------|-----|
| `gpd.read_file()` | Carregar GeoJSON/Shapefile |
| `gdf.plot()` | Visualizar mapa |
| `gdf.to_file()` | Salvar arquivo geoespacial |
| `geometry.distance()` | Calcular distância |
| `geometry.buffer()` | Criar área ao redor |
| `geometry.within()` | Verificar se está dentro |

---

**Você domina GeoPandas básico!** 🐼 Próximo: Mapas interativos com Folium! 🗺️
