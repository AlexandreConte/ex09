from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade


class Pedido:
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        self.__numero = None
        self.__cliente = None
        self.__tipo = None
        self.__itens = []

        if isinstance(numero, int):
            self.__numero = numero
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(tipo, TipoPedido):
            self.__tipo = tipo

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def tipo(self) -> TipoPedido:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: TipoPedido):
        if isinstance(tipo, TipoPedido):
            self.__tipo = tipo

    @property
    def itens(self) -> list:
        return self.__itens

    '''
    Inclui um novo item na lista de itens do pedido.
    Nao deve ser possivel incluir itens duplicados (com o mesmo codigo).
    Retornar o item incluido em caso de sucesso e None em caso
    de item duplicado.
    '''
    def inclui_item_pedido(self, codigo, descricao, preco):
        repetido = self.__verifica_codigo_jah_existe(codigo)
        if repetido:
            return None
        novo_item = ItemPedido(codigo, descricao, preco)
        self.__itens.append(novo_item)
        return novo_item

    def __verifica_codigo_jah_existe(self, codigo):
        for item in self.__itens:
            if item.codigo == codigo:
                return True
        return False

    '''
    Exclui um item do pedido e retorna o item excluido
    Caso o item nao exista, retorne None
    '''
    def exclui_item_pedido(self, codigo):
        existe = self.__verifica_codigo_jah_existe(codigo)
        if existe:
            item = self.__retorna_item_by_codigo(codigo)
            self.__itens.remove(item)
            return item
        return None

    def __retorna_item_by_codigo(self, codigo):
        for item in self.__itens:
            if item is not None:
                if item.codigo == codigo:
                    return item
        return None

    '''
    Deve calcular o valor total do pedido, considerando um custo
    adicional pela distancia e fator por distancia percorrida.
    O fator da distancia varia de acordo com o tipo de pedido.
    O fator_distancia do TipoPedido deve ser multiplicado pela distancia
    e acrescido ao valor total dos itens.
    Por exemplo, se o fator_distancia for 2 e a distancia for 5,
    o total do pedido deve ser acrescido em 10.
    Ainda, se o cliente for ClienteFidelidade, deve  diminuir o valor total
    pelo percentual de desconto armazenado no atributo desconto do ClienteFidelidade.
    Por exemplo, se o valor de desconto for 0.2 e o pedido custar 10:
    O desconto deve ser de 2 e o valor final 8.
    @return um float correspondente ao total do pedido
    '''
    def calcula_valor_pedido(self, distancia: float) -> float:
        frete = self.__tipo.fator_distancia * distancia
        custo_total = frete
        if len(self.__itens) > 0:
            for item in self.__itens:
                custo_total += item.preco_unitario
        if isinstance(self.__cliente, ClienteFidelidade):
            desconto = self.__cliente.desconto
            custo_total = custo_total - (1 * desconto) * custo_total
        return custo_total
