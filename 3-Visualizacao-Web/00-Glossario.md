# 📖 Glossário - Visualização Web

## A

**API (Application Programming Interface)**: Interface que permite comunicação entre sistemas/aplicações.

**AJAX (Asynchronous JavaScript and XML)**: Técnica para atualizar partes de página sem recarregar.

**Atributo HTML**: Informação adicional em tag HTML (ex: `class="container"`).

## B

**Bootstrap**: Framework CSS popular para design responsivo.

**Browser (Navegador)**: Software para acessar páginas web (Chrome, Firefox, Edge).

## C

**Canvas**: Elemento HTML5 para desenho gráfico com JavaScript.

**Cascata (CSS Cascade)**: Mecanismo que resolve conflitos entre regras CSS.

**CDN (Content Delivery Network)**: Rede de servidores para entregar recursos web rapidamente.

**Class (Classe CSS)**: Seletor reutilizável para estilizar múltiplos elementos.

**Console**: Ferramenta do navegador para debugar JavaScript (F12).

**CSS (Cascading Style Sheets)**: Linguagem para estilizar páginas HTML.

## D

**Dev Tools (Ferramentas de Desenvolvimento)**: Conjunto de ferramentas no navegador para depuração (F12).

**DIV**: Elemento HTML genérico para agrupar conteúdo.

**DOM (Document Object Model)**: Representação em árvore de documento HTML que JavaScript pode manipular.

**Deploy**: Processo de publicar aplicação na web.

## E

**Elemento**: Unidade básica de HTML delimitada por tags (`<tag>conteúdo</tag>`).

**Evento**: Ação que ocorre na página (click, hover, load).

**Event Listener**: Função JavaScript que "escuta" eventos.

## F

**Flexbox**: Sistema CSS para layout flexível e responsivo.

**Folium**: Biblioteca Python para criar mapas interativos Leaflet.

**Framework**: Conjunto de ferramentas e padrões para desenvolvimento.

**Frontend**: Parte da aplicação que usuário vê e interage.

## G

**GeoJSON Layer**: Camada Leaflet para exibir dados GeoJSON.

**Git**: Sistema de controle de versão.

**GitHub**: Plataforma web para hospedar repositórios Git.

**GitHub Pages**: Serviço gratuito do GitHub para hospedar sites estáticos.

## H

**HTML (HyperText Markup Language)**: Linguagem de marcação para estruturar páginas web.

**HTML5**: Versão mais recente do HTML com novos elementos (video, canvas, etc).

**HTTP/HTTPS**: Protocolos de comunicação da web (HTTPS é seguro).

## I

**ID (Identificador)**: Atributo HTML único para elemento (`id="mapa"`).

**Inline Style**: Estilo CSS aplicado diretamente no atributo `style=""`.

**Inspetor**: Ferramenta do navegador para ver/editar HTML e CSS.

## J

**JavaScript (JS)**: Linguagem de programação para interatividade web.

**jQuery**: Biblioteca JavaScript para simplificar manipulação DOM (menos usada hoje).

**JSON (JavaScript Object Notation)**: Formato de dados estruturados em texto.

## L

**Layer (Camada)**: Conjunto de elementos visuais em mapa (marcadores, polígonos).

**Leaflet**: Biblioteca JavaScript para mapas interativos.

**Link**: Elemento HTML para vincular recursos (`<link>` para CSS, `<a>` para hiperlinks).

## M

**Marcação (Markup)**: Código que estrutura conteúdo (HTML é linguagem de marcação).

**Marcador (Marker)**: Ícone que indica ponto no mapa Leaflet.

**Mapa Base (Base Layer)**: Camada de fundo do mapa (satélite, ruas, terreno).

**Media Query**: Regra CSS que aplica estilos baseado em tamanho de tela.

## N

**Node.js**: Ambiente JavaScript fora do navegador.

**npm**: Gerenciador de pacotes JavaScript.

