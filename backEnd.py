import sqlite3
import re

def connect():
    '''connect to database or creates if not existing'''
    conn = sqlite3.connect('Students.db')
    print("Opened student database successfully")
    #cursor for ..?
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Students
        (   REG TEXT PRIMARY KEY NOT NULL,
            FNAME TEXT NOT NULL,
            LNAME TEXT NOT NULL,
            AGE INTEGER NOT NULL,
            EMAIL TEXT,
            COURSE TEXT,
            USERNAME TEXT);
    ''')
    print ("Table created successfully")
    conn.commit()
    conn.close()
    print("Opened database successfully")

def add(reg,fn,ln,age,email,course,user):
    '''function to add new student to database'''
    '''
    Arguments: 
    reg: REG_NO text,    email: Email Text
    fn: First Name Text, course: Course Text
    ln: Last Name Text,  user: Username Text
    age: Age Integer
    '''
    conn = sqlite3.connect("Students.db")
    print("Database connected")

    #validating email. Entry only accepted if email is valid
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w{2,3}$'
    if(re.search(regex,email)):
        cur = conn.cursor()
        cur.execute("INSERT INTO Students Values (?,?,?,?,?,?,?)", (reg, fn, ln, age, email, course, user))
        conn.commit()
        print("Record successfully added")

    else:
        print("INVALID EMAIL")
        print("Adding Record Failed")
    conn.close()

def display():
    '''function to get all student data'''
    conn = sqlite3.connect('Students.db')
    print("Connected to database")

    cur = conn.cursor()
    cur.execute("SELECT * FROM Students")
    rows = cur.fetchall()

    for row in rows:
        print("REGISTRATION NUMBER = " + str(row[0]))
        print("NAME = " + str(row[1])+" "+str(row[2]))
        print("======================================")

    conn.close()

def update(reg,targetAttribute,newValue):
    #find data of student with Registration no. = reg, and change the "targetAttribute" to the "newValue"
    conn = sqlite3.connect("Student.db")
    print("Connected to database")
    cur = conn.cursor()
    if (targetAttribute == "FNAME"):
        cur.execute('UPDATE Students SET FNAME=? WHERE REG= ?',(newValue, reg))
        conn.commit()
        display()
    elif (targetAttribute == "LNAME"):
        cur.execute('UPDATE Students SET LNAME=? WHERE REG= ?', (newValue, reg))
        conn.commit()
        display()
    elif (targetAttribute == "AGE"):
        cur.execute('UPDATE Students SET AGE=? WHERE REG= ?', (newValue, reg))
        conn.commit()
        display()
    elif(targetAttribute == "EMAIL"):
        cur.execute('UPDATE Students SET EMAIL=? WHERE REG= ?', (newValue, reg))
        conn.commit()
        display()
    elif (targetAttribute == "COURSE"):
        cur.execute('UPDATE Students SET COURSE=? WHERE REG= ?', (newValue, reg))
        conn.commit()
        display()
    elif (targetAttribute == "USER"):
        cur.execute('UPDATE Students SET USER=? WHERE REG= ?', (newValue, reg))
        conn.commit()
        display()
    else:
        print("wrong input.")

def delete(reg):
    '''function to delete student from database'''
    conn = sqlite3.connect("Students.db")
    print("Connected to database")

    cur = conn.cursor()
    cur.execute("DELETE FROM Students WHERE REG=?",(reg,))
    conn.commit()
    print("Student "+reg+"  was deleted")

    print("Delete Operation successful")
    conn.close()

#========================================================================

#TESTING
connect() #works

add("ABC123","mONSTER","APPLE",100,"FNKJNJ","NKNK","NKNK") #works

display() #works

update("U17CS1104","FNAME","BABYyyyyy") #error
"""ERROR: cur.execute('UPDATE Students SET FNAME=? WHERE REG= ?',(newValue, reg))
sqlite3.OperationalError: no such table: Students"""

delete("U17CS1104") #error
"""ERROR: cur.execute("DELETE FROM Students WHERE REG=?",(reg,))
sqlite3.OperationalError: no such column: REG"""