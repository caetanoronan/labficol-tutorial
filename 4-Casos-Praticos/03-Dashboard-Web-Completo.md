# 🌐 Caso Prático 3: Dashboard Web Completo

## 🎯 Objetivo do Projeto

Criar um **dashboard web profissional** integrando todas as tecnologias aprendidas: Python (backend) + HTML/CSS/JavaScript (frontend) + Leaflet (mapas) + API REST.

**Sistema completo:**
- Backend Python com Flask
- API REST para dados
- Frontend interativo
- Mapas dinâmicos
- Gráficos em tempo real

---

## 🏗️ Arquitetura do Sistema

```
dashboard-labficol/
│
├── backend/
│   ├── app.py              # Servidor Flask
│   ├── dados.py            # Gerador de dados
│   └── requirements.txt
│
├── frontend/
│   ├── index.html          # Dashboard principal
│   ├── style.css           # Estilos
│   └── script.js           # Lógica JavaScript
│
└── dados/
    └── coletas.json        # Base de dados
```

---

## 🐍 Parte 1: Backend Python (Flask API)

### Instalar Dependências

```bash
pip install flask flask-cors pandas
```

### Criar `backend/requirements.txt`:

```
flask==3.0.0
flask-cors==4.0.0
pandas==2.1.4
```

### Criar `backend/dados.py`:

```python
import pandas as pd
import json
from datetime import datetime, timedelta
import random

def gerar_dados_coletas(n=50):
    """Gera dados sintéticos de coletas"""
    
    especies = ['Ulva lactuca', 'Gracilaria', 'Sargassum', 'Laminaria']
    praias = ['Ingleses', 'Barra da Lagoa', 'Armação', 'Garopaba', 'Laguna']
    
    # Coordenadas aproximadas das praias
    coords_praias = {
        'Ingleses': (-27.4374, -48.3923),
        'Barra da Lagoa': (-27.5750, -48.4200),
        'Armação': (-27.7500, -48.5100),
        'Garopaba': (-28.0200, -48.6200),
        'Laguna': (-28.4833, -48.7833)
    }
    
    coletas = []
    data_inicial = datetime(2025, 1, 1)
    
    for i in range(n):
        praia = random.choice(praias)
        lat_base, lon_base = coords_praias[praia]
        
        # Adicionar variação pequena nas coordenadas
        lat = lat_base + random.uniform(-0.01, 0.01)
        lon = lon_base + random.uniform(-0.01, 0.01)
        
        # Data aleatória nos últimos 6 meses
        dias_passados = random.randint(0, 180)
        data = data_inicial + timedelta(days=dias_passados)
        
        coleta = {
            'id': i + 1,
            'data': data.strftime('%Y-%m-%d'),
            'praia': praia,
            'lat': round(lat, 4),
            'lon': round(lon, 4),
            'especie': random.choice(especies),
            'biomassa_g': round(random.uniform(100, 500), 1),
            'temperatura_c': round(random.uniform(17, 26), 1),
            'salinidade_psu': round(random.uniform(34, 36), 1),
            'profundidade_m': round(random.uniform(2, 12), 1)
        }
        
        coletas.append(coleta)
    
    return coletas

def salvar_dados(filename='../dados/coletas.json'):
    """Salva dados em arquivo JSON"""
    import os
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    dados = gerar_dados_coletas(50)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    
    print(f"✅ {len(dados)} coletas salvas em {filename}")

if __name__ == '__main__':
    salvar_dados()
```

### Criar `backend/app.py`:

