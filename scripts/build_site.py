import os
import re
import sys
from pathlib import Path
from datetime import datetime
from markdown import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = DOCS / "html"
ASSETS = DOCS / "assets"
REPO_URL = "https://github.com/caetanoronan/labficol-tutorial"
SITE_URL = "https://caetanoronan.github.io/labficol-tutorial/"

MODULES = [
    "0-Fundamentos",
    "1-Python-Essencial",
    "2-Analise-Geoespacial",
    "3-Visualizacao-Web",
    "4-Casos-Praticos",
    "5-Estatistica-Aplicada",
    "6-Machine-Learning",
]

MD_EXTS = [
    'fenced_code',
    'tables',
    'toc',
    'codehilite',
    'attr_list',
]

TEMPLATE = """<!doctype html>
<html lang=\"pt-BR\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>{title}</title>
    <style>
      * {{ box-sizing: border-box; }}
      body {{ 
        margin: 0; 
        background: linear-gradient(135deg, #e5f5f9 0%, #99d8c9 50%, #2ca25f 100%) !important;
        min-height: 100vh;
        color: #062b1e !important;
        font-family: system-ui, -apple-system, sans-serif;
        line-height: 1.6;
      }}
      header {{ 
        background: linear-gradient(120deg, #2ca25f, #1e7d5a) !important;
        color: #fff !important;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
      }}
      header h1 {{ color: #fff !important; margin: 0; font-size: 1.8rem; }}
      main {{ max-width: 1000px; margin: 24px auto; padding: 0 16px; }}
      .module-content {{ display: grid; gap: 24px; }}
      .module-section {{ 
        background: #fff !important;
        border: 3px solid #99d8c9 !important;
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 16px 40px rgba(0,0,0,0.18);
      }}
      .module-section h2 {{ 
        color: #2ca25f !important; 
        border-left: 8px solid #2ca25f; 
        padding-left: 12px;
        margin-top: 0;
      }}
      .module-section h3 {{ color: #2ca25f !important; }}
      .module-section p, .module-section li {{ color: #062b1e !important; }}
      .module-section code {{ background: #e5f5f9 !important; padding: 2px 6px; border-radius: 4px; color: #062b1e; }}
      .module-section pre {{ 
        position: relative;
        background: #1e1e1e !important; 
        border-left: 6px solid #2ca25f !important;
        padding: 14px 50px 14px 14px;
        overflow-x: auto;
        border-radius: 8px;
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        font-size: 14px;
        line-height: 1.5;
      }}
      .module-section pre code {{ 
        background: transparent !important; 
        color: #d4d4d4 !important; 
        padding: 0; 
      }}
      
      /* Copy Button */
      .copy-btn {{
        position: absolute;
        top: 8px;
        right: 8px;
        background: #2ca25f !important;
        color: #fff !important;
        border: none;
        border-radius: 6px;
        padding: 6px 12px;
        font-size: 12px;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s;
        z-index: 10;
      }}
      .copy-btn:hover {{
        background: #1e7d5a !important;
        transform: scale(1.05);
      }}
      .copy-btn.copied {{
        background: #4ec9b0 !important;
      }}
      
      /* Syntax Highlighting - VS Code Dark Theme (FIXED CONTRAST) */
      .codehilite {{ background: #1e1e1e !important; border-radius: 8px; }}
      .codehilite .hll {{ background-color: #3e3e42; }}
      .codehilite .c {{ color: #6a9955; font-style: italic; }} /* Comentarios */
      .codehilite .k {{ color: #c586c0; font-weight: bold; }} /* Keywords (def, if, for) */
      .codehilite .kn {{ color: #c586c0; }} /* import */
      .codehilite .kt {{ color: #4ec9b0; }} /* tipos */
      .codehilite .nc {{ color: #4ec9b0; }} /* Classes */
      .codehilite .nf {{ color: #dcdcaa; }} /* Funcoes */
      .codehilite .nb {{ color: #4ec9b0; }} /* Built-ins (print, len) */
      .codehilite .s, .codehilite .s1, .codehilite .s2 {{ color: #ce9178; }} /* Strings */
      .codehilite .si {{ color: #d7ba7d; }} /* String interpolation */
      .codehilite .m, .codehilite .mi, .codehilite .mf {{ color: #b5cea8; }} /* Numeros */
      .codehilite .o {{ color: #d4d4d4; }} /* Operadores */
      .codehilite .ow {{ color: #c586c0; }} /* Operadores palavra (and, or) */
      .codehilite .n {{ color: #9cdcfe; }} /* Variaveis */
      .codehilite .na {{ color: #9cdcfe; }} /* Atributos */
      .codehilite .bp {{ color: #c586c0; }} /* self */
      .codehilite .err {{ color: #f48771; background: transparent; }} /* Erros - SEM fundo preto */
      .codehilite .fm {{ color: #dcdcaa; }} /* Magic methods */
      .codehilite .nn {{ color: #4ec9b0; }} /* Namespace */
      .codehilite .p {{ color: #d4d4d4; }} /* Pontuacao - cinza claro ao inves de preto */
      .codehilite .w {{ color: #d4d4d4; }} /* Whitespace */
      
      /* Garantir que NADA seja preto em blocos de codigo */
      pre, pre *, .codehilite, .codehilite * {{
        color: #d4d4d4 !important;
      }}
      
      /* Reaplica cores especificas por cima da regra geral */
      .codehilite .c {{ color: #6a9955 !important; font-style: italic; }}
      .codehilite .k {{ color: #c586c0 !important; font-weight: bold; }}
      .codehilite .kn {{ color: #c586c0 !important; }}
      .codehilite .kt {{ color: #4ec9b0 !important; }}
      .codehilite .nc {{ color: #4ec9b0 !important; }}
      .codehilite .nf {{ color: #dcdcaa !important; }}
      .codehilite .nb {{ color: #4ec9b0 !important; }}
      .codehilite .s, .codehilite .s1, .codehilite .s2 {{ color: #ce9178 !important; }}
      .codehilite .si {{ color: #d7ba7d !important; }}
      .codehilite .m, .codehilite .mi, .codehilite .mf {{ color: #b5cea8 !important; }}
      .codehilite .o {{ color: #d4d4d4 !important; }}
      .codehilite .ow {{ color: #c586c0 !important; }}
      .codehilite .n {{ color: #9cdcfe !important; }}
      .codehilite .na {{ color: #9cdcfe !important; }}
      .codehilite .bp {{ color: #c586c0 !important; }}
      .codehilite .err {{ color: #f48771 !important; background: transparent !important; }}
      .codehilite .fm {{ color: #dcdcaa !important; }}
      .codehilite .nn {{ color: #4ec9b0 !important; }}
      .codehilite .p {{ color: #d4d4d4 !important; }}
      .codehilite .w {{ color: #d4d4d4 !important; }}
      
      /* Tabs System */
      .tabs-container {{ margin: 20px 0; }}
      .tabs-nav {{
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        background: rgba(255,255,255,0.3);
        padding: 12px;
        border-radius: 12px 12px 0 0;
        border-bottom: 3px solid #2ca25f;
      }}
      .tab-button {{
        background: #fff;
        color: #2ca25f;
        border: 2px solid #99d8c9;
        border-radius: 8px;
        padding: 10px 18px;
        cursor: pointer;
        font-weight: 700;
        font-size: 15px;
        transition: all 0.3s;
      }}
      .tab-button:hover {{
        background: #e5f5f9;
        transform: translateY(-2px);
      }}
      .tab-button.active {{
        background: #2ca25f !important;
        color: #fff !important;
        border-color: #1e7d5a;
        box-shadow: 0 4px 12px rgba(44, 162, 95, 0.3);
      }}
      .tab-content {{
        display: none;
        background: #fff;
        border: 3px solid #99d8c9;
        border-top: none;
        border-radius: 0 0 14px 14px;
        padding: 24px;
        animation: fadeIn 0.3s;
      }}
      .tab-content.active {{
        display: block;
      }}
      @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(-10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      
      .hero {{
        background: linear-gradient(120deg, #99d8c9, #2ca25f) !important;
        border: 3px solid #1e7d5a !important;
        border-left: 12px solid #1e7d5a !important;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 28px;
        box-shadow: 0 16px 40px rgba(0,0,0,0.18);
      }}
      .hero h2 {{ margin: 0 0 12px; color: #fff !important; font-size: 2rem; }}
      .hero h3 {{ margin: 16px 0 10px; color: #fff !important; font-size: 1.4rem; }}
      .hero p {{ color: #fff !important; font-size: 1.08rem; }}
      .hero ul {{ margin: 10px 0; padding-left: 24px; color: #fff !important; }}
      .hero li {{ color: #fff !important; margin: 6px 0; }}
      .chips {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 14px; }}
      .chip {{
        background: #1e7d5a !important;
        color: #fff !important;
        border: 2px solid #156048 !important;
        border-radius: 999px;
        padding: 9px 14px;
        font-weight: 700;
        font-size: 0.92rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      }}
      
      /* Module TOC Summary */
      .module-toc-summary {{
        background: linear-gradient(135deg, #fff 0%, #e5f5f9 100%);
        border: 3px solid #2ca25f;
        border-left: 12px solid #2ca25f;
        border-radius: 14px;
        padding: 24px;
        margin: 24px 0;
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
      }}
      .module-toc-summary h2 {{
        color: #2ca25f !important;
        margin: 0 0 16px;
        font-size: 1.5rem;
        border: none !important;
        padding: 0 !important;
      }}
      .toc-list {{
        list-style: none;
        padding: 0;
        margin: 0;
        display: grid;
        gap: 12px;
      }}
      .toc-item {{
        background: #fff;
        border: 2px solid #99d8c9;
        border-radius: 10px;
        transition: all 0.3s;
      }}
      .toc-item:hover {{
        border-color: #2ca25f;
        transform: translateX(8px);
        box-shadow: 0 4px 12px rgba(44, 162, 95, 0.2);
      }}
      .toc-link {{
        display: block;
        padding: 16px;
        text-decoration: none;
        color: inherit;
      }}
      .toc-link strong {{
        display: block;
        color: #2ca25f !important;
        font-size: 1.1rem;
        margin-bottom: 6px;
      }}
      .toc-preview {{
        display: block;
        color: #555 !important;
        font-size: 0.9rem;
        line-height: 1.4;
      }}
      
      footer {{ max-width: 1000px; margin: 24px auto; padding: 0 16px 24px; color: #333; text-align: center; }}
      
      /* ===== PROGRESS TRACKING STYLES ===== */
      .progress-container {{
        background: #e5f5f9;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 30px;
        border: 2px solid #99d8c9;
      }}
      .progress-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
      }}
      .progress-header h3 {{
        margin: 0;
        color: #2ca25f !important;
      }}
      .reset-progress-btn {{
        background: #ff6b6b;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 14px;
        transition: all 0.2s;
      }}
      .reset-progress-btn:hover {{
        background: #ee5a52;
        transform: translateY(-2px);
      }}
      .progress-bar-container {{
        background: white;
        height: 40px;
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid #99d8c9;
      }}
      .module-progress-bar {{
        height: 100%;
        background: linear-gradient(90deg, #2ca25f, #10a05d);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        font-size: 14px;
        transition: width 0.5s ease;
        min-width: 80px;
      }}
      .lesson-checkbox {{
        width: 20px;
        height: 20px;
        cursor: pointer;
        accent-color: #2ca25f;
      }}
      .lesson-checkbox-container {{
        vertical-align: middle;
      }}
      
      /* ===== SEARCH STYLES ===== */
      .search-bar {{
        background: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border: 2px solid #99d8c9;
      }}
      .search-input-container {{
        position: relative;
        display: flex;
        align-items: center;
      }}
      #searchInput {{
        width: 100%;
        padding: 14px 50px 14px 16px;
        font-size: 16px;
        border: 2px solid #2ca25f;
        border-radius: 8px;
        outline: none;
        transition: all 0.2s;
      }}
      #searchInput:focus {{
        border-color: #238b53;
        box-shadow: 0 0 0 3px rgba(44, 162, 95, 0.1);
      }}
      .clear-search-btn {{
        position: absolute;
        right: 10px;
        background: transparent;
        border: none;
        font-size: 20px;
        cursor: pointer;
        color: #999;
        padding: 5px 10px;
        transition: color 0.2s;
      }}
      .clear-search-btn:hover {{
        color: #ff6b6b;
      }}
      .search-results {{
        margin-top: 15px;
        max-height: 400px;
        overflow-y: auto;
        border-radius: 8px;
      }}
      .results-header {{
        background: #e5f5f9;
        padding: 10px 15px;
        font-weight: bold;
        color: #2ca25f;
        border-radius: 6px 6px 0 0;
      }}
      .search-result-item {{
        padding: 12px 15px;
        border-bottom: 1px solid #eee;
        cursor: pointer;
        transition: all 0.2s;
      }}
      .search-result-item:hover {{
        background: #f7fafc;
        border-left: 4px solid #2ca25f;
      }}
      .result-type {{
        font-size: 11px;
        color: #999;
        text-transform: uppercase;
        margin-bottom: 5px;
      }}
      .result-text {{
        margin-bottom: 5px;
        line-height: 1.5;
      }}
      .result-text mark {{
        background: #ffeb3b;
        padding: 2px 4px;
        border-radius: 3px;
      }}
      .result-module {{
        font-size: 12px;
        color: #666;
      }}
      .no-results {{
        padding: 20px;
        text-align: center;
        color: #999;
      }}
      .search-highlight {{
        background: #ffeb3b !important;
        padding: 4px;
        border-radius: 4px;
        transition: background 0.3s;
      }}
      .search-highlight-active {{
        background: #ffc107 !important;
        animation: pulse 0.5s ease;
      }}
      @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
      }}
      
      /* ===== QUIZ STYLES ===== */
      .quiz-card {{
        background: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
        border: 2px solid #99d8c9;
        margin: 20px 0;
      }}
      .quiz-progress-bar {{
        height: 8px;
        background: #e0e0e0;
        border-radius: 4px;
        margin-bottom: 20px;
        overflow: hidden;
      }}
      .quiz-progress-fill {{
        height: 100%;
        background: linear-gradient(90deg, #2ca25f, #10a05d);
        transition: width 0.5s ease;
      }}
      .quiz-header {{
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
        font-size: 14px;
      }}
      .quiz-counter {{
        color: #666;
        font-weight: 500;
      }}
      .quiz-score {{
        color: #2ca25f;
        font-weight: bold;
      }}
      .quiz-question {{
        color: #2ca25f !important;
        font-size: 1.3rem;
        margin-bottom: 20px;
      }}
      .quiz-code {{
        background: #1e1e1e !important;
        color: #d4d4d4 !important;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
        font-family: 'Consolas', monospace;
      }}
      .quiz-options {{
        display: grid;
        gap: 12px;
        margin: 20px 0;
      }}
      .quiz-option {{
        display: flex;
        align-items: center;
        padding: 15px;
        background: #f7fafc;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        cursor: pointer;
        text-align: left;
        font-size: 16px;
        transition: all 0.2s;
        gap: 12px;
      }}
      .quiz-option:hover:not(.disabled) {{
        background: #e5f5f9;
        border-color: #2ca25f;
        transform: translateX(5px);
      }}
      .quiz-option.disabled {{
        cursor: not-allowed;
        opacity: 0.7;
      }}
      .quiz-option.correct {{
        background: #d4f4dd;
        border-color: #2ca25f;
        border-width: 3px;
      }}
      .quiz-option.incorrect {{
        background: #ffe0e0;
        border-color: #ff6b6b;
        border-width: 3px;
      }}
      .option-letter {{
        display: flex;
        align-items: center;
        justify-content: center;
        min-width: 32px;
        height: 32px;
        background: #2ca25f;
        color: white;
        border-radius: 50%;
        font-weight: bold;
        font-size: 14px;
      }}
      .quiz-option.correct .option-letter {{
        background: #10a05d;
      }}
      .quiz-option.incorrect .option-letter {{
        background: #ff6b6b;
      }}
      .option-text {{
        flex: 1;
      }}
      .quiz-feedback {{
        margin-top: 20px;
        padding: 15px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 500;
      }}
      .feedback-correct {{
        background: #d4f4dd;
        color: #1e7d5a;
        display: flex;
        align-items: center;
        gap: 10px;
      }}
      .feedback-incorrect {{
        background: #ffe0e0;
        color: #c92a2a;
        display: flex;
        align-items: center;
        gap: 10px;
      }}
      .feedback-icon {{
        font-size: 24px;
      }}
      .quiz-explanation {{
        margin-top: 15px;
        padding: 15px;
        background: #e5f5f9;
        border-left: 4px solid #2ca25f;
        border-radius: 6px;
        color: #062b1e;
      }}
      .quiz-results {{
        text-align: center;
        padding: 40px 20px;
      }}
      .results-icon {{
        font-size: 80px;
        margin-bottom: 20px;
      }}
      .results-score {{
        margin: 30px 0;
      }}
      .score-circle {{
        position: relative;
        display: inline-block;
      }}
      .score-text {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
      }}
      .score-percent {{
        font-size: 36px;
        font-weight: bold;
        color: #2ca25f;
      }}
      .score-fraction {{
        font-size: 16px;
        color: #666;
      }}
      .results-message {{
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        font-size: 18px;
      }}
      .results-message.pass {{
        background: #d4f4dd;
        color: #1e7d5a;
      }}
      .results-message.fail {{
        background: #ffe0e0;
        color: #c92a2a;
      }}
      .results-details {{
        margin: 30px 0;
        text-align: left;
      }}
      .answers-list {{
        display: grid;
        gap: 10px;
        margin-top: 15px;
      }}
      .answer-item {{
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px;
        border-radius: 6px;
      }}
      .answer-item.correct {{
        background: #d4f4dd;
      }}
      .answer-item.incorrect {{
        background: #ffe0e0;
      }}
      .answer-number {{
        font-weight: bold;
        min-width: 30px;
      }}
      .answer-icon {{
        font-size: 18px;
      }}
      .answer-text {{
        flex: 1;
        font-size: 14px;
      }}
      .results-actions {{
        display: flex;
        gap: 15px;
        justify-content: center;
        margin-top: 30px;
      }}
      .retry-btn, .continue-btn {{
        padding: 15px 30px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
      }}
      .retry-btn {{
        background: #2ca25f;
        color: white;
      }}
      .retry-btn:hover {{
        background: #238b53;
        transform: translateY(-2px);
      }}
      .continue-btn {{
        background: #007bff;
        color: white;
      }}
      .continue-btn:hover {{
        background: #0056b3;
        transform: translateY(-2px);
      }}
    </style>
  </head>
  <body class=\"{body_class}\">
    <header role=\"banner\">
      <div class=\"wrap\">
        <h1>{title}</h1>

      </div>
    </header>
    <main id=\"conteudo\" role=\"main\">
      <article class=\"md-content\" aria-label=\"Conteúdo\">
        {content}
      </article>
    </main>
    <footer role=\"contentinfo\">
      <p>Gerado automaticamente em {date}. Paleta: ColorBrewer BuGn.</p>
    </footer>
    
    <!-- External JavaScript Files -->
    <script src="../../assets/progress.js"></script>
    <script src="../../assets/search.js"></script>
    <script src="../../assets/quiz.js"></script>
    
    <script>
      // Add copy buttons to all code blocks
      document.addEventListener('DOMContentLoaded', function() {{
        const codeBlocks = document.querySelectorAll('pre');
        
        codeBlocks.forEach(block => {{
          const button = document.createElement('button');
          button.className = 'copy-btn';
          button.textContent = 'Copiar';
          button.setAttribute('aria-label', 'Copiar código');
          
          button.addEventListener('click', async () => {{
            const code = block.querySelector('code');
            const text = code ? code.textContent : block.textContent;
            
            try {{
              await navigator.clipboard.writeText(text);
              button.textContent = '✓ Copiado!';
              button.classList.add('copied');
              
              setTimeout(() => {{
                button.textContent = 'Copiar';
                button.classList.remove('copied');
              }}, 2000);
            }} catch (err) {{
              button.textContent = '✗ Erro';
              setTimeout(() => {{
                button.textContent = 'Copiar';
              }}, 2000);
            }}
          }});
          
          block.style.position = 'relative';
          block.appendChild(button);
        }});
      }});
      
      // Tabs System
      document.addEventListener('DOMContentLoaded', function() {{
        const tabButtons = document.querySelectorAll('.tab-button');
        const tabContents = document.querySelectorAll('.tab-content');
        
        tabButtons.forEach((button, index) => {{
          button.addEventListener('click', () => {{
            // Remove active from all
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active to clicked
            button.classList.add('active');
            tabContents[index].classList.add('active');
          }});
        }});
        
        // Activate first tab by default
        if (tabButtons.length > 0) {{
          tabButtons[0].classList.add('active');
          tabContents[0].classList.add('active');
        }}
      }});
    </script>
    <script src=\"{assets}/site.js\"></script>
  </body>
</html>
"""


