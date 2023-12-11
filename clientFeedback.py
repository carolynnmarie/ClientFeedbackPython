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
        cur.execute('''CREATE TABLE IF NOT EXISTS feedback (clientname TEXT, comment TEXT)''')

        