## O

**OpenStreetMap**: Projeto colaborativo de mapa mundial livre.

**Overlay**: Camada sobreposta ao mapa base.

## P

**Popup**: Janela informativa que aparece ao clicar em marcador/área.

**Python Web Server**: Servidor simples para testar páginas localmente.

## Q

**Query Selector**: Método JavaScript para selecionar elementos (`querySelector('#id')`).

## R

**Repositório**: Pasta de projeto com histórico Git.

**Responsivo**: Design que se adapta a diferentes tamanhos de tela.

## S

**Script**: Código JavaScript em página HTML (`<script>`).

**Seletor CSS**: Padrão para identificar elementos (`.class`, `#id`, `tag`).

**Semantic HTML**: Uso de tags HTML que descrevem significado do conteúdo (`<header>`, `<nav>`, `<article>`).

**Servidor Web**: Software que entrega páginas web ao navegador.

**SEO (Search Engine Optimization)**: Otimização para mecanismos de busca.

**SPA (Single Page Application)**: Aplicação web que carrega uma página e atualiza dinamicamente.

## T

**Tag**: Marcador HTML que define elemento (`<tag>`).

**Template**: Modelo/padrão de documento HTML.

**Tile Layer**: Camada de mapa composta por ladrilhos de imagens.

## U

**URL (Uniform Resource Locator)**: Endereço de recurso na web.

**User Agent**: Identificação do navegador do usuário.

## V

**Validação HTML**: Processo de verificar se HTML está correto.

**var/let/const**: Formas de declarar variáveis em JavaScript.

**ViewPort**: Área visível da página no navegador.

## W

**Web Mapping**: Criação e visualização de mapas interativos na web.

**Webhook**: URL que recebe notificações automáticas.

## X

**XMLHttpRequest**: API para fazer requisições HTTP em JavaScript (substituída por `fetch()`).

## Exemplos Práticos

### HTML5 Básico
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Mapa</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Monitoramento Costeiro</h1>
    </header>
    
    <main>
        <div id="mapa"></div>
    </main>
    
    <script src="app.js"></script>
</body>
</html>
```

### JavaScript Essencial
```javascript
// Selecionar elemento
const mapa = document.getElementById('mapa');

// Criar elemento
const marker = document.createElement('div');
marker.className = 'marker';
marker.textContent = 'Local';

// Adicionar à página
mapa.appendChild(marker);

// Escutar evento
marker.addEventListener('click', function() {
    alert('Você clicou no marcador!');
});

// Fetch de dados
fetch('dados.json')
    .then(response => response.json())
    .then(dados => {
        console.log(dados);
    });
```

### Mapa Leaflet
```javascript
// Criar mapa
var mapa = L.map('mapa').setView([-27.5, -48.5], 10);

// Adicionar camada base
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(mapa);

// Adicionar marcador
L.marker([-27.43, -48.45])
    .addTo(mapa)
    .bindPopup('Praia dos Ingleses');

// Adicionar GeoJSON
fetch('pontos.geojson')
    .then(response => response.json())
    .then(dados => {
        L.geoJSON(dados).addTo(mapa);
    });
```

### CSS Responsivo
```css
/* Estilos base */
#mapa {
    width: 100%;
    height: 500px;
}

/* Mobile */
@media (max-width: 768px) {
    #mapa {
        height: 300px;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    #mapa {
        height: 700px;
    }
}
```

## Recursos Úteis

| Ferramenta | Uso | URL |
|------------|-----|-----|
| Leaflet | Mapas interativos | leafletjs.com |
| OpenStreetMap | Mapa base livre | openstreetmap.org |
| GitHub Pages | Hospedar site | pages.github.com |
| MDN Web Docs | Documentação web | developer.mozilla.org |

---

💡 **Dica**: Use sempre `<!DOCTYPE html>` no início do arquivo HTML5!
