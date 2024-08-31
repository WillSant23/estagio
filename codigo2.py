def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    
    return fib_sequence

def verifica_fibonacci(num):
    fib_sequence = fibonacci(num)
    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Solicita ao usuário que informe um número
numero_informado = int(input("Informe um número: "))
resultado = verifica_fibonacci(numero_informado)
print(resultado)