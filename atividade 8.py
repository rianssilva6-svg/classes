from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Criador:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int    
    autor: Criador

    def exibir_detalhes (self):
        os.system("cls")
        print("===EXIBINDO OS DETALHES===")
        print(f"O Autor do livro: {self.autor.nome}")
        print("\n")
        print(f"O titulo do livro: {self.titulo}")
        print("\n")
        print(f"O ano que esse livro foi produzido foi no ano de {self.ano}")
        print("\n")
        print(f"Biografia: {self.autor.biografia}")
        print("\n")

        
dados = Livro(titulo=input("Digite o titulo do livro: "),
              ano=int(input("Digite o ano que foi lançado: ")),
              autor=Criador(nome=input("Digite o nome do autor: "),
                            biografia=input("Digite sua biografia: ")))


dados.exibir_detalhes()


