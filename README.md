# Descrição do Problema:

Nesta atividade, você fará a implementação de um sistema de controle de entregas (delivery). O sistema permite o cadastro de clientes e pedidos, e calcula o valor total devido.

Um pedido tem um tipo, um cliente e uma lista de itens.
Ele permite o calculo total do pedido com base no preço de cada item e na distância de entrega.

Caso o cliente seja um cliente fidelidade, ele tem um desconto no total a ser pago.

Dependendo do tipo do pedido, haverá um fator de distância para aquele pedido. Por exemplo, produtos perecíveis ou frágeis podem ter um fator distância maior que outros tipos de entrega mais simples.

O sistema tem um controlador que controla a lista de pedidos e calcula o faturamento total com todos os pedidos de um determinado cliente.

------

Pontuação:
Questão 01 (1.5 PONTO) - Definição de Classes e Associações:

A estrutura das Classes e Associações deve estar exatamente igual ao modelo de classes. Qualquer diferença de nomes de atributos, tipos de dados, assinaturas de operações, etc. serão descontadas. Siga exatamente o que está definido no diagrama de classes.

Questão 02 (1.0 PONTO) - Instanciar Controlador, Pedidos e Clientes:

O Controlador, Pedidos e Clientes devem poder ser instanciados seguindo as assinaturas dos construtores definidos no diagrama de classes. Os atributos devem ser implementados para receber os parâmetros dos construtores definidos.

Questão 03 (2.0 PONTOS) - Manipulação das listas do controlador

Deve ser possível incluir e excluir pedidos no controlador. Prestar muita atenção quanto a inclusão de valores nulos ou de tipos diferentes, tratar tentativa de inserir entidades duplicadas. Não podem ser cadastrados dois pedidos com o mesmo número.

Questão 04 (2.0 PONTOS) - Implementação da classe Pedido

Deve ser possível incluir e excluir itens no pedido. Prestar muita atenção quanto a inclusão de valores nulos ou de tipos diferentes, tratar tentativa de inserir entidades duplicadas. Não podem ser cadastrados dois itens com o mesmo código.

Questão 05 (1.0 PONTO) - Herança

Herança deve ser implementada corretamente.

Questão 06 (2.0 PONTOS) - Cálculo dos pedidos

Calculo correto do faturamento dos pedidos de um cliente identificado pelo seu cpf, considerando uma distancia dada. Considere atentamente os comentários nos métodos calcular_faturamento_pedidos e calcula_valor_pedido.

Para cada pedido do cliente, deve ser calculado o valor individual. O valor individual leva em consideração o fator distância e se o cliente é ou não um cliente fidelidade. Os valores individuais são somados no cálculo do faturamento total.

Questão 07 (0.5 PONTO) - Estilo de código:

O estilo do código de todas as classes deve estar de acordo com o pep8.

Veja o Diagrama de Classes AQUI. 

IMPORTANTE:

Comece implementando todas as operações exigidas no diagrama de classes e deixe o código compilando;
Em seguida inclua os atributos necessários definidos no diagrama de classes;
Retire acentos e caracteres especiais antes de submeter;
Leia atentamente as mensagens de erro.
Implemente todos os códigos solicitados e não esqueça de clicar em Avaliar.