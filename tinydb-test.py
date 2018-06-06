from tinydb import TinyDB,Query

filepath = 'test-tinydb.json'
db = TinyDB(filepath)

db.purge_table('fruits')

table = db.table('fruits')

table.insert({'name':'banana','price':600})
table.insert({'name':'orange','price':1200})
table.insert({'name':'mango','price':840})

print(table.all())

item = Query()
res = table.search(item.name =='orange')
print('orange is ', res[0]['price'])

print('over 800 yen')
res = table.search(item.price > 800)
for item in res:
    print(item)