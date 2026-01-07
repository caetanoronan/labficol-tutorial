# 📖 Glossário - Python Essencial

## A

**Argumentos**: Valores passados para uma função quando ela é chamada.

**Array**: Estrutura de dados que armazena múltiplos valores em sequência (em Python, use listas).

**Atribuição**: Operação que define o valor de uma variável (ex: `x = 10`).

## B

**Booleano (bool)**: Tipo de dado que pode ser `True` ou `False`.

**Break**: Comando para interromper um loop prematuramente.

## C

**Class (Classe)**: Modelo para criar objetos com atributos e métodos específicos.

**Comentário**: Texto no código que não é executado, usado para explicações (inicia com `#`).

**Comprehension**: Sintaxe concisa para criar listas, dicionários ou conjuntos (ex: `[x**2 for x in range(10)]`).

**Condição**: Expressão que avalia para True ou False, usada em if/while.

**Continue**: Comando que pula para a próxima iteração de um loop.

## D

**def**: Palavra-chave para definir uma função em Python.

**Dicionário (dict)**: Estrutura de dados que mapeia chaves a valores (ex: `{"nome": "Ana", "idade": 25}`).

**Docstring**: String de documentação no início de funções/classes (entre `"""`).

## E

**elif**: Abreviação de "else if", usado para condições adicionais em estruturas if.

**else**: Cláusula executada quando condição if/elif é falsa.

**Escopo**: Região do código onde uma variável é acessível.

**Exceção**: Erro que ocorre durante a execução do programa.

## F

**f-string**: Formatação de strings com variáveis embutidas (ex: `f"Nome: {nome}"`).

**False**: Valor booleano que representa falso.

**Float**: Tipo de dado numérico com ponto decimal (números reais).

**for**: Loop que itera sobre uma sequência (lista, string, range, etc).

## G

**Global**: Variável acessível em todo o programa, fora de funções.

## I

**if**: Estrutura condicional que executa código apenas se condição for verdadeira.

**import**: Comando para carregar módulos/bibliotecas em seu programa.

**in**: Operador que verifica se elemento está em uma sequência.

**Indentação**: Espaços/tabs no início da linha que definem blocos de código em Python.

**IndexError**: Erro quando tenta acessar índice inexistente em lista.

**int**: Tipo de dado numérico inteiro (sem decimais).

**is**: Operador que verifica identidade de objetos (se são o mesmo objeto).

**Iteração**: Uma execução de um loop.

**Iterável**: Objeto que pode ser percorrido em loop (lista, tupla, string, etc).

## K

**KeyError**: Erro quando tenta acessar chave inexistente em dicionário.

**Keyword argument**: Argumento de função especificado por nome (ex: `func(nome="Ana")`).

## L

**Lambda**: Função anônima de uma linha (ex: `lambda x: x**2`).

**len()**: Função que retorna tamanho de sequência.

**Lista (list)**: Sequência ordenada e mutável de elementos `[1, 2, 3]`.

**Local**: Variável acessível apenas dentro da função onde foi criada.

## M

**Método**: Função associada a um objeto.

**Mutável**: Objeto que pode ser modificado após criação (listas, dicionários).

## N

**None**: Valor especial que representa ausência de valor.

**not**: Operador lógico de negação.

## O

**Objeto**: Instância de uma classe com dados e métodos.

**Operador**: Símbolo para operações (`+`, `-`, `*`, `/`, `==`, `>`, etc).

**or**: Operador lógico OU.

## P

**Parâmetro**: Variável na definição de função que recebe argumentos.

**pass**: Comando que não faz nada, usado como placeholder.

**print()**: Função para exibir saída no console.

**PEP 8**: Guia de estilo oficial para código Python.

## R

**range()**: Função que gera sequência de números.

**return**: Comando que retorna valor de uma função.

## S

**Set (conjunto)**: Coleção não ordenada de elementos únicos `{1, 2, 3}`.

**Slice (fatia)**: Operação para obter subsequência `lista[1:5]`.

**str (string)**: Tipo de dado textual (sequência de caracteres).

**SyntaxError**: Erro de sintaxe, código escrito incorretamente.

## T

**True**: Valor booleano que representa verdadeiro.

**try/except**: Estrutura para capturar e tratar exceções.

**Tupla (tuple)**: Sequência ordenada e imutável `(1, 2, 3)`.

**type()**: Função que retorna tipo de um objeto.

## V

**ValueError**: Erro quando função recebe argumento de tipo correto mas valor inadequado.

**Variável**: Nome que armazena valor que pode mudar.

## W

**while**: Loop que executa enquanto condição for verdadeira.

## Exemplos Práticos

```python
# Variáveis e tipos
nome = "Maria"  # string
idade = 25      # int
altura = 1.65   # float
ativo = True    # bool

# Lista (mutável)
frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")

# Tupla (imutável)
coordenadas = (10, 20)

# Dicionário
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "Florianópolis"
}

# Função
def calcular_area(largura, altura):
    """Calcula área de retângulo"""
    return largura * altura

# Condicional
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Loop for
for fruta in frutas:
    print(fruta)

# Loop while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Comprehension
quadrados = [x**2 for x in range(10)]

# Try/except
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero!")
```

---

💡 **Dica**: Use `help(função)` no Python para ver documentação de qualquer função!
