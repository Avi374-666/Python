import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Absolution@1",
    database="python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Joe", "Highway 20")
mycursor.execute(sql, val)

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

print("Name |  Address")

for x in myresult:
    print(x[0] + " | " + x[1])
    print(type(x))
mydb.commit()

print(mycursor.rowcount, "record inserted.")
