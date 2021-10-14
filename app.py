import os
from flask import Flask, render_template

app=Flask(__name__)

app.secret_key=os.urandom(24)



#=============== HOME =====================
@app.route('/')
@app.route('/home/')
@app.route('/index/')
def alternativas_home():
    #TODO
    return render_template('home.html')

#================ LOGIN USUARIO ===================
@app.route("/login/", methods=(['GET','POST']))
def loginUsuario():
    #TODO
    return render_template('loginUsuario.html', titulo='Login')

#================ REGISTRO USUARIO ===================
@app.route("/registro/", methods=(['GET','POST']))
def registrarUsuario():
    #TODO
    return render_template('registrarUsuario.html', titulo='Registro')

#================ AGREGAR HABITACIÓN ===================
@app.route("/habitacion/agregar/", methods=(['GET','POST']))
def agregarHabitacion():
    #TODO
    return render_template('createHabitacion.html', titulo='Agregar habitacion')

#================ EDITAR Y ELIMINAR HABITACIÓN ===================
@app.route("/habitacion/editar/", methods=(['GET', 'UPDATE', 'DELETE']))
def editarHabitacion():
    #TODO
    return render_template('editarHabitacion.html', titulo='Editar habitacion')

#================ BUSCAR HABITACIÓN ===================
@app.route("/habitacion/buscar/", methods=(['GET']))
def buscarHabitacion():
    #TODO
    return render_template('buscarHabitacion.html')

#================ CALIFICAR HABITACIÓN ===================
@app.route("/habitacion/calificar/", methods=(['GET','POST']))
def calificarHabitacion():
    #TODO
    return render_template('calificarHabitacion.html')

#================ RESERVAR HABITACIÓN ===================
@app.route("/habitacion/reservar/", methods=(['GET','POST']))
def reservarHabitacion():
    #TODO
    return render_template('reservarHabitacion.html')

#============== DASHBOARD ADMINISTRATIVO ===================
@app.route("/dashboard/", methods=(['GET']))
def dashboard():
    #TODO
    return render_template('dashboardAdmin.html', titulo='Dashboard')

#============== GESTIONAR COMENTARIOS ===================
@app.route("/comentarios/gestionar/", methods=(['GET', 'PUT', 'DELETE', 'POST']))
def gestionarComentarios():
    #TODO
    return render_template('gestionComen.html', titulo='Gestionar Comentarios')

if __name__=='__main__':
    app.run(debug=True)