import os 
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_dados(self):
        print("===Exibindo Dados===")
        print(f"Nome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}")

pessoa1 = Pessoa(nome = input("Digite seu nome: "), 
                 email = input("Digite seu email: "), 
                 telefone = input("Digite seu telefone: "), 
                 endereco = input("Digite seu endereço: "))     
os.system("cls")

pessoa1.mostrar_dados()