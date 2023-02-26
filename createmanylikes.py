#!/usr/bin/env python3
import sqlite3
import random
import sys

def CreateLikes(numLikes):
    con = sqlite3.connect("SocialMediadb.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    for i in range(numLikes):
        user = random.choice(users)[0]
        res = cur.execute("SELECT * FROM follows WHERE email = ?",[user])
        followedPeople = cur.fetchall()
        followedPerson = random.choice(followedPeople)[1]

        res = cur.execute("SELECT * FROM posts WHERE email = (?)",[followedPerson])
        followedPersonPosts = cur.fetchall()
        if followedPersonPosts != []:
            post_id = random.choice(followedPersonPosts)[1]
            res = cur.execute("INSERT INTO likes (email, post_id) \
            VALUES(?, ?)", (user, post_id))
            con.commit()
    con.close()

if len(sys.argv) > 1:
    numLikes = int(sys.argv[1])
    CreateLikes(numLikes)