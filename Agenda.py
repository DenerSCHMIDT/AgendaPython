import os

# Variável global para armazenar a configuração do idioma
language = "english"

def menu():
    while True:
        if language == "english":
            menu_english()
        elif language == "portuguese":
            menu_portuguese()

        option = input().strip()

        if option == "1":
            insert_contact()
        elif option == "2":
            list_contacts()
        elif option == "3":
            remove_contact()
        elif option == "4":
            search_contact_by_name()
        elif option == "5":
            update_contact()
        elif option == "6":
            change_language()
        elif option == "7":
            exit_program()
        else:
            print("Invalid option")

def menu_english():
    print('''
    =================================================================
                                AGENDA                            v.1
                                    +
                                    + {} STORED CONTACTS
                                    +
    MENU:                           + LAST INSERTION
                                    + {}
    [1] INSERT CONTACT             +
    [2] LIST CONTACTS             +
    [3] REMOVE CONTACT             +     
    [4] SEARCH CONTACT BY NAME    +
    [5] UPDATE CONTACT           +
    [6] CHANGE LANGUAGE           +
    [7] EXIT                        +
                                    +
    ==================================================================

    CHOOSE AN OPTION ABOVE: 
    '''.format(count_records(), last_insertion()))

def menu_portuguese():
    print('''
    =================================================================
                                AGENDA                            v.1
                                    +
                                    + {} CONTATOS ARMAZENADOS
                                    +
    MENU:                           + ÚLTIMA INSERÇÃO
                                    + {}
    [1] INSERIR CONTATO            +
    [2] LISTAR CONTATOS           +
    [3] REMOVER CONTATO            +     
    [4] BUSCAR CONTATO PELO NOME  +
    [5] ATUALIZAR CONTATO         +
    [6] MUDAR IDIOMA              +
    [7] SAIR                        +
                                    +
    ==================================================================

    ESCOLHA UMA OPÇÃO ACIMA: 
    '''.format(count_records(), last_insertion()))

def count_records():
    try:
        with open("storage.txt", "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0

def last_insertion():
    try:
        with open("Dados.txt", "r") as file:
            records = file.readlines()
            return records[-1].strip() if records else "Nenhuma inserção realizada"
    except FileNotFoundError:
        return "Nenhuma inserção realizada"

def insert_contact():
    record_id = input("Escolha o ID do contato: ")
    name = input("Informe o nome do contato: ")
    phone = input("Informe o telefone do contato: ")
    email = input("Informe o email do contato: ")
    try:
        with open("Dados.txt", "a") as file:
            data = f'{record_id};{name};{phone};{email}\n'
            file.write(data)
        print('Contato inserido com sucesso !!!!')
    except Exception as e:
        print("Erro ao inserir contato:", e)

def list_contacts():
    try:
        with open("Dados.txt", "r") as file:
            records = file.readlines()
            if records:
                for record in records:
                    print(record.strip())
            else:
                print("Nenhum contato armazenado")
    except FileNotFoundError:
        print("Nenhum contato armazenado")

def remove_contact():
    name_to_remove = input("Informe o nome a ser removido: ").strip().lower()
    try:
        with open("storage.txt", "r") as file:
            records = [record for record in file if name_to_remove not in record.lower()]
        with open("storage.txt", "w") as file:
            for record in records:
                file.write(record)
        print('Contato removido com sucesso')
        list_contacts()
    except Exception as e:
        print("Erro ao remover contato:", e)

def search_contact_by_name():
    name = input("Informe o nome a ser pesquisado: ").strip().lower()
    try:
        with open("storage.txt", "r") as file:
            contacts_found = [record.strip() for record in file if name in record.lower()]
        if contacts_found:
            for contact in contacts_found:
                print(contact)
        else:
            print("Nenhum contato encontrado com esse nome.")
    except FileNotFoundError:
        print("Nenhum contato armazenado")

def update_contact():
    name_to_update = input("Informe o nome a ser atualizado: ").strip().lower()
    try:
        with open("storage.txt", "r") as file:
            records = [record for record in file if name_to_update not in record.lower()]
        with open("storage.txt", "w") as file:
            for record in records:
                file.write(record)
        record_id = input("Escolha o ID do contato atualizado: ")
        name = input("Informe o nome atualizado do contato: ")
        phone = input("Informe o telefone atualizado do contato: ")
        email = input("Informe o email atualizado do contato: ")
        try:
            with open("storage.txt", "a") as file:
                data = f'{record_id};{name};{phone};{email}\n'
                file.write(data)
            print('Contato atualizado com sucesso !!!!')
        except Exception as e:
            print("Erro ao atualizar contato:", e)
    except FileNotFoundError:
        print("Nenhum contato armazenado")

def change_language():
    global language
    print("Selecione o idioma:\n1. Inglês\n2. Português")
    choice = input("Digite sua escolha: ").strip()
    if choice == "1":
        language = "english"
    elif choice == "2":
        language = "portuguese"
    else:
        print("Escolha inválida")

def exit_program():
    print("Encerrando programa...")
    # Aqui você pode adicionar qualquer limpeza ou ações de encerramento necessárias antes de sair
    exit()

try:
    # Chamada da função menu para iniciar o programa
    menu()
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")
