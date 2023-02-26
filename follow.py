#!/usr/bin/env python3

import sqlite3
import sys
from time import gmtime, strftime

if len(sys.argv) > 2:
    email = sys.argv[1]
    followed_email = sys.argv[2]
else:
    print("Provide your email and the email you want to follow")
    sys.exit(1)

# Check both emails are valid?

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("INSERT INTO follows (email, followed_email) \
VALUES(?, ?)", (email, followed_email))
con.commit()
con.close()