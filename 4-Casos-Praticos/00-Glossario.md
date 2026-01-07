# 📖 Glossário - Casos Práticos

## A

**Análise Espacial**: Estudo de padrões, processos e relações espaciais de fenômenos.

**Automação**: Uso de scripts para executar tarefas repetitivas automaticamente.

**API REST**: Interface de programação que usa protocolo HTTP para comunicação.

## B

**Biodiversidade**: Variedade de vida em diferentes níveis (espécies, genes, ecossistemas).

**Baseline**: Linha de referência ou condição inicial para comparação.

## C

**Coastal Monitoring (Monitoramento Costeiro)**: Acompanhamento sistemático de mudanças em áreas litorâneas.

**Coleta de Dados**: Processo de obter informações para análise.

**Concentração**: Quantidade de substância em volume/área específico.

**Configuração**: Ajustes e parâmetros de sistema ou aplicação.

## D

**Dashboard**: Painel visual com informações resumidas e gráficos.

**Dados Ambientais**: Informações sobre meio ambiente (temperatura, poluição, etc).

**Dataset**: Conjunto de dados relacionados.

**Deploy Automático**: Publicação automática de aplicação quando código é atualizado.

**Distribuição Espacial**: Como fenômeno está disperso geograficamente.

## E

**Ecossistema**: Conjunto de organismos e ambiente físico interagindo.

**Erosão Costeira**: Desgaste e remoção de material da costa por ondas e correntes.

**Espécie**: Grupo de organismos que podem se reproduzir entre si.

**ETL (Extract, Transform, Load)**: Processo de extrair, transformar e carregar dados.

## F

**Filtro**: Operação que seleciona subconjunto de dados baseado em critério.

**Folium**: Biblioteca Python para criar mapas interativos.

**Frontend**: Interface visual de aplicação que usuário vê.

## G

**Geolocalização**: Identificação de posição geográfica de objeto/pessoa.

**Gradiente**: Variação gradual de valor ao longo do espaço.

**Gráfico Interativo**: Visualização que permite exploração dinâmica dos dados.

## H

**Heatmap (Mapa de Calor)**: Visualização que usa cor para mostrar intensidade/densidade.

**HTML Dinâmico**: Página web que muda conteúdo sem recarregar.

**Hospedagem**: Serviço que mantém site/aplicação acessível na internet.

## I

**Indicador Ambiental**: Métrica que representa condição ambiental.

**Integração**: Conexão entre diferentes sistemas/componentes.

**Interface**: Meio de interação entre usuário e sistema.

## L

**Layout Responsivo**: Design que se adapta a diferentes tamanhos de tela.

**Log**: Registro de eventos/ações em sistema.

## M

**Machine Learning**: Técnicas computacionais para aprender padrões em dados.

**Metadados**: Dados que descrevem outros dados (autor, data, fonte).

**Monitoramento**: Observação sistemática e contínua de fenômeno.

**Multiespectral**: Dados capturados em múltiplas faixas do espectro eletromagnético.

## N

**Normalização**: Ajuste de dados para escala comum.

**Notebook**: Documento interativo misturando código, texto e visualizações.

## O

**Observação**: Registro individual de medição ou evento.

**Outlier**: Valor atípico que destoa do padrão geral.

## P

**Padrão Espacial**: Arranjo não-aleatório de fenômenos no espaço.

**Parâmetro**: Valor que controla comportamento de função/sistema.

**Pipeline**: Sequência automatizada de etapas de processamento.

**Plotly**: Biblioteca para criar gráficos interativos.

**Ponto de Coleta**: Local onde amostra foi obtida.

**Predição**: Estimativa de valor futuro baseada em modelo.

**Projeto**: Conjunto organizado de arquivos e configurações.

## Q

**Qualidade da Água**: Condições químicas, físicas e biológicas de corpo d'água.

**Query**: Consulta para buscar dados específicos.

## R

**Rastro (Track)**: Sequência de posições mostrando movimento ao longo do tempo.

**Relatório Automático**: Documento gerado automaticamente com dados atualizados.

**Repositório**: Local onde código e arquivos de projeto são armazenados.

**Resolução Espacial**: Tamanho mínimo de feição detectável em imagem/mapa.

**ROI (Region of Interest)**: Área geográfica de interesse para análise.

## S

**Salinidade**: Quantidade de sal dissolvido em água.

**Sensor**: Dispositivo que detecta e mede fenômenos físicos.

**Script**: Programa automatizado para executar tarefas.

**Série Temporal**: Sequência de observações ao longo do tempo.

**Sistema**: Conjunto integrado de componentes interagindo.

## T

**Template**: Modelo base reutilizável para criar documentos/páginas.

**Threshold (Limiar)**: Valor que define limite para decisão/classificação.

**Timezone**: Fuso horário.

**Tooltip**: Dica informativa que aparece ao passar mouse sobre elemento.

**Transecto**: Linha ao longo da qual observações são feitas.

## V

