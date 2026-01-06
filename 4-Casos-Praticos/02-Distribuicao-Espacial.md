# 🗺️ Caso Prático 2: Distribuição Espacial de Macroalgas

## 🎯 Objetivo do Projeto

Criar um sistema de análise geoespacial para mapear e analisar a distribuição de macroalgas ao longo da costa, usando **GeoPandas + Folium + Shapely**.

**O que faremos:**
- Carregar dados com coordenadas geográficas
- Calcular densidade de ocorrências
- Identificar hotspots de biodiversidade
- Criar mapas interativos profissionais

---

## 🌍 Contexto da Pesquisa

Queremos mapear a distribuição de 4 espécies de macroalgas ao longo de 50km de costa:

- *Ulva lactuca* (alface-do-mar)
- *Gracilaria* (ágar-ágar)
- *Sargassum* (bodelha)
- *Laminaria* (kombu)

**Objetivo científico:** Identificar áreas prioritárias para conservação baseadas em densidade de espécies.

---

## 📍 Estrutura dos Dados Geoespaciais

Arquivo `coletas_geo.csv`:

```csv
id,data,lat,lon,especie,biomassa_g,prof_m
1,2025-01-15,-27.4374,-48.3923,Ulva lactuca,245.3,3.2
2,2025-01-15,-27.4450,-48.3950,Gracilaria,180.7,5.1
3,2025-01-20,-27.5750,-48.4200,Sargassum,310.2,4.5
4,2025-02-10,-28.4833,-48.7833,Laminaria,425.8,10.5
```

---

## 💻 Código Completo - Parte 1: Preparação Geoespacial

Crie `analise_distribuicao.py`:

