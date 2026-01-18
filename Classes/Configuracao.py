import json
import os

class Configuracao:
    """Classe que lê o settings.json e retorna os valores de forma organizada."""
    def __init__(self, arquivo="settings.json"):
        self.caminho = arquivo
        self.dados = self._carregar_configuracoes()

    def _carregar_configuracoes(self):
        """ Caso o arquivo settings.json não exista, retorna valores padrão. """
        if not os.path.exists(self.caminho):
            return {
                "tentativas_maximas": 3, 
                "perguntas_por_quiz": 5,
                "pesos_dificuldade": {"FACIL": 1, "MEDIO": 2, "DIFICIL": 3}
            }
        with open(self.caminho, 'r', encoding='utf-8') as f:
            return json.load(f)

    @property
    def max_tentativas(self):
        return self.dados.get("tentativas_maximas", 3)

    @property
    def qtd_perguntas(self):
        return self.dados.get("perguntas_por_quiz", 5)

    def obter_peso(self, dificuldade):
        pesos = self.dados.get("pesos_dificuldade", {})
        return pesos.get(dificuldade.upper(), 1)