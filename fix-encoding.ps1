# Script para corrigir encoding UTF-8 em todos os HTMLs
# Corrige problema de caracteres especiais (á, é, ç, ã, etc)

Write-Host "🔧 Iniciando correção de encoding UTF-8..." -ForegroundColor Cyan
Write-Host ""

$htmlFiles = Get-ChildItem "docs\html" -Recurse -Filter "*.html"
$count = 0
$success = 0

foreach ($file in $htmlFiles) {
    $count++
    Write-Host "[$count/$($htmlFiles.Count)] Processando: $($file.Name)" -ForegroundColor Yellow
    
    try {
        # Ler arquivo detectando encoding automaticamente
        $content = Get-Content $file.FullName -Raw -Encoding UTF8
        
        # Corrigir caracteres mal codificados comuns
        $content = $content -replace 'Ã¡', 'á'
        $content = $content -replace 'Ã©', 'é'
        $content = $content -replace 'Ã­', 'í'
        $content = $content -replace 'Ã³', 'ó'
        $content = $content -replace 'Ãº', 'ú'
        $content = $content -replace 'Ã¢', 'â'
        $content = $content -replace 'Ãª', 'ê'
        $content = $content -replace 'Ã´', 'ô'
        $content = $content -replace 'Ã£', 'ã'
        $content = $content -replace 'Ãµ', 'õ'
        $content = $content -replace 'Ã§', 'ç'
        $content = $content -replace 'Ã', 'Á'
        $content = $content -replace 'Ã‰', 'É'
        $content = $content -replace 'Ã"', 'Ó'
        $content = $content -replace 'Ãš', 'Ú'
        $content = $content -replace 'Ã‡', 'Ç'
        $content = $content -replace 'ðŸ"š', '📚'
        $content = $content -replace 'ðŸ"‚', '📂'
        $content = $content -replace 'ðŸ'¬', '💬'
        $content = $content -replace 'ðŸŒ™', '🌙'
        $content = $content -replace 'â˜€ï¸', '☀️'
        $content = $content -replace 'â˜€', '☀'
        
        # Salvar com UTF-8 com BOM
        $utf8WithBom = New-Object System.Text.UTF8Encoding $true
        [System.IO.File]::WriteAllText($file.FullName, $content, $utf8WithBom)
        
        Write-Host "  ✅ Sucesso!" -ForegroundColor Green
        $success++
        
    } catch {
        Write-Host "  ❌ Erro: $_" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "🎉 Processo concluído!" -ForegroundColor Green
Write-Host "Total de arquivos: $count" -ForegroundColor White
Write-Host "✅ Sucesso: $success" -ForegroundColor Green
Write-Host "❌ Erros: $($count - $success)" -ForegroundColor Red
Write-Host "================================" -ForegroundColor Cyan
