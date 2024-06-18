def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq


def lucas(n):
    lucas_seq = [2, 1]
    for i in range(2, n):
        lucas_seq.append(lucas_seq[-1] + lucas_seq[-2])
    return lucas_seq


fib_list = fibonacci(12)
lucas_list = lucas(12)


print("Sequência de Fibonacci:", fib_list)
print("Sequência de Números de Lucas:", lucas_list)

def exibir_pares(lista1, lista2):
    pares = [num for num in lista1 + lista2 if num % 2 == 0]
    return pares

numeros_pares = exibir_pares(fib_list, lucas_list)
print("Números pares nas listas:", numeros_pares)