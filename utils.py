import sqlite3, csv, hashlib, datetime
from datetime import date

conn = sqlite3.connect("bloginator.db")
c = conn.cursor()
TEMPLATE = ""

"""
updateUsers(): --> Updates the user table in bloginator.db from users.csv
updateBios(): --> Updates the bio table in bloginator.db from bio.csv
updatePosts(): --> Updates the blogpost table in bloginator.db from blogpost.csv
updateComments(): --> Updates the comments table in bloginator.db from comments
getInfo(table, retAttribute, attribute, value): --> takes the table name, return attrubute, attribute of value, and value, returns value of what you are looking for. Will search in database by:
 SELECT retAttribute FROM table WHERE attribute=value
authenPass(username, password) --> Takes username and password submitted on
website. Will return bool.
"""

conn = sqlite3.connect("bloginator.db")
c = conn.cursor()
TEMPLATE = ""

#Update Users
def updateUsers():
    conn = sqlite3.connect("bloginator.db")
    c = conn.cursor()
    TEMPLATE = ""
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
    conn = sqlite3.connect("bloginator.db")
    c = conn.cursor()
    TEMPLATE = ""
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
    conn = sqlite3.connect("bloginator.db")
    c = conn.cursor()
    TEMPLATE = ""
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

def getInfo(table, retAttribute, attribute, value):
    conn = sqlite3.connect("bloginator.db")
    c = conn.cursor()
    TEMPLATE = ""
    q="SELECT "+retAttribute+" FROM "+table+" where "+attribute+"="+'"'+value+'"'
    c.execute(q)
    return c.fetchone()[0]

def authenticate(username, password):
    if (username == "" or password == ""):
        return False
    if getInfo("users", "password", "uname", username) == hashlib.md5(password):
        return True
    else: 
        return False
        
def register(username, password, age, gender):
    accountwriter = csv.writer("users.csv")
    accountwriter.writerow(username,hashlib.md5(password))
    biowriter = csv.writer("bio.csv")
    content = ""
    biowriter.writerow(username, age, gender, content)
    updateUsers()
    updateBios()
    
def postBlog(username, title, content):
    reader = csv.DictReader(open("blogpost.csv"))
    postDict = {}
    for row in reader:
        postDict = row
    if (postDict):
        newid = 0
    else:
        newid = postDict['id'] + 1
    currtime = datetime.datetime.time(datetime.datetime.now())
    currdate = date.today()
    writer = csv.writer("blogpost.csv")
    writer.writerow(username,title,content,currdate,currtime,newid)
    updatePosts()
    
def postComment(username, content, ID):
    currtime = datetime.datetime.time(datetime.datetime.now())
    currdate = date.today()
    writer = csv.writer("comments.csv")
    writer.writerow(username,content,currdate,currtime,ID)
    updateComments()
    
def editBio(username, age, gender, descript):
    reader = csv.DictReader("bio.csv")
    writer = csv.writer("bio.csv")
    for line in reader:
        if (username == line["username"]):
            line["age"] = age
            line["gender"] = gender
            line["descript"] = descript
    updateBios()
    
def validuname(uname):
    reader = csv.DictReader(open("users.csv"))
    for i in reader: 
        if uname == i['uname']:
            return True

register("danKim", "dannyboi", 13, "F")
postBlog("franklin", "who is dan", "idk anything about this kid")
postComment("danKim", "hey not cool man", 3)
