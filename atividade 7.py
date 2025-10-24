import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Registro:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrar_dados(self):
        print("\n")
        print("===DADOS===")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso}kg")
        print(f"Altura: {self.altura}m")

lista_registro = []

for i in range (4):
    pessoa=Registro(nome=input("Digite o nome: "),
                    idade=int(input("Digite a idade: ")),
                    peso=float(input("Digite o peso: ")),
                    altura=float(input("Digite a altura: ")))
    lista_registro.append(pessoa)
    os.system("cls")

for registro in lista_registro:
    registro.mostrar_dados()    