from src.gerenciador import GerenciadorTarefas


def test_cadastrar_tarefa():
    gerenciador = GerenciadorTarefas()

    tarefa = gerenciador.cadastrar(
        "Estudar Python",
        "Revisar o conteúdo da aula",
        "Alta"
    )

    assert tarefa.titulo == "Estudar Python"
    assert tarefa.descricao == "Revisar o conteúdo da aula"
    assert tarefa.prioridade == "Alta"
    assert len(gerenciador.listar()) == 1


def test_editar_tarefa():
    gerenciador = GerenciadorTarefas()

    tarefa = gerenciador.cadastrar(
        "Fazer trabalho",
        "Finalizar atividade",
        "Média"
    )

    resultado = gerenciador.editar(
        tarefa.identificador,
        titulo="Fazer trabalho de Engenharia de Software",
        prioridade="Alta"
    )

    assert resultado is True
    assert tarefa.titulo == "Fazer trabalho de Engenharia de Software"
    assert tarefa.prioridade == "Alta"


def test_excluir_tarefa():
    gerenciador = GerenciadorTarefas()

    tarefa = gerenciador.cadastrar(
        "Excluir tarefa",
        "Tarefa criada para teste"
    )

    resultado = gerenciador.excluir(tarefa.identificador)

    assert resultado is True
    assert len(gerenciador.listar()) == 0


def test_buscar_tarefa_inexistente():
    gerenciador = GerenciadorTarefas()

    tarefa = gerenciador.buscar_por_id(99)

    assert tarefa is None