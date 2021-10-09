import os
from flask import Flask, render_template

app=Flask(__name__)

app.secret_key=os.urandom(24)

@app.route("/habitacion/agregar", methods=('GET', 'POST'))
def agregarHabitacion():
    titulo = "Agregar habitacion"
    return render_template('createHabitacion.html')