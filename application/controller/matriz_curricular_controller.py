from application import app
from application.model.dao.periodo_dao import PeriodoDAO
from flask import render_template, request
from application.model.entity.periodo import Periodo

@app.route("/matriz-curricular")
def matriz_curricular():
    periodo_id = request.args.get('periodo')
    if periodo_id is None:
        periodo_id = 1
    periodo_dao = PeriodoDAO()
    periodo = periodo_dao.buscar_por_id(int(periodo_id))
    periodo_list = periodo_dao.listar_todos()
    return render_template("matriz_curricular.html", periodo=periodo, periodo_list=periodo_list)
