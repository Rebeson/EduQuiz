# Este projeto tem como objetivo avaliativo. Cuja funcionalidade principal é a criação de gerenciador de questões.
import sqlite3
import json
import os
from enum import Enum


class Dificuldade (Enum):
    FACIL = 1
    MEDIO = 2
    DIFICIL = 3

CONFIGURAÇÃO_PADRAO = {
    "duração_padrão": 10,
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
        self.titulo = titulo
        self.lista_perguntas = []

class Usuario:
    def __init__(self, nome, email, matricula):
        self._nome = nome
        self._email = email
        self._matricula = matricula
        self._tentativas = []    