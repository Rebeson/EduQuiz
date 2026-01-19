import sqlite3
from Classes.Pergunta import Pergunta
from Classes.Usuario import Usuario
from Classes.Perfil import Perfil

class BancoDados:
    
    """Gerencia a persistência de dados em SQLite."""

    def __init__(self, nome_banco="quiz_banco.db"):
        self.conn = sqlite3.connect(nome_banco)
        self._criar_tabelas()

    def _criar_tabelas(self):

        """ Tabelas necessárias para o projeto funcionar """

        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
            matricula TEXT PRIMARY KEY, nome TEXT, email TEXT, senha TEXT, perfil TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS perguntas (
            id INTEGER PRIMARY KEY AUTOINCREMENT, enunciado TEXT, tema TEXT, 
            dificuldade TEXT, resposta_certa INTEGER, alternativas TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS tentativas (
            id INTEGER PRIMARY KEY AUTOINCREMENT, matricula TEXT, 
            quiz_titulo TEXT, pontuacao REAL, data DATE DEFAULT CURRENT_DATE)''')
        self.conn.commit()

    def cadastrar_usuario(self, user: Usuario):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (matricula, nome, email, senha, perfil) VALUES (?, ?, ?, ?, ?)",
                           (user.matricula, user.nome, user.email, user.senha, user.perfil.value))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def autenticar(self, matricula, senha):

        """ Busca usuário para fazer o login """

        cursor = self.conn.cursor()
        cursor.execute("SELECT matricula, nome, email, senha, perfil FROM usuarios WHERE matricula = ? AND senha = ?", 
                       (matricula.strip(), senha.strip()))
        r = cursor.fetchone()
        if r:
            return Usuario(r[1], r[2], r[0], r[3], Perfil(r[4]))
        return None

    def salvar_pergunta(self, p: Pergunta):
        cursor = self.conn.cursor()
        alts = "|".join(p.alternativas)
        cursor.execute("INSERT INTO perguntas (enunciado, tema, dificuldade, resposta_certa, alternativas) VALUES (?, ?, ?, ?, ?)",
                       (p.enunciado, p.tema, p.dificuldade, p.resposta_certa, alts))
        self.conn.commit()

    def carregar_perguntas_aleatorias(self, limite):

        """Seleciona um número limitado de perguntas de forma aleatória do banco."""
        
        cursor = self.conn.cursor()
        cursor.execute('''SELECT enunciado, alternativas, tema, dificuldade, resposta_certa 
                          FROM perguntas ORDER BY RANDOM() LIMIT ?''', (limite,))
        return [Pergunta(r[0], r[1].split("|"), r[2], r[3], r[4]) for r in cursor.fetchall()]

    def salvar_tentativa(self, matricula, titulo, pontos):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO tentativas (matricula, quiz_titulo, pontuacao) VALUES (?, ?, ?)",
                       (matricula, titulo, pontos))
        self.conn.commit()

    def obter_ranking(self):

        """Relatório de ranking baseado na média de pontuação."""
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT matricula, AVG(pontuacao) FROM tentativas GROUP BY matricula ORDER BY AVG(pontuacao) DESC")
        return cursor.fetchall()