**Validação**: Verificação de dados/resultados para garantir qualidade.

**Variável Ambiental**: Característica mensurável do ambiente.

**Visualização**: Representação gráfica de dados.

## W

**Workflow (Fluxo de Trabalho)**: Sequência de etapas para completar tarefa.

**Web App**: Aplicação que roda no navegador.

## Exemplos Práticos

### Dashboard Completo com Plotly
```python
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Carregar dados
df = pd.read_csv('monitoramento_costeiro.csv', parse_dates=['data'])

# Criar dashboard com subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Temperatura', 'Salinidade', 'pH', 'Tendência'),
    specs=[[{"type": "scatter"}, {"type": "scatter"}],
           [{"type": "scatter"}, {"type": "scatter"}]]
)

# Gráfico 1: Temperatura
fig.add_trace(
    go.Scatter(x=df['data'], y=df['temperatura'], name='Temp'),
    row=1, col=1
)

# Gráfico 2: Salinidade
fig.add_trace(
    go.Scatter(x=df['data'], y=df['salinidade'], name='Sal'),
    row=1, col=2
)

# Gráfico 3: pH
fig.add_trace(
    go.Scatter(x=df['data'], y=df['ph'], name='pH'),
    row=2, col=1
)

# Gráfico 4: Tendência
media_movel = df.groupby(df['data'].dt.to_period('M'))['temperatura'].mean()
fig.add_trace(
    go.Scatter(x=media_movel.index.astype(str), y=media_movel.values, name='Média'),
    row=2, col=2
)

# Layout
fig.update_layout(
    height=800,
    title_text="Dashboard de Monitoramento Costeiro",
    showlegend=True
)

fig.write_html('dashboard.html')
print("Dashboard gerado: dashboard.html")
```

### Análise de Distribuição Espacial
```python
import geopandas as gpd
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix

# Carregar dados
pontos = gpd.read_file('coletas.geojson')

# Calcular densidade por área
from shapely.geometry import box
bbox = pontos.total_bounds
area = gpd.GeoDataFrame(geometry=[box(*bbox)], crs=pontos.crs)
area_km2 = area.to_crs('EPSG:31982').area[0] / 1_000_000

densidade = len(pontos) / area_km2
print(f"Densidade: {densidade:.2f} pontos/km²")

# Calcular distância média entre pontos
coords = list(zip(pontos.geometry.x, pontos.geometry.y))
dist_matrix = distance_matrix(coords, coords)
dist_media = dist_matrix[dist_matrix > 0].mean()
print(f"Distância média: {dist_media:.4f}°")

# Plotar mapa de calor
fig, ax = plt.subplots(figsize=(12, 10))
pontos.plot(column='abundancia', cmap='YlOrRd', legend=True, ax=ax)
ax.set_title('Distribuição Espacial de Espécies')
plt.savefig('distribuicao.png', dpi=300, bbox_inches='tight')
```

### Automação de Relatório
```python
from datetime import datetime
import folium

def gerar_relatorio_automatico(dados_csv, saida_html):
    """Gera relatório HTML com mapa e estatísticas"""
    
    # Carregar dados
    df = pd.read_csv(dados_csv)
    
    # Calcular estatísticas
    stats = df.describe()
    ultima_coleta = df['data'].max()
    
    # Criar mapa
    mapa = folium.Map(location=[-27.5, -48.5], zoom_start=10)
    
    for idx, row in df.iterrows():
        folium.Marker(
            [row['lat'], row['lon']],
            popup=f"{row['nome']}<br>Temp: {row['temperatura']}°C",
            icon=folium.Icon(color='blue')
        ).add_to(mapa)
    
    # HTML do relatório
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Relatório - {datetime.now().strftime('%Y-%m-%d')}</title>
        <style>
            body {{ font-family: Arial; margin: 20px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            td, th {{ border: 1px solid #ddd; padding: 8px; }}
        </style>
    </head>
    <body>
        <h1>Relatório de Monitoramento Costeiro</h1>
        <p><strong>Gerado em:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
        <p><strong>Última coleta:</strong> {ultima_coleta}</p>
        
        <h2>Estatísticas</h2>
        {stats.to_html()}
        
        <h2>Mapa de Pontos</h2>
        {mapa._repr_html_()}
    </body>
    </html>
    """
    
    with open(saida_html, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Relatório gerado: {saida_html}")

# Usar
gerar_relatorio_automatico('coletas.csv', 'relatorio.html')
```

## Workflow Típico

```mermaid
Coleta → Limpeza → Análise → Visualização → Dashboard → Publicação
```

1. **Coleta**: Obter dados de sensores/planilhas
2. **Limpeza**: Remover erros e normalizar
3. **Análise**: Calcular estatísticas e padrões
4. **Visualização**: Criar gráficos e mapas
5. **Dashboard**: Integrar tudo em painel
6. **Publicação**: Disponibilizar na web

---

💡 **Dica**: Sempre documente seu workflow para facilitar automação futura!
