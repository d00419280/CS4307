import sqlite3
import random
import sys

def FollowUsers(numFollows):
    con = sqlite3.connect("SocialMediadb.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    for i in range(numFollows):
        person1 = random.choice(users)
        person2 = random.choice(users)
        res2 = cur.execute("INSERT INTO follows (email, followed_email) \
        VALUES(?, ?)", (person1[0], person2[0]))
        con.commit()
    con.close()

if len(sys.argv) > 1:
    numFollows = sys.argv[1]
    FollowUsers(numFollows)