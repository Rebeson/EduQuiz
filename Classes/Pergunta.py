from Classes.Mixins import IdentificavelMixin
from Classes.Excecoes import ValidacaoErro

class Pergunta(IdentificavelMixin):
    """Define a estrutura de uma questão com validações automáticas."""
    def __init__(self, enunciado, alternativas, tema, dificuldade, resposta_certa):
        super().__init__()

        """ A pergunta deve ter entre 3 e 5 alternativas"""

        if not (3 <= len(alternativas) <= 5):
            raise ValidacaoErro("A pergunta deve ter entre 3 e 5 alternativas.")
        
        """ O índice da resposta deve existir na lista"""

        if not (0 <= resposta_certa < len(alternativas)):
            raise ValidacaoErro("Índice de resposta correta inválido.")
        
        self._enunciado = enunciado
        self._alternativas = alternativas
        self._tema = tema.upper()
        self._dificuldade = dificuldade.upper()
        self._resposta_certa = resposta_certa

    @property
    def enunciado(self): return self._enunciado
    @property
    def tema(self): return self._tema
    @property
    def dificuldade(self): return self._dificuldade
    @property
    def alternativas(self): return self._alternativas
    @property
    def resposta_certa(self): return self._resposta_certa

    def __eq__(self, outro):

        """Compara perguntas para evita duplicidade"""
        
        if not isinstance(outro, Pergunta): return False
        return self.enunciado == outro.enunciado and self.tema == outro.tema

    def __str__(self):
        """Resumo visual da pergunta."""
        return f"[{self.dificuldade}] {self.tema}: {self.enunciado}"