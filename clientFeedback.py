import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl



def seedDB():
    conn = sqlite3.connect('feedback.sqlite')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Feedback')
    cur.execute('CREATE TABLE Feedback (name TEXT, comment TEXT);')

    strData = open('feedback.json')
    dataString = strData.read()
    jsonData = json.loads(dataString)

    for entry in jsonData:
        name = entry[0]
        comment = entry[1]

        cur.execute('INSERT INTO Feedback (name) VALUES( ? )', (name,))
        cur.execute('INSERT INTO Feedback (comment) VALUES ( ? )', (comment,))
        conn.commit()

def getFeedback():
    conn = sqlite3.connect('feedback.sqlite')
    cur = conn.cursor()
    feedback = cur.execute('SELECT * FROM Feedback')
    for row in feedback:
        print(row[0],row[1])
    cur.close()

def getFeedbackFromKeyword():
    conn = sqlite3.connect('feedback.sqlite')
    cur = conn.cursor()
    value = input("Enter keyword for search: ")
    feedback = cur.execute('SELECT * FROM Feedback WHERE comment IN ( ? )', (value,))
    for row in feedback:
        print(row[0],row[1])
    cur.close()




if __name__ == '__main__':
    seedDB()
    getFeedbackFromKeyword()