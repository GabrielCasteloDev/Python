list = []

while True:
    choose = input("(D)elete (I)nput (L)ist: ")
    choose = choose.upper()

    if choose == "I":
        item = input("Name item: ")
        list.append(item)

    elif choose == "L":
        for indice, name in enumerate(list):
            print(indice,name)

    elif choose == "D":
        try:  # Tratamento de erro para entradas inválidas
            delete_number = int(input("Whats the number: "))

            if 0 <= delete_number < len(list): # Verifica se o índice é válido
                del list[delete_number] # Forma correta de deletar um item pelo índice
                print(f"Item na posição {delete_number} deletado.")
            else:
                print("Número inválido. Certifique-se de que o número está dentro do intervalo da lista.")

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    
    else:
        break


