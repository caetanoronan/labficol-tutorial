# 🗺️ Mapas Interativos com Folium

## O que é Folium?

**Folium** = biblioteca Python para criar mapas interativos web (Leaflet.js).

```
GeoPandas          Folium
├─ Análise         ├─ Visualização
├─ Mapas estáticos ├─ Mapas interativos
└─ PNG/PDF         └─ HTML (web)
```

**Use para:** Publicar resultados, apresentações, dashboards web

---

## 🚀 Instalação

```powershell
pip install folium
pip install geopandas  # Se ainda não tem
```

---

## 🎯 Criar Mapa Básico

### Exemplo Mínimo

```python
import folium

# Criar mapa centrado em Florianópolis
mapa = folium.Map(
    location=[-27.5969, -48.5495],  # [latitude, longitude]
    zoom_start=12,
    tiles='OpenStreetMap'
)

# Salvar como HTML
mapa.save("meu_primeiro_mapa.html")
print("✅ Mapa criado: meu_primeiro_mapa.html")
```

Abra o arquivo HTML no navegador! 🌐

### Tipos de Tiles (Camadas Base)

```python
import folium

# OpenStreetMap (padrão)
mapa1 = folium.Map(location=[-27.5969, -48.5495], zoom_start=12, 
                   tiles='OpenStreetMap')

# Imagem de satélite
mapa2 = folium.Map(location=[-27.5969, -48.5495], zoom_start=12,
                   tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                   attr='Esri')

# CartoDB Positron (minimalista)
mapa3 = folium.Map(location=[-27.5969, -48.5495], zoom_start=12,
                   tiles='CartoDB positron')

# Stamen Terrain (topografia)
mapa4 = folium.Map(location=[-27.5969, -48.5495], zoom_start=12,
                   tiles='Stamen Terrain')
```

---

## 📍 Adicionar Marcadores

### Marcador Simples

```python
import folium

# Criar mapa
mapa = folium.Map(location=[-27.5969, -48.5495], zoom_start=12)

# Adicionar marcador
folium.Marker(
    location=[-27.4374, -48.3923],
    popup="Praia dos Ingleses",
    tooltip="Clique para mais informações",
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(mapa)

mapa.save("mapa_com_marcador.html")
```

### Marcadores com Ícones Personalizados

```python
import folium

mapa = folium.Map(location=[-27.5969, -48.5495], zoom_start=11)

# Ícone padrão - vermelho
folium.Marker(
    [-27.4374, -48.3923],
    popup="Ulva lactuca - Profundidade: 5.2m",
    icon=folium.Icon(color='red', icon='leaf', prefix='fa')
).add_to(mapa)

# Ícone verde
folium.Marker(
    [-27.4450, -48.3950],
    popup="Gracilaria - Profundidade: 7.8m",
    icon=folium.Icon(color='green', icon='seedling', prefix='fa')
).add_to(mapa)

# Ícone azul
folium.Marker(
    [-27.5750, -48.4200],
    popup="Sargassum - Profundidade: 3.1m",
    icon=folium.Icon(color='blue', icon='water', prefix='fa')
).add_to(mapa)

mapa.save("mapa_especies.html")
```

**Cores disponíveis:** red, blue, green, purple, orange, darkred, lightred, beige, darkblue, darkgreen, cadetblue, darkpurple, white, pink, lightblue, lightgreen, gray, black, lightgray

---

## 🎨 Popups e Tooltips Avançados

### Popup com HTML

```python
import folium

mapa = folium.Map(location=[-27.5969, -48.5495], zoom_start=12)

# HTML formatado
html = """
<div style="font-family: Arial; width: 200px;">
    <h4 style="color: #2E86AB;">Estação 1 - Ingleses</h4>
    <hr>
    <b>Espécie:</b> <i>Ulva lactuca</i><br>
    <b>Profundidade:</b> 5.2m<br>
    <b>Temperatura:</b> 22.5°C<br>
    <b>Salinidade:</b> 35.0 PSU<br>
    <hr>
    <small>Data: 06/01/2025</small>
</div>
"""

folium.Marker(
    [-27.4374, -48.3923],
    popup=folium.Popup(html, max_width=300),
    tooltip="Clique para detalhes"
).add_to(mapa)

mapa.save("mapa_popup_html.html")
```

### Popup com Gráfico (Avançado)

