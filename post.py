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

# Need a check to see if the email is a valid user, though I guess it'll still work if we don't

time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
sum = 0
for char in content:
    sum += ord(char)
post_id = sum % 1000000
# Generating a post id hash could be an assignment all its own, 
# so let's hope this is enough lol

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("INSERT INTO posts (email, post_id, time, content) \
VALUES(?, ?, ?, ?)", (email, post_id, time, content))
res = cur.execute("INSERT INTO bans (post_id, blocked) \
VALUES(?, ?)", (post_id, False))
con.commit()
con.close()