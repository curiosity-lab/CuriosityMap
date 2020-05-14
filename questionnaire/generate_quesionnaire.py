import sqlite3

# conn = sqlite3.connect('../db.sqlite3')
# c = conn.cursor()
# questions = [(1, 'Q1'),
#              (2, 'Q2'),
#              (3, 'Q3'),
#             ]
# c.executemany('INSERT INTO "questionnaire_questionsdata" VALUES (?, ?)', questions)
# conn.commit()
# conn.close()



conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()
for row in c.execute('SELECT * FROM "questionnaire_questionsdata"'):
    print(row)