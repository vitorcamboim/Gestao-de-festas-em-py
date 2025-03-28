# %%

class Festa:
    def __init__(self, nome, data, descricao):
        self.nome = nome
        self.data = data
        self.descricao = descricao
        self.convidados = []

    def adicionar_convidado(self, nome, email):
        self.convidados.append({'nome': nome, 'email': email})

    def mostrar_convidados(self):
        return self.convidados

class SistemaFestas:
    def __init__(self):
        self.festas = []

    def cadastrar_festa(self, nome, data, descricao):
        festa = Festa(nome, data, descricao)
        self.festas.append(festa)
        print(f"Festa '{nome}' cadastrada com sucesso!")

    def mostrar_festas(self):
        if not self.festas:
            print("Não há festas cadastradas.")
            return
        for idx, festa in enumerate(self.festas, 1):
            print(f"{idx}. {festa.nome} - {festa.data} - {festa.descricao}")
            if festa.convidados:
                print("Convidados:")
                for convidado in festa.convidados:
                    print(f"     - {convidado['nome']} ({convidado['email']})")
            else:
                print("Nenhum convidado cadastrado.")

    def adicionar_convidado(self, nomedafesta, nomedoconvidado, emaildoconvidado):
        for festa in self.festas:
            if festa.nome == nomedafesta:
                festa.adicionar_convidado(nomedoconvidado, emaildoconvidado)
                print(f"Convidado {nomedoconvidado} adicionado à festa {nomedafesta}.")
                return
        print(f"Festa com o nome '{nomedafesta}' não encontrada.")

def menu():
    sistema = SistemaFestas()

    # Infinitamente
    while True:
        print("""  --- Menu: ---
Digite o número de acordo com sua opção:
Cadastrar festa -> 1
Cadastrar convidado -> 2
Mostrar festas e convidados -> 3
Sair -> 4 """)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome da festa: ")
            data = input("Data da festa (dd/mm/aaaa): ")
            descricao = input("Descrição da festa: ")
            sistema.cadastrar_festa(nome, data, descricao)
        
        elif opcao == '2':
            nomedafesta = input("Nome da festa para adicionar o convidado: ")
            nomedoconvidado = input("Nome do convidado: ")
            emaildoconvidado = input("E-mail do convidado: ")
            sistema.adicionar_convidado(nomedafesta, nomedoconvidado, emaildoconvidado)
        
        elif opcao == '3':
            sistema.mostrar_festas()
        
        elif opcao == '4':
            print("Terminando por aqui...")
            break
        
        else:
            print("Essa opção não é válida. Tente novamente.")

if __name__ == "__main__":
    menu()
