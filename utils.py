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
    VALUES ("%(uname)s","%(content)s",%(date)s,%(time)s,%(id)s)
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
    if getInfo("users", "password", "uname", username) == str(hashlib.md5(password)):
        return True
    else: 
        return False
        
def register(username, password, age, gender):
    with open ("users.csv", 'ab') as f:
        accountwriter = csv.writer(f)
        m = hashlib.md5(password)
        accountwriter.writerow([username, m.hexdigest()])
        f.close()
    
    with open ("bio.csv", 'ab') as f:    
        biowriter = csv.writer(f)
        content = ""
        biowriter.writerow([username, str(age), gender, content])
        f.close()
        
    updateUsers()
    updateBios()
    
def postBlog(username, title, content):
    reader = csv.DictReader(open("blogpost.csv"))
    postDict = {}
    for row in reader:
        print row
        if (row):
           postDict = row
    print postDict.keys()
    if (postDict == {}):
        newid = 0
    else:
        newid = int(postDict["id"]) + 1
    currtime = datetime.datetime.time(datetime.datetime.now())
    currtime = str(currtime)[0:8]
    currtime = currtime.replace(":","")
    currdate = date.today()
    with open ("blogpost.csv", 'ab') as f:
        writer = csv.writer(f)
        writer.writerow([username, title, content, str(currdate), str(currtime), str(newid)])
        f.close()
        
    updatePosts()
    
def postComment(username, content, ID):
    currtime = datetime.datetime.time(datetime.datetime.now())
    currtime = str(currtime)[0:8]
    currtime = currtime.replace(":","")
    currdate = date.today()
    with open("comments.csv", 'ab') as f:
        writer = csv.writer(f)
        writer.writerow([username, content, str(currdate), str(currtime), str(ID)])
        f.close()
        
    updateComments()
    
def editBio(username, age, gender, descript):
    reader = csv.DictReader(open("bio.csv"))
    with open("bio.csv", "ab") as f:
        writer = csv.writer(f)
        f.close()
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
