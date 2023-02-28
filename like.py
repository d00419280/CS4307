#!/usr/bin/env python3

import sqlite3
import sys

if len(sys.argv) > 2:
    email = sys.argv[1]
    post_id = sys.argv[2]
else:
    print("Provide your email and a post ID to like it")
    sys.exit(1)

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
if not res:
    print(f"The user {email} does not exist")
    sys.exit(1)
res = cur.execute("SELECT * FROM posts WHERE post_id = ?", (int(post_id),)).fetchone()
if not res:
    print(f"The post ID {post_id} does not exist")
    sys.exit(1)

res = cur.execute("INSERT INTO likes (email, post_id) \
VALUES(?, ?)", (email, int(post_id)))
con.commit()
con.close()