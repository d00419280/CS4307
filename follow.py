#!/usr/bin/env python3

import sqlite3
import sys

if len(sys.argv) > 2:
    email = sys.argv[1]
    followed_email = sys.argv[2]
else:
    print("Provide your email and the email you want to follow")
    sys.exit(1)

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
if not res:
    print(f"The user {email} does not exist")
    sys.exit(1)
res = cur.execute("SELECT * FROM users WHERE email = ?", (followed_email,)).fetchone()
if not res:
    print(f"The user {followed_email} does not exist")
    sys.exit(1)

res = cur.execute("INSERT INTO follows (email, followed_email) \
VALUES(?, ?)", (email, followed_email))
con.commit()
con.close()