```python
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import pandas as pd
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Permitir requisições de outros domínios

# Carregar dados
def carregar_dados():
    try:
        with open('../dados/coletas.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# ====================
# ROTAS DA API
# ====================

@app.route('/')
def home():
    return jsonify({
        'message': '🌊 API LABFICOL - Dashboard de Macroalgas',
        'version': '1.0',
        'endpoints': [
            '/api/coletas',
            '/api/estatisticas',
            '/api/especies',
            '/api/praias',
            '/api/timeline'
        ]
    })

@app.route('/api/coletas')
def get_coletas():
    """Retorna todas as coletas"""
    dados = carregar_dados()
    
    # Filtros opcionais
    especie = request.args.get('especie')
    praia = request.args.get('praia')
    
    if especie:
        dados = [d for d in dados if d['especie'] == especie]
    if praia:
        dados = [d for d in dados if d['praia'] == praia]
    
    return jsonify({
        'total': len(dados),
        'coletas': dados
    })

@app.route('/api/estatisticas')
def get_estatisticas():
    """Retorna estatísticas gerais"""
    dados = carregar_dados()
    df = pd.DataFrame(dados)
    
    if df.empty:
        return jsonify({'error': 'Sem dados'}), 404
    
    stats = {
        'total_coletas': len(df),
        'total_especies': df['especie'].nunique(),
        'total_praias': df['praia'].nunique(),
        'biomassa_total': round(df['biomassa_g'].sum(), 1),
        'biomassa_media': round(df['biomassa_g'].mean(), 1),
        'temperatura_media': round(df['temperatura_c'].mean(), 1),
        'salinidade_media': round(df['salinidade_psu'].mean(), 1),
        'profundidade_media': round(df['profundidade_m'].mean(), 1),
        'data_primeira_coleta': df['data'].min(),
        'data_ultima_coleta': df['data'].max()
    }
    
    return jsonify(stats)

@app.route('/api/especies')
def get_especies():
    """Retorna contagem e estatísticas por espécie"""
    dados = carregar_dados()
    df = pd.DataFrame(dados)
    
    if df.empty:
        return jsonify({'error': 'Sem dados'}), 404
    
    especies_stats = df.groupby('especie').agg({
        'id': 'count',
        'biomassa_g': ['mean', 'sum', 'min', 'max'],
        'temperatura_c': 'mean',
        'profundidade_m': 'mean'
    }).round(1)
    
    especies_stats.columns = ['_'.join(col).strip('_') for col in especies_stats.columns]
    
    resultado = []
    for especie in especies_stats.index:
        resultado.append({
            'especie': especie,
            'ocorrencias': int(especies_stats.loc[especie, 'id_count']),
            'biomassa_media': float(especies_stats.loc[especie, 'biomassa_g_mean']),
            'biomassa_total': float(especies_stats.loc[especie, 'biomassa_g_sum']),
            'temperatura_media': float(especies_stats.loc[especie, 'temperatura_c_mean']),
            'profundidade_media': float(especies_stats.loc[especie, 'profundidade_m_mean'])
        })
    
    return jsonify(resultado)

@app.route('/api/praias')
def get_praias():
    """Retorna estatísticas por praia"""
    dados = carregar_dados()
    df = pd.DataFrame(dados)
    
    if df.empty:
        return jsonify({'error': 'Sem dados'}), 404
    
    praias_stats = df.groupby('praia').agg({
        'id': 'count',
        'especie': lambda x: x.nunique(),
        'biomassa_g': 'sum',
        'lat': 'mean',
        'lon': 'mean'
    }).round(4)
    
    resultado = []
    for praia in praias_stats.index:
        resultado.append({
            'praia': praia,
            'coletas': int(praias_stats.loc[praia, 'id']),
            'especies_diferentes': int(praias_stats.loc[praia, 'especie']),
            'biomassa_total': float(praias_stats.loc[praia, 'biomassa_g']),
            'lat': float(praias_stats.loc[praia, 'lat']),
            'lon': float(praias_stats.loc[praia, 'lon'])
        })
    
    return jsonify(resultado)

@app.route('/api/timeline')
def get_timeline():
    """Retorna dados para timeline (agregado por mês)"""
    dados = carregar_dados()
    df = pd.DataFrame(dados)
    
    if df.empty:
        return jsonify({'error': 'Sem dados'}), 404
    
    df['data'] = pd.to_datetime(df['data'])
    df['mes'] = df['data'].dt.to_period('M')
    
    timeline = df.groupby('mes').agg({
        'id': 'count',
        'biomassa_g': 'sum'
    }).round(1)
    
    resultado = []
    for mes in timeline.index:
        resultado.append({
            'mes': str(mes),
            'coletas': int(timeline.loc[mes, 'id']),
            'biomassa_total': float(timeline.loc[mes, 'biomassa_g'])
        })
    
    return jsonify(resultado)

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Iniciando servidor Flask...")
    print("=" * 60)
    print("📍 Acesse: http://localhost:5000")
    print("📚 API Docs: http://localhost:5000/")
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 🌐 Parte 2: Frontend (HTML + CSS + JavaScript)

### Criar `frontend/index.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard LABFICOL - Monitoramento de Macroalgas</title>
    
    <!-- Leaflet CSS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    
    <!-- CSS Customizado -->
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container-header">
            <h1>🌊 Dashboard LABFICOL</h1>
            <p>Monitoramento de Macroalgas - Costa de Santa Catarina</p>
            <div id="lastUpdate">Carregando...</div>
        </div>
    </header>
    
    <!-- Dashboard Grid -->
    <main class="dashboard-grid">
        
        <!-- Cards de Estatísticas -->
        <section class="stats-cards">
            <div class="card stat-card" id="cardColetas">
                <div class="card-icon">📊</div>
                <div class="card-content">
                    <h3>Total de Coletas</h3>
                    <div class="stat-number" id="totalColetas">-</div>
                </div>
            </div>
            
            <div class="card stat-card" id="cardEspecies">
                <div class="card-icon">🌿</div>
                <div class="card-content">
                    <h3>Espécies</h3>
                    <div class="stat-number" id="totalEspecies">-</div>
                </div>
            </div>
            
            <div class="card stat-card" id="cardPraias">
                <div class="card-icon">📍</div>
                <div class="card-content">
                    <h3>Praias Monitoradas</h3>
                    <div class="stat-number" id="totalPraias">-</div>
                </div>
            </div>
            
            <div class="card stat-card" id="cardBiomassa">
                <div class="card-icon">⚖️</div>
                <div class="card-content">
                    <h3>Biomassa Total</h3>
                    <div class="stat-number" id="biomassamTotal">-</div>
                    <div class="stat-unit">gramas</div>
                </div>
            </div>
        </section>
        
        <!-- Mapa -->
        <section class="card map-container">
            <h2>🗺️ Distribuição Geográfica</h2>
            <div id="map"></div>
        </section>
        
        <!-- Lista de Espécies -->
        <section class="card">
            <h2>🌿 Ranking de Espécies</h2>
            <div id="especiesList" class="list-container"></div>
        </section>
        
        <!-- Praias -->
        <section class="card">
            <h2>📍 Estatísticas por Praia</h2>
            <div id="praiasList" class="list-container"></div>
        </section>
        
        <!-- Timeline -->
        <section class="card timeline-container">
            <h2>📈 Evolução Temporal</h2>
            <canvas id="timelineChart"></canvas>
        </section>
        
    </main>
    
    <!-- Footer -->
    <footer>
        <p>© 2025 LABFICOL - UFSC | Desenvolvido para pesquisa em Ficologia</p>
    </footer>
    
    <!-- Scripts -->
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <script src="script.js"></script>
</body>
</html>
```

### Criar `frontend/style.css`:

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
    min-height: 100vh;
}

/* Header */
header {
    background: linear-gradient(135deg, #006064 0%, #00838f 100%);
    color: white;
    padding: 30px 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.container-header {
    max-width: 1400px;
    margin: 0 auto;
    text-align: center;
}

header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
}

header p {
    font-size: 1.2em;
    opacity: 0.9;
}

#lastUpdate {
    margin-top: 15px;
    font-size: 0.9em;
    opacity: 0.8;
}

/* Dashboard Grid */
.dashboard-grid {
    max-width: 1400px;
    margin: 30px auto;
    padding: 0 20px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 20px;
}

/* Cards */
.card {
    background: white;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 12px rgba(0,0,0,0.15);
}

/* Stats Cards */
.stats-cards {
    grid-column: 1 / -1;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    grid-gap: 20px;
}

.stat-card {
    display: flex;
    align-items: center;
    gap: 20px;
}

.card-icon {
    font-size: 3em;
}

.card-content h3 {
    font-size: 0.9em;
    color: #666;
    margin-bottom: 10px;
}

.stat-number {
    font-size: 2.5em;
    font-weight: bold;
    color: #006064;
}

.stat-unit {
    font-size: 0.8em;
    color: #999;
}

/* Mapa */
.map-container {
    grid-column: 1 / 3;
    grid-row: span 2;
}

#map {
    height: 500px;
    border-radius: 8px;
    margin-top: 15px;
}

/* Listas */
.list-container {
    max-height: 400px;
    overflow-y: auto;
    margin-top: 15px;
}

.list-item {
    padding: 15px;
    margin-bottom: 10px;
    background: #f5f5f5;
    border-radius: 8px;
    border-left: 4px solid #00838f;
}

.list-item h4 {
    color: #006064;
    margin-bottom: 8px;
}

.list-item p {
    font-size: 0.9em;
    color: #666;
    margin: 5px 0;
}

/* Timeline */
.timeline-container {
    grid-column: 1 / -1;
}

#timelineChart {
    margin-top: 20px;
}

/* Footer */
footer {
    background: #006064;
    color: white;
    text-align: center;
    padding: 20px;
    margin-top: 40px;
}

/* Responsivo */
@media (max-width: 1024px) {
    .dashboard-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .map-container {
        grid-column: 1 / -1;
    }
}

@media (max-width: 768px) {
    .dashboard-grid {
        grid-template-columns: 1fr;
    }
    
    header h1 {
        font-size: 1.8em;
    }
}
```

