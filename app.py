import os
from flask import Flask, render_template
import functools
#import yagmail as yagmail
import utils
from flask import Flask, render_template, flash, request, redirect, url_for,session,g,send_file,make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from db import desconectar_db, conectar_db
app=Flask(__name__)

app.secret_key=os.urandom(24)

numsave=0
presave=0
tiposave=''
lineaReserva=''

#=============== HOME =====================
@app.route('/')
@app.route('/home/')
@app.route('/index/')
def alternativas_home():
    if "id" in session:
        return render_template("home.html", titulo='Inicio', loged='LogOut')
    else:
        return render_template("loginUsuario.html", titulo='Login')
#================ LOGIN USUARIO ===================
@app.route("/login/", methods=(['GET','POST']))
def loginUsuario():
    try:
        if request.method == 'POST':
            db = conectar_db()
            error = None
            username = request.form['username']
            password = request.form['password']
            
            user = db.execute(
                'SELECT * FROM Huespedes WHERE Usuario = ?', (username,)
            ).fetchone()
            if user is not None:
                contrasena=check_password_hash(user[5], password)
            if user is None:
                user = db.execute(
                'SELECT * FROM Administradores WHERE Usuario = ?', (username,)
                ).fetchone()
                if user is not  None:
                    contrasena=user[2]
                    #contrasena=check_password_hash(user[2], password)
            db.close()
            
            if not contrasena:
                error="Contraseña Inválida"
                flash(error) 
                return render_template("loginUsuario.html",titulo="Inicio de Sesion")
            else:
                error="Iniciando sesión ..."
                flash(error)
                print(error)
                session.clear()
                session["id"]=user[0]
                session["nombre"]=user[1]
                session["adm"]=user[3]
                session["hab"]=0
                return render_template('home.html',titulo="Inicio", loged='LogOut')
        else:
            if "id" in session:
                flash("Sesion cerrada")
                session.clear()
                return render_template("loginUsuario.html", titulo="Inicio de Sesion")
            else:
                return render_template("loginUsuario.html", titulo="Inicio de Sesion")
    except:
        if user is None:
            error="Usuario Inválido"
            flash(error) 
        return render_template('loginUsuario.html', titulo="Inicio de Sesion")
#================ REGISTRO USUARIO ===================
@app.route("/registro/", methods=(['GET','POST']))
def registrarUsuario():
    try:
        if request.method=='POST':
            nombre=request.form['nombre']
            apellido=request.form['apellido']
            correo=request.form['correo']
            username=request.form['usuario']
            password=request.form['contrasena']
            error=None
            db=conectar_db()
            
            if error is not None:
                return render_template("loginUsuario.html", titulo="Inicio de Sesion")
            else:
                db.execute(
                     'INSERT INTO Huespedes (Nombre, Apellido, Correo, Usuario, Contrasena) VALUES (?,?,?,?,?)',
                     (nombre, apellido, correo, username, generate_password_hash (password)) 
                )
                db.commit()
                flash('Registrado con éxito')
                return render_template('loginUsuario.html', titulo="Login")
        else:
            if "id" in session:
                return render_template("home.html", titulo="Inicio", loged='LogOut')
            else:
                return render_template("registarUsuario.html", titulo="Registrar")
    except:
       return render_template('registrarUsuario.html', titulo="Registro")

#================ AGREGAR HABITACIÓN ===================
@app.route("/habitacion/agregar/", methods=(['GET','POST']))
def agregarHabitacion():
    try:
        if request.method=='POST':
            numero=request.form['numero']
            disponible=request.form['dispo']
            f_inicio=request.form['dispoini']
            f_fin=request.form['dispofin']
            tipo=request.form['tipo']
            precio=request.form['precio']
            descripcion=request.form['descrip']
            db=conectar_db()
            db.execute(
                     'INSERT INTO Habitaciones (Num_Cuarto, Disponibilidad, Fecha_Inicio, Fecha_Fin, Tipo, Precio, Descripcion) VALUES (?,?,?,?,?,?,?)',
                     (numero, disponible, f_inicio, f_fin, tipo, precio, descripcion) 
                )
            db.commit()
            desconectar_db()
            return render_template('home.html', titulo="Inicio", loged='LogOut')
        else:
            if "id" in session:
                return render_template('createHabitacion.html', titulo="Agregar Habitacion", loged='LogOut')
            else:
                return render_template('loginUsuario.html', titulo="Login")
    except:
        return render_template('createHabitacion.html', titulo="Agregar habitacion")

