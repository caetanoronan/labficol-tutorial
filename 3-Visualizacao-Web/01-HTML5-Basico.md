# 🌐 HTML5 Básico - Criar Páginas Web

## O que é HTML?

**HTML (HyperText Markup Language)** = linguagem de marcação para criar páginas web.

```
HTML        → Estrutura (conteúdo)
CSS         → Aparência (estilo)
JavaScript  → Comportamento (interação)
```

**Analogia:**
- HTML = Esqueleto de uma casa
- CSS = Pintura e decoração
- JavaScript = Eletricidade e encanamento

---

## 📝 Estrutura Básica de HTML

### Documento Mínimo

Crie arquivo `pagina.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Primeira Página</title>
</head>
<body>
    <h1>Olá, Mundo!</h1>
    <p>Esta é minha primeira página web.</p>
</body>
</html>
```

Abra no navegador (duplo clique ou arrastar para o navegador)!

### Anatomia de uma Tag

```html
<tagname atributo="valor">Conteúdo</tagname>
   ↑        ↑        ↑         ↑           ↑
 abertura  atrib   valor   conteúdo    fechamento
```

---

## 📋 Tags Essenciais

### Cabeçalhos (Títulos)

```html
<h1>Título Principal</h1>
<h2>Subtítulo</h2>
<h3>Seção</h3>
<h4>Subseção</h4>
<h5>Menor</h5>
<h6>Mínimo</h6>
```

### Parágrafos e Texto

```html
<p>Este é um parágrafo.</p>
<p>Este é outro parágrafo.</p>

<strong>Texto em negrito</strong>
<em>Texto em itálico</em>
<u>Texto sublinhado</u>
<br>  <!-- Quebra de linha -->
<hr>  <!-- Linha horizontal -->
```

### Listas

```html
<!-- Lista não ordenada (bullet points) -->
<ul>
    <li>Ulva lactuca</li>
    <li>Gracilaria</li>
    <li>Sargassum</li>
</ul>

<!-- Lista ordenada (numerada) -->
<ol>
    <li>Coletar amostra</li>
    <li>Identificar espécie</li>
    <li>Registrar dados</li>
</ol>
```

### Links

```html
<!-- Link externo -->
<a href="https://www.ufsc.br">Visite a UFSC</a>

<!-- Link em nova aba -->
<a href="https://www.ufsc.br" target="_blank">UFSC (nova aba)</a>

<!-- Link para email -->
<a href="mailto:contato@labficol.ufsc.br">Enviar email</a>
```

### Imagens

```html
<img src="macroalga.jpg" alt="Ulva lactuca" width="400">

<!-- Com legenda -->
<figure>
    <img src="macroalga.jpg" alt="Ulva lactuca" width="400">
    <figcaption>Figura 1: Ulva lactuca coletada em Ingleses</figcaption>
</figure>
```

---

## 📊 Tabelas

```html
<table border="1">
    <thead>
        <tr>
            <th>Espécie</th>
            <th>Profundidade (m)</th>
            <th>Temperatura (°C)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ulva lactuca</td>
            <td>5.2</td>
            <td>22.5</td>
        </tr>
        <tr>
            <td>Gracilaria</td>
            <td>7.8</td>
            <td>23.1</td>
        </tr>
        <tr>
            <td>Sargassum</td>
            <td>3.1</td>
            <td>22.8</td>
        </tr>
    </tbody>
</table>
```

---

## 🎨 CSS Básico (Estilo)

### CSS Inline (dentro da tag)

```html
<p style="color: blue; font-size: 20px;">Texto azul e grande</p>
```

### CSS no `<head>` (interno)

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f0f8ff;
        }
        
        h1 {
            color: #2E86AB;
            text-align: center;
        }
        
        .destaque {
            background-color: yellow;
            padding: 10px;
        }
    </style>
</head>
<body>
    <h1>LABFICOL - UFSC</h1>
    <p class="destaque">Texto destacado</p>
</body>
</html>
```

### CSS Externo (arquivo separado)

Crie `estilos.css`:

```css
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1 {
    color: #2E86AB;
}

.tabela-dados {
    border-collapse: collapse;
    width: 100%;
}

.tabela-dados th, .tabela-dados td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

.tabela-dados th {
    background-color: #2E86AB;
    color: white;
}
```

No HTML:

```html
<head>
    <link rel="stylesheet" href="estilos.css">
