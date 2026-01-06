# 🛠️ Configurar Seu Ambiente de Desenvolvimento

## O que é Ambiente de Desenvolvimento?

É um espaço no seu computador onde você escreve, testa e executa programas.

**Analogia:** 
- Sem ambiente = tentar fazer culinária sem cozinha
- Com ambiente = uma cozinha equipada e organizada ✨

---

## 📋 Pré-requisitos

- ✅ Windows 10/11, macOS ou Linux
- ✅ ~10GB de espaço em disco
- ✅ Conexão internet (para download)
- ✅ Paciência de 30 minutos

---

## 🎯 Ferramentas que Instalaremos

```
┌──────────────────────────────────────┐
│    SEU AMBIENTE DE DESENVOLVIMENTO   │
├──────────────────────────────────────┤
│ 1️⃣  Python 3.11+       (linguagem)   │
│ 2️⃣  VS Code            (editor)      │
│ 3️⃣  Git                (versionamento)│
│ 4️⃣  Bibliotecas Python (ferramentas) │
└──────────────────────────────────────┘
```

---

## 🐍 Passo 1: Instalar Python

### Windows

1. Visite: **https://www.python.org/downloads/**
2. Clique em "Download Python 3.11" (ou versão mais recente)
3. Abra o instalador
4. **⚠️ IMPORTANTE:** Marque "Add Python to PATH"

```
[x] Install launcher for all users
[x] Add Python 3.11 to PATH  ← MARQUE ISTO!
```

5. Clique "Install Now"
6. Aguarde conclusão

**Verificar instalação:**

Abra o PowerShell e execute:

```powershell
python --version
```

Você deve ver:
```
Python 3.11.x (ou versão mais recente)
```

### macOS

```bash
# Via Homebrew (recomendado)
brew install python3

# Verificar
python3 --version
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip

python3 --version
```

---

## 💻 Passo 2: Instalar VS Code

### O que é VS Code?
Um **editor de código moderno** onde você escreve seus programas.

### Instalação

1. Visite: **https://code.visualstudio.com/**
2. Baixe a versão para seu SO
3. Instale normalmente
4. Abra VS Code

### Extensões Recomendadas

No VS Code, clique em "Extensions" (ícone de quadrado ao lado) e instale:

- **Python** (Microsoft) - Essencial!
- **Pylance** - Autocomplete inteligente
- **GitLens** - Melhor integração Git
- **Thunder Client** - Testar APIs

---

## 🌳 Passo 3: Configurar Pasta de Trabalho

### Criar estrutura de pastas

```powershell
# Windows PowerShell
mkdir $HOME\Documentos\Projetos-Programacao
cd $HOME\Documentos\Projetos-Programacao

# Criar subpastas
mkdir aulas
mkdir projetos
mkdir datasets
```

Ou criar manualmente no Windows Explorer:
```
Documentos/
└── Projetos-Programacao/
    ├── aulas/
    ├── projetos/
    └── datasets/
```

---

## 🔄 Passo 4: Instalar Git (Versionamento)

### Por que Git?
Rastreia mudanças no seu código. Essencial para pesquisa reproduzível!

### Windows

1. Visite: **https://git-scm.com/download/win**
2. Baixe e instale
3. Use opções padrão

**Verificar:**
```powershell
git --version
```

### macOS
```bash
brew install git
git --version
```

### Linux
```bash
sudo apt install git
git --version
```

---

## 📦 Passo 5: Instalar Bibliotecas Python

As "ferramentas" que você usará para análise de dados.

### Abra PowerShell/Terminal

```powershell
# Windows
python -m pip install --upgrade pip

# Instalar bibliotecas essenciais
pip install numpy pandas matplotlib
pip install geopandas folium
pip install jupyter notebook
pip install requests beautifulsoup4
```

### Verificar Instalação

```powershell
python
```

Agora você está em Python. Digite:

```python
import numpy
import pandas
import matplotlib
import geopandas
print("✅ Tudo instalado!")
```

Se aparecer "✅ Tudo instalado!" sem erros, parabéns! 🎉

Saia do Python:
```python
exit()
```

---

## 🧪 Passo 6: Teste Seu Primeiro Programa

### Criar arquivo

