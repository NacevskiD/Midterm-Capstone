import sqlite3

username = ""

class myDB():
    def __init__(self):
        self.dbName = "Retail Database.sqlite"
        self.conn = sqlite3.connect(self.dbName)
        self.c = self.conn.cursor()
        self.tableName1 = "Information"
        self.id1 = "ID"
        self.column1 = "FirstName"
        self.column2 = "LastName"
        self.column3 = "Employed"
        self.column4 = "Phone"
        self.column5 = "Salary"

    def dropTable(self):
        self.c.execute('DROP TABLE Login')
        self.conn.commit()

    def createTable(self):
        try:
            self.c.execute('CREATE TABLE Login (id INTEGER PRIMARY KEY ,FirstName TEXT,LastName TEXT,'
                           'UserName TEXT,Password TEXT,Phone INTEGER,Supervisor BOOLEAN,Hours FLOAT DEFAULT 0)')
        except sqlite3.OperationalError:
            print("Table already exists")

        self.conn.commit()

    def addItem(self,firstName,lastName,phone,supervisor):
        userName = lastName + firstName[0]
        password = "password"
        arguments = [firstName,lastName,userName,password,phone,supervisor]
        self.c.execute('INSERT INTO Login(FirstName,LastName,UserName,Password,Phone,Supervisor) VALUES (?,?,?,?,?,?)',arguments)
        self.conn.commit()

    def deleteItem(self,id):

        self.c.execute('DELETE FROM Login WHERE id =?',(id,))
        self.conn.commit()

    def showAll(self):
        self.c.execute("SELECT * FROM Login")

        rows = self.c.fetchall()

        for row in rows:
            print(row)

    def getAll(self):
        self.c.execute("SELECT * FROM Login")
        rows = self.c.fetchall()

        return rows

    def checkLogin(self,userName,password):
        self.c.execute("SELECT UserName,Password,Supervisor FROM Login WHERE UserName = ? AND Password = ?",(userName,password,))
        rows = self.c.fetchall()

        if len(rows) > 0:
            print("User Found")
            print(rows[0][0])
            return True,rows[0][2]
        return False,False

    def getInfo(self,userName):
        self.c.execute("SELECT FirstName,LastName,Hours FROM Login WHERE UserName = ? ",(userName, ))
        rows = self.c.fetchall()
        return rows

    def addTime(self,time,user):
        data = [time,user]
        self.c.execute('UPDATE Login SET Hours = Hours + ? WHERE UserName = ? ',data)
        self.conn.commit()

    def closeConnection(self):
        self.conn.close()
