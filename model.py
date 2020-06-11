import sqlite3

ROOT = path.dirname(path.relpath(__file__))

def create_post(name, content):
	con = sql.connect(path.join(ROOT, 'database.db'))
	cur = con.cursor()
	cur.execute('insert into posts(name, content) values(?,?)', (name, content)
	con.commit()
	con.close()
