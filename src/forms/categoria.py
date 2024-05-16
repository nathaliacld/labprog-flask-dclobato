from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import InputRequired


class NovoCategoriaForm(FlaskForm):
    nome = StringField('Nome da categoria', validators=[
                                                    InputRequired(message="É obrigatório informar um nome para categoria")
                                 ])
    submit = SubmitField("Adicionar")