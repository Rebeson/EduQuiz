"""Mensagens de erro para identificar exatamente o que falhou"""

class EduQuizError(Exception):
    """Classe base para as exceções do projeto."""
    pass

class ValidacaoErro(EduQuizError):
    """Erro quando dados não atendem aos critérios de validação."""
    pass

class LimiteTentativasError(EduQuizError):
    """Quando o limite de tentativas do usuário é excedido."""
    pass