```python
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import numpy as np

# ==========================
# 1. CRIAR DATASET GEOESPACIAL
# ==========================

print("=" * 60)
print("🗺️  ANÁLISE DE DISTRIBUIÇÃO ESPACIAL - LABFICOL")
print("=" * 60)

# Dados de coleta (coordenadas reais de SC)
dados = {
    'id': list(range(1, 31)),
    'data': ['2025-01-15'] * 10 + ['2025-02-20'] * 10 + ['2025-03-18'] * 10,
    'lat': [
        -27.4374, -27.4450, -27.4520, -27.4600, -27.5750,
        -27.5850, -27.5950, -27.7500, -27.7600, -27.7700,
        -28.0200, -28.0300, -28.0400, -28.4833, -28.5000,
        -28.5200, -26.2500, -26.2600, -26.2700, -26.9500,
        -27.4380, -27.4470, -27.4550, -27.5800, -27.5900,
        -27.6000, -27.7550, -28.0250, -28.4900, -26.9600
    ],
    'lon': [
        -48.3923, -48.3950, -48.4000, -48.4050, -48.4200,
        -48.4250, -48.4300, -48.5100, -48.5150, -48.5200,
        -48.6200, -48.6250, -48.6300, -48.7833, -48.7900,
        -48.8000, -48.6300, -48.6350, -48.6400, -48.8100,
        -48.3930, -48.3960, -48.4010, -48.4210, -48.4260,
        -48.4310, -48.5110, -48.6210, -48.7850, -48.8110
    ],
    'especie': [
        'Ulva lactuca', 'Gracilaria', 'Sargassum', 'Ulva lactuca', 'Gracilaria',
        'Sargassum', 'Laminaria', 'Ulva lactuca', 'Gracilaria', 'Sargassum',
        'Ulva lactuca', 'Gracilaria', 'Laminaria', 'Sargassum', 'Ulva lactuca',
        'Gracilaria', 'Ulva lactuca', 'Sargassum', 'Gracilaria', 'Laminaria',
        'Ulva lactuca', 'Ulva lactuca', 'Gracilaria', 'Sargassum', 'Ulva lactuca',
        'Gracilaria', 'Sargassum', 'Ulva lactuca', 'Gracilaria', 'Laminaria'
    ],
    'biomassa_g': np.random.uniform(150, 450, 30).round(1),
    'prof_m': np.random.uniform(2, 12, 30).round(1)
}

df = pd.DataFrame(dados)

# Converter para GeoDataFrame
geometry = [Point(lon, lat) for lon, lat in zip(df['lon'], df['lat'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

print(f"\n✅ Dataset carregado: {len(gdf)} pontos de coleta")
print(f"📍 Extensão geográfica:")
print(f"   Latitude: {gdf['lat'].min():.4f} até {gdf['lat'].max():.4f}")
print(f"   Longitude: {gdf['lon'].min():.4f} até {gdf['lon'].max():.4f}")
print(f"🌿 Espécies: {gdf['especie'].unique()}")

# ==========================
# 2. ANÁLISE ESPACIAL
# ==========================

print("\n" + "=" * 60)
print("📊 ANÁLISE DE DENSIDADE ESPACIAL")
print("=" * 60)

# Contar ocorrências por espécie
contagem_especies = gdf['especie'].value_counts()
print("\nDistribuição de espécies:")
for especie, count in contagem_especies.items():
    porcentagem = (count / len(gdf)) * 100
    print(f"  {especie}: {count} ({porcentagem:.1f}%)")

# ==========================
# 3. IDENTIFICAR HOTSPOTS
# ==========================

print("\n" + "=" * 60)
print("🔥 IDENTIFICAÇÃO DE HOTSPOTS")
print("=" * 60)

# Criar grid para análise de densidade
# Dividir área em células de 0.1° x 0.1° (~11km x 11km)

lat_min, lat_max = gdf['lat'].min(), gdf['lat'].max()
lon_min, lon_max = gdf['lon'].min(), gdf['lon'].max()

# Criar células do grid
resolucao = 0.5  # graus
lat_bins = np.arange(lat_min, lat_max + resolucao, resolucao)
lon_bins = np.arange(lon_min, lon_max + resolucao, resolucao)

# Adicionar célula do grid a cada ponto
gdf['lat_bin'] = pd.cut(gdf['lat'], bins=lat_bins, labels=False)
gdf['lon_bin'] = pd.cut(gdf['lon'], bins=lon_bins, labels=False)
gdf['celula'] = gdf['lat_bin'].astype(str) + '_' + gdf['lon_bin'].astype(str)

# Contar pontos por célula
densidade_celulas = gdf.groupby('celula').agg({
    'id': 'count',
    'especie': lambda x: x.nunique(),
    'lat': 'mean',
    'lon': 'mean'
}).rename(columns={'id': 'n_coletas', 'especie': 'n_especies'})

# Identificar hotspots (células com >3 espécies)
hotspots = densidade_celulas[densidade_celulas['n_especies'] >= 3].sort_values('n_especies', ascending=False)

print(f"\n🔥 {len(hotspots)} hotspots identificados!")
print("\nTop 3 áreas de maior biodiversidade:")
for idx, (celula, dados) in enumerate(hotspots.head(3).iterrows(), 1):
    print(f"\n  {idx}. Célula {celula}")
    print(f"     📍 Centro: ({dados['lat']:.4f}, {dados['lon']:.4f})")
    print(f"     🌿 {dados['n_especies']} espécies diferentes")
    print(f"     📊 {dados['n_coletas']} coletas realizadas")

# ==========================
# 4. ANÁLISE POR ESPÉCIE
# ==========================

print("\n" + "=" * 60)
print("🌿 ANÁLISE GEOGRÁFICA POR ESPÉCIE")
print("=" * 60)

for especie in gdf['especie'].unique():
    dados_especie = gdf[gdf['especie'] == especie]
    
    # Calcular centro geográfico
    centro_lat = dados_especie['lat'].mean()
    centro_lon = dados_especie['lon'].mean()
    
    # Calcular dispersão geográfica
    dispersao_lat = dados_especie['lat'].std()
    dispersao_lon = dados_especie['lon'].std()
    
    print(f"\n📍 {especie}")
    print(f"   Ocorrências: {len(dados_especie)}")
    print(f"   Centro: ({centro_lat:.4f}, {centro_lon:.4f})")
    print(f"   Dispersão: Lat={dispersao_lat:.4f}°, Lon={dispersao_lon:.4f}°")
    
    # Profundidade preferencial
    prof_media = dados_especie['prof_m'].mean()
    print(f"   Profundidade média: {prof_media:.1f}m")

# ==========================
# 5. DISTÂNCIAS E PROXIMIDADE
# ==========================

print("\n" + "=" * 60)
print("📏 ANÁLISE DE PROXIMIDADE")
print("=" * 60)

# Calcular distância entre pontos consecutivos
gdf_sorted = gdf.sort_values('id')
distancias = []

for i in range(len(gdf_sorted) - 1):
    p1 = gdf_sorted.iloc[i].geometry
    p2 = gdf_sorted.iloc[i + 1].geometry
    # Distância em graus (aproximação)
    dist = p1.distance(p2)
    # Converter para km (1° ≈ 111km)
    dist_km = dist * 111
    distancias.append(dist_km)

print(f"\nDistância média entre pontos: {np.mean(distancias):.2f} km")
print(f"Distância mínima: {np.min(distancias):.2f} km")
print(f"Distância máxima: {np.max(distancias):.2f} km")

# ==========================
# 6. BUFFER ZONES
# ==========================

print("\n" + "=" * 60)
print("🛡️ CRIAÇÃO DE ZONAS DE PROTEÇÃO")
print("=" * 60)

# Criar buffer de 5km (≈0.045°) ao redor dos hotspots
buffer_raio = 0.045  # ~5km

print(f"\nCriando buffers de ~5km ao redor dos {len(hotspots)} hotspots...")

# Área total de proteção sugerida
area_protegida_total = len(hotspots) * (np.pi * (5 ** 2))  # km²
print(f"📊 Área total sugerida para proteção: {area_protegida_total:.1f} km²")

print("\n" + "=" * 60)
print("✅ ANÁLISE ESPACIAL CONCLUÍDA")
print("=" * 60)
```

