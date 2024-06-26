
N = int(input("Digite um número inteiro para determinar a quantidade de números da sequência de Fibonacci a serem impressos: "))

if N <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    
    fibonacci = [0, 1]
    for i in range(2, N):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    print(f"Os primeiros {N} números da sequência de Fibonacci são:")
    for num in fibonacci[:N]:
        print(num, end=" ")
    print() 