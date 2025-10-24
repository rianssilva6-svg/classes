import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    cpf: str
    telefone: str

    def mostrar_dados(self):
        print("\n")
        print("===Dados===")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
    
    def sms_dados(self):
        print("===Dados SMS===")
        print(f"Telefone: {self.telefone}. Pertencente: {self.nome}")
        print("\n")


lista_cliente = []

for i in range(3):
    dados = Cliente(nome=input("Digite seu nome: "),
                    cpf=input("Digite seu CPF: "),
                    telefone=input("Digite seu telefone: "))

    lista_cliente.append(dados)
    os.system("cls")

for dados in lista_cliente:
    dados.mostrar_dados() 
print("\n")
for dados in lista_cliente:
    dados.sms_dados() 
    

    