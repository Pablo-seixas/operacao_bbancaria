class ContaBancaria:
    def __init__(self, saldo_inicial=1000):
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


# Função principal para executar o sistema
def main():
    # Cria uma conta bancária com saldo inicial de 1000
    conta = ContaBancaria(saldo_inicial=1000)

    while True:
        print("\nMenu:")
        print("1. Consultar Saldo")
        print("2. Realizar Depósito")
        print("3. Realizar Saque")
        print("4. Imprimir Extrato")
        print("0. Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 0:
            print("Obrigado por utilizar o sistema bancário. Até mais!")
            break
        elif opcao == 1:
            saldo_atual = conta.consultar_saldo()
            print(f"Saldo atual: R${saldo_atual:.2f}")
        elif opcao == 2:
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor_deposito)
            print("Depósito realizado com sucesso!")
        elif opcao == 3:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor_saque)
        elif opcao == 4:
            conta.imprimir_extrato()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
