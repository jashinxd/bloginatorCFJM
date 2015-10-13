import sqlite3
import csv

conn = sqlite3.connect("bloginator.db")
c = conn.cursor()

q="DELETE FROM users"
c.execute(q)
TEMPLATE="""INSERT INTO users
   VALUES ("%(uname)s",%(password)s)
"""
reader = csv.DictReader(open("users.csv"))
for item in reader:
    q=TEMPLATE%item
    #print q
    c.execute(q)

q="DELETE FROM bio"
c.execute(q)
TEMPLATE="""
INSERT INTO bio
   VALUES ("%(uname)s",%(age)d,%(gender)s,%(descript)s)
"""
reader = csv.DictReader(open("bio.csv"))
for item in reader:
    q=TEMPLATE%item
    #print q
    c.execute(q)

q="DELETE FROM blogpost"
c.execute(q)
TEMPLATE="""
INSERT INTO blogpost
   VALUES ("%(uname)s",%(title)s,%(content)s,%(date)d,%(time)d,%(id)d)
"""
reader = csv.DictReader(open("blogpost.csv"))
for item in reader:
    q=TEMPLATE%item
    #print q
    c.execute(q)

q="DELETE FROM comments"
c.execute(q)
TEMPLATE="""
INSERT INTO comments
   VALUES ("%(uname)s",%(content)s,%(date)d,%(time)d,%(id)d)
"""
reader = csv.DictReader(open("comments.csv"))
for item in reader:
    q=TEMPLATE%item
    #print q
    c.execute(q)

conn.commit()
