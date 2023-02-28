#!/usr/bin/env python3

import sqlite3
import sys

if len(sys.argv) > 2:
    email = sys.argv[1]
    password = sys.argv[2]
else:
    print("Provide an email and password to create an account")
    sys.exit(1)

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
if res:
    print(f"The user {email} already exists")
    sys.exit(1)

res = cur.execute("INSERT INTO users (email, password) \
VALUES(?, ?)", (email, password))
res = cur.execute("INSERT INTO follows (email, followed_email) \
VALUES(?, ?)", (email, email)) # Follow...yourself...yes...
con.commit()
con.close()