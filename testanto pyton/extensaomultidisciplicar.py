""" Através da conversa com a gestora da empresa consegui saber as informações que seriam necessárias para que eles conseguissem fazer o cadastro dos seus clientes, que resultou nessa código. """

class Cliente:
    def __init__(self, nome, endereco, telefone, email, data_nascimento, cpf, genero=None):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero

    def __str__(self):
        return (f'Nome: {self.nome}, Endereço: {self.endereco}, Telefone: {self.telefone}, '
                f'Email: {self.email}, Data de Nascimento: {self.data_nascimento}, CPF: {self.cpf}, '
                f'Gênero: {self.genero}')

class SistemaDeCadastro:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self):
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        data_nascimento = input("Data de Nascimento: ")
        cpf = input("CPF: ")
        genero = input("Gênero (opcional): ")

        cliente = Cliente(nome, endereco, telefone, email, data_nascimento, cpf, genero)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in self.clientes:
                print(cliente)

def menu():
    sistema = SistemaDeCadastro()
    while True:
        print("\nMenu:")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            sistema.cadastrar_cliente()
        elif opcao == '2':
            sistema.listar_clientes()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()