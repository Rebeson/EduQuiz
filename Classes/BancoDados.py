class BancoDados:
    def __init__(self, nome_banco = "quiz_banco.db"):
        self.conn = sqlite3.connect(nome_banco)
        self._criar_tabela()