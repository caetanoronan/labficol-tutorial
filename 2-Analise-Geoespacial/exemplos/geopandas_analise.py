"""
GeoPandas - Análise Espacial - LABFICOL
========================================

Exemplo prático: Análise espacial com GeoPandas
Cálculo de distâncias, buffers e operações geométricas

Autor: LABFICOL/UFSC

Instalar: pip install geopandas matplotlib
"""

import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

print("="*70)
print("🌍 ANÁLISE ESPACIAL COM GEOPANDAS")
print("="*70)

# Dados de coleta
dados = {
    'id': [1, 2, 3, 4, 5],
    'praia': ['Ingleses', 'Barra da Lagoa', 'Armação', 'Garopaba', 'Laguna'],
    'lat': [-27.4374, -27.5750, -27.7500, -28.0200, -28.4833],
    'lon': [-48.3923, -48.4200, -48.5100, -48.6200, -48.7833],
    'especie': ['Ulva lactuca', 'Gracilaria', 'Sargassum', 'Laminaria', 'Ulva lactuca'],
    'biomassa_g': [245.3, 310.2, 275.4, 425.8, 295.7]
}

# Criar geometrias Point
geometria = [Point(lon, lat) for lon, lat in zip(dados['lon'], dados['lat'])]

# Criar GeoDataFrame
gdf = gpd.GeoDataFrame(dados, geometry=geometria, crs='EPSG:4326')

print(f"\n✅ GeoDataFrame criado com {len(gdf)} pontos")
print("\n" + str(gdf))

# ====================
# ANÁLISE 1: DISTÂNCIAS
# ====================

print("\n" + "="*70)
print("📏 ANÁLISE DE DISTÂNCIAS")
print("="*70)

# Calcular distância do primeiro ponto para todos os outros
ponto_referencia = gdf.iloc[0].geometry
praia_ref = gdf.iloc[0]['praia']

print(f"\n🎯 Referência: {praia_ref}")
print("-"*70)

for idx, row in gdf.iterrows():
    if idx == 0:
        continue
    
    # Distância em graus
    distancia_graus = ponto_referencia.distance(row.geometry)
    
    # Converter para km (1 grau ≈ 111 km)
    distancia_km = distancia_graus * 111
    
    print(f"{row['praia']}: {distancia_km:.2f} km")

# ====================
# ANÁLISE 2: BUFFERS
# ====================

print("\n" + "="*70)
print("🛡️ CRIAÇÃO DE BUFFERS (ZONAS DE PROTEÇÃO)")
print("="*70)

# Criar buffer de 10km (≈0.09 graus) ao redor de cada ponto
buffer_raio = 0.09  # ~10km

gdf['buffer'] = gdf.geometry.buffer(buffer_raio)

# Calcular área dos buffers (aproximada)
area_buffer = 3.14159 * (10 ** 2)  # πr² para 10km

print(f"\n📊 Buffer de ~10km criado ao redor de cada ponto")
print(f"   Área aproximada por buffer: {area_buffer:.2f} km²")
print(f"   Área total protegida: {area_buffer * len(gdf):.2f} km²")

# ====================
# ANÁLISE 3: HOTSPOTS
# ====================

print("\n" + "="*70)
print("🔥 IDENTIFICAÇÃO DE HOTSPOTS (CLUSTERING)")
print("="*70)

# Definir threshold de proximidade (20km ≈ 0.18 graus)
threshold = 0.18

clusters = []
for idx1, row1 in gdf.iterrows():
    cluster = [row1['praia']]
    for idx2, row2 in gdf.iterrows():
        if idx1 != idx2:
            dist = row1.geometry.distance(row2.geometry)
            if dist < threshold:
                cluster.append(row2['praia'])
    
    if len(cluster) > 1:
        cluster_str = ', '.join(sorted(set(cluster)))
        if cluster_str not in [c[1] for c in clusters]:
            clusters.append((len(cluster), cluster_str))

if clusters:
    print(f"\n✅ {len(clusters)} cluster(s) identificado(s):")
    for i, (tamanho, praias) in enumerate(sorted(clusters, reverse=True), 1):
        print(f"\n   Cluster {i}: {tamanho} pontos")
        print(f"   Praias: {praias}")
else:
    print("\n⚠️ Nenhum cluster identificado com threshold de 20km")

# ====================
# ANÁLISE 4: ESTATÍSTICAS
# ====================

print("\n" + "="*70)
print("📊 ESTATÍSTICAS ESPACIAIS")
print("="*70)

# Centro geométrico (centroide)
centro = gdf.geometry.unary_union.centroid

print(f"\n🎯 Centro geográfico das coletas:")
print(f"   Latitude: {centro.y:.4f}")
print(f"   Longitude: {centro.x:.4f}")

# Extensão geográfica (bounding box)
bounds = gdf.total_bounds  # [minx, miny, maxx, maxy]

print(f"\n📐 Extensão geográfica:")
print(f"   Lat: {bounds[1]:.4f} até {bounds[3]:.4f}")
print(f"   Lon: {bounds[0]:.4f} até {bounds[2]:.4f}")

# Amplitude
lat_range = (bounds[3] - bounds[1]) * 111  # km
lon_range = (bounds[2] - bounds[0]) * 111  # km

print(f"\n📏 Amplitude:")
print(f"   Norte-Sul: {lat_range:.2f} km")
print(f"   Leste-Oeste: {lon_range:.2f} km")

# ====================
# VISUALIZAÇÃO
# ====================

print("\n" + "="*70)
print("🎨 GERANDO VISUALIZAÇÃO")
print("="*70)

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Mapa 1: Pontos coloridos por espécie
cores_especies = {
    'Ulva lactuca': 'green',
    'Gracilaria': 'red',
    'Sargassum': 'blue',
    'Laminaria': 'purple'
}

ax1 = axes[0]
for especie in gdf['especie'].unique():
    dados_especie = gdf[gdf['especie'] == especie]
    dados_especie.plot(ax=ax1, color=cores_especies[especie], 
                       markersize=100, label=especie, alpha=0.6)

ax1.set_title('Distribuição por Espécie', fontsize=14, fontweight='bold')
ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Mapa 2: Pontos com buffers
ax2 = axes[1]
gdf.plot(ax=ax2, color='red', markersize=50, label='Coletas', zorder=2)

# Adicionar buffers
for idx, row in gdf.iterrows():
    buffer_geom = Point(row.geometry.x, row.geometry.y).buffer(buffer_raio)
    gpd.GeoSeries([buffer_geom]).plot(ax=ax2, color='blue', alpha=0.2, edgecolor='blue')

ax2.set_title('Zonas de Proteção (Buffer 10km)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Longitude')
ax2.set_ylabel('Latitude')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('analise_espacial.png', dpi=300, bbox_inches='tight')

print("\n✅ Gráfico salvo: analise_espacial.png")
print("\n" + "="*70)
print("🎉 ANÁLISE CONCLUÍDA!")
print("="*70)

plt.show()
