#!/usr/bin/env python3

import sqlite3
import sys
from time import gmtime, strftime

if len(sys.argv) > 2:
    email = sys.argv[1]
    content = sys.argv[2]
else:
    print("Provide a poster email and post content")
    sys.exit(1)

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
if not res:
    print(f"The user {email} does not exist")
    sys.exit(1)

time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
sum = 0
for char in content:
    sum += ord(char)
post_id = sum
# Generating a post id hash could be an assignment all its own, 
# and I need them to be predictable for testing, so eh lol

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("INSERT INTO posts (email, post_id, time, content) \
VALUES(?, ?, ?, ?)", (email, post_id, time, content))
con.commit()
con.close()