---

## 🗺️ Código Completo - Parte 2: Mapa Interativo

Adicione ao mesmo arquivo:

```python
# ==========================
# 7. CRIAR MAPA INTERATIVO
# ==========================

import folium
from folium.plugins import HeatMap, MarkerCluster

print("\n🗺️  Gerando mapa interativo...")

# Criar mapa base centrado em SC
centro_lat = gdf['lat'].mean()
centro_lon = gdf['lon'].mean()
mapa = folium.Map(location=[centro_lat, centro_lon], zoom_start=8, tiles='OpenStreetMap')

# Cores por espécie
cores_especies = {
    'Ulva lactuca': 'green',
    'Gracilaria': 'red',
    'Sargassum': 'blue',
    'Laminaria': 'purple'
}

# Ícones por espécie
icones_especies = {
    'Ulva lactuca': '🥬',
    'Gracilaria': '🌺',
    'Sargassum': '🌊',
    'Laminaria': '🍃'
}

# Criar grupos de camadas por espécie
grupos_especies = {especie: folium.FeatureGroup(name=especie) for especie in gdf['especie'].unique()}

# Adicionar marcadores
for idx, row in gdf.iterrows():
    popup_html = f"""
    <div style="font-family: Arial; min-width: 220px;">
        <h3 style="color: {cores_especies[row['especie']]}; margin: 0 0 10px 0;">
            {icones_especies[row['especie']]} {row['especie']}
        </h3>
        <hr style="margin: 10px 0; border: none; border-top: 2px solid #ddd;">
        <table style="width: 100%; font-size: 13px;">
            <tr><td><strong>ID:</strong></td><td>#{row['id']}</td></tr>
            <tr><td><strong>Data:</strong></td><td>{row['data']}</td></tr>
            <tr><td><strong>Latitude:</strong></td><td>{row['lat']:.4f}</td></tr>
            <tr><td><strong>Longitude:</strong></td><td>{row['lon']:.4f}</td></tr>
            <tr><td><strong>Biomassa:</strong></td><td>{row['biomassa_g']:.1f}g</td></tr>
            <tr><td><strong>Profundidade:</strong></td><td>{row['prof_m']:.1f}m</td></tr>
        </table>
    </div>
    """
    
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=8,
        popup=folium.Popup(popup_html, max_width=300),
        color=cores_especies[row['especie']],
        fill=True,
        fillColor=cores_especies[row['especie']],
        fillOpacity=0.7,
        weight=2
    ).add_to(grupos_especies[row['especie']])

# Adicionar grupos ao mapa
for grupo in grupos_especies.values():
    grupo.add_to(mapa)

# Adicionar hotspots
grupo_hotspots = folium.FeatureGroup(name='🔥 Hotspots de Biodiversidade')
for celula, dados in hotspots.iterrows():
    # Círculo de raio ~5km
    folium.Circle(
        location=[dados['lat'], dados['lon']],
        radius=5000,  # metros
        popup=f"<b>Hotspot</b><br>{dados['n_especies']} espécies<br>{dados['n_coletas']} coletas",
        color='orange',
        fill=True,
        fillColor='orange',
        fillOpacity=0.2,
        weight=3
    ).add_to(grupo_hotspots)
    
    # Marcador central
    folium.Marker(
        location=[dados['lat'], dados['lon']],
        popup=f"<b>🔥 HOTSPOT</b><br>{dados['n_especies']} espécies",
        icon=folium.Icon(color='orange', icon='fire', prefix='fa')
    ).add_to(grupo_hotspots)

grupo_hotspots.add_to(mapa)

# Adicionar mapa de calor (densidade)
dados_heatmap = [[row['lat'], row['lon']] for idx, row in gdf.iterrows()]
HeatMap(dados_heatmap, name='🌡️ Mapa de Calor', radius=25, blur=35, max_zoom=13).add_to(mapa)

# Adicionar controle de camadas
folium.LayerControl(collapsed=False).add_to(mapa)

# Adicionar legenda
legenda_html = '''
<div style="position: fixed; bottom: 50px; right: 50px; width: 250px; background-color: white; 
            border:2px solid grey; z-index:9999; padding: 15px; border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <h4 style="margin-top: 0; color: #2E86AB;">🗺️ Legenda</h4>
    <hr style="margin: 10px 0;">
    <p><span style="color: green;">⬤</span> Ulva lactuca</p>
    <p><span style="color: red;">⬤</span> Gracilaria</p>
    <p><span style="color: blue;">⬤</span> Sargassum</p>
    <p><span style="color: purple;">⬤</span> Laminaria</p>
    <hr style="margin: 10px 0;">
    <p><span style="color: orange;">🔥</span> Hotspot (≥3 espécies)</p>
    <p style="font-size: 11px; color: #666; margin-top: 15px;">
        <strong>Total:</strong> ''' + str(len(gdf)) + ''' coletas<br>
        <strong>Hotspots:</strong> ''' + str(len(hotspots)) + ''' áreas
    </p>
</div>
'''
mapa.get_root().html.add_child(folium.Element(legenda_html))

# Salvar mapa
mapa.save('distribuicao_espacial.html')
print("✅ Mapa interativo salvo: distribuicao_espacial.html")

print("\n" + "=" * 60)
print("🎉 PROJETO CONCLUÍDO COM SUCESSO!")
print("=" * 60)
print("\n📂 Arquivos gerados:")
print("   - distribuicao_espacial.html (abra no navegador)")
print("\n💡 Insights principais:")
print(f"   - {len(hotspots)} hotspots de biodiversidade identificados")
print(f"   - Área sugerida para proteção: {area_protegida_total:.1f} km²")
print(f"   - Espécie mais comum: {contagem_especies.index[0]} ({contagem_especies.iloc[0]} ocorrências)")
```

