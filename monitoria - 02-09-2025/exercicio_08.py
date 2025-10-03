
from abc import ABC, abstractmethod


"""
Nível 5: O Desafio Final (Complexo)

Exercício 8: Abstração e Herança para Sistema de Cadastro
1. Crie um sistema de cadastro com classes abstratas e herança:

2. Classe Abstrata Pessoa com atributos cpf e nome e um método abstrato detalhes_de_cadastro().

3. Classe Concreta Cliente que herda de Pessoa e adiciona o atributo data_cadastro. Implemente detalhes_de_cadastro().

4. Classe Concreta Fornecedor que herda de Pessoa e adiciona o atributo cnpj. Implemente detalhes_de_cadastro().

5. Crie uma função que aceita uma lista de objetos que são Pessoa (ou seja, instâncias de Cliente ou Fornecedor) e 
itere sobre ela, chamando o método detalhes_de_cadastro() para cada item.

"""

#classe abstrata 

class Pessoa(ABC): 
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome 

  @abstractmethod
  def detalhes_de_cadastro(self): 
    pass

class Cliente(Pessoa):
  def __init__(self, id, nome, data_cadastro):
    super().__init__(id, nome) 
    self.data_cadastro = data_cadastro

  def detalhes_de_cadastro(self): 
    return f"Cliente id: {self.id}, Nome: {self.nome}, Data de cadastro {self.data_cadastro}" 

class Fornecedor(Pessoa): 
  def __init__(self, id, nome, cnpj):
    super().__init__(id, nome)
    self.cnpj = cnpj
  
  def detalhes_de_cadastro(self): 
    return f"Fornecedor cnpj: {self.cnpj}, Nome: {self.nome}" 
  

def exibir_cadastros(lista_pessoas):
  for pessoa in lista_pessoas: 
    print(pessoa.detalhes_de_cadastro())


if __name__ == "__main__": 
  cliente1 = Cliente(1, "PAULO", "01/10/2025")
  fornecedor = Fornecedor(2, "contabilidade xpto", "1234.1234123.4123")

  pessoas = [cliente1, fornecedor]

  exibir_cadastros(pessoas)