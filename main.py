# Este projeto tem como objetivo avaliativo. Cuja funcionalidade principal é a criação de gerenciador de questões.
import sqlite3
import json
import os
from enum import Enum


class Dificuldade (Enum):
    FACIL = 1
    MEDIO = 2
    DIFICIL = 3

CONFIGURACAO_PADRAO = {
    "duracao_padrao": 10,
    "máximo_tentativas": 3,
    "peso_dificuldade": {"FACIL": 1, "MEDIO": 2, "DIFICIL": 3}
}


class Pergunta:
    def __init__(self, enunciado, alternativas, tema, dificuldade, resposta_certa):
        if not (3 <= len(alternativas) <= 5):
            raise ValueError("A pergunta deve ter entre 3 e 5 alternativas.")
        if not (0 <= resposta_certa < len(alternativas)):
            raise ValueError("Índice de resposta correta inválido.")
        
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.resposta_certa = resposta_certa
        self.dificuldade = dificuldade.upper()
        self.tema = tema.upper()


class BancoDados:
    def __init__(self, nome_banco = "quiz_banco.db"):
        self.conn = sqlite3.connect(nome_banco)
        self._criar_tabela()


class Sistema_Quiz:
    def __init__(self, titulo):
        self._titulo = titulo
        self._lista_perguntas = []

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def perguntas(self):
        return self._lista_perguntas

    def adicionar_pergunta(self, pergunta):
        self._lista_perguntas.append(pergunta)

class Usuario:
    def __init__(self, nome, email, matricula):
        self._nome = nome
        self._email = email
        self._matricula = matricula
        self._tentativas = []    

    @property
    def nome(self):
        return self._nome
    
    @property
    def email(self):
        return self._email
    
    @property
    def matricula(self):
        return self._matricula
    
    @property
    def tentativas(self):
        return self._tentativas
    
    def adicionar_tentativa(self, tentativa):
        self._tentativas.append(tentativa)  

    def __str__(self):
        return f"Usuário: {self.nome}, Email: {self.email}, Matrícula: {self.matricula}"
# Interface 
def menu_principal():
    sistema = Sistema_Quiz("Gerenciado de Questões")
    
    while True:
        print("\n" + "="*30)
        print(f" {sistema.titulo} ")
        print("1 - Cadastrar uma Determinada Pergunta")
        print("2 - Listar as Perguntas")
        print("3 - Sair")
        print("="*30)
        
        opcao = input("Escolha uma das opções seguintes: ")

        if opcao == "1":
            print("\n_Nova Pergunta:_")
            enunciado = input("Enunciado: ")
            tema = input("Tema: ")
            dif = input("Dificuldade (FACIL, MEDIO, DIFICIL): ")
            
            
            alts = []
            for i in range(4): # Padrão com 4 alternativas
                alts.append(input(f"Alternativa {i}: "))
            
            resp = int(input("O índice da resposta correta (0-3): "))

            try:
                p = Pergunta(enunciado, alts, tema, dif, resp)
                sistema.adicionar_pergunta(p)
                print("\n Pergunta adicionada com sucesso!")
            except Exception as e:
                print(f"\n Erro! {e}")

        elif opcao == "2":
            print("\n_LISTA DE PERGUNTAS_")
            if not sistema.perguntas:
                print("Nenhuma pergunta cadastrada no momento.")
            else:
                for idx, p in enumerate(sistema.perguntas):
                    print(f"{idx} | {p.enunciado} [{p.dificuldade}]")
            
            input("\nPressione Enter para voltar.")

        elif opcao == "3":
            print("Encerrando programa. Obrigado!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()
