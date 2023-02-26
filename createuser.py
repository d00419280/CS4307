#!/usr/bin/env python3

import sqlite3
import sys
from time import gmtime, strftime

if len(sys.argv) > 2:
    email = sys.argv[1]
    password = sys.argv[2]
else:
    print("Provide an email and password to create an account")
    sys.exit(1)

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("INSERT INTO users (email, password) \
VALUES(?, ?)", (email, password))
res = cur.execute("INSERT INTO follows (email, followed_email) \
VALUES(?, ?)", (email, email)) # Follow...yourself...yes...
con.commit()
con.close()