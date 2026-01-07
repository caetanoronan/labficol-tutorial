// Sistema de quiz interativo
class Quiz {
    constructor(questions, containerId = 'quizContainer') {
        this.questions = questions;
        this.containerId = containerId;
        this.currentQuestion = 0;
        this.score = 0;
        this.answers = [];
    }
    
    render() {
        const container = document.getElementById(this.containerId);
        if (!container) {
            console.error(`Container #${this.containerId} não encontrado`);
            return;
        }
        
        const q = this.questions[this.currentQuestion];
        const progress = ((this.currentQuestion) / this.questions.length) * 100;
        
        container.innerHTML = `
            <div class="quiz-card">
                <div class="quiz-progress-bar">
                    <div class="quiz-progress-fill" style="width: ${progress}%"></div>
                </div>
                
                <div class="quiz-header">
                    <span class="quiz-counter">Questão ${this.currentQuestion + 1} de ${this.questions.length}</span>
                    <span class="quiz-score">Pontuação: ${this.score}</span>
                </div>
                
                <h3 class="quiz-question">${q.question}</h3>
                
                ${q.code ? `<pre class="quiz-code"><code>${this.escapeHtml(q.code)}</code></pre>` : ''}
                
                <div class="quiz-options">
                    ${q.options.map((opt, i) => `
                        <button class="quiz-option" data-answer="${i}">
                            <span class="option-letter">${String.fromCharCode(65 + i)}</span>
                            <span class="option-text">${opt}</span>
                        </button>
                    `).join('')}
                </div>
                
                <div class="quiz-feedback"></div>
                
                ${q.explanation ? `<div class="quiz-explanation" style="display: none;">
                    💡 <strong>Explicação:</strong> ${q.explanation}
                </div>` : ''}
            </div>
        `;
        
        // Event listeners
        container.querySelectorAll('.quiz-option').forEach(btn => {
            btn.addEventListener('click', () => {
                if (!btn.classList.contains('disabled')) {
                    this.checkAnswer(parseInt(btn.dataset.answer));
                }
            });
        });
    }
    
    checkAnswer(selected) {
        const q = this.questions[this.currentQuestion];
        const feedback = document.querySelector('.quiz-feedback');
        const explanation = document.querySelector('.quiz-explanation');
        const buttons = document.querySelectorAll('.quiz-option');
        
        // Desabilitar todos botões
        buttons.forEach(btn => btn.classList.add('disabled'));
        
        // Registrar resposta
        this.answers.push({
            question: q.question,
            selected: selected,
            correct: q.correct,
            isCorrect: selected === q.correct
        });
        
        // Marcar resposta correta e incorreta
        buttons[q.correct].classList.add('correct');
        if (selected !== q.correct) {
            buttons[selected].classList.add('incorrect');
        }
        
        // Feedback
        if (selected === q.correct) {
            this.score++;
            feedback.innerHTML = `
                <div class="feedback-correct">
                    <span class="feedback-icon">✅</span>
                    <span>Correto! +1 ponto</span>
                </div>
            `;
            this.playSound('correct');
        } else {
            feedback.innerHTML = `
                <div class="feedback-incorrect">
                    <span class="feedback-icon">❌</span>
                    <span>Incorreto. A resposta correta é: <strong>${q.options[q.correct]}</strong></span>
                </div>
            `;
            this.playSound('incorrect');
        }
        
        // Mostrar explicação se existir
        if (explanation) {
            explanation.style.display = 'block';
        }
        
        // Próxima questão após 3s
        setTimeout(() => {
            this.currentQuestion++;
            if (this.currentQuestion < this.questions.length) {
                this.render();
            } else {
                this.showResults();
            }
        }, 3000);
    }
    
