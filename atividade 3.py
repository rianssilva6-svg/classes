import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    endereco: str

    def dados_entrega(self):
        print("===Dados de Entrega===")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
    

    def dados_email_marketing(self):
        print("===Dados do Email===")
        print (f"Nome: {self.nome} ")     
        print (f"Email: {self.email} ")    

pessoa1 = Cliente(nome = input("Digite seu nome: "), 
                  endereco = input("Digite seu endereço: "), 
                  email=input("Digite seu email: "))         
os.system("cls")

pessoa1.dados_entrega()
pessoa1.dados_email_marketing()
