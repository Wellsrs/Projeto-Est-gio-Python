def fibonacci(n):
    # Função para calcular a sequência de Fibonacci até o número n
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

# Input do usuário
num = int(input("Informe um número: "))

# Verificar se o número pertence à sequência de Fibonacci
if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
