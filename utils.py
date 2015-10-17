import sqlite3, csv, updatetables

conn = sqlite3.connect("demo.db")
c = conn.cursor()

def csv_dict():
    reader = csv.DictReader(open("users.csv"))
    TEMPLATE = "username: %(username)s, password: %(password)s)"
#    for item in reader:
 #       print TEMPLATE%(username)
            
def authenticate(uname,pword):
    updatetables.authenPass("franklin", "wangboi")
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