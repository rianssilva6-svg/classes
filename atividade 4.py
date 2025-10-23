import os
os.system("cls")
from dataclasses import dataclass

@dataclass 
class Cliente:
    nome: str
    email: str
    endereco: str


    def mostrar_nome(self):
        print(f"Nome das pessoas: {self.nome}")    


    def mostrar_dados(self):
        print("\n")
        print("===Dados===")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereco}")

    
    

pessoa1 = Cliente(nome = input("Digite seu nome: "),
                  email = input("Digite seu email: "),
                  endereco=input("Digite seu endereço: "))
os.system("cls")

pessoa2 = Cliente(nome = input("Digite seu nome: "),
                  email = input("Digite seu email: "),
                  endereco=input("Digite seu endereço: "))

       
os.system("cls")

pessoa1.mostrar_nome()
pessoa2.mostrar_nome()

pessoa1.mostrar_dados()
pessoa2.mostrar_dados()




