from peewee import *

psql_db = PostgresqlDatabase('db2', user='valegomez')

class Cobro(Model):
    
    def __init__(self):
        self._id_pedido = IntegerField()
        self._nro_cuenta = IntegerField()
        self._aprobado = CharField()
        self._nro_aprobacion = IntegerField()

    @property
    def id_pedido(self):
        return self._id_pedido

    @property
    def nro_cuenta(self):
        return self._nro_cuenta

    @property
    def aprobado(self):
        return self._aprobado
    
    @property
    def nro_aprobacion(self):
        return self._nro_aprobacion

    class Meta:
        database = psql_db