#================ EDITAR HABITACIÓN ===================
@app.route("/habitacion/editar/", methods=(['GET', 'POST']))
def editarHabitacion():
    try:
        
        if request.method == 'GET':
            numero=request.args.get('numero')
            precio=request.args.get('precio')
            tipo=request.args.get('tipo')
            dispoini=request.args.get('dispoini')
            dispofin=request.args.get('dispofin')
            descrip=request.args.get('descrip')
            db=conectar_db()
            user = db.execute(
                'SELECT * FROM Habitaciones WHERE Num_Cuarto = ?;', (numero,)
            ).fetchone()
            num=user[1]
            fi=user[3]
            ff=user[4]
            ti=user[5]
            pr=user[6]
            des=user[7]
            flash('Habitación encontrada')
            desconectar_db()
            if "id" in session:
                return render_template('editarHabitacion.html', titulo="Editar Habitacion",fi=fi, ff=ff, ti=ti, pr=pr, des=des, num=num, loged="LogOut")
            else:
                return render_template('loginUsuario.html', titulo="Login")
        if request.method == 'POST':
            numero=request.form['numero']
            precio=request.form['precio']
            tipo=request.form['tipo']
            dispoini=request.form['dispoini']
            dispofin=request.form['dispofin']
            descrip=request.form['descrip']
            db=conectar_db()
            db.execute(
                     'UPDATE Habitaciones SET Fecha_Inicio=?, Fecha_Fin= ?, Tipo=?, Precio=?, Descripcion=? WHERE Num_Cuarto =?;',
                     (dispoini, dispofin, tipo, precio, descrip, numero) 
                )
            db.commit()
            desconectar_db()
            flash("Actualizado con éxito")
            return render_template('editarHabitacion.html', titulo="Editar Habitacion", loged="LogOut")
    except:
        flash('Habitación NO encontrada')
        return render_template('editarHabitacion.html', titulo='Editar habitacion', loged="LogOut")

#================ ELIMINAR HABITACIÓN ===================
@app.route("/habitacion/eliminar/", methods=(['GET', 'POST']))
def eliminarHabitacion():
    try:
        
        if request.method == 'GET':
            numero=request.args.get('numero')
            precio=request.args.get('precio')
            tipo=request.args.get('tipo')
            dispoini=request.args.get('dispoini')
            dispofin=request.args.get('dispofin')
            descrip=request.args.get('descrip')
            db=conectar_db()
            user = db.execute(
                'SELECT * FROM Habitaciones WHERE Num_Cuarto = ?;', (numero,)
            ).fetchone()
            num=user[1]
            fi=user[3]
            ff=user[4]
            ti=user[5]
            pr=user[6]
            des=user[7]
            flash('Habitación encontrada')
            desconectar_db()
            if "id" in session:
                return render_template('editarHabitacion.html', titulo="Eliminar Habitacion",fi=fi, ff=ff, ti=ti, pr=pr, des=des, num=num, loged="LogOut")
            else:
                return render_template('loginUsuario.html', titulo="Login")
        elif request.method == 'POST':
            numero=request.form['numero']
            
            db=conectar_db()
            db.execute(
                     'DELETE FROM Habitaciones WHERE Num_Cuarto = ?',(numero,) 
                )
            db.commit()
            desconectar_db()
            flash("Eliminado con éxito")
            return render_template('editarHabitacion.html', titulo="Eliminar Habitacion", loged="LogOut")
    except:
        flash('Habitación NO encontrada')
        return render_template('editarHabitacion.html', titulo='Eliminar Habitacion')


