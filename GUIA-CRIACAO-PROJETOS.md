# 🚀 Guia Completo para Criação de Projetos Educacionais
## Do Planejamento à Publicação

---

## 📋 ÍNDICE RÁPIDO

1. [Fase 1: Planejamento](#fase-1-planejamento)
2. [Fase 2: Estruturação](#fase-2-estruturação)
3. [Fase 3: Criação de Conteúdo](#fase-3-criação-de-conteúdo)
4. [Fase 4: Geração de HTML](#fase-4-geração-de-html)
5. [Fase 5: Publicação](#fase-5-publicação)
6. [Fase 6: Manutenção](#fase-6-manutenção)
7. [Roteiro para QGIS](#roteiro-qgis)
8. [Checklist Completo](#checklist-completo)

---

## 🎯 FASE 1: PLANEJAMENTO

### 1.1 Definir Objetivo e Público-Alvo

**Perguntas essenciais:**
- ❓ **Para quem** é este tutorial? (técnico, graduação, pós-graduação?)
- ❓ **Qual o objetivo final** do aluno ao completar? (fazer mapas, analisar dados, criar dashboards?)
- ❓ **Quanto tempo** eles terão disponível? (1 semana, 1 mês, 1 semestre?)
- ❓ **Qual o conhecimento prévio** necessário? (zero, básico, intermediário?)

**Exemplo do Tutorial Python:**
```markdown
Público: Biólogos, oceanógrafos (graduação e pós)
Objetivo: Criar mapas interativos e dashboards de pesquisa
Tempo: 120-160 horas (3-4 meses, 1h/dia)
Pré-requisitos: Nenhum
```

---

### 1.2 Estruturar Módulos e Progressão

**Princípio da progressão:** Do simples ao complexo, do concreto ao abstrato

**Template de estrutura:**
```
0-Fundamentos/          ← Sempre começar aqui
  01-Introducao.md      ← Por quê aprender?
  02-Configuracao.md    ← Como instalar ferramentas?
  03-Conceitos.md       ← Conceitos básicos essenciais

1-Modulo-Basico/        ← Habilidades fundamentais
  01-Primeira-Tarefa.md
  02-Segunda-Tarefa.md
  03-Terceira-Tarefa.md
  00-Glossario.md       ← Sempre incluir!

2-Modulo-Intermediario/ ← Aplicações práticas
  ...

N-Casos-Praticos/       ← Projetos completos reais
  01-Projeto-Real.md
```

**Regras de ouro:**
- ✅ Cada módulo deve ser **completável em 1-2 semanas**
- ✅ Cada lição deve ter **1 exemplo prático**
- ✅ Sempre incluir **glossário** por módulo
- ✅ Progressão: Fundamentos → Básico → Intermediário → Avançado → Casos Reais

---

### 1.3 Definir Tecnologias e Ferramentas

**Para Tutorial de Programação:**
```yaml
Linguagem: Python 3.10+
IDE: VS Code
Controle de versão: Git + GitHub
Publicação: GitHub Pages (gratuito)
Bibliotecas principais:
  - pandas (dados)
  - geopandas (geoespacial)
  - folium (mapas)
  - matplotlib (gráficos)
```

**Para Tutorial de QGIS (exemplo futuro):**
```yaml
Software: QGIS 3.34+
Plugins essenciais:
  - QuickMapServices
  - MMQGIS
  - Profile Tool
Formatos de dados:
  - Shapefile (.shp)
  - GeoPackage (.gpkg)
  - GeoJSON (.geojson)
Publicação: QGIS2Web → GitHub Pages
```

---

### 1.4 Planejar Exemplos e Datasets

**Regra crítica:** Use **dados reais** da área de estudo!

**Estrutura de exemplos:**
```
exemplos/
  dados/
    coletas_2024.csv          ← Dados reais anonimizados
    estacoes.geojson          ← Coordenadas reais
    temperatura_mar.csv       ← Séries temporais
  exercicios/
    01_exercicio_basico.py    ← Código inicial
    01_exercicio_solucao.py   ← Solução completa
  projetos/
    dashboard_completo/       ← Projeto end-to-end
```

**Características de bons exemplos:**
- ✅ **Realistas:** Dados que o aluno encontrará na vida real
- ✅ **Relevantes:** Relacionados à área de estudo (oceanografia, biologia)
- ✅ **Incrementais:** Cada exemplo adiciona 1-2 conceitos novos
- ✅ **Testados:** Todos devem funcionar sem erros

---

## 🏗️ FASE 2: ESTRUTURAÇÃO

### 2.1 Criar Repositório Git

```bash
# 1. Criar pasta do projeto
mkdir nome-do-tutorial
cd nome-do-tutorial

# 2. Inicializar Git
git init

# 3. Criar estrutura de pastas
mkdir -p 0-Fundamentos 1-Modulo-Basico 2-Modulo-Intermediario
mkdir -p exemplos/dados exemplos/exercicios
mkdir -p docs/assets docs/html
mkdir -p scripts

# 4. Criar arquivo README.md inicial
echo "# Nome do Tutorial" > README.md

# 5. Criar .gitignore
cat > .gitignore << EOF
__pycache__/
*.pyc
.venv/
*.log
.DS_Store
Thumbs.db
EOF

# 6. Primeiro commit
git add .
git commit -m "feat: Estrutura inicial do projeto"

# 7. Criar repositório no GitHub e conectar
git remote add origin https://github.com/seu-usuario/seu-repo.git
git branch -M main
git push -u origin main
```

---

### 2.2 Configurar Ambiente de Desenvolvimento

**requirements.txt** (para Python):
```txt
# Manipulação de dados
pandas>=2.0.0
numpy>=1.24.0

# Análise geoespacial
geopandas>=0.14.0
shapely>=2.0.0
folium>=0.15.0

# Visualização
matplotlib>=3.7.0
seaborn>=0.12.0

# Web e exportação
jinja2>=3.1.0

# Geração de documentação
markdown>=3.5.0
pygments>=2.16.0  # Syntax highlighting
```

**Instalação:**
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar (Windows)
.venv\Scripts\activate

# Ativar (Linux/Mac)
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

---

### 2.3 Criar Script de Geração HTML

**Copiar do projeto atual:**
```bash
# Use o build_site.py como base
cp ../labficol-tutorial/scripts/build_site.py scripts/

# Adaptar conforme necessário:
# - Mudar paleta de cores
# - Ajustar template HTML
# - Modificar estrutura de módulos
```

**Principais pontos de customização:**
```python
# 1. Paleta de cores (linha ~10)
COLORS = {
    'light': '#e5f5f9',    # Fundo claro
    'medium': '#99d8c9',   # Médio
    'dark': '#2ca25f',     # Escuro/destaque
}

# 2. Título do projeto (linha ~40)
TEMPLATE = """<!doctype html>
<html lang="pt-BR">
  <head>
    <title>{title} - Seu Tutorial</title>
    
# 3. Footer com seus dados (linha ~900)
<footer>
    <strong>Autor:</strong> Seu Nome<br>
    Sua Instituição<br>
```

---

## ✍️ FASE 3: CRIAÇÃO DE CONTEÚDO

### 3.1 Estrutura de uma Lição (Markdown)

**Template padrão:**
```markdown
# 📘 Título da Lição

> **Objetivos de aprendizagem:**
> - Objetivo 1 claro e mensurável
> - Objetivo 2 claro e mensurável
> - Objetivo 3 claro e mensurável

---

## 🎯 Introdução

Contextualização da lição:
- Por que este tópico é importante?
- Como se conecta com lições anteriores?
- Onde será usado na prática?

---

## 📚 Conceitos Fundamentais

### Conceito 1

Explicação clara com:
- Definição simples
- Analogia do mundo real
- Exemplo visual (se possível)

```python
# Exemplo de código comentado
def exemplo():
    """
    Código deve ser COMPLETO e EXECUTÁVEL
    """
    pass
```

### Conceito 2

Repita a estrutura...

---

## 💻 Exemplo Prático 1: [Nome Descritivo]

**Cenário real:**
> Você é um pesquisador que precisa [descrever situação real]

**Dados:**
- `arquivo.csv` - Descrição dos dados
- `coordenadas.geojson` - Descrição das coordenadas

**Código completo:**
```python
# Sempre incluir imports
import pandas as pd
import geopandas as gpd

# Código passo a passo com comentários
dados = pd.read_csv('dados.csv')

# Explicar CADA linha importante
print(dados.head())
```

**Saída esperada:**
```
[Mostrar output exato do código]
```

**Explicação:**
- Linha X faz Y porque Z
- Atenção ao detalhe W

---

## 🔬 Exemplo Prático 2: [Mais Avançado]

Repita estrutura, aumentando complexidade...

---

## 🎓 Exercícios

### Exercício 1: Nível Básico
**Enunciado:**
[Tarefa clara e específica]

**Dicas:**
- Dica 1
- Dica 2

**Solução:**
<details>
<summary>Clique para ver a solução</summary>

```python
# Solução completa comentada
```
</details>

### Exercício 2: Nível Intermediário
[Repetir estrutura]

### Exercício 3: Desafio
[Exercício que combina múltiplos conceitos]

---

## 📊 Checklist de Aprendizado

Ao final desta lição, você deve ser capaz de:

- [ ] Tarefa específica 1
- [ ] Tarefa específica 2
- [ ] Tarefa específica 3

---

## 🔗 Próximos Passos

- **Anterior:** [Nome da Lição Anterior](arquivo-anterior.md)
- **Próxima:** [Nome da Próxima Lição](proximo-arquivo.md)
- **Voltar ao Índice:** [Módulo X](index.md)

---

## 📚 Glossário Rápido

| Termo | Definição |
|-------|-----------|
| Termo 1 | Definição curta |
| Termo 2 | Definição curta |

> **Glossário completo:** [00-Glossario.md](00-Glossario.md)
```

---

### 3.2 Estrutura de um Glossário

**00-Glossario.md template:**
```markdown
# 📖 Glossário - [Nome do Módulo]

> Termos técnicos, conceitos e definições para consulta rápida

---

## A

### API (Application Programming Interface)
**Definição:** Interface que permite comunicação entre diferentes softwares.

**Exemplo em Python:**
```python
import requests
response = requests.get('https://api.exemplo.com/dados')
```

**Uso em Oceanografia:**
Acessar dados de boias oceanográficas, estações meteorológicas, etc.

**Veja também:** REST API, JSON, HTTP

---

## B

### Buffer (Área de Influência)
**Definição:** Polígono ao redor de uma geometria com distância especificada.

**Exemplo em GeoPandas:**
```python
# Criar buffer de 1km ao redor de pontos
pontos_gdf.buffer(1000)  # metros
```

**Uso em Ficologia:**
Definir área de influência de estações de coleta.

**Veja também:** Geometria, Shapely, CRS

---

[... continuar alfabeticamente ...]

---

## 📊 Tabela de Referência Rápida

### Sistemas de Coordenadas Comuns

| EPSG | Nome | Uso |
|------|------|-----|
| 4326 | WGS84 | GPS, web (lat/lon) |
| 3857 | Web Mercator | Mapas web (metros) |
| 31982 | SIRGAS 2000 / UTM 22S | Brasil Sul |

---

## 🔗 Recursos Externos

- [Documentação Python](https://docs.python.org/3/)
- [GeoPandas Docs](https://geopandas.org/)
- [EPSG.io](https://epsg.io/) - Buscar sistemas de coordenadas
```

---

### 3.3 Ordem de Criação de Conteúdo

**Recomendação (aprendida na prática):**

1. **Criar estrutura de pastas e arquivos vazios**
   ```bash
   touch 0-Fundamentos/01-Introducao.md
   touch 0-Fundamentos/02-Configuracao.md
   # etc...
   ```

2. **Escrever README.md geral** (visão do projeto completo)

3. **Criar 0-Fundamentos/** completamente
   - Introdução
   - Configuração (com screenshots!)
   - Conceitos básicos

4. **Para cada módulo seguinte:**
   - Escrever lição 01 (mais simples)
   - Testar TODOS os exemplos de código
   - Escrever lições 02, 03...
   - Criar glossário do módulo
   - Criar `index.md` do módulo

5. **Criar exemplos e exercícios**
   - Sempre criar versão inicial E solução
   - Testar com dados reais
   - Documentar datasets

6. **Revisão completa** antes de gerar HTML

---

## 🎨 FASE 4: GERAÇÃO DE HTML

### 4.1 Testar Geração Local

```bash
# Gerar todos os HTMLs
python scripts/build_site.py

# Verificar saída
ls docs/html/

# Abrir no navegador para testar
# Windows:
start docs/index.html

# Linux/Mac:
open docs/index.html
```

**Checklist de verificação:**
- [ ] Todos os links funcionam?
- [ ] Imagens carregam corretamente?
- [ ] Exemplos de código têm syntax highlighting?
- [ ] Botão de copiar código funciona?
- [ ] Dark mode funciona?
- [ ] Footer aparece em todas as páginas?
- [ ] Caracteres UTF-8 (acentos, emojis) corretos?

---

### 4.2 Adicionar Dark Mode e Footer

**Use o script Python (NÃO PowerShell!):**

```python
# add_dark_mode_footer.py
# Copiar do projeto atual e adaptar conforme necessário

# Executar:
python add_dark_mode_footer.py
```

**Customizar cores do dark mode:**
```css
/* No script, modificar as cores */
body.dark-mode {
    background: linear-gradient(135deg, 
        #0a0a0a 0%,      /* Sua cor escura 1 */
        #1a1a1a 50%,     /* Sua cor escura 2 */
        #0d2419 100%);   /* Sua cor escura 3 (tom da paleta) */
}

/* Cores de destaque no dark mode */
body.dark-mode .module-section h2 {
    color: #4ade80 !important;  /* Sua cor de destaque */
}
```

---

### 4.3 Criar Página Inicial (index.html)

**Elementos essenciais:**
```html
<!-- docs/index.html -->

1. Hero Section
   - Título do tutorial
   - Subtítulo/descrição
   - Link para começar

2. Seção "Sobre o Tutorial"
   - Objetivos
   - Público-alvo
   - Pré-requisitos

3. Cards dos Módulos
   - Título e número
   - Descrição curta
   - Lista de lições
   - Link para módulo completo

4. Seção de Referências
   - Links externos úteis
   - Materiais complementares

5. Footer
   - Informações do autor
   - Links GitHub (repo + issues)
   - Última atualização
```

**Copiar do projeto atual e adaptar:**
```bash
cp docs/index.html novo-projeto/docs/index.html
# Editar: título, descrição, módulos, referências, autor
```

---

## 🌐 FASE 5: PUBLICAÇÃO

### 5.1 Configurar GitHub Pages

**Passo a passo:**

1. **Commit de tudo:**
   ```bash
   git add .
   git commit -m "feat: Tutorial completo pronto para publicação"
   git push origin main
   ```

2. **No GitHub:**
   - Ir em: `Settings` → `Pages`
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/docs`
   - Salvar

3. **Aguardar 2-3 minutos**

4. **Acessar:** `https://seu-usuario.github.io/seu-repo/`

---

### 5.2 Verificação Pós-Publicação

**Checklist obrigatório:**

- [ ] Site carrega sem erros (abrir Console do navegador F12)
- [ ] Todos os links internos funcionam
- [ ] Dark mode funciona e persiste
- [ ] Imagens carregam
- [ ] CSS aplicado corretamente
- [ ] Mobile responsive (testar no celular)
- [ ] UTF-8 correto (emojis e acentos)

**Testar em múltiplos navegadores:**
- Chrome/Edge
- Firefox
- Safari (se tiver Mac)
- Mobile (Chrome Android / Safari iOS)

---

### 5.3 Configurar Domínio Customizado (Opcional)

**Se quiser usar domínio próprio:**

1. **Comprar domínio** (ex: namecheap.com, registro.br)

2. **Configurar DNS:**
   ```
   Tipo: CNAME
   Nome: www
   Valor: seu-usuario.github.io
   ```

3. **No GitHub Pages:**
   - Custom domain: `www.seu-dominio.com`
   - Enforce HTTPS: ✅

4. **Aguardar propagação** (até 24h)

---

## 🔧 FASE 6: MANUTENÇÃO E EVOLUÇÃO

### 6.1 Workflow de Atualizações

**Fluxo recomendado:**

```bash
# 1. Criar branch para mudanças
git checkout -b atualiza-modulo-2

# 2. Fazer alterações nos .md
# Editar arquivos, testar código...

# 3. Regenerar HTMLs
python scripts/build_site.py
python add_dark_mode_footer.py  # Se necessário

# 4. Testar localmente
# Abrir docs/index.html no navegador

# 5. Commit
git add .
git commit -m "feat: Adiciona exercícios no Módulo 2"

# 6. Merge e push
git checkout main
git merge atualiza-modulo-2
git push origin main

# 7. Verificar site online após 2-3 min
```

---

### 6.2 Coletar Feedback

**Métodos:**

1. **GitHub Issues:**
   - Estudantes podem reportar erros
   - Sugerir melhorias
   - Pedir esclarecimentos

2. **Google Forms:**
   - Pesquisa de satisfação
   - Dificuldades encontradas
   - Sugestões de conteúdo

3. **Análise de uso:**
   - Google Analytics (gratuito)
   - Ver páginas mais visitadas
   - Identificar onde alunos desistem

**Responder feedback:**
- Priorizar erros técnicos
- Considerar sugestões populares
- Atualizar glossário com dúvidas comuns

---

### 6.3 Evolução de Conteúdo

**Roadmap sugerido:**

**Versão 1.0:**
- Módulos 0-3 completos
- Exemplos básicos funcionando
- Site publicado

**Versão 1.5 (após 3 meses):**
- Correções de bugs reportados
- Módulos 4-5 adicionados
- Mais exercícios práticos

**Versão 2.0 (após 6 meses):**
- Todos os módulos completos
- Vídeo-aulas (opcional)
- Certificado de conclusão (opcional)
- Versão em inglês (opcional)

---

## 🗺️ ROTEIRO ESPECÍFICO: TUTORIAL QGIS

### Planejamento do Tutorial QGIS

**Título sugerido:** "QGIS para Oceanografia e Ficologia"

**Estrutura recomendada:**

```
0-Fundamentos-QGIS/
  01-Introducao-SIG.md          # O que são Sistemas de Informação Geográfica?
  02-Instalar-QGIS.md           # Download, instalação, primeira configuração
  03-Interface-Basica.md        # Painéis, menus, ferramentas essenciais
  04-Sistemas-Coordenadas.md    # CRS, projeções, transformações
  00-Glossario.md

1-Dados-Vetoriais/
  01-Pontos-Coleta.md           # Criar pontos de estações de coleta
  02-Linhas-Transectos.md       # Desenhar transectos de amostragem
  03-Poligonos-Areas.md         # Delimitar áreas de estudo
  04-Tabela-Atributos.md        # Adicionar dados às geometrias
  05-Estilizacao-Vetores.md     # Cores, símbolos, rótulos
  00-Glossario.md

2-Dados-Raster/
  01-Imagens-Satelite.md        # Sentinel, Landsat
  02-Batimetria.md              # Modelos digitais de elevação marinha
  03-Temperatura-Superficial.md # SST (Sea Surface Temperature)
  04-Calculos-Raster.md         # Algebra de mapas, NDVI
  00-Glossario.md

3-Analise-Espacial/
  01-Buffer-Area-Influencia.md
  02-Intersecao-Sobreposicao.md
  03-Pontos-em-Poligonos.md
  04-Densidade-Kernel.md
  05-Interpolacao-IDW.md
  00-Glossario.md

4-Mapas-Web/
  01-qgis2web-Basico.md         # Plugin para exportar mapas web
  02-Customizar-Popup.md        # Informações ao clicar
  03-Camadas-Tematicas.md       # Múltiplas camadas controláveis
  04-Publicar-GitHub-Pages.md   # Hospedar mapa online grátis
  00-Glossario.md

5-Casos-Praticos/
  01-Mapa-Distribuicao-Especies.md
  02-Analise-Temporal-SST.md
  03-Dashboard-Monitoramento.md
  04-Atlas-Impresso-PDF.md
  00-Glossario.md
```

---

### Diferenças QGIS vs Python

| Aspecto | Python | QGIS |
|---------|--------|------|
| **Curva de aprendizado** | Íngreme (programação) | Suave (interface visual) |
| **Automação** | Excelente (scripts) | Moderada (Processing Toolbox) |
| **Visualização** | Boa (mapas estáticos) | Excelente (mapas interativos) |
| **Análise espacial** | Poderosa (código) | Intuitiva (clique) |
| **Reprodutibilidade** | Perfeita (código versionado) | Moderada (salvar projeto) |
| **Colaboração** | Fácil (GitHub) | Moderada (compartilhar .qgz) |
| **Uso típico** | Workflows automatizados | Exploração e edição visual |

**Recomendação:** Ensinar **ambos**!
- QGIS: Para explorar dados, criar mapas bonitos rapidamente
- Python: Para automatizar, processar grandes volumes, integrar com análises

---

### Exemplos de Lições QGIS

**Exemplo: 1-Dados-Vetoriais/01-Pontos-Coleta.md**

```markdown
# 📍 Criando Pontos de Estações de Coleta

> **Você aprenderá:**
> - Criar camada de pontos manualmente
> - Importar coordenadas de CSV
> - Adicionar atributos (espécie, data, temperatura)
> - Estilizar pontos por categoria

---

## 📚 Método 1: Criação Manual

### Passo 1: Nova Camada de Pontos

1. **Menu:** `Layer` → `Create Layer` → `New Shapefile Layer`
2. **Configurações:**
   - File name: `estacoes_coleta.shp`
   - Geometry type: `Point`
   - CRS: `EPSG:4326 - WGS 84`
3. **Adicionar campos:**
   - Nome: `estacao` | Tipo: `Text` | Length: 50
   - Nome: `data` | Tipo: `Date`
   - Nome: `especie` | Tipo: `Text` | Length: 100
   - Nome: `temp_c` | Tipo: `Decimal` | Precision: 5, Scale: 2
4. **OK**

### Passo 2: Adicionar Pontos

1. **Selecionar camada** no painel Layers
2. **Toggle Editing:** 🖊️ (barra de ferramentas)
3. **Add Point Feature:** ➕ 
4. **Clicar no mapa** onde está a estação
5. **Preencher atributos:**
   ```
   estacao: E001
   data: 2024-01-15
   especie: Ulva lactuca
   temp_c: 22.5
   ```
6. **OK**
7. Repetir para mais pontos...
8. **Save Edits:** 💾
9. **Toggle Editing OFF**

---

## 📊 Método 2: Importar de CSV

### Formato do CSV

```csv
longitude,latitude,estacao,data,especie,temp_c
-48.5234,-27.5969,E001,2024-01-15,Ulva lactuca,22.5
-48.5456,-27.6123,E002,2024-01-15,Gracilaria domingensis,21.8
-48.5678,-27.6234,E003,2024-01-16,Sargassum cymosum,23.2
```

### Importar no QGIS

1. **Menu:** `Layer` → `Add Layer` → `Add Delimited Text Layer`
2. **File name:** Selecionar `coletas.csv`
3. **File Format:** CSV
4. **Geometry definition:**
   - Point coordinates
   - X field: `longitude`
   - Y field: `latitude`
   - Geometry CRS: `EPSG:4326`
5. **Add** → **Close**

✅ Camada aparece no mapa!

---

## 🎨 Estilização por Categoria

### Colorir por Espécie

1. **Botão direito na camada** → `Properties`
2. **Aba:** `Symbology`
3. **Trocar de:** `Single symbol` → `Categorized`
4. **Value:** `especie`
5. **Classify**
6. **Personalizar cores:**
   - Ulva lactuca: Verde claro
   - Gracilaria: Vermelho
   - Sargassum: Marrom
7. **OK**

🎨 Cada espécie agora tem cor diferente!

---

## 💡 Exercício Prático

**Tarefa:** Criar mapa com suas próprias estações

1. Crie um CSV com pelo menos 5 estações
2. Importe no QGIS
3. Estilize por espécie
4. Adicione uma camada de fundo (QuickMapServices → OSM Standard)
5. Exporte como imagem PNG: `Project` → `Import/Export` → `Export Map to Image`

**Salve o projeto:** `Project` → `Save As` → `mapa_coletas.qgz`

---

## 🔗 Próxima Lição

[02-Linhas-Transectos.md](02-Linhas-Transectos.md) - Desenhar transectos de amostragem
```

---

### Datasets para Tutorial QGIS

**Preparar:**

```
dados-qgis/
  vetoriais/
    costa_sc.shp              # Shapefile da costa de SC
    ucs_marinhas.shp          # Unidades de conservação
    municipios.gpkg           # Limite municipal (GeoPackage)
  
  raster/
    batimetria_sc.tif         # Modelo digital batimétrico
    sst_2024_01.tif           # Temperatura superficial do mar
    sentinel2_chl.tif         # Clorofila de imagem Sentinel
  
  tabelas/
    coletas_exemplo.csv       # Coordenadas de estações
    especies_registradas.xlsx # Tabela de ocorrências
  
  projetos/
    exemplo_completo.qgz      # Projeto QGIS exemplo
```

**Fontes de dados gratuitas:**
- **IBGE:** Malhas municipais, estaduais
- **GEBCO:** Batimetria global
- **Copernicus:** Sentinel-2, SST, Clorofila
- **Natural Earth:** Dados globais base
- **MarineCadastre:** Dados marinhos EUA (exemplo)

---

## ✅ CHECKLIST COMPLETO DE PROJETO

### Planejamento ✓
- [ ] Público-alvo definido
- [ ] Objetivos de aprendizagem claros
- [ ] Módulos estruturados (progressão lógica)
- [ ] Tecnologias selecionadas
- [ ] Datasets preparados

### Estruturação ✓
- [ ] Repositório Git criado
- [ ] Estrutura de pastas criada
- [ ] README.md inicial escrito
- [ ] requirements.txt configurado
- [ ] Script build_site.py adaptado
- [ ] .gitignore configurado

### Conteúdo ✓
- [ ] 0-Fundamentos completo
- [ ] Todos os módulos escritos
- [ ] Glossários de todos os módulos
- [ ] Exemplos testados e funcionando
- [ ] Exercícios com soluções
- [ ] Links de navegação corretos

### HTML ✓
- [ ] build_site.py gera todos os HTMLs
- [ ] index.html criado
- [ ] Dark mode implementado
- [ ] Footer com informações do autor
- [ ] UTF-8 correto (emojis e acentos)
- [ ] Syntax highlighting funcionando
- [ ] Botões de copiar código

### Publicação ✓
- [ ] GitHub Pages configurado
- [ ] Site acessível online
- [ ] Todos os links funcionam
- [ ] Mobile responsive
- [ ] Testado em múltiplos navegadores

### Documentação ✓
- [ ] README.md completo
- [ ] PROJETO-DOCUMENTACAO.md atualizado
- [ ] GUIA-CRIACAO-PROJETOS.md criado
- [ ] Licença definida (LICENSE)
- [ ] CONTRIBUTING.md (se aceitar contribuições)

### Manutenção ✓
- [ ] Workflow de atualização definido
- [ ] Issues do GitHub ativo
- [ ] Feedback sendo coletado
- [ ] Roadmap de evolução planejado

---

## 🎯 DICAS FINAIS DE OURO

### Do's ✅

1. **Comece pequeno, cresça organicamente**
   - Versão 1.0 com 3-4 módulos está ótimo
   - Adicione módulos conforme feedback

2. **Teste TUDO antes de publicar**
   - Execute cada linha de código
   - Clique em cada link
   - Teste em mobile

3. **Use dados reais anonimizados**
   - Alunos se engajam mais
   - Exemplos ficam relevantes

4. **Mantenha consistência**
   - Mesma estrutura de lição
   - Mesma paleta de cores
   - Mesmo nível de detalhe

5. **Documente o processo**
   - PROJETO-DOCUMENTACAO.md é essencial
   - Seu "eu futuro" agradecerá

### Don'ts ❌

1. **Não use PowerShell para UTF-8**
   - Use Python para manipular HTMLs
   - Evite double-encoding

2. **Não publique código não testado**
   - Um erro quebra confiança
   - Sempre testar localmente primeiro

3. **Não faça lições muito longas**
   - Máximo 1h de leitura/prática
   - Dividir em múltiplas lições

4. **Não assuma conhecimento prévio**
   - Sempre revisar conceitos
   - Link para glossário

5. **Não negligencie mobile**
   - 40%+ acessam de celular
   - Testar responsividade

---

## 🚀 COMEÇAR AGORA

**Próximos 7 dias:**

- **Dia 1:** Planejar módulos e estrutura
- **Dia 2:** Criar repo Git e estrutura de pastas
- **Dia 3-4:** Escrever 0-Fundamentos completo
- **Dia 5:** Preparar datasets e exemplos
- **Dia 6:** Escrever módulo 1
- **Dia 7:** Gerar HTML e publicar versão beta

**Compartilhe** com 2-3 alunos para feedback inicial!

---

## 📞 SUPORTE

**Se precisar de ajuda:**

1. **Revisar este guia** completo
2. **Consultar PROJETO-DOCUMENTACAO.md** para detalhes técnicos
3. **Ver projeto labficol-tutorial** como exemplo funcional
4. **Criar issue no GitHub** se encontrar problemas

---

<div align="center">

## 🎓 Você Está Pronto!

**Com este guia, você tem tudo para criar tutoriais educacionais de alta qualidade.**

*Boa sorte no seu projeto de tutorial QGIS! 🗺️*

---

**Criado por:** Ronan Armando Caetano  
**Data:** Janeiro 2026  
**Versão:** 1.0.0

</div>