def ensure_dirs():
    OUT.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)


def md_to_html(md_text: str) -> str:
    return markdown(md_text, extensions=MD_EXTS)


def extract_title(md_text: str, fallback: str) -> str:
    # first H1 or H2
    for line in md_text.splitlines():
        if line.startswith('# '):
            return line[2:].strip()
        if line.startswith('## '):
            return line[3:].strip()
    return fallback


def build_page(md_path: Path, out_path: Path):
    md_text = md_path.read_text(encoding='utf-8')
    title = extract_title(md_text, md_path.stem.replace('-', ' '))
    html_body = md_to_html(md_text)
    
    html = TEMPLATE.format(
        title=title,
        content=html_body,
      assets=Path('../assets').as_posix(),
      index=Path('../index.html').as_posix(),
        repo=REPO_URL,
        site=SITE_URL,
      date=datetime.now().strftime('%d/%m/%Y %H:%M'),
      body_class="presentation"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding='utf-8')
    print(f"✔ {md_path} → {out_path}")


def strip_first_heading(html_text: str) -> str:
    # remove the first <h1> or <h2> to avoid duplicated titles inside panels
    pattern = re.compile(r"^\s*<h[12][^>]*>.*?</h[12]>", re.IGNORECASE | re.DOTALL)
    return re.sub(pattern, "", html_text, count=1)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip('-')
    return text or "sec"


