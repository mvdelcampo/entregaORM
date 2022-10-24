from peewee import *

psql_db = PostgresqlDatabase('db2', user='valegomez')

class PedidoSimple(Model):
    
    def __init__(self):
        self._id = IntegerField()
        self._precio_total = FloatField()
        self._estado = CharField()
        self._fecha = DateField()
        self._canal_de_compra = CharField()
        self._nro_pedido_compuesto = IntegerField()
        self._dni_cliente = IntegerField()

    @property
    def id(self):
        return self._id

    @property
    def nro_pedido_compuesto(self):
        return self._nro_pedido_compuesto

    @property
    def precio_total(self):
        return self._precio_total
    
    @property
    def estado(self):
        return self._estado

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
