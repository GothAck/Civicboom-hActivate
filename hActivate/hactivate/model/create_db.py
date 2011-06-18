from sqlalchemy import schema, types
from sqlalchemy.engine import create_engine

metadata = schema.MetaData()

user_table = schema.Table('users', metadata,
    schema.Column('id', types.Integer, primary_key=True),
    schema.Column('user', types.Unicode(64), default=u''), # unique=True, nullable=False), <- 
)

item_table = schema.Table('items', metadata,
    schema.Column('id', types.Integer, primary_key=True),
    schema.Column('title', types.Unicode(64), default=u''),
    schema.Column('description', types.Unicode(255), default=u''),
)

for t in metadata.sorted_tables:
    print t.name
    for c in t.c:
        print "\t",c.name,"->",c.type
    print
    
engine = create_engine('sqlite:///../data/live.db')
metadata.bind = engine

metadata.create_all(checkfirst=True)