    showResults() {
        const container = document.getElementById(this.containerId);
        const percent = (this.score / this.questions.length) * 100;
        const passed = percent >= 70;
        
        container.innerHTML = `
            <div class="quiz-results">
                <div class="results-icon">${passed ? '🎉' : '📚'}</div>
                <h2>Quiz Completo!</h2>
                
                <div class="results-score">
                    <div class="score-circle">
                        <svg width="150" height="150">
                            <circle cx="75" cy="75" r="65" fill="none" stroke="#e0e0e0" stroke-width="10"/>
                            <circle cx="75" cy="75" r="65" fill="none" stroke="${passed ? '#2ca25f' : '#ff6b6b'}" 
                                    stroke-width="10" stroke-dasharray="${(percent/100) * 408.4} 408.4" 
                                    transform="rotate(-90 75 75)"/>
                        </svg>
                        <div class="score-text">
                            <div class="score-percent">${percent.toFixed(0)}%</div>
                            <div class="score-fraction">${this.score}/${this.questions.length}</div>
                        </div>
                    </div>
                </div>
                
                <div class="results-message ${passed ? 'pass' : 'fail'}">
                    ${passed ? 
                        '✅ <strong>Parabéns!</strong> Você atingiu a pontuação mínima e pode prosseguir para o próximo módulo.' :
                        '❌ <strong>Quase lá!</strong> Revise o conteúdo e tente novamente. Você precisa de 70% para avançar.'
                    }
                </div>
                
                <div class="results-details">
                    <h3>📊 Detalhes das Respostas</h3>
                    <div class="answers-list">
                        ${this.answers.map((ans, i) => `
                            <div class="answer-item ${ans.isCorrect ? 'correct' : 'incorrect'}">
                                <span class="answer-number">Q${i + 1}</span>
                                <span class="answer-icon">${ans.isCorrect ? '✅' : '❌'}</span>
                                <span class="answer-text">${ans.question.substring(0, 60)}...</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
                
                <div class="results-actions">
                    <button class="retry-btn" onclick="location.reload()">🔄 Refazer Quiz</button>
                    ${passed ? '<button class="continue-btn" onclick="window.scrollTo(0,0)">➡️ Continuar</button>' : ''}
                </div>
            </div>
        `;
        
        this.playSound(passed ? 'success' : 'fail');
    }
    
    playSound(type) {
        // Simples feedback sonoro usando Web Audio API
        try {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            if (type === 'correct') {
                oscillator.frequency.value = 800;
                gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.2);
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 0.2);
            } else if (type === 'incorrect') {
                oscillator.frequency.value = 200;
                gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.3);
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 0.3);
            }
        } catch (e) {
            // Navegador não suporta Web Audio API
        }
    }
    
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Função auxiliar para criar quiz facilmente
function createQuiz(containerId, questions) {
    const quiz = new Quiz(questions, containerId);
    quiz.render();
    return quiz;
}

// Exemplo de quiz Python básico (pode ser usado em qualquer página)
const examplePythonQuiz = [
    {
        question: "Qual é a saída do seguinte código?",
        code: "print(2 ** 3)",
        options: ["5", "6", "8", "9"],
        correct: 2,
        explanation: "O operador ** representa exponenciação em Python. 2³ = 8"
    },
    {
        question: "Como criar uma lista vazia em Python?",
        options: ["list = ()", "list = {}", "list = []", "list = <>"],
        correct: 2,
        explanation: "Listas em Python são criadas com colchetes []. Parênteses () são tuplas, chaves {} são dicionários."
    },
    {
        question: "Qual palavra-chave é usada para criar uma função?",
        options: ["function", "def", "func", "define"],
        correct: 1,
        explanation: "Em Python, usamos a palavra-chave 'def' para definir funções."
    },
    {
        question: "O que o seguinte código imprime?",
        code: "x = [1, 2, 3]\nprint(len(x))",
        options: ["[1, 2, 3]", "1, 2, 3", "3", "6"],
        correct: 2,
        explanation: "A função len() retorna o número de elementos em uma lista. A lista tem 3 elementos."
    },
    {
        question: "Qual é o tipo de dado de True em Python?",
        options: ["string", "int", "bool", "float"],
        correct: 2,
        explanation: "True e False são valores booleanos (bool) em Python."
    }
];

// Auto-inicializar quiz se container existir na página
document.addEventListener('DOMContentLoaded', function() {
    const quizContainer = document.getElementById('quizContainer');
    if (quizContainer && window.quizQuestions) {
        createQuiz('quizContainer', window.quizQuestions);
    }
});
