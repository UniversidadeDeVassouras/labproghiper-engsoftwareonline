from application import app
from application.model.dao.periodo_dao import PeriodoDAO
from flask import render_template
from application.model.entity.periodo import Periodo

@app.route("/periodo/<periodo_id>")
def periodo_por_id(periodo_id):
    periodo = PeriodoDAO().buscar_por_id(periodo_id)
    return render_template("periodo.html", periodo=periodo, periodo_id=periodo_id)
