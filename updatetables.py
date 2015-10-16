import sqlite3
import csv

conn = sqlite3.connect("bloginator.db")
c = conn.cursor()
TEMPLATE = ""

#Updating Users
def updateUsers():
    q="DELETE FROM users"
    c.execute(q)
    TEMPLATE="""INSERT INTO users
    VALUES ("%(uname)s","%(password)s")
    """
    reader = csv.DictReader(open("users.csv"))
    for item in reader:
        q=TEMPLATE%item
        #print q
        c.execute(q)
    conn.commit()

#Updating User Bios
def updateBios():
    q="DELETE FROM bio"
    c.execute(q)
    TEMPLATE="""
    INSERT INTO bio
    VALUES ("%(uname)s",%(age)s,"%(gender)s","%(descript)s")
    """
    reader = csv.DictReader(open("bio.csv"))
    for item in reader:
        q=TEMPLATE%item
        #print q
        c.execute(q)
    conn.commit()

#Updating Blogposts
def updatePosts():
    q="DELETE FROM blogpost"
    c.execute(q)
    #date --> MMDDYY
    #time --> HHMMSS
    TEMPLATE="""
    INSERT INTO blogpost
    VALUES ("%(uname)s","%(title)s","%(content)s",%(date)s,%(time)s,%(id)s)
    """
    reader = csv.DictReader(open("blogpost.csv"))
    for item in reader:
        q=TEMPLATE%item
        #print q
        c.execute(q)
    conn.commit()

#Updating Comments
def updateComments():
    q="DELETE FROM comments"
    c.execute(q)
    TEMPLATE="""
    INSERT INTO comments
    VALUES ("%(uname)s","%(comment)s",%(date)s,%(time)s,%(id)s)
    """
    reader = csv.DictReader(open("comments.csv"))
    for item in reader:
        q=TEMPLATE%item
        #print q
        c.execute(q)
    conn.commit()
