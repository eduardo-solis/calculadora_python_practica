
from wtforms import Form
from wtforms import IntegerField, RadioField
from wtforms.validators import NumberRange

class OperacionForm(Form):
    numero1 = IntegerField('Número 1', validators=[NumberRange(10,9999, 'Se necesita un numero de entre 2 y 4 cifras')])
    numero2 = IntegerField('Número 2', validators=[NumberRange(10,9999, 'Se necesita un numero de entre 2 y 4 cifras')])
    
    brGrupo = RadioField('grupo',choices=['Sumar','Restar','Multiplicar','Dividir'],default='Sumar')
    


