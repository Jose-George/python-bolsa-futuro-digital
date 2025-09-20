

#POO -> PROGRAMACAO ORIENTADA A OBJETOS
#OBJETO -> INSTANCIA DE UMA CLASSE
#CLASSE -> MODELO DO OBJETO
#ATRIBUTOS -> CARACTERISTICAS DO OBJETO
#METODOS -> ACOES DO OBJETO
#ENCAPSULAMENTO -> PROTEGER ATRIBUTOS E METODOS
# PUBLICO -> PODE SER ACESSADO DE QUALQUER LUGAR
# PROTEGIDO -> PODE SER ACESSADO APENAS DENTRO DA CLASSE E SUAS SUBCLASSES
# PRIVADO -> PODE SER ACESSADO APENAS DENTRO DA CLASSE

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome #atributo publico
        self.idade = idade
        self.__cpf = '123.456.789-00' #atributo privado

    def falar(self):
        print(f'{self.nome} está falando.')

    def envelhecer(self):
        self.idade += 1
        print(f'{self.nome} agora tem {self.idade} anos.')

    def mostrar_cpf(self):
        print(f'O CPF de {self.nome} é {self.__cpf}.')



p1 = Pessoa('João', 30)
#p1.falar()
#p1.envelhecer()
#p1.mostrar_cpf()


#print(p1.nome)
print(p1.mostrar_cpf())