import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl

class clientFeedback:

    def seedDB(self):
        conn = sqlite3.connect('feedback.sqlite')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE Feedback (name TEXT,comment TEXT);''')

        strData = open('feedback.json')
        jsonData = json.loads(strData)

        for entry in jsonData:
            name = entry[0]
            comment = entry[1]

            cur.execute('INSERT INTO Feedback (name) VALUES( ? )', (name,))
            cur.execute('INSERT INTO Feedback (comment) VALUES ( ? )', (comment,))

    def getFeedback(self):
        conn = sqlite3.connect('feedback.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Feedback')
        feedback = cur.fetchall()
        print(feedback)