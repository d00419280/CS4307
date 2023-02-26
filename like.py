#!/usr/bin/env python3

import sqlite3
import sys
from time import gmtime, strftime

if len(sys.argv) > 2:
    email = sys.argv[1]
    post_id = sys.argv[2]
else:
    print("Provide your email and a post ID to like it")
    sys.exit(1)

# A check to see if the email and post ID are valid might help but isn't necessary

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("INSERT INTO likes (email, post_id) \
VALUES(?, ?)", (email, post_id))
con.commit()
con.close()