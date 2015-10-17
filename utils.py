import sqlite3, csv, hashlib, updatetables

conn = sqlite3.connect("bloginator.db")
c = conn.cursor()
TEMPLATE = ""

def authenticate(uname,pword):
    """
    reader = csv.DictReader(open("users.csv"))
    for i in reader:
        #print i['uname']
        if uname == i['uname'] and pword == i['password']:
            return True
    """        
    updatetables.authenPass("franklin", "wangboi")

def validuname(uname):
    reader = csv.DictReader(open("users.csv"))
    for i in reader: 
        if uname == i['uname']:
            return True

