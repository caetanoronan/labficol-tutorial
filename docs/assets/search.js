// Sistema de busca em tempo real no conteúdo
class CourseSearch {
    constructor() {
        this.index = [];
        this.buildIndex();
    }
    
    buildIndex() {
        // Indexar títulos e parágrafos
        const selectors = '.module-section h2, .module-section h3, .module-section p, .module-section li, .toc-item';
        document.querySelectorAll(selectors).forEach(el => {
            const text = el.textContent.trim();
            if (text.length < 10) return; // Ignorar textos muito curtos
            
            this.index.push({
                text: text,
                element: el,
                module: this.getModuleName(el),
                type: el.tagName.toLowerCase(),
                id: el.id || this.generateId(el)
            });
        });
        
        console.log(`📚 Índice de busca criado com ${this.index.length} itens`);
    }
    
    getModuleName(element) {
        const path = window.location.pathname;
        const match = path.match(/\/(\d+-[^\/]+)\//);
        if (match) {
            return match[1].replace(/-/g, ' ').replace(/\d+\s*/, '');
        }
        return document.querySelector('.hero h1')?.textContent || 'Conteúdo';
    }
    
    generateId(element) {
        if (!element.id) {
            element.id = 'search-' + Math.random().toString(36).substr(2, 9);
        }
        return element.id;
    }
    
    search(query) {
        if (query.length < 2) return [];
        
        const lowerQuery = query.toLowerCase();
        const words = lowerQuery.split(/\s+/).filter(w => w.length > 1);
        
        return this.index
            .map(item => {
                const text = item.text.toLowerCase();
                let score = 0;
                
                // Pontuação por correspondência exata
                if (text.includes(lowerQuery)) {
                    score += 10;
                }
                
                // Pontuação por palavras individuais
                words.forEach(word => {
                    if (text.includes(word)) {
                        score += 3;
                    }
                });
                
                // Bônus para títulos
                if (item.type === 'h2' || item.type === 'h3') {
                    score *= 1.5;
                }
                
                return { ...item, score };
            })
            .filter(item => item.score > 0)
            .sort((a, b) => b.score - a.score);
    }
    
    highlight(results, query) {
        // Remover highlights anteriores
        document.querySelectorAll('.search-highlight').forEach(el => {
            el.classList.remove('search-highlight');
        });
        
        // Adicionar novos highlights
        results.slice(0, 5).forEach(result => {
            result.element.classList.add('search-highlight');
        });
    }
    
    scrollTo(elementId) {
        const element = document.getElementById(elementId);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth', block: 'center' });
            element.classList.add('search-highlight-active');
            
            setTimeout(() => {
                element.classList.remove('search-highlight-active');
            }, 2000);
        }
    }
}

// Inicializar busca
document.addEventListener('DOMContentLoaded', function() {
    const search = new CourseSearch();
    
    // Criar UI de busca
    const searchBar = document.createElement('div');
    searchBar.className = 'search-bar';
    searchBar.innerHTML = `
        <div class="search-input-container">
            <input type="text" id="searchInput" placeholder="🔍 Buscar no conteúdo... (mín. 2 caracteres)">
            <button id="clearSearch" class="clear-search-btn" style="display: none;">✕</button>
        </div>
        <div id="searchResults" class="search-results"></div>
    `;
    
    const hero = document.querySelector('.hero');
    if (hero) {
        hero.after(searchBar);
    }
    
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');
    const clearBtn = document.getElementById('clearSearch');
    
    // Busca em tempo real com debounce
    let debounceTimer;
    searchInput.addEventListener('input', function() {
        const query = this.value.trim();
        
        // Mostrar/ocultar botão de limpar
        clearBtn.style.display = query.length > 0 ? 'block' : 'none';
        
        clearTimeout(debounceTimer);
        
        if (query.length < 2) {
            searchResults.innerHTML = '';
            searchResults.style.display = 'none';
            return;
        }
        
        debounceTimer = setTimeout(() => {
            const results = search.search(query);
            displayResults(results.slice(0, 10), query);
            search.highlight(results, query);
        }, 300);
    });
    
    // Botão de limpar
    clearBtn.addEventListener('click', function() {
        searchInput.value = '';
        searchResults.innerHTML = '';
        searchResults.style.display = 'none';
        this.style.display = 'none';
        document.querySelectorAll('.search-highlight').forEach(el => {
            el.classList.remove('search-highlight');
        });
    });
    
    // Enter para ir ao primeiro resultado
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            const firstResult = searchResults.querySelector('.search-result-item');
            if (firstResult) {
                firstResult.click();
            }
        }
    });
    
    function displayResults(results, query) {
        if (results.length === 0) {
            searchResults.innerHTML = '<div class="no-results">❌ Nenhum resultado encontrado</div>';
            searchResults.style.display = 'block';
            return;
        }
        
        const highlightQuery = (text, query) => {
            const regex = new RegExp(`(${query})`, 'gi');
            return text.replace(regex, '<mark>$1</mark>');
        };
        
        searchResults.innerHTML = `
            <div class="results-header">
                📚 ${results.length} resultado${results.length > 1 ? 's' : ''} encontrado${results.length > 1 ? 's' : ''}
            </div>
            ${results.map(r => {
                const preview = r.text.length > 120 ? r.text.substring(0, 120) + '...' : r.text;
                const highlighted = highlightQuery(preview, query);
                
                return `
                    <div class="search-result-item" data-id="${r.id}">
                        <div class="result-type">${getTypeIcon(r.type)} ${r.type.toUpperCase()}</div>
                        <div class="result-text">${highlighted}</div>
                        <div class="result-module">📂 ${r.module}</div>
                    </div>
                `;
            }).join('')}
        `;
        
        searchResults.style.display = 'block';
        
        // Click nos resultados
        searchResults.querySelectorAll('.search-result-item').forEach(item => {
            item.addEventListener('click', function() {
                const id = this.dataset.id;
                search.scrollTo(id);
                searchInput.value = '';
                searchResults.style.display = 'none';
                clearBtn.style.display = 'none';
            });
        });
    }
    
    function getTypeIcon(type) {
        const icons = {
            'h2': '📌',
            'h3': '📍',
            'p': '📄',
            'li': '•',
            'div': '📦'
        };
        return icons[type] || '📄';
    }
    
    // Atalho Ctrl+K para focar busca
    document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            searchInput.focus();
        }
        
        // ESC para limpar busca
        if (e.key === 'Escape') {
            searchInput.value = '';
            searchResults.innerHTML = '';
            searchResults.style.display = 'none';
            clearBtn.style.display = 'none';
        }
    });
});
