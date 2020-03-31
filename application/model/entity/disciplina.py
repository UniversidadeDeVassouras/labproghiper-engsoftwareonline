class Disciplina:

    def __init__(self, id, carga_horaria, disciplina_prerequisito, credito):
        self._id = id
        self._carga_horaria = carga_horaria
        self._disciplina_prerequisito = disciplina_prerequisito
        self._credito = credito
    
    
    class Credito:

        def __init__(self, pratica, teorica):
            self._pratica = pratica
            self._teorica = teorica 

    