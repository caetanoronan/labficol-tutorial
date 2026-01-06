# 🗺️ Leaflet.js - Mapas Interativos com JavaScript

## O que é Leaflet.js?

**Leaflet** = biblioteca JavaScript para criar mapas interativos na web.

```
Folium (Python)  → Gera HTML com Leaflet
Leaflet.js       → Controle total com JavaScript
```

**Vantagens:**
- Leve e rápido
- Open source
- Funciona em mobile
- Altamente customizável

**Site oficial:** https://leafletjs.com

---

## 🚀 Setup Básico

### HTML com Leaflet

Crie `mapa_leaflet.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mapa Leaflet - LABFICOL</title>
    
    <!-- Leaflet CSS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }
        
        #map {
            height: 600px;
            width: 100%;
        }
    </style>
</head>
<body>
    <div id="map"></div>
    
    <!-- Leaflet JavaScript -->
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    
    <script>
        // Criar mapa centrado em Florianópolis
        const map = L.map('map').setView([-27.5969, -48.5495], 12);
        
        // Adicionar camada de tiles (OpenStreetMap)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);
        
        // Adicionar marcador
        L.marker([-27.5969, -48.5495])
            .addTo(map)
            .bindPopup('UFSC - Florianópolis')
            .openPopup();
    </script>
</body>
</html>
```

Abra no navegador! Você verá um mapa interativo! 🗺️

---

## 📍 Marcadores (Markers)

### Marcador Básico

```javascript
// Criar marcador
const marcador = L.marker([-27.5969, -48.5495]).addTo(map);

// Com popup
marcador.bindPopup('UFSC');

// Com tooltip (aparece ao passar mouse)
marcador.bindTooltip('Campus Trindade');
```

### Múltiplos Marcadores

```javascript
const coletas = [
    { lat: -27.4374, lon: -48.3923, nome: "Ingleses Norte", especie: "Ulva lactuca" },
    { lat: -27.4450, lon: -48.3950, nome: "Ingleses Sul", especie: "Gracilaria" },
    { lat: -27.5750, lon: -48.4200, nome: "Barra da Lagoa", especie: "Sargassum" }
];

coletas.forEach(coleta => {
    L.marker([coleta.lat, coleta.lon])
        .addTo(map)
        .bindPopup(`<b>${coleta.nome}</b><br>${coleta.especie}`);
});
```

### Ícones Personalizados

```javascript
// Criar ícone customizado
const iconeVerde = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34]
});

// Usar ícone
L.marker([-27.4374, -48.3923], { icon: iconeVerde })
    .addTo(map)
    .bindPopup('Ulva lactuca');
```

---

## ⭕ Círculos e Formas

### Circle Markers

```javascript
// Círculo proporcional a valor
const coletas = [
    { lat: -27.4374, lon: -48.3923, prof: 5.2 },
    { lat: -27.4450, lon: -48.3950, prof: 12.8 },
    { lat: -27.5750, lon: -48.4200, prof: 3.1 }
];

coletas.forEach(c => {
    L.circleMarker([c.lat, c.lon], {
        radius: c.prof * 2,  // Proporcional à profundidade
        color: 'blue',
        fillColor: '#30a3dc',
        fillOpacity: 0.6
    })
    .addTo(map)
    .bindPopup(`Profundidade: ${c.prof}m`);
});
```

### Polígonos

```javascript
// Área de estudo (polígono)
const areaEstudo = [
    [-27.55, -48.55],
    [-27.55, -48.50],
    [-27.60, -48.50],
    [-27.60, -48.55]
];

L.polygon(areaEstudo, {
    color: 'red',
    fillColor: '#ff0000',
    fillOpacity: 0.2
})
.addTo(map)
.bindPopup('Área de Proteção Marinha');
```

---

## 🎨 Popups HTML Avançados

```javascript
const coleta = {
    id: 1,
    local: "Ingleses Norte",
    especie: "Ulva lactuca",
    prof: 5.2,
    temp: 22.5,
    sal: 35.0
};

const popupHTML = `
    <div style="font-family: Arial; min-width: 200px;">
        <h3 style="color: #2E86AB; margin-top: 0;">
            📍 ${coleta.local}
        </h3>
        <hr style="margin: 10px 0;">
        <table style="width: 100%; font-size: 14px;">
            <tr>
                <td><strong>ID:</strong></td>
                <td>${coleta.id}</td>
            </tr>
            <tr>
                <td><strong>Espécie:</strong></td>
                <td><em>${coleta.especie}</em></td>
            </tr>
            <tr>
                <td><strong>Profundidade:</strong></td>
                <td>${coleta.prof}m</td>
            </tr>
            <tr>
                <td><strong>Temperatura:</strong></td>
                <td>${coleta.temp}°C</td>
            </tr>
            <tr>
                <td><strong>Salinidade:</strong></td>
                <td>${coleta.sal} PSU</td>
            </tr>
        </table>
        <hr style="margin: 10px 0;">
        <button onclick="verDetalhes(${coleta.id})" 
                style="width: 100%; padding: 8px; background: #2E86AB; color: white; border: none; cursor: pointer; border-radius: 4px;">
            Ver Detalhes
        </button>
    </div>
