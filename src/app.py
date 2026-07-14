from src.gerenciador import GerenciadorTarefas


def mostrar_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")


def main():
    gerenciador = GerenciadorTarefas()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade (Baixa, Média ou Alta): ")

            tarefa = gerenciador.cadastrar(
                titulo,
                descricao,
                prioridade
            )

            print(f"Tarefa cadastrada com o ID {tarefa.identificador}.")

        elif opcao == "2":
            tarefas = gerenciador.listar()

            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("\nTarefas cadastradas:")

                for tarefa in tarefas:
                    print(tarefa)

        elif opcao == "3":
            try:
                identificador = int(input("Informe o ID da tarefa: "))
            except ValueError:
                print("O ID precisa ser um número.")
                continue

            tarefa = gerenciador.buscar_por_id(identificador)

            if tarefa is None:
                print("Tarefa não encontrada.")
                continue

            titulo = input("Novo título (Enter para manter): ")
            descricao = input("Nova descrição (Enter para manter): ")
            status = input("Novo status (Enter para manter): ")
            prioridade = input("Nova prioridade (Enter para manter): ")

            gerenciador.editar(
                identificador,
                titulo or None,
                descricao or None,
                status or None,
                prioridade or None
            )

            print("Tarefa atualizada com sucesso.")

        elif opcao == "4":
            try:
                identificador = int(input("Informe o ID da tarefa: "))
            except ValueError:
                print("O ID precisa ser um número.")
                continue

            if gerenciador.excluir(identificador):
                print("Tarefa excluída com sucesso.")
            else:
                print("Tarefa não encontrada.")

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()