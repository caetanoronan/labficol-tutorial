# ⚡ JavaScript Essencial - Interatividade Web

## O que é JavaScript?

**JavaScript** = linguagem de programação para web (navegadores).

```
HTML       → Conteúdo estático
CSS        → Aparência estática
JavaScript → Comportamento dinâmico
```

**JavaScript faz:**
- Responder a cliques
- Validar formulários
- Processar dados
- Atualizar conteúdo sem recarregar página
- Criar animações

---

## 📝 Adicionar JavaScript ao HTML

### Método 1: Inline (dentro de tag)

```html
<button onclick="alert('Olá!')">Clique Aqui</button>
```

### Método 2: No `<script>` interno

```html
<!DOCTYPE html>
<html>
<head>
    <title>Minha Página</title>
</head>
<body>
    <h1 id="titulo">LABFICOL</h1>
    <button onclick="mudarTitulo()">Mudar Título</button>
    
    <script>
        function mudarTitulo() {
            document.getElementById('titulo').textContent = 'Oceanografia UFSC';
        }
    </script>
</body>
</html>
```

### Método 3: Arquivo externo (RECOMENDADO)

Crie `script.js`:

```javascript
function mudarTitulo() {
    document.getElementById('titulo').textContent = 'Oceanografia UFSC';
}
```

No HTML:

```html
<body>
    <h1 id="titulo">LABFICOL</h1>
    <button onclick="mudarTitulo()">Mudar Título</button>
    
    <script src="script.js"></script>
</body>
```

---

## 🔤 Sintaxe Básica

### Variáveis

```javascript
// var (antigo - evitar)
var nome = "Caetano";

// let (moderno - pode mudar)
let temperatura = 22.5;
temperatura = 23.0;  // OK

// const (constante - não muda)
const PI = 3.14159;
// PI = 3.14;  // ERRO!
```

### Tipos de Dados

```javascript
// String (texto)
let especie = "Ulva lactuca";
let local = 'Ingleses';  // aspas simples ou duplas

// Number (número)
let profundidade = 5.2;
let quantidade = 10;

// Boolean (verdadeiro/falso)
let valida = true;
let coletada = false;

// Array (lista)
let especies = ["Ulva", "Gracilaria", "Sargassum"];
let temperaturas = [22.5, 23.1, 22.8];

// Object (objeto)
let amostra = {
    especie: "Ulva lactuca",
    profundidade: 5.2,
    temperatura: 22.5,
    valida: true
};
```

### Operadores

```javascript
// Aritméticos
let soma = 10 + 5;          // 15
let subtracao = 10 - 5;     // 5
let multiplicacao = 10 * 5; // 50
let divisao = 10 / 5;       // 2
let resto = 10 % 3;         // 1

// Comparação
console.log(10 == "10");    // true (valor igual)
console.log(10 === "10");   // false (valor E tipo iguais)
console.log(10 != 5);       // true
console.log(10 > 5);        // true

// Lógicos
console.log(true && false); // false (E)
console.log(true || false); // true (OU)
console.log(!true);         // false (NÃO)
```

---

## 🔧 Funções

```javascript
// Função simples
function saudar() {
    console.log("Olá, LABFICOL!");
}

saudar();  // Chamar função

// Função com parâmetros
function calcularMedia(a, b, c) {
    return (a + b + c) / 3;
}

let media = calcularMedia(22.5, 23.1, 22.8);
console.log(media);  // 22.8

// Arrow function (moderna)
const quadrado = (x) => x * x;
console.log(quadrado(5));  // 25

// Função com objeto
function validarAmostra(temp, prof) {
    if (temp >= 20 && temp <= 25 && prof < 10) {
        return { valida: true, mensagem: "✓ VÁLIDA" };
    } else {
        return { valida: false, mensagem: "✗ INVÁLIDA" };
    }
}

let resultado = validarAmostra(22.5, 5.2);
console.log(resultado.mensagem);  // "✓ VÁLIDA"
```

---

## 🎯 Manipular o DOM (Document Object Model)

