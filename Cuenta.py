from peewee import *

psql_db = PostgresqlDatabase('db2', user='valegomez')

class Cuenta(Model):
    
    def __init__(self):
        self._nro_cuenta = IntegerField()
        self._usuario = CharField()
        self._dni = IntegerField()
        self._fecha_creacion = DateTimeField()

    @property
    def nro_cuenta(self):
        return self._nro_cuenta

    @property
    def usuario(self):
        return self._usuario

    @property
    def dni(self):
        return self._dni
    
    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    class Meta:
        database = psql_db



    


