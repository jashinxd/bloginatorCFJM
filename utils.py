import sqlite3, csv, updatetables

def authenticate(uname,pword):
    reader = csv.DictReader(open("users.csv"))
    for i in reader:
        #print i['uname']
        if uname == i['uname'] and pword == i['password']:
            return True
            
    #updatetables.authenPass("franklin", "wangboi")

def validuname(uname):
    reader = csv.DictReader(open("users.csv"))
    for i in reader: 
        if uname == i['uname']:
            return True

    """
    if uname == "cindyli" and pword == "cindy":
        return True
    if uname == "jasonshin" and pword == "jason":
        return True
    if uname == "franklinwang" and pword == "franklin":
        return True
    if uname == "masaheromasuda" and pword == "masahero":
        return True
    else:
        return False
    """
    