DOM = representação da página HTML que JavaScript pode modificar.

### Selecionar Elementos

```javascript
// Por ID
let titulo = document.getElementById('titulo');

// Por classe
let elementos = document.getElementsByClassName('destaque');

// Por tag
let paragrafos = document.getElementsByTagName('p');

// Query Selector (moderno - mais flexível)
let primeiroP = document.querySelector('p');
let todosP = document.querySelectorAll('p');
```

### Modificar Conteúdo

```javascript
// Alterar texto
document.getElementById('titulo').textContent = 'Novo Título';

// Alterar HTML
document.getElementById('container').innerHTML = '<p>Novo parágrafo</p>';

// Alterar atributos
let imagem = document.getElementById('foto');
imagem.src = 'nova_foto.jpg';
imagem.alt = 'Nova descrição';
```

### Modificar Estilo

```javascript
let elemento = document.getElementById('caixa');

// Alterar CSS
elemento.style.color = 'blue';
elemento.style.backgroundColor = '#f0f0f0';
elemento.style.fontSize = '20px';
elemento.style.display = 'none';  // Esconder

// Adicionar/remover classe
elemento.classList.add('destaque');
elemento.classList.remove('destaque');
elemento.classList.toggle('ativo');  // Alterna
```

---

## 🖱️ Eventos (Interatividade)

### Click

```javascript
// Método 1: HTML
<button onclick="minhaFuncao()">Clique</button>

// Método 2: JavaScript (RECOMENDADO)
document.getElementById('botao').addEventListener('click', function() {
    alert('Botão clicado!');
});

// Método 3: Arrow function
document.getElementById('botao').addEventListener('click', () => {
    alert('Botão clicado!');
});
```

### Outros Eventos

```javascript
// Mouse
elemento.addEventListener('mouseover', () => {
    console.log('Mouse em cima');
});

elemento.addEventListener('mouseout', () => {
    console.log('Mouse saiu');
});

// Teclado
input.addEventListener('keyup', (event) => {
    console.log('Tecla pressionada:', event.key);
});

// Formulário
formulario.addEventListener('submit', (event) => {
    event.preventDefault();  // Evitar envio padrão
    console.log('Formulário enviado');
});

// Página carregada
document.addEventListener('DOMContentLoaded', () => {
    console.log('Página carregada!');
});
```

---

## 📊 Trabalhar com Arrays

```javascript
let especies = ["Ulva", "Gracilaria", "Sargassum"];

// Acessar
console.log(especies[0]);  // "Ulva"

// Adicionar
especies.push("Laminaria");  // Adiciona no final
especies.unshift("Codium");  // Adiciona no início

// Remover
let ultimo = especies.pop();     // Remove e retorna último
let primeiro = especies.shift(); // Remove e retorna primeiro

// Tamanho
console.log(especies.length);  // 3

// Iterar
especies.forEach((especie, index) => {
    console.log(`${index}: ${especie}`);
});

// Map (transformar)
let maiusculas = especies.map(e => e.toUpperCase());

// Filter (filtrar)
let comU = especies.filter(e => e.startsWith('U'));

// Find (encontrar)
let gracilaria = especies.find(e => e === 'Gracilaria');
```

---

## 🎯 Exemplo Prático 1: Calculadora Oceanográfica

