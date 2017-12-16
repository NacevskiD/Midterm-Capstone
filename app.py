import os

import datetime
from flask import Flask, render_template, request, redirect, url_for,sessions,session,flash
import Database

app = Flask(__name__)


db = Database.myDB()

def calculateTime(timeIn,timeOut):
    timeIn = timeIn.split(":")
    timeOut = timeOut.split(":")
    timeInReal = int(timeIn[0])
    timeOutReal = int(timeOut[0])
    if timeOutReal > timeInReal:
        return timeOutReal - timeInReal
    else:
        return int((12 - timeInReal) + timeOutReal)


@app.route('/', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        ifUser, ifAdmin = db.checkLogin(request.form['username'], request.form['password'])
        if ifUser and ifAdmin == 1:
            employees = db.getAll()
            return render_template('employer.html',employees = employees)

        elif ifUser:
            Database.username = request.form['username']
            data = db.getInfo(Database.username)
            date = datetime.datetime.now().strftime("%y-%m-%d")
            return render_template('employee.html' ,data = data,date = date)

        else:
            flash("Wrong Password")


    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('signup.html')

@app.route('/delete', methods=['POST'])
def deleteOrAdd():
    id = request.form['deleteID']
    if len(id) == 0:
        fName = request.form['firstName']
        lName = request.form['lastName']
        phone = request.form['phone']
        supervisor = request.form['supervisor']

        if supervisor == "Supervisor":
            db.addItem(fName,lName,phone,True)


        else:
            db.addItem(fName, lName, phone, False)
            employees = db.getAll()
            return render_template('employer.html', employees=employees)

    else:

        db.deleteItem(id)
    employees = db.getAll()
    return render_template('employer.html', employees = employees)


@app.route('/add_time', methods=['POST'])
def add_time():
    print("TEST")
    total = calculateTime(request.form["time-in"],request.form["time-out"])
    db.addTime(total,Database.username)
    data = db.getInfo(Database.username)
    date = datetime.datetime.now().strftime("%y-%m-%d")
    print(date)
    return render_template('employee.html', data=data ,date= date)


@app.route('/logout', methods=['POST'])
def logout():
    login()



if __name__ == "__main__":
    app.run()