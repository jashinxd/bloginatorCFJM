import sqlite3, csv

conn = sqlite3.connect("demo.db")
c = conn.cursor()

def csv_dict():
    reader = csv.DictReader(open("users.csv"))
    TEMPLATE = "username: %(username)s, password: %(password)s)"
    for item in reader:
        print TEMPLATE%(username)
        
def authenticate(uname,pword):
    if csv_dict