`;

L.marker([coleta.lat, coleta.lon])
    .addTo(map)
    .bindPopup(popupHTML);
```

---

## 🗂️ Controle de Camadas

```javascript
// Criar grupos de camadas
const grupoUlva = L.layerGroup();
const grupoGracilaria = L.layerGroup();
const grupoSargassum = L.layerGroup();

// Adicionar marcadores aos grupos
L.marker([-27.4374, -48.3923])
    .bindPopup('Ulva lactuca')
    .addTo(grupoUlva);

L.marker([-27.4450, -48.3950])
    .bindPopup('Gracilaria')
    .addTo(grupoGracilaria);

// Criar controle de camadas
const overlays = {
    "Ulva lactuca": grupoUlva,
    "Gracilaria": grupoGracilaria,
    "Sargassum": grupoSargassum
};

L.control.layers(null, overlays).addTo(map);

// Adicionar grupos ao mapa por padrão
grupoUlva.addTo(map);
grupoGracilaria.addTo(map);
```

---

## 🎯 Exemplo Completo: Dashboard Interativo

Crie `dashboard_completo.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard LABFICOL</title>
    
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        header {
            background: linear-gradient(135deg, #2E86AB 0%, #1a5c7a 100%);
            color: white;
            padding: 20px;
            text-align: center;
        }
        
        .container {
            display: flex;
            height: calc(100vh - 80px);
        }
        
        .sidebar {
            width: 300px;
            background: #f8f9fa;
            padding: 20px;
            overflow-y: auto;
            border-right: 1px solid #dee2e6;
        }
        
        #map {
            flex: 1;
        }
        
        .stat-card {
            background: white;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .stat-card h3 {
            color: #2E86AB;
            font-size: 14px;
            margin-bottom: 10px;
        }
        
        .stat-number {
            font-size: 32px;
            font-weight: bold;
            color: #333;
        }
        
        .species-list {
            list-style: none;
            margin-top: 10px;
        }
        
        .species-list li {
            padding: 8px;
            margin-bottom: 5px;
            background: white;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .species-list li:hover {
            background: #e9ecef;
        }
        
        .badge {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: bold;
        }
        
        .badge-green { background: #28a745; color: white; }
        .badge-red { background: #dc3545; color: white; }
        .badge-blue { background: #007bff; color: white; }
        .badge-yellow { background: #ffc107; color: white; }
    </style>
</head>
<body>
    <header>
        <h1>🌊 Dashboard de Coletas - LABFICOL/UFSC</h1>
        <p>Monitoramento de Macroalgas na Costa de Santa Catarina</p>
    </header>
    
    <div class="container">
        <div class="sidebar">
            <div class="stat-card">
                <h3>📊 ESTATÍSTICAS GERAIS</h3>
                <div style="text-align: center;">
                    <div class="stat-number" id="totalColetas">0</div>
                    <div>Total de Coletas</div>
                </div>
            </div>
            
            <div class="stat-card">
                <h3>🌿 ESPÉCIES</h3>
                <ul class="species-list" id="especiesList"></ul>
            </div>
            
            <div class="stat-card">
                <h3>📈 MÉDIAS</h3>
                <div id="medias"></div>
            </div>
        </div>
        
        <div id="map"></div>
    </div>
    
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    
    <script>
        // Dados de coleta
        const coletas = [
            { id: 1, lat: -27.4374, lon: -48.3923, local: "Ingleses N", especie: "Ulva lactuca", prof: 5.2, temp: 22.5, sal: 35.0 },
            { id: 2, lat: -27.4450, lon: -48.3950, local: "Ingleses S", especie: "Gracilaria", prof: 7.8, temp: 23.1, sal: 34.8 },
            { id: 3, lat: -27.5750, lon: -48.4200, local: "Barra Lagoa", especie: "Sargassum", prof: 3.1, temp: 22.8, sal: 35.1 },
            { id: 4, lat: -28.4833, lon: -48.7833, local: "Laguna", especie: "Laminaria", prof: 10.5, temp: 21.2, sal: 35.0 },
            { id: 5, lat: -28.0200, lon: -48.6200, local: "Garopaba", especie: "Gracilaria", prof: 6.0, temp: 22.0, sal: 34.9 },
            { id: 6, lat: -27.7500, lon: -48.5100, local: "Armação", especie: "Ulva lactuca", prof: 4.5, temp: 23.5, sal: 35.1 }
        ];
        
        // Cores por espécie
        const coresEspecies = {
            "Ulva lactuca": "#28a745",
            "Gracilaria": "#dc3545",
            "Sargassum": "#007bff",
            "Laminaria": "#6f42c1"
        };
        
        // Criar mapa
        const map = L.map('map').setView([-27.8, -48.5], 9);
        
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap'
        }).addTo(map);
        
        // Adicionar marcadores
        coletas.forEach(coleta => {
            const cor = coresEspecies[coleta.especie];
            const valida = (coleta.temp >= 20 && coleta.temp <= 25 && coleta.prof < 10);
            
            // Criar ícone SVG personalizado
            const iconeHTML = `
                <div style="background-color: ${cor}; width: 30px; height: 30px; 
                            border-radius: 50%; border: 3px solid white; 
                            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                            display: flex; align-items: center; justify-content: center;
                            color: white; font-weight: bold; font-size: 12px;">
                    ${coleta.id}
                </div>
            `;
            
            const icone = L.divIcon({
                html: iconeHTML,
                iconSize: [30, 30],
                className: ''
            });
            
            // Popup
            const popupHTML = `
                <div style="font-family: Arial; min-width: 220px;">
                    <h3 style="color: ${cor}; margin: 0 0 10px 0;">
                        📍 ${coleta.local}
                    </h3>
                    <hr style="margin: 10px 0; border: none; border-top: 1px solid #ddd;">
                    <table style="width: 100%; font-size: 13px;">
                        <tr><td><strong>ID:</strong></td><td>#${coleta.id}</td></tr>
                        <tr><td><strong>Espécie:</strong></td><td><em>${coleta.especie}</em></td></tr>
                        <tr><td><strong>Profundidade:</strong></td><td>${coleta.prof}m</td></tr>
                        <tr><td><strong>Temperatura:</strong></td><td>${coleta.temp}°C</td></tr>
                        <tr><td><strong>Salinidade:</strong></td><td>${coleta.sal} PSU</td></tr>
                    </table>
                    <hr style="margin: 10px 0; border: none; border-top: 1px solid #ddd;">
                    <div style="text-align: center; padding: 8px; background: ${valida ? '#d4edda' : '#fff3cd'}; border-radius: 4px;">
                        <strong>${valida ? '✅ VÁLIDA' : '⚠️ ATENÇÃO'}</strong>
                    </div>
                </div>
            `;
            
            L.marker([coleta.lat, coleta.lon], { icon: icone })
                .addTo(map)
                .bindPopup(popupHTML);
        });
        
        // Atualizar sidebar
        function atualizarEstatisticas() {
            // Total
            document.getElementById('totalColetas').textContent = coletas.length;
            
            // Espécies
            const especiesCount = {};
            coletas.forEach(c => {
                especiesCount[c.especie] = (especiesCount[c.especie] || 0) + 1;
            });
            
            const especiesList = document.getElementById('especiesList');
            especiesList.innerHTML = '';
            Object.entries(especiesCount).forEach(([especie, count]) => {
                const cor = coresEspecies[especie];
                const li = document.createElement('li');
                li.innerHTML = `
                    <span class="badge" style="background: ${cor};">${count}</span>
                    <em style="margin-left: 10px;">${especie}</em>
                `;
                especiesList.appendChild(li);
            });
            
            // Médias
            const tempMedia = (coletas.reduce((sum, c) => sum + c.temp, 0) / coletas.length).toFixed(1);
            const profMedia = (coletas.reduce((sum, c) => sum + c.prof, 0) / coletas.length).toFixed(1);
            const salMedia = (coletas.reduce((sum, c) => sum + c.sal, 0) / coletas.length).toFixed(1);
            
            document.getElementById('medias').innerHTML = `
                <p><strong>Temperatura:</strong> ${tempMedia}°C</p>
                <p><strong>Profundidade:</strong> ${profMedia}m</p>
                <p><strong>Salinidade:</strong> ${salMedia} PSU</p>
            `;
        }
        
        atualizarEstatisticas();
    </script>
</body>
</html>
```

