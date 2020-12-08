import pymysql

db = pymysql.connect(host="192.168.9.5", user="sa", password="sa", database="KIS")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print("Database version: %s" % data)

db.close()