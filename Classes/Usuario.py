class Usuario:
    def __init__(self, nome, email, matricula):
        self._nome = nome
        self._email = email
        self._matricula = matricula
        self._tentativas = []    


    @property
    def nome(self):
        return self._nome
    
    @property
    def email(self):
        return self._email
    
    @property
    def matricula(self):
        return self._matricula
    
    @property
    def tentativas(self):
        return self._tentativas
    
    def adicionar_tentativa(self, tentativa):
        self._tentativas.append(tentativa)  

    def __str__(self):
        return f"Usuário: {self.nome}, Email: {self.email}, Matrícula: {self.matricula}"