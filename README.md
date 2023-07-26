# Operacao_bancaria

 # Operação Bancária em Python

Este é um projeto simples de uma Operação Bancária em Python. O sistema foi desenvolvido para permitir a realização de operações básicas em uma conta bancária, como depósito, saque e consulta de saldo.

## Funcionalidades

- **Depósito**: Permite adicionar um valor ao saldo da conta bancária.
- **Saque**: Permite sacar um valor da conta, respeitando o limite diário de 23 saques e o limite máximo de R$500,00 por saque.
- **Consulta de Saldo**: Exibe o saldo atual da conta bancária.
- **Extrato**: Imprime o extrato da conta, mostrando todas as transações realizadas, incluindo depósitos e saques.

## Utilização

Para utilizar a Operação Bancária em Python, siga as instruções abaixo:

1. Ao iniciar o programa, uma conta bancária é criada automaticamente com um saldo inicial de R$1000,00.

2. O usuário verá um menu com as seguintes opções:

Menu:

Consultar Saldo
Realizar Depósito
Realizar Saque
Imprimir Extrato
Sair


3. Para escolher uma opção, basta digitar o número correspondente no teclado e pressionar "Enter".

4. Para realizar um depósito (opção 2) ou um saque (opção 3), o sistema solicitará ao usuário que insira o valor desejado.

5. O extrato (opção 4) exibirá todas as transações realizadas na conta, incluindo depósitos e saques.

6. Para sair do programa, basta escolher a opção 0.

## Observações

- O sistema controla o número de saques realizados em um dia, respeitando o limite diário de 23 saques.
- O valor máximo permitido para cada saque é de R$500,00.
- Caso o usuário tente sacar um valor superior ao saldo disponível na conta, o sistema exibirá uma mensagem informando que não é possível realizar o saque por falta de saldo.

Esperamos que esta Operação Bancária em Python seja útil para realizar operações bancárias básicas e que contribua para o seu aprendizado em Python.


#Atualizações do código

Descrição

Este é um sistema bancário simples implementado em Python. Ele permite cadastrar usuários e criar contas correntes ou contas poupança para esses usuários. As contas têm funcionalidades para consultar saldo, realizar depósitos e saques, além de imprimir o extrato da conta.

Funcionalidades

Cadastrar Usuário e Conta: Permite cadastrar um novo usuário associado a uma conta corrente ou conta poupança. O usuário é identificado pelo seu CPF, e o sistema verifica se o CPF já está cadastrado para outro cliente.
Consultar Saldo: Informa o saldo atual de uma conta específica, a partir do número da conta.
Realizar Depósito: Permite fazer um depósito em uma conta específica.
Realizar Saque: Permite realizar um saque em uma conta específica, respeitando o limite diário de saques e o limite máximo por saque (R$500,00).
Imprimir Extrato: Mostra o extrato da conta, exibindo os movimentos realizados e o saldo atual.
Instruções

Ao executar o código, o programa apresentará um menu com as opções numeradas para cada funcionalidade.
Digite o número da opção desejada para executar a tarefa correspondente.
Para cadastrar um usuário e criar uma conta, selecione a opção 1 e siga as instruções.
Para realizar outras operações, informe o número da conta associada à operação desejada.
O programa continuará executando até que a opção 0 seja selecionada para sair.

Exemplo de Uso

markdown

Menu:
1. Cadastrar Usuário e Conta
2. Consultar Saldo
3. Realizar Depósito
4. Realizar Saque
5. Imprimir Extrato
0. Sair

Digite o número da opção desejada: 1
Digite o CPF do cliente: 12345678900
Digite o endereço do cliente: Rua das Flores, 123
Escolha o tipo de conta:
1. Conta Corrente
2. Conta Poupança
1
Conta criada com sucesso. Número da conta: 1

Menu:
1. Cadastrar Usuário e Conta
2. Consultar Saldo
3. Realizar Depósito
4. Realizar Saque
5. Imprimir Extrato
0. Sair

Digite o número da opção desejada: 2
Digite o número da conta: 1
Saldo atual da conta 1: R$1000.00

Menu:
1. Cadastrar Usuário e Conta
2. Consultar Saldo
3. Realizar Depósito
4. Realizar Saque
5. Imprimir Extrato
0. Sair

Digite o número da opção desejada: 3
Digite o número da conta para o depósito: 1
Digite o valor a ser depositado: 500
Depósito realizado com sucesso!

Menu:
1. Cadastrar Usuário e Conta
2. Consultar Saldo
3. Realizar Depósito
4. Realizar Saque
5. Imprimir Extrato
0. Sair

Digite o número da opção desejada: 4
Digite o número da conta para o saque: 1
Digite o valor a ser sacado: 200
Saque: -R$200.00

Menu:
1. Cadastrar Usuário e Conta
2. Consultar Saldo
3. Realizar Depósito
4. Realizar Saque
5. Imprimir Extrato
0. Sair

Digite o número da opção desejada: 5
Digite o número da conta para imprimir o extrato: 1
Extrato da Conta:
Depósito: +R$500.00
Saque: -R$200.00
Saldo atual: R$1300.00

Menu:
1. Cadastrar Usuário e Conta
2. Consultar Saldo
3. Realizar Depósito
4. Realizar Saque
5. Imprimir Extrato
0. Sair

Digite o número da opção desejada: 0
Obrigado por utilizar o sistema bancário. Até mais!
Isso é apenas um exemplo do uso do sistema. O usuário pode continuar realizando operações, cadastrando novos usuários e contas, consultando saldos, depositando e sacando valores, enquanto quiser. Ao finalizar, basta selecionar a opção 0 para sair do programa.


## Autor

Este projeto foi desenvolvido por [seu-nome-de-usuario](https://github.com/SciDevPablo).
