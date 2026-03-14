def exercicio_1():
    print("=" * 40)
    print("EXERCICIO 1 - SOMA DOS ELEMENTOS")
    print("=" * 40)
    lista = []
    for i in range(5):
        num = int(input(f"Digite o {i+1}o numero: "))
        lista.append(num)
    print(f"Lista: {lista}")
    print(f"Soma: {sum(lista)}")

def menu_principal():
    while True:
        print("\n" + "=" * 40)
        print("LISTA DE EXERCICIOS")
        print("=" * 40)
        print("1.  Soma dos Elementos")
        opcao = input("\nEscolha o exercicio: ")
        if opcao == "1":
            exercicio_1()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opcao invalida!")


menu_principal()