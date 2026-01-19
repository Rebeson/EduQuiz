# Este projeto tem como objetivo avaliativo. Cuja funcionalidade principal é a criação de gerenciador de questões.
import sqlite3
import json
import os
from enum import Enum

from Classes.Pergunta import Pergunta 
from Classes.Quiz import Quiz
from Classes.BancoDados import BancoDados 
from Classes.Dificuldade import Dificuldade
from Classes.Usuario import Usuario


# Configuração Padrão do Sistema
CONFIGURACAO_PADRAO = {
    "duracao_padrao": 10,
    "máximo_tentativas": 3,
    "peso_dificuldade": {"FACIL": 1, "MEDIO": 2, "DIFICIL": 3}
}


# Interface 
def menu_principal():
    sistema = Quiz("Gerenciado de Questões")
    
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
            
#BancoDeDados           
def main():
    bd = BancoDados()
    config = Configuracao()
    
    while True:
        print("\n=== BEM-VINDO AO EDUQUIZ UFCA ===")
        print("1 - Fazer Login")
        print("2 - Criar Nova Conta")
        print("3 - Sair")
        op = input("Opção: ").strip()
        
        if op == "1":
            mat = input("Matrícula: ").strip()
            sen = input("Senha: ").strip()
            u = bd.autenticar(mat, sen)
            if u: menu_restrito(bd, config, u)
            else: print("\n[!] Matrícula ou senha incorretos.")
            
        elif op == "2":
            print("\n--- FORMULÁRIO DE CADASTRO ---")
            nome = input("Nome: ").strip()
            mail = input("Email: ").strip()
            mat = input("Matrícula: ").strip()
            sen = input("Senha: ").strip()
            tipo = input("É Administrador? (s/n): ").lower() == 's'
            
            novo_u = Usuario(nome, mail, mat, sen, Perfil.ADMIN if tipo else Perfil.ALUNO)
            if bd.cadastrar_usuario(novo_u):
                print("\n[OK] Conta criada! Você já pode fazer login.")
            else:
                print("\n[!] Erro: Esta matrícula já existe no sistema.")
                
        elif op == "3": sys.exit()

if __name__ == "__main__":
    menu_principal()

