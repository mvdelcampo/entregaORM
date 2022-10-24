from peewee import *

psql_db = PostgresqlDatabase('db2', user='valegomez')

class ProductoPedido(Model):
    
    def __init__(self):
        self._cod_producto = IntegerField()
        self._id_pedido_simple = IntegerField()
        self._cantidad = IntegerField()

    @property
    def cod_producto(self):
        return self._cod_producto
    
    @property
    def id_pedido_simple(self):
        return self._id_pedido_simple
    
    @property
    def cantidad(self):
        return self._cantidad

    class Meta:
        database = psql_db
