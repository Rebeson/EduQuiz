from Classes.Mixins import IdentificavelMixin

class Quiz(IdentificavelMixin):
    
    """Composição de perguntas selecionadas aleatoriamente."""
    
    def __init__(self, titulo):
        super().__init__()
        self._titulo = titulo
        self._lista_perguntas = []

    @property
    def titulo(self): return self._titulo

    def adicionar_pergunta(self, pergunta):
        if pergunta not in self._lista_perguntas:
            self._lista_perguntas.append(pergunta)

    def __len__(self):

        """Retorna o número de perguntas no quiz atual."""
        
        return len(self._lista_perguntas)

    def __iter__(self):

        """Permite iterar sobre as perguntas selecionadas."""
        
        return iter(self._lista_perguntas)

    def __str__(self):
        return f"Quiz: {self.titulo} ({len(self)} questões)"