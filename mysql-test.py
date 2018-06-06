import MySQLdb

conn = MySQLdb.connect(
    user = 'root',
    passwd = 'pass',
    host = 'localhost',
    db = 'test'
)

cur = conn.cursor()

cur.execute('DROP TABLE items')
cur.execute("""CREATE TABLE items (item_id INTEGER PRIMARY KEY AUTO_INCREMENT,name TEXT,price INTEGER)""")

data = [('banana',300),('mango',640),('kiwi',280)]
for item in data:
    cur.execute('INSERT INTO items(name, price) VALUES(%s,%s)', item)

cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)