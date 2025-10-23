import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

    def mostrar_dados (self):
        print(f"Nome: {self.nome}")
        print(f"idade: {self.idade}")

pessoa1 = Pessoa(nome = input("Digite seu nome: "),
                 idade = int(input("Digite sua idade: ")))        

os.system("cls")

pessoa2 = Pessoa(nome = input("Digite seu nome: "),
                 idade = int(input("Digite sua idade: ")))        

os.system("cls")

print("===Exibindo Dados===")
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()