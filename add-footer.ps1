# Script para adicionar Footer com informações do autor em todos os HTMLs
# Autor: Ronan Caetano

$footerCSS = @"

      /* Footer Styling */
      footer {
        background: linear-gradient(120deg, #e5f5f9, #99d8c9);
        color: #062b1e;
        padding: 30px 20px;
        margin-top: 60px;
        border-top: 4px solid #2ca25f;
        text-align: center;
        font-size: 0.95rem;
        line-height: 1.8;
      }
      
      footer strong {
        color: #1e7d5a;
        font-size: 1.1rem;
      }
      
      footer a {
        color: #2ca25f;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s;
      }
      
      footer a:hover {
        color: #1e7d5a;
        text-decoration: underline;
      }
      
      footer .footer-links {
        margin: 15px 0;
        font-size: 1rem;
      }
      
      footer .footer-author {
        margin: 20px 0;
        padding: 15px;
        background: rgba(255, 255, 255, 0.6);
        border-radius: 8px;
        display: inline-block;
      }
      
      footer .footer-meta {
        margin-top: 15px;
        font-size: 0.85rem;
        color: #0f3d2a;
        opacity: 0.8;
      }
      
      /* Dark Mode - Footer */
      body.dark-mode footer {
        background: linear-gradient(120deg, #0a0a0a, #1a1a1a);
        color: #b0b0b0;
        border-top-color: #4ade80;
      }
      
      body.dark-mode footer strong {
        color: #4ade80;
      }
      
      body.dark-mode footer a {
        color: #4ade80;
      }
      
      body.dark-mode footer a:hover {
        color: #22c55e;
      }
      
      body.dark-mode footer .footer-author {
        background: rgba(30, 30, 30, 0.6);
      }
      
      body.dark-mode footer .footer-meta {
        color: #888;
      }
"@

$footerHTML = @"

    <footer>
      <p><strong>📚 Tutorial Python</strong></p>
      <div class="footer-links">
        <a href="https://github.com/caetanoronan/labficol-tutorial" target="_blank" rel="noopener">📂 Repositório GitHub</a> | 
        <a href="https://github.com/caetanoronan/labficol-tutorial/issues" target="_blank" rel="noopener">💬 Reportar Problema</a>
      </div>
      <div class="footer-author">
        <strong>Autor:</strong> Ronan Armando Caetano<br>
        Pós-Graduando em Oceanografia - UFSC<br>
        Bacharel em Ciências Biológicas - UFSC<br>
        Técnico em Geoprocessamento e Técnico em Saneamento - IFSC
      </div>
      <p class="footer-meta">
        Última atualização: Janeiro 2026 | Paleta de Cores: ColorBrewer BuGn
      </p>
    </footer>
"@

Write-Host "📄 Iniciando adição de Footer em todos os HTMLs..." -ForegroundColor Cyan
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
        
        # Verificar se já tem footer
        if ($content -match 'footer-author') {
            Write-Host "  ⏭️  Já possui footer, pulando..." -ForegroundColor Gray
            $skipped++
            continue
        }
        
        # Adicionar CSS do footer antes do CSS do dark mode (antes do comentário MODO ESCURO)
        if ($content -match '/\* ================================\s+MODO ESCURO') {
            $content = $content -replace '(/\* ================================\s+MODO ESCURO)', "$footerCSS`n`n      `$1"
        } else {
            # Se não tem dark mode ainda, adiciona antes de </style>
            if ($content -match '</style>') {
                $content = $content -replace '</style>', "$footerCSS`n    </style>"
            } else {
                Write-Host "  ⚠️  Não encontrou onde adicionar CSS, pulando..." -ForegroundColor Red
                continue
            }
        }
        
        # Adicionar footer HTML antes de </body>
        if ($content -match '</body>') {
            $content = $content -replace '</body>', "$footerHTML`n  </body>"
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
