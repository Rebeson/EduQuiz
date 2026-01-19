from Classes.Perfil import Perfil

class Usuario:
    """Guarda os dados do usuário e verifica o tipo de acesso."""
    def __init__(self, nome, email, matricula, senha, perfil=Perfil.ALUNO):
        self._nome = nome
        self._email = email
        self._matricula = matricula # Matrícula para efetuar o login
        self._senha = senha # Senha para efetuar o login
        self._perfil = perfil if isinstance(perfil, Perfil) else Perfil(perfil)

    @property
    def nome(self): return self._nome
    
    @property
    def email(self): return self._email
    
    @property
    def matricula(self): return self._matricula
    
    @property
    def senha(self): return self._senha
    
    @property
    def perfil(self): return self._perfil

    def __str__(self):
        """ Método especial para mostrar o usuário formatado """
        return f"[{self.perfil.value}] {self.nome} ({self.matricula})"