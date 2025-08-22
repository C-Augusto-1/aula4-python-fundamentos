"""
 Compreensão de Lista (List Comprehension) em Python
---------------------------------------------------------

O que é:
    Uma forma curta e prática de criar listas a partir de outras listas,
    ranges ou strings, sem precisar usar vários "for" e "append".

Sintaxe:
    [expressão for item in iterável if condição]

- expressão → o que você quer guardar na lista.
- for item in iterável → percorre os elementos.
- if condição → (opcional) serve para filtrar.


Para que serve:
    - Deixar o código menor e mais fácil de ler.
    - Criar listas transformando dados ou filtrando informações.
"""

# ---------------------------
# Exemplo 1: Criando uma lista de números dobrados (sem compreensão de lista)
dobrados = []                     # cria uma lista vazia chamada 'dobrados'

for x in range(5):                 # percorre os números 0, 1, 2, 3 e 4
    resultado = x * 2              # multiplica cada número por 2
    dobrados.append(resultado)     # adiciona o resultado dentro da lista 'dobrados'

print("Números dobrados:", dobrados)  # mostra a lista final
# Saída: [0, 2, 4, 6, 8]

# ---------------------------
# Exemplo 1: Criando uma lista de números dobrados
dobrados = [x * 2 for x in range(5)]
print("Números dobrados:", dobrados)
# Saída: [0, 2, 4, 6, 8]


# ---------------------------
# Exemplo 2: Trabalhando com strings (sem compreensão de lista)
# Transformar cada letra em maiúscula
letras = []                        # cria uma lista vazia chamada 'letras'

for letra in "python":             # percorre cada caractere da string "python"
    maiuscula = letra.upper()      # transforma a letra em maiúscula
    letras.append(maiuscula)       # adiciona a letra maiúscula à lista 'letras'

print("Letras em maiúsculas:", letras)  # mostra a lista final
# Saída: ['P', 'Y', 'T', 'H', 'O', 'N']
# ---------------------------

# Exemplo 2: Trabalhando com strings
# Transformar cada letra em maiúscula
letras = [letra.upper() for letra in "python"]
print("Letras em maiúsculas:", letras)
# Saída: ['P', 'Y', 'T', 'H', 'O', 'N']
# ---------------------------

# Exemplo 3: Usando filtro (if) (sem compreensão de lista)
# Guardar apenas os números pares de 0 a 10
pares = []                         # cria uma lista vazia chamada 'pares'

for n in range(11):                # percorre os números de 0 até 10
    if n % 2 == 0:                 # verifica se o número é par (resto da divisão por 2 é zero)
        pares.append(n)            # adiciona o número par à lista 'pares'

print("Números pares de 0 a 10:", pares)  # mostra a lista final
# Saída: [0, 2, 4, 6, 8, 10]

# ---------------------------
# Exemplo 3: Usando filtro (if)
# Guardar apenas os números pares de 0 a 10
pares = [n for n in range(11) if n % 2 == 0]
print("Números pares de 0 a 10:", pares)
# Saída: [0, 2, 4, 6, 8, 10]
