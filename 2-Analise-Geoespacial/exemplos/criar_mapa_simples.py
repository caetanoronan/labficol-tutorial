"""
Criar Mapa Simples - LABFICOL
==============================

Exemplo prático: Mapa interativo básico com Folium
Visualiza pontos de coleta em mapa web

Autor: LABFICOL/UFSC

Instalar: pip install folium
"""

import folium

# Dados de coleta (coordenadas reais de praias de SC)
coletas = [
    {'id': 1, 'praia': 'Ingleses Norte', 'lat': -27.4374, 'lon': -48.3923, 'especie': 'Ulva lactuca'},
    {'id': 2, 'praia': 'Barra da Lagoa', 'lat': -27.5750, 'lon': -48.4200, 'especie': 'Gracilaria'},
    {'id': 3, 'praia': 'Armação', 'lat': -27.7500, 'lon': -48.5100, 'especie': 'Sargassum'},
    {'id': 4, 'praia': 'Garopaba', 'lat': -28.0200, 'lon': -48.6200, 'especie': 'Laminaria'},
    {'id': 5, 'praia': 'Laguna', 'lat': -28.4833, 'lon': -48.7833, 'especie': 'Ulva lactuca'}
]

# Cores por espécie
cores = {
    'Ulva lactuca': 'green',
    'Gracilaria': 'red',
    'Sargassum': 'blue',
    'Laminaria': 'purple'
}

print("="*60)
print("🗺️  CRIANDO MAPA INTERATIVO")
print("="*60)

# Criar mapa centrado em Santa Catarina
mapa = folium.Map(
    location=[-27.8, -48.5],  # Centro aproximado de SC
    zoom_start=9,
    tiles='OpenStreetMap'
)

# Adicionar marcadores
print("\n📍 Adicionando pontos de coleta...")

for coleta in coletas:
    # Criar popup com informações
    popup_html = f"""
    <div style="font-family: Arial; min-width: 200px;">
        <h3 style="color: {cores[coleta['especie']]}; margin: 0;">
            {coleta['praia']}
        </h3>
        <hr style="margin: 10px 0;">
        <p><strong>ID:</strong> {coleta['id']}</p>
        <p><strong>Espécie:</strong> <em>{coleta['especie']}</em></p>
        <p><strong>Coordenadas:</strong><br>
           Lat: {coleta['lat']}<br>
           Lon: {coleta['lon']}</p>
    </div>
    """
    
    # Adicionar marcador
    folium.Marker(
        location=[coleta['lat'], coleta['lon']],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=coleta['praia'],
        icon=folium.Icon(color=cores[coleta['especie']], icon='info-sign')
    ).add_to(mapa)
    
    print(f"   ✓ {coleta['praia']} - {coleta['especie']}")

# Salvar mapa
nome_arquivo = 'mapa_coletas.html'
mapa.save(nome_arquivo)

print(f"\n✅ Mapa salvo em: {nome_arquivo}")
print(f"\n💡 Abra o arquivo '{nome_arquivo}' no navegador!")
print("\n" + "="*60)
