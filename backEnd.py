import sqlite3

def connect():
    '''connect to database or creates if not existing'''
    conn = sqlite3.connect('Students.db')
    print("Opened student database successfully")

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
    cur = conn.cursor()
    cur.execute("INSERT INTO Students Values (?,?,?,?,?,?,?)",(reg,fn,ln,age,email,course,user))
    conn.commit()
    print("Record successfully added")
    conn.close()

def display():
    '''function to get all student data'''
    conn = sqlite3.connect('Students.db')
    print("Connected to database")

    cursor = conn.execute("SELECT REG, FNAME, LNAME, AGE, EMAIL, COURSE, USERNAME from Students")
    for row in cursor:
        print("REG. NUMBER = " + str(row[0]))
        print("NAME = " + str(row[1]) + " " + str(row[2]))
        print("AGE = " + str(row[3]))
        print("EMAIL = " + str(row[4]))
        print("COURSE = " + str(row[5]))
        print("____________________________________________")
    print("Display operation successful")
    conn.close()

def update(reg):
    print("hey baby!!")

def delete(reg):
    '''function to delete student from database'''
    conn = sqlite3.connect("Students.db")
    print("Connected to database")

    conn.execute("DELETE from Students where REG=?",(reg))
    conn.commit()
    print("Student "+reg+"  was deleted")

    print("Delete Operation successful")
    conn.close()

connect()
#add("1103","dss",'dsd',23,"sdsa","dsds","dsddd")
display()