#================ BUSCAR HABITACIÓN ===================
@app.route("/home/habitacion/buscar/", methods=(['GET','POST']))
@app.route("/habitacion/buscar/", methods=(['GET','POST']))
def buscarHabitacion():
    try:
        if request.method == 'POST':
            tipo=request.form['tipo']
            checkin=request.form['Checkin']
            checkout=request.form['Checkout']
            db=conectar_db()
            if checkin == "" or checkout == "":
                user = db.execute(
                'SELECT * FROM Habitaciones WHERE Tipo = ? AND Disponibilidad = "D"',(tipo, )
                ).fetchall()
            elif tipo == "default":
                user = db.execute(
                    'SELECT * FROM Habitaciones WHERE Fecha_Inicio <= ? AND Fecha_Fin >= ? AND Disponibilidad = "D"',(checkin, checkout)
                ).fetchall()
            else:
                user = db.execute(
                    'SELECT * FROM Habitaciones WHERE Fecha_Inicio <= ? AND Fecha_Fin >= ? AND Tipo = ? AND Disponibilidad = "D"',(checkin, checkout, tipo )
                ).fetchall()
            if user is not None:
                for n in user:
                    flash(f'{n[1]} - {n[6]}')
            elif user == []:
                flash("Cambiar criterios de búsqueda")
            desconectar_db()
            
            return render_template('buscarHabitacion.html', titulo="Buscar Habitacion")
            
        else:
            mostrar=request.args.get('mostrar')
            if mostrar is None or mostrar == 'default':
                return render_template('buscarHabitacion.html', titulo="Buscar Habitacion") 
            else:
                return render_template('reservarHabitacion.html', titulo='Reservar Habitacion', loged='LogOut') 
    except:
        flash('Habitación NO encontrada')
        return render_template('buscarHabitacion.html', titulo="Buscar Habitacion")

    
#================ CALIFICAR HABITACIÓN ===================
@app.route("/habitacion/calificar/", methods=(['GET','POST']))
def calificarHabitacion():
    try:
        if request.method=='POST':
            idc=request.form['cliente']
            idh=request.form['hab']
            cal=request.form['rating1']
            com=request.form['message']
            print('Antes del insert')
            db=conectar_db()
            db.execute(
            'INSERT INTO Comentarios (Id_Huesped, Id_Habitacion, Comentario, Calificacion) VALUES (?,?,?,?)',(session["id"], session["hab"], com, cal)
                    )
            db.commit()
            desconectar_db()
            print('Después del insert')
            return redirect(url_for('alternativas_home'))
        else:
            print('Cargando el calificar Habitacion')
            return render_template('calificarHabitacion.html', titulo='Calificar Habitacion', loged='LogOut')
    except Exception as e:
        print(e)
        return render_template('calificarHabitacion.html')

#================ RESERVAR HABITACIÓN ===================
@app.route("/habitacion/reservar/", methods=(['GET','POST']))
def reservarHabitacion():
        try:
            if request.method=='POST':
                mostrar=request.form["mostrar"]
                num=mostrar.split("-")[0].strip()
                ini=request.form["Checkin"]
                fin=request.form["Checkout"]
                db=conectar_db()
                db.execute(
                'UPDATE Habitaciones SET Disponibilidad = "R" WHERE Num_Cuarto = ?',(num,)
                )
                db.commit()
                user = db.execute(
                'SELECT Id_Habitacion FROM Habitaciones WHERE Num_Cuarto =?',(num,)
                ).fetchone()
                idh=user[0]
                db.execute(
                'INSERT INTO Reservas (Id_Huesped, Id_Habitacion, Fecha_Inicio, Fecha_Fin) VALUES (?,?,?,?)',(session["id"], idh, ini, fin)
                )
                db.commit()
                desconectar_db()
                flash(f'Habitación {num} reservada')
                print(f'Habitación {num} reservada')
                session["hab"]=idh
                return render_template('calificarHabitacion.html', titulo='Calificar Habitacion', loged='LogOut')
            else:
                print('Cargando el Reservar')
                return render_template('buscarHabitacion.html', titulo="Reservar Habitacion",loged='LogOut')
        except Exception as e:
            print(e)
            return render_template('buscarHabitacion.html', titulo="Reservar Habitacion", loged='LogOut')

#============== DASHBOARD ADMINISTRATIVO ===================
@app.route("/dashboard/", methods=(['GET']))
def dashboard():
    #TODO
    return render_template('dashboardAdmin.html', titulo='Dashboard', loged='LogOut')

if __name__=='__main__':
    app.run(debug=True)