from sqlalchemy import schema, types
from sqlalchemy.sql import select
from sqlalchemy.engine import create_engine

print "SQL Expression Example\n"

metadata = schema.MetaData()
engine = create_engine('sqlite:///../data/live.db')
connection = engine.connect()
metadata.bind = engine

user_table = schema.Table('users', metadata, autoload=True)
item_table = schema.Table('items', metadata, autoload=True)

"""
ins = user_table.insert(
    values=dict(user=u'unittest')
)
print ins
result = connection.execute(ins)
print result
"""

print "\nSelecting Results\n"

for table in [user_table, item_table]:
    s = select([table])
    print table.name
    result = connection.execute(s)
    for row in result:
        print row
    print

connection.close()