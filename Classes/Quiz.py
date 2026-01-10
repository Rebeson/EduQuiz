class Quiz:
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

