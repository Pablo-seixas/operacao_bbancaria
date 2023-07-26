class Usuario:
    def __init__(self, cpf, endereco):
        self.cpf = cpf
        self.endereco = endereco


class ContaBancaria:
    def __init__(self, usuario, saldo_inicial=1000):
        self.usuario = usuario
        self.agencia = "0001"
        self.numero_conta = len(contas_bancarias) + 1
        self.saldo = saldo_inicial
        self.extrato = []
        self.saques_diarios = 0

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        self.saldo += valor
        self.extrato.append(f"Depósito: +R${valor:.2f}")

    def sacar(self, valor):
        """Realiza um saque da conta se houver saldo suficiente e respeitando o limite diário."""
        if self.saques_diarios < 23 and valor <= 500 and self.saldo >= valor:
            self.saldo -= valor
            self.saques_diarios += 1
            self.extrato.append(f"Saque: -R${valor:.2f}")
        elif self.saques_diarios >= 23:
            print("Limite diário de saques atingido.")
        elif valor > 500:
            print("Limite máximo por saque é de R$500,00.")
        else:
            print("Saldo insuficiente para o saque!")

    def consultar_saldo(self):
        """Retorna o saldo atual da conta."""
        return self.saldo

    def imprimir_extrato(self):
        """Imprime o extrato da conta."""
        print("Extrato da Conta:")
        for movimento in self.extrato:
            print(movimento)
        print(f"Saldo atual: R${self.saldo:.2f}")


class ContaCorrente(ContaBancaria):
    def __init__(self, usuario, saldo_inicial=1000):
        super().__init__(usuario, saldo_inicial)


class ContaPoupanca(ContaBancaria):
    def __init__(self, usuario, saldo_inicial=1000):
        super().__init__(usuario, saldo_inicial)
        # Aqui você pode adicionar atributos específicos da conta poupança, como taxa de juros, por exemplo.


# Lista para armazenar as contas bancárias
contas_bancarias = []


def cadastrar_usuario():
    cpf = input("Digite o CPF do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    # Verifica se o CPF já está cadastrado
    if any(conta.usuario.cpf == cpf for conta in contas_bancarias):
        print("CPF já cadastrado para outro cliente.")
        return
    usuario = Usuario(cpf, endereco)
    opcao_conta = int(input("Escolha o tipo de conta:\n1. Conta Corrente\n2. Conta Poupança\n"))
    if opcao_conta == 1:
        conta = ContaCorrente(usuario)
    elif opcao_conta == 2:
        conta = ContaPoupanca(usuario)
    else:
        print("Opção inválida.")
        return

    contas_bancarias.append(conta)
    print(f"Conta criada com sucesso. Número da conta: {conta.numero_conta}")


def consultar_saldo():
    numero_conta = int(input("Digite o número da conta: "))
    conta = obter_conta_por_numero(numero_conta)
    if conta:
        saldo_atual = conta.consultar_saldo()
        print(f"Saldo atual da conta {numero_conta}: R${saldo_atual:.2f}")
    else:
        print("Conta não encontrada.")


def realizar_deposito():
    numero_conta = int(input("Digite o número da conta para o depósito: "))
    conta = obter_conta_por_numero(numero_conta)
    if conta:
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        conta.depositar(valor_deposito)
        print("Depósito realizado com sucesso!")
    else:
        print("Conta não encontrada.")


def realizar_saque():
    numero_conta = int(input("Digite o número da conta para o saque: "))
    conta = obter_conta_por_numero(numero_conta)
    if conta:
        valor_saque = float(input("Digite o valor a ser sacado: "))
        conta.sacar(valor_saque)
    else:
        print("Conta não encontrada.")


def imprimir_extrato():
    numero_conta = int(input("Digite o número da conta para imprimir o extrato: "))
    conta = obter_conta_por_numero(numero_conta)
    if conta:
        conta.imprimir_extrato()
    else:
        print("Conta não encontrada.")


def obter_conta_por_numero(numero_conta):
    for conta in contas_bancarias:
        if conta.numero_conta == numero_conta:
            return conta
    return None


def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Usuário e Conta")
        print("2. Consultar Saldo")
        print("3. Realizar Depósito")
        print("4. Realizar Saque")
        print("5. Imprimir Extrato")
        print("0. Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 0:
            print("Obrigado por utilizar o sistema bancário. Até mais!")
            break
        elif opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            consultar_saldo()
        elif opcao == 3:
            realizar_deposito()
        elif opcao == 4:
            realizar_saque()
        elif opcao == 5:
            imprimir_extrato()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
