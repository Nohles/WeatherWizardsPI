import sqlite3

connection = sqlite3.connect("./sensors.db")
#print(connection.total_changes)
cursor = connection.cursor()
#cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")
#cursor.execute("INSERT INTO Runs VALUES ('3','DONE')")
#cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
#cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
#rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
#print(rows)
#target_fish_name = "Jamie"
#rows = cursor.execute(
#    "SELECT name, species, tank_number FROM fish WHERE name = ?",
#    (target_fish_name,),
#).fetchall()
#print(rows)
#connection.commit()

print(cursor.lastrowid)
#rows = cursor.execute("SELECT * FROM Runs where runID=1").fetchall()
#print(rows[0][0])

#print(type(rows))
connection.close()
