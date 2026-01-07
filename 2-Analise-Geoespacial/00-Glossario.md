# 📖 Glossário - Análise Geoespacial

## A

**Atributo (Feature Attribute)**: Informação descritiva associada a uma feição geográfica (nome, população, área, etc).

## B

**Bounding Box**: Retângulo que delimita a extensão mínima de um conjunto de geometrias.

**Buffer**: Operação que cria área ao redor de geometria com distância específica.

## C

**Centroide**: Ponto central de uma geometria.

**CRS (Coordinate Reference System)**: Sistema de coordenadas que define como posições geográficas são representadas.

**CSV (Comma-Separated Values)**: Formato de arquivo tabular com valores separados por vírgula.

## D

**DataFrame**: Estrutura de dados tabular do pandas com linhas e colunas.

**Dissolve**: Operação que combina geometrias adjacentes em uma única.

## E

**EPSG**: Código numérico que identifica sistemas de coordenadas (ex: EPSG:4326 = WGS84).

**Extent**: Limites geográficos (min/max X e Y) de uma área.

## F

**Feature (Feição)**: Entidade geográfica com geometria e atributos (ponto, linha ou polígono).

**Feature Collection**: Coleção de múltiplas feições GeoJSON.

## G

**Geocodificação**: Processo de converter endereços em coordenadas.

**GeoDataFrame**: DataFrame do GeoPandas com coluna de geometrias.

**Geografia**: Ciência que estuda a superfície terrestre e distribuição espacial de fenômenos.

**GeoJSON**: Formato JSON para codificar estruturas de dados geográficos.

**GeoPandas**: Biblioteca Python para manipular dados geoespaciais.

**Geometria**: Representação matemática de forma espacial (ponto, linha, polígono).

**GIS (Geographic Information System)**: Sistema para capturar, armazenar, analisar e gerenciar dados espaciais.

## I

**Interseção (Intersection)**: Operação que retorna geometria comum entre duas outras.

## L

**Latitude**: Coordenada que indica posição norte-sul (0° no Equador, -90° a +90°).

**Layer (Camada)**: Conjunto de dados geográficos relacionados.

**LineString**: Geometria GeoJSON representando linha conectando pontos.

**Longitude**: Coordenada que indica posição leste-oeste (0° em Greenwich, -180° a +180°).

## M

**Mapa**: Representação visual de informações geográficas.

**Mapa de calor (Heatmap)**: Visualização que usa cor para mostrar densidade/intensidade.

**Marker (Marcador)**: Ícone que indica localização em mapa.

**Mercator**: Projeção cilíndrica comum em mapas web.

**MultiPoint/MultiLineString/MultiPolygon**: Geometrias compostas por múltiplas partes.

## O

**Overlay**: Operação que combina duas camadas espaciais.

## P

**Plotly**: Biblioteca Python para visualizações interativas.

**Point (Ponto)**: Geometria mais simples representando localização (X, Y).

**Polygon (Polígono)**: Geometria fechada representando área.

**Projeção**: Transformação de coordenadas 3D (Terra) para 2D (mapa).

## R

**Raster**: Dados espaciais em formato de grade de pixels (imagens, elevação).

**Reprojetar**: Converter dados de um CRS para outro.

## S

**Shapefile**: Formato popular de arquivo para dados vetoriais GIS (.shp, .shx, .dbf).

**SIG (Sistema de Informação Geográfica)**: Termo em português para GIS.

**Spatial Join**: Operação que une atributos baseado em relação espacial.

## T

**Tiles (Ladrilhos)**: Pequenas imagens que compõem mapa web em diferentes zooms.

**Topology (Topologia)**: Relações espaciais entre geometrias (adjacência, interseção, etc).

## U

**Union**: Operação que combina geometrias em uma única.

## V

**Vetor**: Dados geográficos representados por pontos, linhas e polígonos.

**Visualização**: Representação gráfica de dados para facilitar compreensão.

## W

**WGS84 (World Geodetic System 1984)**: Sistema de coordenadas geográficas padrão (EPSG:4326).

## Z

**Zoom**: Nível de detalhe de visualização em mapa (maior número = mais próximo).

## Exemplos Práticos

```python
import geopandas as gpd
from shapely.geometry import Point, Polygon

# Criar GeoDataFrame de pontos
dados = {
    'nome': ['Ingleses', 'Lagoa', 'Centro'],
    'geometry': [
        Point(-48.4, -27.4),
        Point(-48.5, -27.6),
        Point(-48.55, -27.58)
    ]
}
gdf = gpd.GeoDataFrame(dados, crs="EPSG:4326")

# Criar buffer de 1 km
gdf_buffer = gdf.to_crs("EPSG:31982")  # Projetar para metros
gdf_buffer['geometry'] = gdf_buffer.buffer(1000)

# Ler shapefile
praias = gpd.read_file("praias.shp")

# Interseção espacial
praias_proximas = gpd.sjoin(praias, gdf_buffer, how='inner')

# Salvar como GeoJSON
praias_proximas.to_file("praias_proximas.geojson", driver='GeoJSON')

# Plotar
praias.plot(figsize=(10, 10), color='blue')
```

## Sistemas de Coordenadas Comuns

| EPSG | Nome | Uso |
|------|------|-----|
| 4326 | WGS84 | GPS, Google Maps, coordenadas geográficas |
| 3857 | Web Mercator | Mapas web (Google, OpenStreetMap) |
| 31982 | SIRGAS 2000 / UTM 22S | Brasil - SC, RS (coordenadas métricas) |
| 4674 | SIRGAS 2000 | Brasil - coordenadas geográficas |

---

💡 **Dica**: Use sempre `gdf.crs` para verificar o sistema de coordenadas do seu GeoDataFrame!
