import sqlite3

conn = sqlite3.connect('domains.db')
cursor = conn.cursor()

cursor.execute('SELECT DISTINCT project_id, name FROM domains')
projects = cursor.fetchall()

for project_id, domain in projects:
    regex = r'.*\.sub\.yyy\.com|.*static\.developer\.xxx\.com'
    cursor.execute('INSERT INTO rules (regexp, project_id) VALUES (?, ?)', (regex, project_id))

conn.commit()
conn.close()