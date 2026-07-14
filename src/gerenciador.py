from src.tarefa import Tarefa


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def cadastrar(self, titulo, descricao, prioridade="Média"):
        tarefa = Tarefa(
            self.proximo_id,
            titulo,
            descricao,
            prioridade=prioridade
        )

        self.tarefas.append(tarefa)
        self.proximo_id += 1

        return tarefa

    def listar(self):
        return self.tarefas

    def buscar_por_id(self, identificador):
        for tarefa in self.tarefas:
            if tarefa.identificador == identificador:
                return tarefa

        return None

    def editar(
        self,
        identificador,
        titulo=None,
        descricao=None,
        status=None,
        prioridade=None
    ):
        tarefa = self.buscar_por_id(identificador)

        if tarefa is None:
            return False

        tarefa.atualizar(
            titulo,
            descricao,
            status,
            prioridade
        )

        return True

    def excluir(self, identificador):
        tarefa = self.buscar_por_id(identificador)

        if tarefa is None:
            return False

        self.tarefas.remove(tarefa)
        return True