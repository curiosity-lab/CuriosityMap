import sqlite3

conn = sqlite3.connect('CuriosityMap/db.sqlite3')
c = conn.cursor()
for row in c.execute('SELECT * FROM "questionnaire_questionsdata"'):
    print(row)