</head>
```

---

## 🎯 Exemplo Prático: Relatório de Coleta

Crie `relatorio_coleta.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Coleta - LABFICOL</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        header {
            background-color: #2E86AB;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        .secao {
            background-color: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        h2 {
            color: #2E86AB;
            border-bottom: 2px solid #2E86AB;
            padding-bottom: 10px;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
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
        
        .badge {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
        }
        
        .badge-valida {
            background-color: #28a745;
            color: white;
        }
        
        .badge-invalida {
            background-color: #dc3545;
            color: white;
        }
        
        .estatisticas {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }
        
        .stat-box {
            text-align: center;
            padding: 15px;
            background-color: #e7f3f8;
            border-radius: 8px;
            flex: 1;
            margin: 0 10px;
        }
        
        .stat-numero {
            font-size: 36px;
            font-weight: bold;
            color: #2E86AB;
        }
        
        .stat-label {
            font-size: 14px;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <h1>🌊 Relatório de Coleta de Macroalgas</h1>
        <p>LABFICOL - Laboratório de Ficologia / UFSC</p>
        <p>Data: 06 de Janeiro de 2025</p>
    </header>
    
    <div class="secao">
        <h2>📊 Estatísticas Gerais</h2>
        <div class="estatisticas">
            <div class="stat-box">
                <div class="stat-numero">10</div>
                <div class="stat-label">Total de Coletas</div>
            </div>
            <div class="stat-box">
                <div class="stat-numero">4</div>
                <div class="stat-label">Espécies Identificadas</div>
            </div>
            <div class="stat-box">
                <div class="stat-numero">22.7°C</div>
                <div class="stat-label">Temperatura Média</div>
            </div>
            <div class="stat-box">
                <div class="stat-numero">6.8m</div>
                <div class="stat-label">Profundidade Média</div>
            </div>
        </div>
    </div>
    
    <div class="secao">
        <h2>🗺️ Locais de Coleta</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Local</th>
                    <th>Espécie</th>
                    <th>Profundidade</th>
                    <th>Temperatura</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>Ingleses Norte</td>
                    <td><em>Ulva lactuca</em></td>
                    <td>5.2m</td>
                    <td>22.5°C</td>
                    <td><span class="badge badge-valida">✓ VÁLIDA</span></td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Ingleses Sul</td>
                    <td><em>Gracilaria</em></td>
                    <td>7.8m</td>
                    <td>23.1°C</td>
                    <td><span class="badge badge-valida">✓ VÁLIDA</span></td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Barra da Lagoa</td>
                    <td><em>Sargassum</em></td>
                    <td>3.1m</td>
                    <td>22.8°C</td>
                    <td><span class="badge badge-valida">✓ VÁLIDA</span></td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Laguna</td>
                    <td><em>Laminaria</em></td>
                    <td>10.5m</td>
                    <td>21.2°C</td>
                    <td><span class="badge badge-invalida">✗ ATENÇÃO</span></td>
                </tr>
            </tbody>
        </table>
    </div>
    
    <div class="secao">
        <h2>🌿 Espécies Coletadas</h2>
        <ul>
            <li><strong>Ulva lactuca</strong> - 4 amostras (40%)</li>
            <li><strong>Gracilaria</strong> - 3 amostras (30%)</li>
            <li><strong>Sargassum</strong> - 2 amostras (20%)</li>
            <li><strong>Laminaria</strong> - 1 amostra (10%)</li>
        </ul>
    </div>
    
    <div class="secao">
        <h2>📝 Observações</h2>
        <p>
            As coletas foram realizadas em condições favoráveis, com mar calmo e 
            visibilidade adequada. A maioria das amostras (90%) foi validada de acordo 
            com os parâmetros estabelecidos (temperatura entre 20-25°C, profundidade 
            menor que 10m).
        </p>
        <p>
            A espécie <em>Ulva lactuca</em> foi predominante na região de Ingleses, 
            corroborando estudos anteriores sobre sua distribuição na costa catarinense.
        </p>
    </div>
    
    <footer style="text-align: center; padding: 20px; color: #666;">
        <p>
            <strong>LABFICOL - Laboratório de Ficologia</strong><br>
            Departamento de Botânica - UFSC<br>
            Florianópolis, Santa Catarina, Brasil
        </p>
    </footer>
</body>
</html>
```

Abra no navegador! Você verá um relatório profissional! 📊

---

## 📱 Design Responsivo

Fazer a página se adaptar a diferentes tamanhos de tela:

```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Desktop */
        .container {
            display: flex;
            gap: 20px;
        }
        
        .coluna {
            flex: 1;
        }
        
        /* Mobile (telas menores que 768px) */
        @media (max-width: 768px) {
            .container {
                flex-direction: column;
            }
        }
    </style>
</head>
```

---

## 🎓 Formulários

Coletar dados do usuário:

```html
<form action="/processar" method="POST">
    <label for="especie">Espécie:</label>
    <input type="text" id="especie" name="especie" required>
    
    <label for="profundidade">Profundidade (m):</label>
    <input type="number" id="profundidade" name="profundidade" step="0.1" required>
    
    <label for="temperatura">Temperatura (°C):</label>
    <input type="number" id="temperatura" name="temperatura" step="0.1" required>
    
    <label for="local">Local:</label>
    <select id="local" name="local">
        <option value="ingleses">Praia dos Ingleses</option>
        <option value="laguna">Laguna</option>
        <option value="garopaba">Garopaba</option>
    </select>
    
    <label for="observacoes">Observações:</label>
    <textarea id="observacoes" name="observacoes" rows="4"></textarea>
    
    <button type="submit">Enviar</button>
</form>
```

---

## 🎓 Checklist desta Lição

- [ ] Entendo a estrutura básica de HTML
- [ ] Conheço as principais tags
- [ ] Criei uma tabela HTML
- [ ] Apliquei CSS básico
- [ ] Criei um relatório formatado
- [ ] Testei no navegador

Se marcou tudo, você está pronto para **JavaScript**! 🎉

---

## ➡️ Próximo Tópico

**👉 [02-JavaScript-Essencial.md](02-JavaScript-Essencial.md)**

Lá você aprenderá:
- Sintaxe JavaScript
- Manipular elementos HTML
- Interatividade
- Processar dados

---

## 📝 Resumo de Tags

| Tag | Uso |
|-----|-----|
| `<h1>-<h6>` | Títulos |
| `<p>` | Parágrafo |
| `<a>` | Link |
| `<img>` | Imagem |
| `<table>` | Tabela |
| `<ul>/<ol>` | Listas |
| `<div>` | Container genérico |
| `<span>` | Texto inline |

---

**Você criou sua primeira página web!** 🌐 Próximo: JavaScript para interatividade! ⚡
