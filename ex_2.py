def main():
    texto = input("Digite uma string: ")

    texto_minusculo = texto.lower()

    quantidade_a = texto_minusculo.count('a')

    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vezes na string informada.")
    else:
        print("A letra 'a' não foi encontrada na string informada.")

if __name__ == "__main__":
    main()