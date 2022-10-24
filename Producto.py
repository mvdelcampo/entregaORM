from peewee import *

psql_db = PostgresqlDatabase('db2', user='valegomez')

class Producto(Model):
    
    def __init__(self):
        self._cod_producto = IntegerField()
        self._nombre = CharField()
        self._precio = FloatField()
        self._stock = IntegerField()
        self._qr = BlobField()

    @property
    def cod_producto(self):
        return self._cod_producto
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    @property
    def qr(self):
        return self._qr

    class Meta:
        database = psql_db
