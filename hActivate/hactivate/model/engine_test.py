from sqlalchemy.engine import create_engine

engine = create_engine('sqlite:///../data/test_db.db')
connection = engine.connect()

connection.execute(
    """
    CREATE TABLE users (
        username VARCHAR PRIMARY KEY,
        password VARCHAR NOT NULL
    );
    """
)

connection.execute(
    """
    INSERT INTO users (username, password) VALUES (?, ?);
    """,
    "foo", "bar"
)

result = connection.execute("select username from users")

for row in result:
    print "username:", row['username']
connection.close()