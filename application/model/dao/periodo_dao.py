from application.model.entity.periodo import Periodo

class PeriodoDAO:

    def __init__(self):
        self._periodo_list = []
        self._periodo_list.append(Periodo("1", "1º Período"))
        self._periodo_list.append(Periodo("2", "2º Período"))


    def inserir(self, periodo):
        self._periodo_list.append(periodo)


    def buscar_por_id(self, id):
        periodo_list = list(filter(lambda periodo : periodo.get_id() == id, self._periodo_list))
        if len(periodo_list) == 0:
            return None
        return periodo_list[0] 
        #for i in range(0, len(self._periodo_list)):
        #    if self._periodo_list[i].get_id() == id:
        #        return self._periodo_list[i] 
        #return None
