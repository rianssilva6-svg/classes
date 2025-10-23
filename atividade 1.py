import os
os.system("cls")
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = Pessoa(nome = "Rian", idade = 19, peso = 67.9, altura = 1.75)

print("===Exibindo Dados===")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade} anos\nPeso: {pessoa1.peso}kg\nAltura: {pessoa1.altura}m")

