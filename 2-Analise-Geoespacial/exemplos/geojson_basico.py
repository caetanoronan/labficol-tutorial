"""
GeoJSON Básico - LABFICOL
==========================

Exemplo prático: Criar e salvar arquivos GeoJSON
Formato padrão para dados geoespaciais

Autor: LABFICOL/UFSC
"""

import json

# Dados de coleta
coletas = [
    {'id': 1, 'praia': 'Ingleses Norte', 'lat': -27.4374, 'lon': -48.3923, 
     'especie': 'Ulva lactuca', 'biomassa': 245.3, 'temperatura': 24.5},
    {'id': 2, 'praia': 'Barra da Lagoa', 'lat': -27.5750, 'lon': -48.4200, 
     'especie': 'Gracilaria', 'biomassa': 310.2, 'temperatura': 23.8},
    {'id': 3, 'praia': 'Armação', 'lat': -27.7500, 'lon': -48.5100, 
     'especie': 'Sargassum', 'biomassa': 275.4, 'temperatura': 21.5},
    {'id': 4, 'praia': 'Garopaba', 'lat': -28.0200, 'lon': -48.6200, 
     'especie': 'Laminaria', 'biomassa': 425.8, 'temperatura': 21.0},
    {'id': 5, 'praia': 'Laguna', 'lat': -28.4833, 'lon': -48.7833, 
     'especie': 'Ulva lactuca', 'biomassa': 295.7, 'temperatura': 18.0}
]

print("="*60)
print("📝 CRIANDO ARQUIVO GEOJSON")
print("="*60)

# Criar estrutura GeoJSON
geojson = {
    "type": "FeatureCollection",
    "name": "Coletas LABFICOL",
    "features": []
}

# Adicionar cada coleta como Feature
print("\n🔄 Convertendo coletas para formato GeoJSON...")

for coleta in coletas:
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [coleta['lon'], coleta['lat']]  # [longitude, latitude]
        },
        "properties": {
            "id": coleta['id'],
            "praia": coleta['praia'],
            "especie": coleta['especie'],
            "biomassa_g": coleta['biomassa'],
            "temperatura_c": coleta['temperatura']
        }
    }
    
    geojson['features'].append(feature)
    print(f"   ✓ Coleta #{coleta['id']} - {coleta['praia']}")

# Salvar arquivo GeoJSON
nome_arquivo = 'coletas.geojson'

with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(geojson, arquivo, ensure_ascii=False, indent=2)

print(f"\n✅ Arquivo GeoJSON salvo: {nome_arquivo}")
print(f"\n📊 Total de features: {len(geojson['features'])}")

# Mostrar preview do arquivo
print("\n" + "="*60)
print("👁️  PREVIEW DO GEOJSON")
print("="*60)
print(json.dumps(geojson, ensure_ascii=False, indent=2)[:500] + "...")

print("\n" + "="*60)
print("💡 Dicas:")
print("   - Abra este arquivo em QGIS ou ArcGIS")
print("   - Use em mapas web com Leaflet.js")
print("   - Compartilhe em repositórios GitHub")
print("="*60)
