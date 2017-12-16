import Database
import datetime

db = Database.myDB()

db.addItem("Test","Test",123,True)


db.showAll()
