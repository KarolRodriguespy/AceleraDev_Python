# Heranças

# Criação de classes genéricas, criando outras classes que vão herdando dessas classes e se especializando, fazendo a extensão delas.

class Animal:
    def fazer_barulho(self):
        print('Barulho de um animal')


class Domestico:
    def esta_dormindo(self):
        return True


class Mamifero(Animal):
    pass


class Cachorro(Mamifero, Domestico):
    def enterrar_osso(self):
        print("O osso foi enterrado")


class Gato(Mamifero):
    def fazer_barulho(self):
        print('Miau..miau')


gato = Gato()

gato.fazer_barulho()

cachorro = Cachorro()

cachorro.fazer_barulho()
print(cachorro.esta_dormindo())
cachorro.enterrar_osso()


# composição

class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class CarrinhoCompras:
    def __init__(self, cliente, produtos):
        self.num_pedido = '123'
        self.produtos = produtos
        self.cliente = cliente

    @property
    def valor_carrinho(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco

        return total

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def fechar_carrinho(self):
        print(f'Fechando o pedido: {self.num_pedido}')
        print(f'Valor do carrinho: {self.valor_carrinho}')
        print(f'Nome do cliente: {self.cliente.nome}')
        print('obrigada pela compra')


cliente = Cliente('Karol', '123456')

televisao = Produto('Televisão', 1000.90)
maquina_cafe = Produto('Maquina de café', 89.80)

produtos = [televisao, maquina_cafe]

carrinho = CarrinhoCompras(cliente, produtos)

teclado = Produto('teclado mecanico', 175.20)

carrinho.adicionar_produto(teclado)

carrinho.remover_produto(televisao)

print(carrinho.valor_carrinho)
print(carrinho.fechar_carrinho())


# polimorfismo

# capacidade de uma classe mais abstrata definir um comportamento mais genérico e nas estensões você coloca o comportamento mais especifico


class Mamifero:
    def emitir_som(self):
        pass


class Cachorro(Mamifero):
    def emitir_som(self):
        print('au au')


class Gato(Mamifero):
    def emitir_som(self):
        print('miau miau')


class Rato(Mamifero):
    def emitir_som(self):
        print('algum som que o rato faz')


cachorro = Cachorro()
gato = Gato()
rato = Rato()

mamiferos = [cachorro, gato, rato]

for mamifero in mamiferos:
    mamifero.emitir_som()


# Metodos de Classes

# eles tem escopo de classe, não de instância

class Impressora:

    def __init__(self):
        self.a = 10

    @classmethod
    def imprimir_folha(cls):
        print("Folha impressa")

    @classmethod
    def imprimir_livro(cls, paginas):
        for i in range(paginas):
            cls.imprimir_folha()

    @classmethod
    def imprimir_a(cls):
        print(cls.a)


Impressora.imprimir_folha()

print('==========')

Impressora.imprimir_livro(5)

impressora = Impressora()

print('==========')

impressora.imprimir_folha()

print('==========')


# Impressora.imprimir_a()

# impressora.imprimir_a() da erro


# metodo de instancia

# Tem escopo de istancia, mas herda o comportamento da classe


class Impressora:
    modelo = 'Epson'

    def __init__(self, numero_folhas):
        self.numero_folhas = numero_folhas

    def imprimir_folha(self):
        print('Folha impressa')

    def imprimir_livro(self, paginas):
        if paginas <= self.numero_folhas:
            for i in range(paginas):
                self.imprimir_folha()
                self.numero_folhas -= 1

    @classmethod
    def print_modelo(cls):
        print(cls.modelo)

    def print_modelo_instancia(self):
        print(self.modelo)


impressora = Impressora(15)

impressora.imprimir_folha()

print('==========')
impressora.imprimir_livro(10)

print('==========')

impressora.print_modelo()

impressora.print_modelo_instancia()


# metodos estaticos

# um metodo declarado dentro da classe, que não possui escopo da classe, mas sim dele próprio

class Impressora:
    @staticmethod
    def ligar_para_suporte():
        print('Liguei para suporte')

    @classmethod
    def deu_problema_na_impressora(cls):
        print('Analisando problema')
        cls.ligar_para_suporte()

    def imprimir(self):
        print('Imprimindo página 1')
        self.ligar_para_suporte()


Impressora.ligar_para_suporte()

Impressora.deu_problema_na_impressora()

impressora = Impressora()

impressora.imprimir()