Abra no navegador! Dashboard completo e interativo! 📊🗺️

---

## 🎓 Integrar com GeoJSON

```javascript
// Carregar GeoJSON
fetch('coletas.geojson')
    .then(response => response.json())
    .then(data => {
        L.geoJSON(data, {
            onEachFeature: function(feature, layer) {
                const props = feature.properties;
                layer.bindPopup(`
                    <h3>${props.nome}</h3>
                    <p><strong>Espécie:</strong> ${props.especie}</p>
                `);
            }
        }).addTo(map);
    });
```

---

## 🎓 Checklist desta Lição

- [ ] Criei mapa básico com Leaflet
- [ ] Adicionei marcadores interativos
- [ ] Customizei popups com HTML
- [ ] Implementei controle de camadas
- [ ] Desenvolvi dashboard completo

Se marcou tudo, você completou **Visualização Web**! 🎉

---

## ➡️ Próximos Passos

Parabéns! Você domina desenvolvimento web para visualização de dados! 🌐

**Próximo módulo:**
- **4-Casos-Praticos** (Projetos completos de Oceanografia)

---

## 📝 Resumo de Funções Leaflet

| Função | Uso |
|--------|-----|
| `L.map()` | Criar mapa |
| `L.tileLayer()` | Adicionar camada base |
| `L.marker()` | Adicionar marcador |
| `L.circleMarker()` | Círculo no mapa |
| `L.polygon()` | Polígono |
| `L.layerGroup()` | Agrupar camadas |
| `L.control.layers()` | Controle de camadas |

---

**Você é um desenvolvedor web completo!** 🌐✨

Pronto para criar dashboards profissionais para pesquisa! 🚀
