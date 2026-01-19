class IdentificavelMixin:
    """Mixin para fornecer um identificador único baseado na instância do objeto."""
    def __init__(self):
        self._id_interno = id(self)

    @property
    def id_interno(self):
        return self._id_interno