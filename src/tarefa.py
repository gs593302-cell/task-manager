class Tarefa:
    def __init__(
        self,
        identificador: int,
        titulo: str,
        descricao: str,
        status: str = "Pendente",
        prioridade: str = "Média",
    ):
        self.identificador = identificador
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade

    def atualizar(
        self,
        titulo: str | None = None,
        descricao: str | None = None,
        status: str | None = None,
        prioridade: str | None = None,
    ) -> None:
        if titulo:
            self.titulo = titulo

        if descricao:
            self.descricao = descricao

        if status:
            self.status = status

        if prioridade:
            self.prioridade = prioridade

    def concluir(self) -> None:
        self.status = "Concluída"

    def __str__(self) -> str:
        return (
            f"ID: {self.identificador} | "
            f"Título: {self.titulo} | "
            f"Descrição: {self.descricao} | "
            f"Status: {self.status} | "
            f"Prioridade: {self.prioridade}"
        )