```python
import folium
import base64
from io import BytesIO
import matplotlib.pyplot as plt

mapa = folium.Map(location=[-27.5969, -48.5495], zoom_start=12)

# Criar mini-gráfico
fig, ax = plt.subplots(figsize=(4, 2))
temps = [22.5, 23.1, 22.8, 23.4, 22.9]
ax.plot(temps, marker='o', color='#2E86AB')
ax.set_title("Temperatura (últimos 5 dias)")
ax.set_ylabel("°C")
ax.grid(True, alpha=0.3)

# Salvar como PNG em memória
buffer = BytesIO()
plt.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
buffer.seek(0)
image_base64 = base64.b64encode(buffer.read()).decode()
plt.close()

# Criar HTML com imagem
html = f"""
<div style="font-family: Arial;">
    <h4>Estação 1</h4>
    <img src="data:image/png;base64,{image_base64}" width="300">
</div>
"""

folium.Marker(
    [-27.4374, -48.3923],
    popup=folium.Popup(html, max_width=350)
).add_to(mapa)

mapa.save("mapa_popup_grafico.html")
```

---

## 🌐 Adicionar Múltiplos Pontos de GeoDataFrame

### Integração com GeoPandas

```python
import folium
import geopandas as gpd
from shapely.geometry import Point

# Criar dados
dados = {
    'nome': ['Ingleses N', 'Ingleses S', 'Barra Lagoa', 'Laguna'],
    'especie': ['Ulva lactuca', 'Gracilaria', 'Sargassum', 'Laminaria'],
    'profundidade_m': [5.2, 7.8, 3.1, 10.5],
    'temperatura_c': [22.5, 23.1, 22.8, 21.2]
}

geometry = [
    Point(-48.3923, -27.4374),
    Point(-48.3950, -27.4450),
    Point(-48.4200, -27.5750),
    Point(-48.7833, -28.4833)
]

gdf = gpd.GeoDataFrame(dados, geometry=geometry, crs="EPSG:4326")

# Criar mapa
mapa = folium.Map(location=[-27.8, -48.5], zoom_start=9)

# Adicionar cada ponto
for idx, row in gdf.iterrows():
    # Popup com informações
    popup_html = f"""
    <b>{row['nome']}</b><br>
    Espécie: <i>{row['especie']}</i><br>
    Profundidade: {row['profundidade_m']}m<br>
    Temperatura: {row['temperatura_c']}°C
    """
    
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=folium.Popup(popup_html, max_width=200),
        tooltip=row['nome'],
        icon=folium.Icon(color='blue', icon='leaf', prefix='fa')
    ).add_to(mapa)

mapa.save("mapa_geodataframe.html")
print("✅ Mapa criado com dados GeoPandas")
```

---

## 🎨 Marcadores com Cores Dinâmicas

### Colorir por Categoria

```python
import folium
import geopandas as gpd
from shapely.geometry import Point

# Dados
gdf = gpd.GeoDataFrame({
    'nome': ['Local 1', 'Local 2', 'Local 3', 'Local 4'],
    'especie': ['Ulva', 'Gracilaria', 'Ulva', 'Sargassum'],
    'geometry': [Point(-48.39, -27.44), Point(-48.40, -27.45),
                 Point(-48.42, -27.58), Point(-48.78, -28.48)]
}, crs="EPSG:4326")

# Mapa de cores por espécie
cores_especies = {
    'Ulva': 'green',
    'Gracilaria': 'red',
    'Sargassum': 'blue'
}

mapa = folium.Map(location=[-27.8, -48.5], zoom_start=9)

for idx, row in gdf.iterrows():
    cor = cores_especies.get(row['especie'], 'gray')
    
    folium.Marker(
        [row.geometry.y, row.geometry.x],
        popup=f"{row['nome']}: {row['especie']}",
        icon=folium.Icon(color=cor, icon='leaf', prefix='fa')
    ).add_to(mapa)

mapa.save("mapa_cores_especies.html")
```

---

## ⭕ CircleMarkers (Círculos)

### Tamanho Proporcional a Valor

```python
import folium
import geopandas as gpd
from shapely.geometry import Point

gdf = gpd.GeoDataFrame({
    'nome': ['Est. 1', 'Est. 2', 'Est. 3'],
    'profundidade_m': [5.2, 12.8, 3.1],
    'geometry': [Point(-48.39, -27.44), Point(-48.40, -27.45), Point(-48.42, -27.58)]
}, crs="EPSG:4326")

mapa = folium.Map(location=[-27.5, -48.4], zoom_start=11)

for idx, row in gdf.iterrows():
    # Raio proporcional à profundidade
    raio = row['profundidade_m'] * 2  # Multiplicar para visualizar melhor
    
    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=raio,
        popup=f"{row['nome']}<br>Prof: {row['profundidade_m']}m",
        color='blue',
        fill=True,
        fillColor='cyan',
        fillOpacity=0.6
    ).add_to(mapa)

mapa.save("mapa_circle_markers.html")
```

