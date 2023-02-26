import RandomData
import sqlite3
import sys

def CreateManyUsers(numUsers):
    con = sqlite3.connect("SocialMediadb.db")
    cur = con.cursor()
    for i in range(numUsers):
        email = RandomData.RandomEmail()
        res = cur.execute("INSERT INTO users (email, password) \
        VALUES(?, ?)", (email, RandomData.RandomPassword()))
        res = cur.execute("INSERT INTO follows (email, followed_email) \
        VALUES(?, ?)", (email, email)) # Follow...yourself...yes...
        con.commit()
    con.close()

if len(sys.argv) > 1:
    numUsers = sys.argv[1]
    CreateManyUsers(numUsers)