### Criar `frontend/script.js`:

```javascript
// Configuração da API
const API_URL = 'http://localhost:5000/api';

// Cores por espécie
const CORES_ESPECIES = {
    'Ulva lactuca': '#4CAF50',
    'Gracilaria': '#F44336',
    'Sargassum': '#2196F3',
    'Laminaria': '#9C27B0'
};

// Mapa global
let mapa;

// ====================
// CARREGAR DADOS
// ====================

async function carregarDashboard() {
    try {
        console.log('🔄 Carregando dados da API...');
        
        // Carregar todos os endpoints
        const [stats, especies, praias, timeline, coletas] = await Promise.all([
            fetch(`${API_URL}/estatisticas`).then(r => r.json()),
            fetch(`${API_URL}/especies`).then(r => r.json()),
            fetch(`${API_URL}/praias`).then(r => r.json()),
            fetch(`${API_URL}/timeline`).then(r => r.json()),
            fetch(`${API_URL}/coletas`).then(r => r.json())
        ]);
        
        console.log('✅ Dados carregados!');
        
        // Atualizar interface
        atualizarStats(stats);
        atualizarEspecies(especies);
        atualizarPraias(praias);
        criarTimeline(timeline);
        inicializarMapa(coletas.coletas);
        
        // Atualizar timestamp
        document.getElementById('lastUpdate').textContent = 
            `Última atualização: ${new Date().toLocaleString('pt-BR')}`;
        
    } catch (error) {
        console.error('❌ Erro ao carregar dados:', error);
        alert('Erro ao conectar com a API. Certifique-se de que o servidor Flask está rodando.');
    }
}

// ====================
// ATUALIZAR STATS
// ====================

function atualizarStats(stats) {
    document.getElementById('totalColetas').textContent = stats.total_coletas;
    document.getElementById('totalEspecies').textContent = stats.total_especies;
    document.getElementById('totalPraias').textContent = stats.total_praias;
    document.getElementById('biomassamTotal').textContent = 
        stats.biomassa_total.toLocaleString('pt-BR');
}

// ====================
// LISTA DE ESPÉCIES
// ====================

function atualizarEspecies(especies) {
    const container = document.getElementById('especiesList');
    container.innerHTML = '';
    
    // Ordenar por ocorrências
    especies.sort((a, b) => b.ocorrencias - a.ocorrencias);
    
    especies.forEach((especie, index) => {
        const item = document.createElement('div');
        item.className = 'list-item';
        item.style.borderLeftColor = CORES_ESPECIES[especie.especie];
        
        item.innerHTML = `
            <h4>${index + 1}. ${especie.especie}</h4>
            <p><strong>Ocorrências:</strong> ${especie.ocorrencias}</p>
            <p><strong>Biomassa média:</strong> ${especie.biomassa_media.toFixed(1)}g</p>
            <p><strong>Temperatura média:</strong> ${especie.temperatura_media.toFixed(1)}°C</p>
        `;
        
        container.appendChild(item);
    });
}

// ====================
// LISTA DE PRAIAS
// ====================

function atualizarPraias(praias) {
    const container = document.getElementById('praiasList');
    container.innerHTML = '';
    
    // Ordenar por coletas
    praias.sort((a, b) => b.coletas - a.coletas);
    
    praias.forEach((praia, index) => {
        const item = document.createElement('div');
        item.className = 'list-item';
        
        item.innerHTML = `
            <h4>${index + 1}. ${praia.praia}</h4>
            <p><strong>Coletas:</strong> ${praia.coletas}</p>
            <p><strong>Espécies:</strong> ${praia.especies_diferentes}</p>
            <p><strong>Biomassa total:</strong> ${praia.biomassa_total.toFixed(1)}g</p>
        `;
        
        container.appendChild(item);
    });
}

// ====================
// TIMELINE (Chart.js)
// ====================

function criarTimeline(timeline) {
    const ctx = document.getElementById('timelineChart').getContext('2d');
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: timeline.map(t => t.mes),
            datasets: [{
                label: 'Número de Coletas',
                data: timeline.map(t => t.coletas),
                borderColor: '#2196F3',
                backgroundColor: 'rgba(33, 150, 243, 0.1)',
                tension: 0.4,
                fill: true
            }, {
                label: 'Biomassa Total (g)',
                data: timeline.map(t => t.biomassa_total),
                borderColor: '#4CAF50',
                backgroundColor: 'rgba(76, 175, 80, 0.1)',
                tension: 0.4,
                fill: true,
                yAxisID: 'y1'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: false
                }
            },
            scales: {
                y: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                    title: {
                        display: true,
                        text: 'Número de Coletas'
                    }
                },
                y1: {
                    type: 'linear',
                    display: true,
                    position: 'right',
                    title: {
                        display: true,
                        text: 'Biomassa (g)'
                    },
                    grid: {
                        drawOnChartArea: false
                    }
                }
            }
        }
    });
}

// ====================
// MAPA LEAFLET
// ====================

function inicializarMapa(coletas) {
    // Criar mapa centrado em SC
    mapa = L.map('map').setView([-27.5, -48.5], 8);
    
    // Adicionar tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap'
    }).addTo(mapa);
    
    // Adicionar marcadores
    coletas.forEach(coleta => {
        const cor = CORES_ESPECIES[coleta.especie];
        
        const popup = `
            <div style="font-family: Arial; min-width: 200px;">
                <h3 style="color: ${cor}; margin: 0 0 10px 0;">
                    ${coleta.especie}
                </h3>
                <hr style="margin: 10px 0;">
                <p><strong>Praia:</strong> ${coleta.praia}</p>
                <p><strong>Data:</strong> ${new Date(coleta.data).toLocaleDateString('pt-BR')}</p>
                <p><strong>Biomassa:</strong> ${coleta.biomassa_g}g</p>
                <p><strong>Temperatura:</strong> ${coleta.temperatura_c}°C</p>
                <p><strong>Profundidade:</strong> ${coleta.profundidade_m}m</p>
            </div>
        `;
        
        L.circleMarker([coleta.lat, coleta.lon], {
            radius: 8,
            fillColor: cor,
            color: '#fff',
            weight: 2,
            opacity: 1,
            fillOpacity: 0.8
        }).bindPopup(popup).addTo(mapa);
    });
}

// ====================
// INICIALIZAR
// ====================

document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 Dashboard inicializado');
    carregarDashboard();
    
    // Atualizar a cada 30 segundos
    setInterval(carregarDashboard, 30000);
});
```

