def verifica_fibonacci(numero):
    fibonacci = [0, 1]
    while fibonacci[-1] < numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if numero in fibonacci:
        return True, fibonacci
    else:
        return False, fibonacci

numero_informado = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

pertence, sequencia = verifica_fibonacci(numero_informado)

if pertence:
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
    print("Sequência de Fibonacci até o número informado:", sequencia)
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")
    print("Sequência de Fibonacci até o número informado:", sequencia[:-1])
