import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

pessoal1 = Pessoa("Marta", 30, "123.456.789-10")
pet1 = Pet("Totó", 4, 35.50)

print("===Exibindo Dados===")
print (f"Nome: {pessoal1.nome}\nIdade: {pessoal1.idade}\nCPF: {pessoal1.cpf}\n")
print (f"Nome: {pet1.nome}\nIdade: {pet1.idade}\nPeso: {pet1.peso}\n")