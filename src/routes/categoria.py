from flask import Blueprint, render_template, flash, redirect, url_for

from src.forms.categoria import NovoCategoriaForm
from src.models.categoria import Categoria
from src.modules import db
from src.models.categoria import Categoria
import sqlalchemy as sa
from flask_login import login_required

bp = Blueprint('categoria',
               __name__,
               url_prefix='/categoria')

@bp.route('/', methods=['GET', 'POST'])
def lista():
    sentenca = sa.select(Categoria).order_by(Categoria.nome)
    rset = db.session.execute(sentenca).scalars()

    return render_template('categoria/lista.jinja2',
                           rset=rset)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = NovoCategoriaForm()
    if form.validate_on_submit():
        categoria = Categoria()
        categoria.nome = form.nome.data
        db.session.add(categoria)
        db.session.commit()
        flash(f"Categoria'{form.nome.data}' adicionada")
        return redirect(url_for('categoria.lista'))

    return render_template('categoria/add.jinja2',
                           tittle="Nova categoria",
                           form=form)