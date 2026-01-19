import sys
from Classes.Pergunta import Pergunta
from Classes.Quiz import Quiz
from Classes.BancoDados import BancoDados
from Classes.Configuracao import Configuracao
from Classes.Usuario import Usuario
from Classes.Perfil import Perfil
from Classes.Excecoes import ValidacaoErro

def executar_quiz(bd, config, usuario):
    # Carrega o número configurado de perguntas aleatórias
    dados = bd.carregar_perguntas_aleatorias(config.qtd_perguntas)
    
    if not dados:
        print("\n[!] Não há perguntas cadastradas para iniciar o quiz.")
        return
    
    # Verifica o limite de tentativas do usuário
    cursor = bd.conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tentativas WHERE matricula = ?", (usuario.matricula,))
    if cursor.fetchone()[0] >= config.max_tentativas:
        print(f"\n[!] Você já atingiu o limite de {config.max_tentativas} tentativas.")
        return

    quiz = Quiz("Quiz Randômico UFCA")
    for p in dados: quiz.adicionar_pergunta(p)
    
    pontos = 0
    print(f"\n--- INICIANDO: {quiz.titulo} ({len(quiz)} questões) ---")
    
    for i, p in enumerate(quiz, 1):
        print(f"\nQuestão {i}: {p}")
        for idx, a in enumerate(p.alternativas):
            print(f"  {idx}) {a}")
        
        try:
            resp = int(input("Sua resposta (índice): ").strip())
            if resp == p.resposta_certa:
                valor_questao = config.obter_peso(p.dificuldade)
                pontos += valor_questao
                print(f">> CORRETO! (+{valor_questao} pontos)")
            else:
                print(f">> ERRADO. (A correta era: {p.resposta_certa})")
        except:
            print(">> Entrada inválida. Questão ignorada.")

    bd.salvar_tentativa(usuario.matricula, quiz.titulo, pontos)
    print(f"\n[FIM] Quiz finalizado. Pontuação total obtida: {pontos}")

def menu_restrito(bd, config, user):
    while True:
        print(f"\n=== EDUQUIZ | {user.nome} ({user.perfil.value}) ===")
        if user.perfil == Perfil.ADMIN:
            print("1 - [ADMIN] Cadastrar Nova Pergunta")
        print("2 - Responder Quiz Aleatório")
        print("3 - Ver Ranking de Usuários")
        print("4 - Logout")
        
        op = input("Escolha uma opção: ").strip()

        if op == "1" and user.perfil == Perfil.ADMIN:
            try:
                enun = input("Enunciado: ").strip()
                tema = input("Tema: ").strip()

                print("Dificuldade: 1-FACIL, 2-MEDIO, 3-DIFICIL")
                dif_input = input("Escolha (1, 2 ou 3): ").strip()
                mapa_dif = {"1": "FACIL", "2": "MEDIO", "3": "DIFICIL"}
                dif = mapa_dif.get(dif_input, dif_input.upper())
                
                alts = [input(f"Alt {i}: ").strip() for i in range(4)]
                resp = int(input("Índice correta (0-3): ").strip())
                
                bd.salvar_pergunta(Pergunta(enun, alts, tema, dif, resp))
                print("\n[OK] Pergunta cadastrada!")
            except Exception as e: print(f"\n[ERRO] {e}")
            
        elif op == "2":
            executar_quiz(bd, config, user)
            
        elif op == "3":
            ranking = bd.obter_ranking()
            print("\n--- RANKING GERAL (MÉDIA) ---")
            for mat, med in ranking:
                print(f"Matrícula: {mat} | Pontuação Média: {med:.2f}")
                
        elif op == "4": break

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

if __name__ == "__main__": main()