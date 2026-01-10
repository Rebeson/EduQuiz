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