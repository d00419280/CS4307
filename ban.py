#!/usr/bin/env python3

import sqlite3
import sys
from time import gmtime, strftime

if len(sys.argv) > 1:
    post_id = sys.argv[1]
else:
    print("Provide a post ID to ban that post")
    sys.exit(1)

# Check that the post ID exists?

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("INSERT INTO bans (post_id, blocked) \
VALUES(?, ?)", (post_id, True))
con.commit()
con.close()