Crie `calculadora.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Calculadora Oceanográfica</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f0f8ff;
        }
        
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        h1 {
            color: #2E86AB;
            text-align: center;
        }
        
        .form-group {
            margin-bottom: 15px;
        }
        
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box;
        }
        
        button {
            width: 100%;
            padding: 12px;
            background-color: #2E86AB;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        
        button:hover {
            background-color: #236a8c;
        }
        
        #resultado {
            margin-top: 20px;
            padding: 15px;
            border-radius: 5px;
            display: none;
        }
        
        .valida {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
        }
        
        .invalida {
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌊 Calculadora Oceanográfica</h1>
        
        <div class="form-group">
            <label for="profundidade">Profundidade (m):</label>
            <input type="number" id="profundidade" step="0.1" placeholder="Ex: 5.2">
        </div>
        
        <div class="form-group">
            <label for="temperatura">Temperatura (°C):</label>
            <input type="number" id="temperatura" step="0.1" placeholder="Ex: 22.5">
        </div>
        
        <div class="form-group">
            <label for="salinidade">Salinidade (PSU):</label>
            <input type="number" id="salinidade" step="0.1" placeholder="Ex: 35.0">
        </div>
        
        <button onclick="calcular()">Calcular</button>
        
        <div id="resultado"></div>
    </div>
    
    <script>
        function calcular() {
            // Obter valores
            const prof = parseFloat(document.getElementById('profundidade').value);
            const temp = parseFloat(document.getElementById('temperatura').value);
            const sal = parseFloat(document.getElementById('salinidade').value);
            
            // Validar entrada
            if (isNaN(prof) || isNaN(temp) || isNaN(sal)) {
                alert('Por favor, preencha todos os campos!');
                return;
            }
            
            // Cálculos
            const pressao = 1 + (prof / 10);  // 1 atm por 10m
            const densidade = 1000 + (sal - 35) * 0.78;  // Simplificado
            const luzPenetracao = 100 * Math.pow(0.7, prof / 10);
            
            // Validação
            const tempValida = temp >= 20 && temp <= 25;
            const salValida = sal >= 34 && sal <= 36;
            const profValida = prof < 50;
            const todasValidas = tempValida && salValida && profValida;
            
            // Montar resultado
            let html = `
                <h3>${todasValidas ? '✅' : '⚠️'} Resultados:</h3>
                <p><strong>Pressão:</strong> ${pressao.toFixed(2)} atm</p>
                <p><strong>Densidade:</strong> ${densidade.toFixed(2)} kg/m³</p>
                <p><strong>Penetração de Luz:</strong> ${luzPenetracao.toFixed(1)}%</p>
                <hr>
                <h4>Validação:</h4>
                <p>Temperatura: ${tempValida ? '✓' : '✗'} ${temp}°C</p>
                <p>Salinidade: ${salValida ? '✓' : '✗'} ${sal} PSU</p>
                <p>Profundidade: ${profValida ? '✓' : '✗'} ${prof}m</p>
                <hr>
                <p><strong>Status: ${todasValidas ? 'CONDIÇÕES IDEAIS' : 'ATENÇÃO AOS PARÂMETROS'}</strong></p>
            `;
            
            // Mostrar resultado
            const divResultado = document.getElementById('resultado');
            divResultado.innerHTML = html;
            divResultado.className = todasValidas ? 'valida' : 'invalida';
            divResultado.style.display = 'block';
        }
        
        // Permitir Enter para calcular
        document.addEventListener('keyup', (event) => {
            if (event.key === 'Enter') {
                calcular();
            }
        });
    </script>
</body>
</html>
```

Teste no navegador! 🧮

---

## 🎯 Exemplo Prático 2: Tabela Dinâmica de Coletas

