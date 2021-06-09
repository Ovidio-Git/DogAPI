import datetime
from peewee import *

database_name='test'

# create a mysql object
database = MySQLDatabase(
    database_name,
    user='root',
    password='testeando',
    host='localhost'
)

#table representation
class Dogs(Model):
    id =IntegerField(primary_key=True, unique=True, null=False)
    name = CharField(max_length=20, null=False)
    picture = CharField(max_length=100)
    is_adopted = BooleanField()
    created_date = DateTimeField(default=datetime.datetime.now)

    # for print name without problem
    def __str__(self):
        return self.name

    class Meta:
        database = database
        tabel_name = 'Dogs'