---

## 🗂️ Grupos e Camadas

### Controle de Camadas

```python
import folium

mapa = folium.Map(location=[-27.5969, -48.5495], zoom_start=11)

# Criar grupos de camadas
grupo_ulva = folium.FeatureGroup(name='Ulva lactuca')
grupo_gracilaria = folium.FeatureGroup(name='Gracilaria')

# Adicionar marcadores aos grupos
folium.Marker(
    [-27.4374, -48.3923],
    popup="Ulva - Local 1",
    icon=folium.Icon(color='green')
).add_to(grupo_ulva)

folium.Marker(
    [-27.4450, -48.3950],
    popup="Ulva - Local 2",
    icon=folium.Icon(color='green')
).add_to(grupo_ulva)

folium.Marker(
    [-27.5750, -48.4200],
    popup="Gracilaria - Local 1",
    icon=folium.Icon(color='red')
).add_to(grupo_gracilaria)

# Adicionar grupos ao mapa
grupo_ulva.add_to(mapa)
grupo_gracilaria.add_to(mapa)

# Adicionar controle de camadas
folium.LayerControl().add_to(mapa)

mapa.save("mapa_com_camadas.html")
```

---

## 📊 Heatmap (Mapa de Calor)

```python
import folium
from folium.plugins import HeatMap

# Dados: [latitude, longitude, intensidade]
dados_calor = [
    [-27.4374, -48.3923, 0.8],
    [-27.4450, -48.3950, 0.6],
    [-27.5750, -48.4200, 0.9],
    [-27.4400, -48.3930, 0.7],
    [-27.4500, -48.4000, 0.5]
]

mapa = folium.Map(location=[-27.5, -48.4], zoom_start=11)

# Adicionar heatmap
HeatMap(dados_calor, radius=20, blur=25, max_zoom=13).add_to(mapa)

mapa.save("mapa_heatmap.html")
```

---

## 🎯 Exemplo Completo: Dashboard de Coletas

