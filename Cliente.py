from peewee import *

psql_db = PostgresqlDatabase('db2', user='valegomez')

class Cliente(Model):
    
    def __init__(self):
        self._dni = IntegerField()
        self._nombre = CharField()
        self._apellido = CharField()
        self._mail = CharField()
        self._cel = IntegerField()
        self._calle = CharField()
        self._nro_puerta = IntegerField()
        self._apartamento = IntegerField()
        self._cod_postal = IntegerField()
        self._departamento = CharField()
        self._localidad = CharField()

    @property
    def dni(self):
        return self._dni

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido
    
    @property
    def mail(self):
        return self._mail

    @property
    def cel(self):
        return self._cel

    @property
    def calle(self):
        return self._calle
    
    @property
    def nro_puerta(self):
        return self._nro_puerta
    
    @property
    def apartamento(self):
        return self._apartamento
    
    @property
    def cod_postal(self):
        return self._cod_postal

    @property
    def departamento(self):
        return self._departamento
    
    @property
    def localidad(self):
        return self._localidad

    class Meta:
        database = psql_db
