import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: Endereco

    def mostrar_dados(self):
        os.system("cls")
        print("===DADOS===")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Rua: {self.endereco.logradouro}")
        print(f"numero: {self.endereco.numero}")
        print(f"Cidade: {self.endereco.cidade}")

dados=Pessoa(nome=input("Digite seu nome: "),
             email=input("Digite seu email: "),
             endereco=Endereco(logradouro=input("Digite sua Rua: "),
                               numero=int(input("Digite o número da sua morada: ")),
                               cidade=input("Digite a sua cidade: ")))

dados.mostrar_dados()    