```python
import folium
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from folium.plugins import MarkerCluster

# 1. PREPARAR DADOS
dados = {
    'id': range(1, 11),
    'local': ['Ingleses N', 'Ingleses S', 'Barra Lagoa', 'Laguna', 
              'Garopaba', 'Armação', 'Campeche', 'Pântano Sul',
              'Joaquina', 'Mole'],
    'especie': ['Ulva lactuca', 'Gracilaria', 'Sargassum', 'Ulva lactuca',
                'Gracilaria', 'Ulva lactuca', 'Sargassum', 'Laminaria',
                'Ulva lactuca', 'Gracilaria'],
    'profundidade_m': [5.2, 7.8, 3.1, 10.5, 6.0, 4.5, 8.2, 12.0, 5.5, 7.0],
    'temperatura_c': [22.5, 23.1, 22.8, 21.2, 22.0, 23.5, 22.9, 20.5, 23.0, 22.7],
    'longitude': [-48.39, -48.40, -48.42, -48.78, -48.62, -48.51, -48.48, -48.50, -48.44, -48.43],
    'latitude': [-27.44, -27.45, -27.58, -28.48, -28.02, -27.75, -27.67, -27.78, -27.63, -27.58]
}

df = pd.DataFrame(dados)
geometry = [Point(lon, lat) for lon, lat in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# 2. CONFIGURAR MAPA
mapa = folium.Map(
    location=[-27.8, -48.5],
    zoom_start=9,
    tiles='OpenStreetMap'
)

# 3. DEFINIR CORES POR ESPÉCIE
cores_especies = {
    'Ulva lactuca': 'green',
    'Gracilaria': 'red',
    'Sargassum': 'blue',
    'Laminaria': 'purple'
}

# 4. CRIAR GRUPOS DE CAMADAS
grupos = {}
for especie in gdf['especie'].unique():
    grupos[especie] = folium.FeatureGroup(name=especie)

# 5. ADICIONAR MARCADORES
for idx, row in gdf.iterrows():
    # Determinar status de validação
    valida = (20 <= row['temperatura_c'] <= 25) and (row['profundidade_m'] < 10)
    status = "✅ VÁLIDA" if valida else "⚠️ ATENÇÃO"
    
    # HTML do popup
    popup_html = f"""
    <div style="font-family: Arial; width: 220px;">
        <h4 style="color: #2E86AB; margin-bottom: 8px;">
            📍 {row['local']}
        </h4>
        <hr style="margin: 5px 0;">
        <table style="width: 100%; font-size: 12px;">
            <tr>
                <td><b>ID:</b></td>
                <td>{row['id']}</td>
            </tr>
            <tr>
                <td><b>Espécie:</b></td>
                <td><i>{row['especie']}</i></td>
            </tr>
            <tr>
                <td><b>Profundidade:</b></td>
                <td>{row['profundidade_m']}m</td>
            </tr>
            <tr>
                <td><b>Temperatura:</b></td>
                <td>{row['temperatura_c']}°C</td>
            </tr>
            <tr>
                <td><b>Coordenadas:</b></td>
                <td>{row['latitude']:.4f}°, {row['longitude']:.4f}°</td>
            </tr>
        </table>
        <hr style="margin: 5px 0;">
        <div style="text-align: center; padding: 5px; background-color: {'#d4edda' if valida else '#fff3cd'}; border-radius: 3px;">
            <b>{status}</b>
        </div>
    </div>
    """
    
    # Criar marcador
    cor = cores_especies.get(row['especie'], 'gray')
    marcador = folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=f"{row['local']} - {row['especie']}",
        icon=folium.Icon(color=cor, icon='leaf', prefix='fa')
    )
    
    # Adicionar ao grupo correspondente
    marcador.add_to(grupos[row['especie']])

# 6. ADICIONAR GRUPOS AO MAPA
for grupo in grupos.values():
    grupo.add_to(mapa)

# 7. ADICIONAR CONTROLE DE CAMADAS
folium.LayerControl(position='topright', collapsed=False).add_to(mapa)

# 8. ADICIONAR TÍTULO
titulo_html = '''
<div style="position: fixed; 
            top: 10px; 
            left: 50px; 
            width: 400px; 
            height: auto; 
            background-color: white; 
            border: 2px solid #2E86AB;
            border-radius: 5px;
            z-index: 9999; 
            padding: 10px;
            font-family: Arial;">
    <h3 style="margin: 0; color: #2E86AB;">
        🌊 Distribuição de Macroalgas - LABFICOL/UFSC
    </h3>
    <p style="margin: 5px 0; font-size: 12px;">
        Total de coletas: <b>{}</b> | Espécies: <b>{}</b>
    </p>
</div>
'''.format(len(gdf), gdf['especie'].nunique())

mapa.get_root().html.add_child(folium.Element(titulo_html))

# 9. SALVAR
mapa.save("dashboard_coletas_labficol.html")
print("✅ Dashboard criado: dashboard_coletas_labficol.html")
print(f"📊 {len(gdf)} coletas mapeadas")
print(f"🌿 {gdf['especie'].nunique()} espécies diferentes")
```

Execute e abra o arquivo HTML! 🚀

---

## 🎓 Checklist desta Lição

- [ ] Criei mapa básico com Folium
- [ ] Adicionei marcadores com popups
- [ ] Integrei GeoPandas com Folium
- [ ] Usei cores e ícones personalizados
- [ ] Criei camadas controláveis
- [ ] Desenvolvi dashboard completo

Se marcou tudo, você completou **Análise Geoespacial**! 🎉

---

## ➡️ Próximos Passos

Parabéns! Você domina análise geoespacial com Python! 🗺️

**Próximos módulos:**
1. **Visualização Web** (HTML, JavaScript avançado)
2. **Casos Práticos** (Aplicações reais em Oceanografia)

---

## 📝 Resumo de Funções Folium

| Função | Uso |
|--------|-----|
| `folium.Map()` | Criar mapa base |
| `folium.Marker()` | Adicionar marcador |
| `folium.CircleMarker()` | Círculo proporcional |
| `folium.Popup()` | Popup HTML |
| `folium.FeatureGroup()` | Grupo de camadas |
| `folium.LayerControl()` | Controle de camadas |
| `HeatMap()` | Mapa de calor |

---

**Você é um expert em mapas interativos!** 🗺️✨

Abra seus mapas HTML no navegador e compartilhe com sua equipe do LABFICOL! 🌊
