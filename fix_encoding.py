import os
from pathlib import Path

# Mapeamento de caracteres mal codificados para corretos
replacements = {
    'ðŸ"š': '📚',
    'ðŸ"‚': '📂',
    'ðŸ'¬': '💬',
    'ðŸŒ™': '🌙',
    'â˜€ï¸': '☀️',
    'â˜€': '☀',
    'Ã¡': 'á',
    'Ã©': 'é',
    'Ã­': 'í',
    'Ã³': 'ó',
    'Ãº': 'ú',
    'Ã§': 'ç',
    'Ã£': 'ã',
    'Ãª': 'ê',
    'Ã´': 'ô',
    'Ã"': 'Ó',
    'Ãš': 'Ú',
    'Ã': 'Á'
}

docs_html = Path('docs/html')
count = 0
success = 0

print("🔧 Corrigindo encoding UTF-8...")
print()

for html_file in docs_html.rglob('*.html'):
    try:
        # Ler arquivo em UTF-8
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Aplicar substituições
        modified = False
        for wrong, correct in replacements.items():
            if wrong in content:
                content = content.replace(wrong, correct)
                modified = True
        
        if modified:
            # Salvar com UTF-8 com BOM
            with open(html_file, 'w', encoding='utf-8-sig') as f:
                f.write(content)
            print(f"✓ {html_file.name}")
            success += 1
        
        count += 1
        
    except Exception as e:
        print(f"❌ Erro em {html_file.name}: {e}")

print()
print(f"🎉 Processo concluído!")
print(f"Total: {count} arquivos")
print(f"✅ Corrigidos: {success} arquivos")