Crie `tabela_dinamica.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Gerenciador de Coletas</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 30px auto;
            padding: 20px;
        }
        
        h1 {
            color: #2E86AB;
        }
        
        .form-container {
            background: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }
        
        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        
        button {
            padding: 10px 20px;
            background-color: #2E86AB;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 10px;
        }
        
        button:hover {
            background-color: #236a8c;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        
        th {
            background-color: #2E86AB;
            color: white;
        }
        
        tr:hover {
            background-color: #f5f5f5;
        }
        
        .btn-remover {
            background-color: #dc3545;
            padding: 5px 10px;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <h1>📊 Gerenciador de Coletas - LABFICOL</h1>
    
    <div class="form-container">
        <h3>Adicionar Nova Coleta</h3>
        <div class="form-grid">
            <input type="text" id="local" placeholder="Local">
            <input type="text" id="especie" placeholder="Espécie">
            <input type="number" id="prof" step="0.1" placeholder="Profundidade (m)">
            <input type="number" id="temp" step="0.1" placeholder="Temperatura (°C)">
        </div>
        <button onclick="adicionarColeta()">➕ Adicionar Coleta</button>
    </div>
    
    <h3>Coletas Registradas: <span id="total">0</span></h3>
    <table id="tabela">
        <thead>
            <tr>
                <th>ID</th>
                <th>Local</th>
                <th>Espécie</th>
                <th>Profundidade</th>
                <th>Temperatura</th>
                <th>Status</th>
                <th>Ação</th>
            </tr>
        </thead>
        <tbody id="tbody">
        </tbody>
    </table>
    
    <script>
        let coletas = [];
        let proximoId = 1;
        
        function adicionarColeta() {
            // Obter valores
            const local = document.getElementById('local').value;
            const especie = document.getElementById('especie').value;
            const prof = parseFloat(document.getElementById('prof').value);
            const temp = parseFloat(document.getElementById('temp').value);
            
            // Validar
            if (!local || !especie || isNaN(prof) || isNaN(temp)) {
                alert('Preencha todos os campos!');
                return;
            }
            
            // Criar coleta
            const coleta = {
                id: proximoId++,
                local: local,
                especie: especie,
                profundidade: prof,
                temperatura: temp,
                valida: (temp >= 20 && temp <= 25 && prof < 10)
            };
            
            // Adicionar ao array
            coletas.push(coleta);
            
            // Limpar formulário
            document.getElementById('local').value = '';
            document.getElementById('especie').value = '';
            document.getElementById('prof').value = '';
            document.getElementById('temp').value = '';
            
            // Atualizar tabela
            atualizarTabela();
        }
        
        function removerColeta(id) {
            coletas = coletas.filter(c => c.id !== id);
            atualizarTabela();
        }
        
        function atualizarTabela() {
            const tbody = document.getElementById('tbody');
            tbody.innerHTML = '';
            
            coletas.forEach(coleta => {
                const tr = document.createElement('tr');
                
                const status = coleta.valida ? 
                    '<span style="color: green;">✓ VÁLIDA</span>' :
                    '<span style="color: red;">✗ ATENÇÃO</span>';
                
                tr.innerHTML = `
                    <td>${coleta.id}</td>
                    <td>${coleta.local}</td>
                    <td><em>${coleta.especie}</em></td>
                    <td>${coleta.profundidade.toFixed(1)}m</td>
                    <td>${coleta.temperatura.toFixed(1)}°C</td>
                    <td>${status}</td>
                    <td>
                        <button class="btn-remover" onclick="removerColeta(${coleta.id})">
                            🗑️ Remover
                        </button>
                    </td>
                `;
                
                tbody.appendChild(tr);
            });
            
            // Atualizar contador
            document.getElementById('total').textContent = coletas.length;
        }
    </script>
</body>
</html>
```

Teste adicionando e removendo coletas! ✨

---

## 🎓 Checklist desta Lição

- [ ] Entendo sintaxe JavaScript básica
- [ ] Consigo manipular o DOM
- [ ] Sei trabalhar com eventos
- [ ] Criei uma aplicação interativa
- [ ] Testei no navegador

Se marcou tudo, você está pronto para **Leaflet.js**! 🎉

---

## ➡️ Próximo Tópico

**👉 [03-Leaflet-Mapas.md](03-Leaflet-Mapas.md)**

Lá você aprenderá:
- Criar mapas com Leaflet.js
- Adicionar marcadores dinamicamente
- Integrar com dados JavaScript
- Criar dashboards completos

---

## 📝 Resumo de Conceitos

| Conceito | Descrição |
|----------|-----------|
| **DOM** | Representação da página HTML |
| **Event** | Ação do usuário (click, etc) |
| **querySelector** | Selecionar elementos |
| **addEventListener** | Escutar eventos |
| **innerHTML** | Modificar HTML |
| **classList** | Manipular classes CSS |

---

**Você domina JavaScript básico!** ⚡ Próximo: Mapas interativos com Leaflet! 🗺️
