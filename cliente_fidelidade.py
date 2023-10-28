from cliente import Cliente


class ClienteFidelidade(Cliente):
    def __init__(
        self,
        codigo_fidelidade: int,
        desconto: float,
        cpf: str,
        nome: str,
        endereco: str,
        telefone: str
    ):
        super().__init__(cpf, nome, endereco, telefone)
        self.__codigo_fidelidade = None
        self.__desconto = None

        if isinstance(codigo_fidelidade, int):
            self.__codigo_fidelidade = codigo_fidelidade
        if isinstance(desconto, float):
            self.__desconto = desconto

    @property
    def codigo_fidelidade(self) -> int:
        return self.codigo_fidelidade

    @codigo_fidelidade.setter
    def codigo_fidelidade(self, codigo_fidelidade):
        if isinstance(codigo_fidelidade, int):
            self.__codigo_fidelidade = codigo_fidelidade

    @property
    def desconto(self) -> float:
        return self.__desconto

    @desconto.setter
    def desconto(self, desconto: float):
        if isinstance(desconto, float):
            self.__desconto = desconto

    @property
    def cpf(self) -> str:
        return super().cpf

    @cpf.setter
    def cpf(self, cpf: str):
        super().cpf = cpf

    @property
    def nome(self) -> str:
        return super().nome

    @nome.setter
    def nome(self, nome: str):
        self.nome = nome

    @property
    def endereco(self) -> str:
        return super().endereco

    @endereco.setter
    def endereco(self, endereco: str):
        super().endereco = endereco

    @property
    def telefone(self) -> str:
        return super().telefone

    @telefone.setter
    def telefone(self, telefone: str):
        super().telefone = telefone
