import sqlite3

conn = sqlite3.connect("./sensors.db")
#print(connection.total_changes)
cursor = conn.cursor()
#cursor.execute("CREATE TABLE Sensors (runID TEXT, temp TEXT, humidity TEXT , light TEXT, moisture TEXT, ph TEXT)")
runID = "755"
#cursor.execute("Update Runs set status= 'Done' where runID="+runID+";")
cursor.execute("Insert into Runs Values('785', 'Done')")
#cursor.execute("INSERT INTO Sensors VALUES ('1', '70', '20','300','400','7')")
rows = cursor.execute("SELECT * FROM Runs").fetchall()

print(rows)
#target_fish_name = "Jamie"
#rows = cursor.execute(
#    "SELECT name, species, tank_number FROM fish WHERE name = ?",
#    (target_fish_name,),
#).fetchall()
#print(rows)
conn.commit()
conn.close()
