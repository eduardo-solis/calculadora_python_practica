
from flask import Flask, render_template
from flask import request

import forms
import operaciones

app = Flask(__name__)
'''
@app.route('/')
def index():
    return render_template('plantilla.html')
'''
@app.route('/', methods=['GET','POST'])
def formulario():
    
    user_form = forms.OperacionForm(request.form)
    r = 0
    
    if request.method == 'POST' and user_form.validate():
        
        num1 = int(user_form.numero1.data)
        num2 = int(user_form.numero2.data)
        
        option = str(user_form.brGrupo.data)
        
        objeto = operaciones.Operaciones(num1, num2, option)
        
        r = objeto.calcular()
    
    return render_template('formulario.html', form = user_form, respuesta = r)


if __name__=="__main__":
    app.run(debug=True, port=3000)
