from statistics import median


def ler_inteiro(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            return int(entrada)
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")


def ler_lista_numeros(quantidade):
    numeros = []
    for i in range(quantidade):
        numero = ler_inteiro(f"Digite o {i + 1}o numero: ")
        numeros.append(numero)
    return numeros


def exercicio_1():
    print("=" * 40)
    print("EXERCICIO 1 - SOMA DOS ELEMENTOS")
    print("=" * 40)
    lista = ler_lista_numeros(5)
    print(f"Lista: {lista}")
    print(f"Soma: {sum(lista)}")


def exercicio_2():
    print("=" * 40)
    print("EXERCICIO 2 - ESTATISTICAS DA LISTA")
    print("=" * 40)

    quantidade = ler_inteiro("Quantos numeros deseja informar? ")
    while quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        quantidade = ler_inteiro("Quantos numeros deseja informar? ")

    lista = ler_lista_numeros(quantidade)
    media = sum(lista) / len(lista)

    print(f"Lista: {lista}")
    print(f"Media: {media:.2f}")
    print(f"Mediana: {median(lista)}")
    print(f"Menor valor: {min(lista)}")
    print(f"Maior valor: {max(lista)}")


def menu_principal():
    while True:
        print("\n" + "=" * 40)
        print("LISTA DE EXERCICIOS")
        print("=" * 40)
        print("1.  Soma dos Elementos")
        print("2.  Estatisticas da Lista")
        print("0.  Sair")
        opcao = input("\nEscolha o exercicio: ")
        if opcao == "1":
            exercicio_1()
        elif opcao == "2":
            exercicio_2()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opcao invalida!")


menu_principal()
