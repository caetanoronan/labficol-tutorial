// Sistema de progresso do aluno usando LocalStorage
class CourseProgress {
    constructor() {
        this.storageKey = 'courseProgress';
        this.progress = this.load();
    }
    
    load() {
        const saved = localStorage.getItem(this.storageKey);
        return saved ? JSON.parse(saved) : {};
    }
    
    save() {
        localStorage.setItem(this.storageKey, JSON.stringify(this.progress));
    }
    
    markComplete(moduleId, lessonId) {
        if (!this.progress[moduleId]) {
            this.progress[moduleId] = {};
        }
        this.progress[moduleId][lessonId] = {
            completed: true,
            date: new Date().toISOString()
        };
        this.save();
        this.updateUI();
    }
    
    isComplete(moduleId, lessonId) {
        return this.progress[moduleId]?.[lessonId]?.completed || false;
    }
    
    getModuleProgress(moduleId) {
        const lessons = this.progress[moduleId] || {};
        const completed = Object.values(lessons).filter(l => l.completed).length;
        const total = document.querySelectorAll(`.lesson-checkbox[data-module="${moduleId}"]`).length;
        return { completed, total: total || 1 };
    }
    
    updateUI() {
        // Atualizar checkboxes
        document.querySelectorAll('.lesson-checkbox').forEach(checkbox => {
            const moduleId = checkbox.dataset.module;
            const lessonId = checkbox.dataset.lesson;
            checkbox.checked = this.isComplete(moduleId, lessonId);
        });
        
        // Atualizar progress bar se existir
        const progressBar = document.querySelector('.module-progress-bar');
        if (progressBar) {
            const moduleId = progressBar.dataset.module;
            const progress = this.getModuleProgress(moduleId);
            const percent = progress.total > 0 ? (progress.completed / progress.total) * 100 : 0;
            progressBar.style.width = `${percent}%`;
            progressBar.innerHTML = `<span>${progress.completed}/${progress.total} completo (${percent.toFixed(0)}%)</span>`;
        }
    }
    
    reset() {
        if (confirm('Tem certeza que deseja resetar todo o progresso?')) {
            localStorage.removeItem(this.storageKey);
            this.progress = {};
            this.updateUI();
            alert('Progresso resetado com sucesso!');
        }
    }
}

// Inicializar ao carregar página
document.addEventListener('DOMContentLoaded', function() {
    const tracker = new CourseProgress();
    
    // Obter módulo atual da URL ou título
    const getCurrentModule = () => {
        const path = window.location.pathname;
        const match = path.match(/\/(\d+-[^\/]+)\//);
        return match ? match[1] : 'unknown';
    };
    
    const currentModule = getCurrentModule();
    
    // Adicionar checkboxes em cada item do TOC
    document.querySelectorAll('.toc-item').forEach((item, index) => {
        const lessonLink = item.querySelector('h3 a');
        if (!lessonLink) return;
        
        const lessonId = lessonLink.getAttribute('href')?.replace('#', '') || `lesson-${index}`;
        
        const checkboxContainer = document.createElement('div');
        checkboxContainer.className = 'lesson-checkbox-container';
        checkboxContainer.style.display = 'inline-block';
        checkboxContainer.style.marginRight = '10px';
        
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.className = 'lesson-checkbox';
        checkbox.dataset.module = currentModule;
        checkbox.dataset.lesson = lessonId;
        checkbox.title = 'Marcar como completo';
        
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                tracker.markComplete(this.dataset.module, this.dataset.lesson);
                showCompletionEffect(this);
            } else {
                // Remover marcação
                if (tracker.progress[this.dataset.module]) {
                    delete tracker.progress[this.dataset.module][this.dataset.lesson];
                    tracker.save();
                    tracker.updateUI();
                }
            }
        });
        
        checkboxContainer.appendChild(checkbox);
        lessonLink.parentElement.insertBefore(checkboxContainer, lessonLink);
    });
    
    // Adicionar progress bar no topo do módulo
    const moduleSection = document.querySelector('.module-section');
    if (moduleSection && document.querySelectorAll('.lesson-checkbox').length > 0) {
        const progressContainer = document.createElement('div');
        progressContainer.className = 'progress-container';
        progressContainer.innerHTML = `
            <div class="progress-header">
                <h3>📊 Seu Progresso</h3>
                <button class="reset-progress-btn" onclick="window.courseTracker.reset()">🔄 Resetar</button>
            </div>
            <div class="progress-bar-container">
                <div class="module-progress-bar" data-module="${currentModule}">
                    <span>0/0 completo (0%)</span>
                </div>
            </div>
        `;
        moduleSection.insertBefore(progressContainer, moduleSection.firstChild);
    }
    
    // Tornar tracker global para acesso no reset
    window.courseTracker = tracker;
    
    // Atualizar UI inicial
    tracker.updateUI();
});

// Efeito visual ao completar lição
function showCompletionEffect(element) {
    const container = element.closest('.toc-item') || element.parentElement;
    
    // Animação de confete simples
    container.style.transition = 'all 0.3s';
    container.style.transform = 'scale(1.05)';
    container.style.background = '#d4f4dd';
    
    setTimeout(() => {
        container.style.transform = 'scale(1)';
    }, 300);
    
    setTimeout(() => {
        container.style.background = '';
    }, 1000);
    
    // Emoji de celebração
    const celebration = document.createElement('span');
    celebration.textContent = '🎉';
    celebration.style.position = 'absolute';
    celebration.style.fontSize = '24px';
    celebration.style.animation = 'float-up 1s ease-out';
    element.parentElement.appendChild(celebration);
    
    setTimeout(() => celebration.remove(), 1000);
}

// CSS para animação
const style = document.createElement('style');
style.textContent = `
    @keyframes float-up {
        0% { transform: translateY(0) scale(1); opacity: 1; }
        100% { transform: translateY(-50px) scale(1.5); opacity: 0; }
    }
`;
document.head.appendChild(style);
