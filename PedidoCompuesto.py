from peewee import *

psql_db = PostgresqlDatabase('db2', user='valegomez')

class PedidoCompuesto(Model):
    
    def __init__(self):
        self._id = IntegerField()
        self._fecha = DateField()
        self._canal_de_compra = CharField()
        self._dni_cliente = IntegerField()

    @property
    def id(self):
        return self._id

    @property
    def fecha(self):
        return self._fecha
    
    @property
    def canal_de_compra(self):
        return self._canal_de_compra
    
    @property
    def dni_cliente(self):
        return self._dni_cliente

    class Meta:
        database = psql_db
