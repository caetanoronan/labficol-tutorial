# 🌐 Git, GitHub e GitHub Pages

## 🎯 Objetivo

Aprender a versionar seu projeto com **Git**, hospedar no **GitHub** e publicar páginas estáticas (mapas/dashboards) com **GitHub Pages**.

---

## 🛠️ Instalação e Configuração (Windows)

1. Instale Git: https://git-scm.com/download/win
2. Abra "Git Bash" ou PowerShell
3. Configure sua identidade:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email"
```

— Opcional: instalar GitHub CLI: https://cli.github.com/

---

## 📦 Iniciar Repositório Local

No diretório do projeto (esta pasta):

```bash
git init
git branch -M main
git add .
git commit -m "Inicial: tutorial LABFICOL (módulos 0-6, exemplos)"
```

— Cria `.git` e registra estado inicial.

---

## ☁️ Criar Repositório no GitHub

Pelo navegador:
- Vá a https://github.com/new
- Nome: `tutorial-labficol` (exemplo)
- Público (para GitHub Pages)
- Crie sem README (já temos)

Depois, vincule remoto e envie:

```bash
git remote add origin https://github.com/<seu-usuario>/<seu-repo>.git
git push -u origin main
```

— Se pedir login/token, gere um PAT: https://github.com/settings/tokens

---

## 🗺️ Publicar com GitHub Pages (site estático)

GitHub Pages hospeda HTML/CSS/JS (ex.: mapas Leaflet, dashboards front-end).

1. No repositório no GitHub, acesse Settings → Pages
2. Build and deployment:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/root` (ou `/docs`)
3. Salvar → espere 1–2 minutos
4. Seu site: `https://<usuario>.github.io/<repo>/`

### Publicar página `index.html`

Crie uma pasta `docs/` (ou use raiz) com seu `index.html` (ex.: dashboard front-end):

```bash
mkdir docs
copy frontend\index.html docs\index.html
copy frontend\style.css docs\style.css
copy frontend\script.js docs\script.js

git add docs
git commit -m "Publicar dashboard estático em GitHub Pages"
git push
```

— GH Pages servirá `docs/index.html`.

### Publicar mapas gerados (Folium)

Arquivos `.html` gerados (ex.: `distribuicao_espacial.html`) devem ser copiados para `docs/`:

```bash
copy 4-Casos-Praticos\distribuicao_espacial.html docs\distribuicao_espacial.html

git add docs\distribuicao_espacial.html
git commit -m "Publicar mapa Folium"
git push
```

Acesse: `https://<usuario>.github.io/<repo>/distribuicao_espacial.html`

---

## 🔒 Dicas de Segurança

- Nunca commitar senhas/tokens
- Adicionar `.gitignore` para `venv/`, `__pycache__/`, etc.

```bash
echo __pycache__/> .gitignore
echo venv/> .gitignore
echo .ipynb_checkpoints/> .gitignore
echo *.pyc>> .gitignore
```

— Commit: `git add .gitignore && git commit -m "Add .gitignore" && git push`

---

## 🔄 Fluxo de Trabalho Sugerido

```bash
# 1. Edite/crie arquivos
# 2. Veja mudanças
git status

# 3. Selecione para commit
git add caminho/do/arquivo

# 4. Commit com mensagem clara
git commit -m "Adicionar lição de regressão (módulo 5)"

# 5. Envie ao GitHub
git push
```

— Para colaborações: use branches (`git checkout -b feature/nome`), PRs e reviews.

---

## 🧪 Verificação Rápida

Depois do push, confira:
- Repositório mostra seus commits
- GH Pages ativo (Settings → Pages)
- Site acessível na URL 

— Problemas comuns: branch errado, pasta Pages não configurada, arquivos faltando.

---

## 🎓 Checklist

- [ ] Repositório Git inicializado
- [ ] Remote GitHub configurado
- [ ] Commit e push funcionando
- [ ] GH Pages habilitado
- [ ] Dashboard/Mapas publicados

Com isso, você publica seus resultados científicos online de forma profissional! 🚀