---

## 🎯 Execute o Projeto

```bash
python analise_distribuicao.py
```

Depois, abra no navegador:
```bash
distribuicao_espacial.html
```

---

## 📊 Resultados Esperados

### Console:
```
🗺️  ANÁLISE DE DISTRIBUIÇÃO ESPACIAL - LABFICOL
✅ Dataset carregado: 30 pontos de coleta
📍 Extensão geográfica:
   Latitude: -28.5200 até -26.2500
   Longitude: -48.8110 até -48.3923

🔥 3 hotspots identificados!
```

### Mapa Interativo:
- ✅ Marcadores coloridos por espécie
- ✅ Hotspots destacados com círculos
- ✅ Mapa de calor de densidade
- ✅ Controle de camadas
- ✅ Popups informativos

---

## 🔬 Interpretação Científica

### Hotspots Identificados

```
📍 Área 1: Florianópolis Norte (-27.44, -48.39)
   → 4 espécies | Alta diversidade
   → PRIORIDADE ALTA para conservação

📍 Área 2: Garopaba (-28.02, -48.62)
   → 3 espécies | Diversidade moderada
   → PRIORIDADE MÉDIA

📍 Área 3: Laguna (-28.48, -48.78)
   → 3 espécies | Zona produtiva
   → Potencial para aquicultura
```

### Recomendações de Gestão

1. **Criar Unidades de Conservação** nos 3 hotspots
2. **Buffers de 5km** = ~235 km² protegidos
3. **Monitoramento intensivo** nas zonas intermediárias

---

## 🎓 O que você aprendeu

- ✅ Análise espacial com GeoPandas
- ✅ Identificação de hotspots de biodiversidade
- ✅ Cálculo de densidades em grid
- ✅ Criação de buffers de proteção
- ✅ Mapas interativos com Folium
- ✅ Interpretação geográfica de dados biológicos

---

## 🚀 Desafio Extra

1. **Conectividade:** Calcule corredores ecológicos entre hotspots
2. **Interpolação:** Use Kriging para prever distribuição em áreas não amostradas
3. **Análise temporal:** Compare distribuição entre anos
4. **Exportar para QGIS:** Salve como Shapefile

---

## ➡️ Próximo Caso Prático

- **03-Dashboard-Web-Completo.md** (Sistema web integrado)

---

**Parabéns!** Você domina análise geoespacial aplicada! 🗺️🌿
