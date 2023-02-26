#!/usr/bin/env python3

import sqlite3

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
cur.execute("CREATE TABLE users(email, password)")
cur.execute("CREATE TABLE follows(email, followed_email)")
cur.execute("CREATE TABLE likes(post_id, email)")
cur.execute("CREATE TABLE posts(email, post_id, time, content)")
cur.execute("CREATE TABLE bans(post_id, blocked)")
con.commit()
con.close()