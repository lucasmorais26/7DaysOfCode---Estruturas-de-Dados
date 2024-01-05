import os
class ListaDeCompras():
    itens = ["Banana", "Maça", "Pera", "Açucar"]
    quantidade = [10, 20, 30, 40]

    def __init__(self):
        print(f'O objeto {id(self)} foi instanciado')
        self.main()

    def main(self):
        os.system('cls')
        self.exibe_boas_vindas()
        self.escolhe_opcao()
    def exibe_boas_vindas(self):
        print("\nBoas vindas ao sistema de lista de compras!")
        print("Digite a função desejada")
        print("1-Adicionar item\n2-Remover item\n3-Listar itens\n4-Encerrar programa")
    def escolhe_opcao(self):
        opcao = int(input("Digite a opcao desejada: "))
        match(opcao):
            case 1:
                self.adicionar_item()
            case 2:
                self.remover_item()
            case 3:
                self.listar_itens()
            case 4:
                self.encerrar_programa()
            case _:
                print("Opção inválida")
                self.exibe_erro()
    def adicionar_item(self):
        opcao = 0
        while opcao != 2:
            nome_do_produto = input("Digite o nome do produto a ser adicionado: ")
            qtd_desejada = int(input("Digite a quantidade do item: "))
            if isinstance(qtd_desejada, int):
                self.itens.append(nome_do_produto)
                self.quantidade.append(qtd_desejada)
            else:
                self.exibe_erro()
            opcao = int(input("Deseja adicionar mais um item?\n1-Sim\n2-Não "))
        self.main()
    def remover_item(self):
        opcao = 0

        while opcao != 2:
            nome_do_produto = input("Digite o nome do produto a ser removido: ")
            if nome_do_produto in self.itens:
                index = self.itens.index(nome_do_produto)
                self.itens.pop(index)
                self.quantidade.pop(index)
                print(f'O item {nome_do_produto} foi removido da lista com sucesso!')
            else:
                print("O nome do produto digitado não é válido")
                self.exibe_erro()
            opcao = int(input("Deseja remover mais algum item?\n1-Sim\n2-Não "))
        self.main()
    def listar_itens(self):
        index = 0
        opcao = 0
        while opcao == 0:
            for item in self.itens:
                print(f'Item [{index}]: {self.itens[index]} | Quantidade: {self.quantidade[index]}')
                index += 1
            opcao = input("Pressione qualquer tecla para voltar ao menu principal: ")
        self.main()
    def exibe_erro(self):
        print("Ocorreu um erro, o programa será reiniciado.")
        os.system('cls')
        self.main()
    def encerrar_programa(self):
        os.system('cls')
        print("Encerrando o programa!")
        exit()

if __name__ == '__main__':
    Lista1 = ListaDeCompras()


