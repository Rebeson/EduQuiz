from Classes.Pergunta import Pergunta 
from Classes.Quiz import Quiz
from Classes.BancoDados import BancoDados 
from Classes.Dificuldade import Dificuldade
from Classes.Usuario import Usuario


# Teste da Classe Pergunta
print("\n--- Teste Pergunta ---")

try:
    # Caso de sucesso
    p1 = Pergunta(
        enunciado="Qual a capital do Brasil?", 
        alternativas=["Brasilia", "Paris", "Berlim", "Roma"], 
        tema="Geografia", 
        dificuldade="FACIL", 
        resposta_certa=1
    )
    print(f"Pergunta criada: {p1.enunciado}")
    print(f"Tema: {p1.tema}")
    
    # Testando a validação
    print("Pergunta com poucas alternativas...")
    p2 = Pergunta("2+2?", ["3", "4"], "Matemática", "FACIL", 1)
except ValueError as e:
    print(f"Validação funcionou: {e}")


# Teste da Classe Quiz
print("\n--- Teste Quiz ---")

q1 = Quiz("Quiz de Conhecimentos Gerais")
print(q1.titulo)

# Adicionando perguntas
q1.adicionar_pergunta("Quanto é 2 + 2?")
q1.adicionar_pergunta("Qual a capital da França?")
q1.adicionar_pergunta("Quem escreveu 'Iracema'?")
print(q1.perguntas) 


# Teste da Classe Usuario
print("\n--- Teste Usuario ---")

user = Usuario("Victor", "victor@email.com", "2025tbd01")
print(user)

# Adicionando tentativas
user.adicionar_tentativa(5) # Adiciona um valor à lista de tentativas
print(f"Tentativas do usuário: {user.tentativas}")