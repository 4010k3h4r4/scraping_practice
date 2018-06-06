import sqlite3

#connect to sqlite db
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

#create table
cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS items;

CREATE TABLE items(
item_id INTEGER PRIMARY KEY,
name TEXT UNIQUE,
price INTEGER
);

INSERT INTO items(name, price) VALUES('apple',300);
INSERT INTO items(name, price) VALUES('orange',200);
INSERT INTO items(name, price) VALUES('mango',800);
""")
#commit
conn.commit()

#exttract data
cur = conn.cursor()
cur.execute("SELECT item_id, name, price FROM items")
item_list = cur.fetchall()

#print result
for list in item_list:
    print(list)