def build_module_index(module_dir: Path):
  md_files = sorted(module_dir.glob('*.md'))
  if not md_files:
    return
  
  # Build sections and collect TOC info
  sections: list[str] = []
  toc_items: list[dict] = []
  
  for md_path in md_files:
    md_text = md_path.read_text(encoding='utf-8')
    title = extract_title(md_text, md_path.stem.replace('-', ' '))
    html_body = md_to_html(md_text)
    html_body = strip_first_heading(html_body)
    anchor = slugify(title)
    
    # Extract first paragraph as preview
    preview_match = re.search(r'<p>(.*?)</p>', html_body, re.DOTALL)
    preview = preview_match.group(1)[:150] + '...' if preview_match else ''
    preview = re.sub(r'<[^>]+>', '', preview)  # Remove HTML tags
    
    toc_items.append({
      'title': title,
      'anchor': anchor,
      'preview': preview,
      'filename': md_path.stem
    })
    
    sections.append(
      f"<section class=\"module-section\" id=\"{anchor}\"><h2>{title}</h2>{html_body}</section>"
    )

  # Build TOC HTML
  toc_html = '<nav class="module-toc-summary"><h2>📚 Neste módulo</h2><ul class="toc-list">'
  for item in toc_items:
    toc_html += f'''
    <li class="toc-item">
      <a href="#{item['anchor']}" class="toc-link">
        <strong>{item['title']}</strong>
        <span class="toc-preview">{item['preview']}</span>
      </a>
    </li>
    '''
  toc_html += '</ul></nav>'

  hero_html = ""
  if module_dir.name == "0-Fundamentos":
    hero_html = (
      "<section class=\"hero\">"
      "<h2>Este tutorial é para você!</h2>"
      "<p>Desenvolvido para biólogos, oceanógrafos e pesquisadores que desejam aprender programação aplicada à pesquisa científica. Não precisa experiência prévia.</p>"
      "<div class=\"chips\">"
      "<span class=\"chip\">Python • Geoespacial • Web</span>"
      "<span class=\"chip\">Didático • Acessível • Reproduzível</span>"
      "</div>"
      "<h3>Objetivos</h3>"
      "<ul>"
      "<li>✅ Programar em Python do zero ao intermediário</li>"
      "<li>✅ Processar e analisar dados de pesquisa automaticamente</li>"
      "<li>✅ Criar mapas interativos de distribuição de espécies</li>"
      "<li>✅ Desenvolver dashboards web para apresentar resultados</li>"
      "<li>✅ Automatizar workflows de coleta e análise</li>"
      "<li>✅ Publicar resultados de forma reproduzível e profissional</li>"
      "</ul>"
      "<h3>Foco em Ficologia e Oceanografia</h3>"
      "<ul>"
      "<li>Distribuição de macroalgas (Ulva lactuca, Gracilaria, Sargassum)</li>"
      "<li>Parâmetros oceanográficos (temperatura, salinidade, profundidade)</li>"
      "<li>Mapeamento de estações de coleta</li>"
      "<li>Análise de biodiversidade marinha</li>"
      "</ul>"
      "</section>"
    )
  content = "<div class=\"module-content\">" + hero_html + toc_html + "\n" + "\n".join(sections) + "</div>"

  title = module_dir.name.replace('-', ' ') + " — Módulo completo"
  out_path = OUT / module_dir.name / "index.html"
  out_path.parent.mkdir(parents=True, exist_ok=True)
  html = TEMPLATE.format(
    title=title,
    content=content,
    assets=Path('../assets').as_posix(),
    index=Path('../index.html').as_posix(),
    repo=REPO_URL,
    site=SITE_URL,
    date=datetime.now().strftime('%d/%m/%Y %H:%M'),
    body_class="presentation"
  )
  out_path.write_text(html, encoding='utf-8')
  print(f"★ módulo {module_dir.name} → {out_path}")


def build_all():
  ensure_dirs()
  for module in MODULES:
    mod_dir = ROOT / module
    if not mod_dir.exists():
      continue
    for md in mod_dir.glob('**/*.md'):
      rel = md.relative_to(ROOT)
      out_rel = Path(rel).with_suffix('.html')
      out_path = OUT / out_rel
      build_page(md, out_path)
    # também gera uma página consolidada do módulo
    build_module_index(mod_dir)


if __name__ == '__main__':
  # Modo de uso:
  #   python build_site.py            -> gera tudo (páginas e índices por módulo)
  #   python build_site.py 0-Fundamentos -> gera apenas o índice consolidado desse módulo
  if len(sys.argv) > 1:
    target = sys.argv[1]
    mod_dir = (ROOT / target) if not target.startswith(str(ROOT)) else Path(target)
    if not mod_dir.exists() or not mod_dir.is_dir():
      print(f"Módulo não encontrado: {mod_dir}")
      sys.exit(1)
    ensure_dirs()
    build_module_index(mod_dir)
  else:
    build_all()
