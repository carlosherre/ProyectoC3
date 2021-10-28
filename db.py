import sqlite3
from sqlite3 import Error
from flask import g

def conectar_db():
    try: 
        if 'db' not in g:
            g.db=sqlite3.connect('Hotel_Swissotel.db')
        return g.db
    except Error:
        print(Error)

def desconectar_db():
    db = g.pop( 'db', None )
    if db is not None:
        db.close()