---

## 🚀 Como Executar

### 1. Gerar dados:
```bash
cd backend
python dados.py
```

### 2. Iniciar servidor Flask:
```bash
python app.py
```

### 3. Abrir dashboard:
```bash
cd ../frontend
# Abra index.html no navegador
# Ou use um servidor simples:
python -m http.server 8000
# Acesse: http://localhost:8000
```

---

## ✅ Funcionalidades do Dashboard

- ✅ **Cards estatísticos** em tempo real
- ✅ **Mapa interativo** com todas as coletas
- ✅ **Ranking de espécies** ordenado
- ✅ **Estatísticas por praia**
- ✅ **Timeline** com gráfico Chart.js
- ✅ **API REST** completa
- ✅ **Auto-atualização** a cada 30s
- ✅ **Design responsivo**

---

## 🎓 O que você aprendeu

- ✅ Criar API REST com Flask
- ✅ Integrar Python (backend) + JavaScript (frontend)
- ✅ Consumir APIs com fetch()
- ✅ Manipular DOM dinamicamente
- ✅ Criar gráficos com Chart.js
- ✅ Mapas Leaflet integrados
- ✅ Dashboard profissional completo

---

## 🚀 Melhorias Futuras

1. **Banco de dados:** Substituir JSON por PostgreSQL/PostGIS
2. **Autenticação:** Login de usuários
3. **Exportação:** PDF/Excel dos relatórios
4. **Upload:** Enviar novos dados via formulário
5. **Deploy:** Hospedar na nuvem (Heroku, AWS, Azure)

---

**Parabéns!** Você criou um sistema web completo de ponta a ponta! 🎉🌐
