import sqlite3

#set db
filepath = "test2.sqlite"
conn = sqlite3.connect(filepath)

#create table
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("""CREATE TABLE items(
item_id INTEGER PRIMARY KEY,
name TEXT UNIQUE,
price INTEGER
)
""")
conn.commit()

#insert a data
cur = conn.cursor()
cur.execute(
    "INSERT INTO items(name, price) VALUES(?,?)",
    ("orange",520))
conn.commit()

#insert multiple data
cur = conn.cursor()
data =[
    ("mango",720),
    ("kiwi", 400),
    ("grape", 800),
    ("peach", 940),
    ("persimon", 700),
    ("banana", 400)
]
cur.executemany(
    "INSERT INTO items(name, price) VALUES(?,?)",
    data)
conn.commit()

#select
cur = conn.cursor()
price_range = (400, 700)
cur.execute("SELECT item_id, name, price FROM items WHERE price >= ? and price <= ?",
            price_range)
item_list = cur.fetchall()

#print
for item in item_list:
    print(item)