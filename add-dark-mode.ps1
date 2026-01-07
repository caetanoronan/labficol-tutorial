# Script para adicionar Dark Mode em todos os HTMLs
# Autor: Ronan Caetano

$darkModeCSS = @"

      /* ================================
         MODO ESCURO (DARK MODE)
         ================================ */
      
      /* Botão de Toggle Dark Mode */
      .dark-mode-toggle {
        position: fixed;
        top: 20px;
        right: 20px;
        background: rgba(255, 255, 255, 0.95);
        border: 2px solid #2ca25f;
        border-radius: 50px;
        padding: 10px 18px;
        cursor: pointer;
        font-size: 1.1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        transition: all 0.3s;
        z-index: 10000;
        display: flex;
        align-items: center;
        gap: 8px;
        font-weight: 600;
        color: #062b1e;
      }
      
      .dark-mode-toggle:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 16px rgba(0,0,0,0.35);
      }
      
      /* Estilos do Modo Escuro - Body e containers principais */
      body.dark-mode {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0d2419 100%) !important;
        color: #e5e5e5 !important;
      }
      
      body.dark-mode .dark-mode-toggle {
        background: rgba(20, 20, 20, 0.95);
        border-color: #4ade80;
        color: #e5e5e5;
      }
      
      /* Header */
      body.dark-mode header {
        background: linear-gradient(120deg, #0f3d2a, #1e5a3f) !important;
        color: #fff !important;
      }
      
      body.dark-mode header h1 {
        color: #fff !important;
      }
      
      /* Module Content e Sections */
      body.dark-mode .module-content {
        color: #e5e5e5 !important;
      }
      
      body.dark-mode .module-section {
        background: #1e1e1e !important;
        border-color: #4ade80 !important;
        color: #e5e5e5 !important;
        box-shadow: 0 16px 40px rgba(0,0,0,0.6);
      }
      
      body.dark-mode .module-section h2 {
        color: #4ade80 !important;
        border-left-color: #4ade80 !important;
      }
      
      body.dark-mode .module-section h3 {
        color: #4ade80 !important;
      }
      
      body.dark-mode .module-section h4 {
        color: #22c55e !important;
      }
      
      body.dark-mode .module-section p,
      body.dark-mode .module-section li,
      body.dark-mode .module-section td,
      body.dark-mode .module-section span {
        color: #d4d4d4 !important;
      }
      
      body.dark-mode .module-section strong {
        color: #f0f0f0 !important;
      }
      
      body.dark-mode .module-section code {
        background: #2a2a2a !important;
        color: #4ade80 !important;
      }
      
      body.dark-mode .module-section pre {
        background: #0a0a0a !important;
        border-left-color: #4ade80 !important;
      }
      
      body.dark-mode .module-section a {
        color: #4ade80 !important;
      }
      
      body.dark-mode .module-section a:hover {
        color: #22c55e !important;
      }
      
      /* Tabelas */
      body.dark-mode table {
        border-color: #4ade80 !important;
      }
      
      body.dark-mode th {
        background: #0f3d2a !important;
        color: #fff !important;
        border-color: #4ade80 !important;
      }
      
      body.dark-mode td {
        background: #1a1a1a !important;
        color: #d4d4d4 !important;
        border-color: #333 !important;
      }
      
      body.dark-mode tr:nth-child(even) td {
        background: #222 !important;
      }
      
      /* Botões */
      body.dark-mode button,
      body.dark-mode .copy-btn {
        background: #1e5a3f !important;
        color: #fff !important;
        border-color: #4ade80 !important;
      }
      
      body.dark-mode button:hover,
      body.dark-mode .copy-btn:hover {
        background: #22c55e !important;
      }
      
      body.dark-mode .copy-btn.copied {
        background: #4ade80 !important;
      }
      
      /* Tabs */
      body.dark-mode .tabs-container {
        background: #1e1e1e !important;
      }
      
      body.dark-mode .tabs-nav {
        background: #2a2a2a !important;
        border-bottom-color: #4ade80 !important;
      }
      
      body.dark-mode .tab-button {
        background: #1a1a1a !important;
        color: #4ade80 !important;
        border-color: #4ade80 !important;
      }
      
      body.dark-mode .tab-button.active {
        background: #1e5a3f !important;
        color: #fff !important;
      }
      
      body.dark-mode .tab-content {
        background: #1e1e1e !important;
        color: #d4d4d4 !important;
      }
      
      /* Search */
      body.dark-mode .search-container {
        background: #1e1e1e !important;
      }
      
      body.dark-mode #search-input {
        background: #2a2a2a !important;
        color: #e5e5e5 !important;
        border-color: #4ade80 !important;
      }
      
      body.dark-mode .search-results {
        background: #1a1a1a !important;
        border-color: #4ade80 !important;
      }
      
      body.dark-mode .search-result-item {
        border-bottom-color: #333 !important;
      }
      
      body.dark-mode .search-result-item:hover {
        background: #2a2a2a !important;
      }
      
      body.dark-mode .search-result-title {
        color: #4ade80 !important;
      }
      
      body.dark-mode .search-result-snippet {
        color: #b0b0b0 !important;
      }
      
      /* Progress */
      body.dark-mode .progress-container {
        background: #1e1e1e !important;
        border-color: #4ade80 !important;
      }
      
      body.dark-mode .progress-header {
        background: #0f3d2a !important;
        color: #fff !important;
      }
      
      body.dark-mode .progress-bar-bg {
        background: #2a2a2a !important;
      }
      
      body.dark-mode .progress-bar-fill {
        background: linear-gradient(90deg, #1e5a3f, #4ade80) !important;
      }
      
      body.dark-mode .progress-text {
        color: #e5e5e5 !important;
      }
      
      /* Quiz */
      body.dark-mode .quiz-container {
        background: #1e1e1e !important;
        border-color: #4ade80 !important;
      }
      
      body.dark-mode .quiz-header {
        background: #0f3d2a !important;
        color: #fff !important;
      }
      
      body.dark-mode .quiz-question {
        color: #e5e5e5 !important;
      }
      
      body.dark-mode .quiz-option {
        background: #2a2a2a !important;
        color: #d4d4d4 !important;
        border-color: #4ade80 !important;
      }
      
      body.dark-mode .quiz-option:hover {
        background: #1e5a3f !important;
        color: #fff !important;
      }
      
      body.dark-mode .quiz-option.correct {
        background: #1e5a3f !important;
        border-color: #22c55e !important;
      }
      
      body.dark-mode .quiz-option.incorrect {
        background: #7f1d1d !important;
        border-color: #ef4444 !important;
      }
      
      body.dark-mode .results-header {
        background: #0f3d2a !important;
        color: #fff !important;
      }
      
      body.dark-mode .score-display {
        color: #4ade80 !important;
      }
      
      /* Navigation e Footer */
      body.dark-mode nav {
        background: #1a1a1a !important;
        border-bottom-color: #4ade80 !important;
      }
      
      body.dark-mode nav a {
        color: #4ade80 !important;
      }
      
      body.dark-mode nav a:hover {
        background: #2a2a2a !important;
        color: #22c55e !important;
      }
      
      body.dark-mode footer {
        background: #0a0a0a !important;
        color: #b0b0b0 !important;
        border-top: 3px solid #4ade80 !important;
      }
      
      body.dark-mode footer a {
        color: #4ade80 !important;
      }
      
      body.dark-mode footer a:hover {
        color: #22c55e !important;
      }
      
      /* Alertas e Boxes especiais */
      body.dark-mode .alert,
      body.dark-mode .warning,
      body.dark-mode .info {
        background: #2a2a2a !important;
        border-color: #4ade80 !important;
        color: #e5e5e5 !important;
      }
      
      /* Syntax Highlighting - mantém tema escuro VS Code */
      body.dark-mode .codehilite {
        background: #0a0a0a !important;
      }
"@

$darkModeButton = @"

    <!-- Botão de Toggle Dark Mode -->
    <button class="dark-mode-toggle" onclick="toggleDarkMode()" aria-label="Alternar modo escuro" title="Alternar tema claro/escuro">
      <span id="dark-mode-icon">🌙</span>
      <span id="dark-mode-text">Escuro</span>
    </button>
"@

$darkModeScript = @"

    <script>
      // Sistema de Dark Mode com persistência
      function toggleDarkMode() {
        const body = document.body;
        const icon = document.getElementById('dark-mode-icon');
        const text = document.getElementById('dark-mode-text');
        
        body.classList.toggle('dark-mode');
        
        if (body.classList.contains('dark-mode')) {
          icon.textContent = '☀️';
          text.textContent = 'Claro';
          localStorage.setItem('darkMode', 'enabled');
        } else {
          icon.textContent = '🌙';
          text.textContent = 'Escuro';
          localStorage.setItem('darkMode', 'disabled');
        }
      }
      
      // Verificar preferência salva ao carregar a página
      document.addEventListener('DOMContentLoaded', function() {
        const darkMode = localStorage.getItem('darkMode');
        const icon = document.getElementById('dark-mode-icon');
        const text = document.getElementById('dark-mode-text');
        
        if (darkMode === 'enabled') {
          document.body.classList.add('dark-mode');
          icon.textContent = '☀️';
          text.textContent = 'Claro';
        }
      });
    </script>
"@

Write-Host "🌙 Iniciando adição de Dark Mode em todos os HTMLs..." -ForegroundColor Cyan
Write-Host ""

$htmlFiles = Get-ChildItem "docs\html" -Recurse -Filter "*.html"
$count = 0
$success = 0
$skipped = 0

foreach ($file in $htmlFiles) {
    $count++
    Write-Host "[$count/$($htmlFiles.Count)] Processando: $($file.Name)" -ForegroundColor Yellow
    
    try {
        $content = Get-Content $file.FullName -Raw -Encoding UTF8
        
        # Verificar se já tem dark mode
        if ($content -match 'dark-mode-toggle') {
            Write-Host "  ⏭️  Já possui dark mode, pulando..." -ForegroundColor Gray
            $skipped++
            continue
        }
        
        # Adicionar CSS antes de </style>
        if ($content -match '</style>') {
            $content = $content -replace '</style>', "$darkModeCSS`n    </style>"
        } else {
            Write-Host "  ⚠️  Não encontrou tag </style>, pulando..." -ForegroundColor Red
            continue
        }
        
        # Adicionar botão após <body> (com espaços ou sem)
        if ($content -match '<body[^>]*>') {
            $content = $content -replace '(<body[^>]*>)', "`$1$darkModeButton"
        } else {
            Write-Host "  ⚠️  Não encontrou tag <body>, pulando..." -ForegroundColor Red
            continue
        }
        
        # Adicionar script antes de </body>
        if ($content -match '</body>') {
            $content = $content -replace '</body>', "$darkModeScript`n  </body>"
        } else {
            Write-Host "  ⚠️  Não encontrou tag </body>, pulando..." -ForegroundColor Red
            continue
        }
        
        # Salvar arquivo
        [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.UTF8Encoding]::new($false))
        Write-Host "  ✅ Sucesso!" -ForegroundColor Green
        $success++
        
    } catch {
        Write-Host "  ❌ Erro: $_" -ForegroundColor Red
    }
    
    Write-Host ""
}

Write-Host "================================" -ForegroundColor Cyan
Write-Host "🎉 Processo concluído!" -ForegroundColor Green
Write-Host "Total de arquivos: $count" -ForegroundColor White
Write-Host "✅ Sucesso: $success" -ForegroundColor Green
Write-Host "⏭️  Pulados: $skipped" -ForegroundColor Gray
Write-Host "❌ Erros: $($count - $success - $skipped)" -ForegroundColor Red
Write-Host "================================" -ForegroundColor Cyan
