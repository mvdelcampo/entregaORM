from peewee import *

psql_db = PostgresqlDatabase('db2', user='valegomez')

class Tarjeta(Model):
    
    def __init__(self):
        self._nro = IntegerField()
        self._emisor = CharField()
        self._tipo = CharField()
        self._vencimiento = DateField()
        self._nro_cuenta = IntegerField()

    @property
    def nro_cuenta(self):
        return self._nro_cuenta

    @property
    def nro(self):
        return self._nro

    @property
    def emisor(self):
        return self._emisor
    
    @property
    def vencimiento(self):
        return self._vencimiento

    @property
    def tipo(self):
        return self._vencimiento


    class Meta:
        database = psql_db
