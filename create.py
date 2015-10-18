import sqlite3

conn = sqlite3.connect("bloginator.db")
c = conn.cursor()
q = "create table users (uname text, password text, id integer)"
c.execute(q)

q = "create table bio (uname text, age integer, gender text, descript text)"
c.execute(q)

#date --> MMDDYY
#time --> HHMMSS
q = "create table blogpost (uname text, title text, content text, date integer, time integer, id integer)"
c.execute(q)

q = "create table comments (uname text, content text, date integer, time integer, id integer)"
c.execute(q)

conn.commit()
