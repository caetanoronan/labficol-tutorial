#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove o footer antigo com 'Gerado automaticamente' dos HTMLs
"""

from pathlib import Path
import re

def remove_old_footer():
    """Remove o footer antigo com timestamp"""
    docs_html = Path('docs/html')
    count = 0
    success = 0
    
    print("🗑️  Removendo footer antigo 'Gerado automaticamente'...")
    print()
    
    # Padrão para encontrar o footer antigo
    old_footer_pattern = r'\s*<footer role="contentinfo">\s*<p>Gerado automaticamente em.*?</p>\s*</footer>\s*'
    
    for html_file in docs_html.rglob('*.html'):
        count += 1
        try:
            # Ler arquivo em UTF-8
            content = html_file.read_text(encoding='utf-8')
            
            # Verificar se tem o footer antigo
            if 'Gerado automaticamente em' not in content:
                print(f"[{count}] ⏭️  {html_file.name} - Não tem footer antigo")
                continue
            
            # Remover o footer antigo (com espaços e quebras de linha)
            new_content = re.sub(old_footer_pattern, '\n    ', content, flags=re.DOTALL)
            
            # Verificar se algo foi removido
            if new_content == content:
                print(f"[{count}] ⚠️  {html_file.name} - Padrão não encontrado")
                continue
            
            # Salvar com UTF-8
            html_file.write_text(new_content, encoding='utf-8')
            print(f"[{count}] ✅ {html_file.name}")
            success += 1
            
        except Exception as e:
            print(f"[{count}] ❌ {html_file.name} - Erro: {e}")
    
    print()
    print("=" * 40)
    print(f"🎉 Processo concluído!")
    print(f"Total: {count} arquivos")
    print(f"✅ Removidos: {success} footers antigos")
    print(f"⏭️  Sem alteração: {count - success} arquivos")
    print("=" * 40)

if __name__ == '__main__':
    remove_old_footer()
