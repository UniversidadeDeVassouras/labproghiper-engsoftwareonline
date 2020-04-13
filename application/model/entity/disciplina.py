class Disciplina:

    def __init__(self, id, nome, disciplina_prerequisito, carga_horaria, credito):
        self._id = id
        self._nome = nome
        self._carga_horaria = carga_horaria
        self._disciplina_prerequisito = disciplina_prerequisito
        self._credito = credito
    
    def get_nome(self):
        return self._nome

    def get_carga_horaria(self):
        return self._carga_horaria

    def get_disciplina_prerequisito(self):
        return self._disciplina_prerequisito
    
    def get_credito(self):
        return self._credito

    class Credito:

        def __init__(self, teorica, pratica):
            self._pratica = pratica
            self._teorica = teorica 

        def get_pratica(self):
            return self._pratica

        def get_teorica(self):
            return self._teorica