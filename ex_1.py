def main():
    numero = int(input("Informe um número: "))

    fibonacci = [0, 1]

    while fibonacci[-1] < numero:
        proximo_valor = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_valor)

    if numero in fibonacci:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