1. Abra VS Code
2. Crie arquivo: `teste-setup.py`
3. Escreva:

```python
# Seu primeiro programa!
print("🎉 Olá, Mundo!")
print("🐍 Python está funcionando!")
print("🎓 Você está pronto para aprender!")

# Testar bibliotecas
import numpy as np
import pandas as pd

dados = [1, 2, 3, 4, 5]
print(f"✅ Numpy funcionando: {np.mean(dados)}")
print(f"✅ Pandas funcionando: v{pd.__version__}")
```

### Executar

No terminal do VS Code (Ctrl + Backtick):

```powershell
python teste-setup.py
```

Você deve ver:
```
🎉 Olá, Mundo!
🐍 Python está funcionando!
🎓 Você está pronto para aprender!
✅ Numpy funcionando: 3.0
✅ Pandas funcionando: v2.x.x
```

Se viu isso, **PARABÉNS!** ✨ Seu ambiente está pronto!

---

## 🚀 Passo 7: Primeiro Programa com Dados Reais

Agora vamos fazer algo interessante!

### Criar: `analise-simples.py`

```python
import pandas as pd
import numpy as np

# Simular dados de coleta de plâncton
dados_fitoplancton = {
    'Data': ['2025-01-01', '2025-01-02', '2025-01-03'],
    'Densidade': [150, 230, 180],
    'Temperatura': [22.5, 23.1, 22.8],
    'Salinidade': [35.0, 34.8, 35.1]
}

# Criar tabela
df = pd.DataFrame(dados_fitoplancton)

# Análises
print("=" * 50)
print("📊 ANÁLISE DE FITOPLÂNCTON")
print("=" * 50)
print(df)
print("\n📈 Estatísticas:")
print(f"Densidade média: {df['Densidade'].mean():.1f} células/mL")
print(f"Temperatura média: {df['Temperatura'].mean():.1f}°C")
print(f"Salinidade média: {df['Salinidade'].mean():.1f} PSU")
```

**Executar:**
```powershell
python analise-simples.py
```

Você verá:
```
==================================================
📊 ANÁLISE DE FITOPLÂNCTON
==================================================
        Data  Densidade  Temperatura  Salinidade
0 2025-01-01        150         22.5        35.0
1 2025-01-02        230         23.1        34.8
2 2025-01-03        180         22.8        35.1

📈 Estatísticas:
Densidade média: 186.7 células/mL
Temperatura média: 22.8°C
Salinidade média: 35.0 PSU
```

---

## ✅ Checklist de Instalação

- [ ] Python 3.11+ instalado e no PATH
- [ ] VS Code instalado com extensão Python
- [ ] Git instalado
- [ ] Pasta de trabalho criada
- [ ] Bibliotecas Python instaladas (numpy, pandas, geopandas, folium)
- [ ] Primeiro programa executado com sucesso
- [ ] Análise simples funcionando

Se tudo estiver marcado, **você está pronto!** 🎉

---

## ⚠️ Troubleshooting

### Problema: "python não é reconhecido"
**Solução:** 
- Reinstale Python e MARQUE "Add Python to PATH"
- Reinicie o computador após instalação

### Problema: "ModuleNotFoundError: No module named 'pandas'"
**Solução:**
```powershell
pip install pandas
```

### Problema: VS Code não encontra Python
**Solução:**
- Ctrl+Shift+P → "Python: Select Interpreter"
- Escolha a versão que você instalou

### Problema: Git não aparece no PowerShell
**Solução:**
- Feche e reabra PowerShell após instalar Git

---

## 🎓 Próximo Passo

Seu ambiente está configurado! Agora:

**👉 Vá para: [03-Conceitos-Basicos.md](03-Conceitos-Basicos.md)**

Lá você aprenderá:
- O que é código?
- Como pensa um programador?
- Conceitos fundamentais de programação

---

## 📝 Resumo

| Ferramenta | Função |
|-----------|--------|
| **Python** | Linguagem de programação |
| **VS Code** | Editor de código |
| **Git** | Controle de versão |
| **Pandas** | Análise de dados |
| **GeoPandas** | Dados geoespaciais |

---

**Parabéns por completar a configuração!** 🚀

Você agora tem um ambiente profissional de desenvolvimento!

Vamos aprender os conceitos fundamentais? ➡️
