import RandomData
import sqlite3
import random
import sys
from time import gmtime, strftime

def GeneratePostIdTimeContent():
    content = RandomData.RandomContent()
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    sum = 0
    for char in content:
        sum += ord(char)
    post_id = sum % 1000000
    return post_id,time,content

def CreatePosts(numPosts):
    con = sqlite3.connect("SocialMediadb.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    for i in range(numPosts):
        email = random.choice(users)
        post_id,time,content = GeneratePostIdTimeContent()
        res = cur.execute("INSERT INTO posts (email, post_id, time, content) \
        VALUES(?, ?, ?, ?)", (email[0], post_id, time, content))
        res = cur.execute("INSERT INTO bans (post_id, blocked) \
        VALUES(?, ?)", (post_id, False))
        con.commit()
    con.close()

if len(sys.argv) > 1:
    numPosts = sys.argv[1]
    CreatePosts(numPosts)