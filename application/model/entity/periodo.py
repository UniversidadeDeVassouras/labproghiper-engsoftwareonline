class Periodo:

    def __init__(self, codigo, nome):
        self._id = codigo
        self._nome = nome
    
    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome