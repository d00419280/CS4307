#!/usr/bin/env python3

import sqlite3
import sys

if len(sys.argv) > 1:
    post_id = sys.argv[1]
else:
    print("Provide a post ID to ban that post")
    sys.exit(1)

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM posts WHERE post_id = ?", (int(post_id),)).fetchone()
if not res:
    print(f"The post ID {post_id} does not exist")
    sys.exit(1)

res = cur.execute("INSERT INTO bans (post_id, blocked) \
VALUES(?, ?)", (int(post_id), True))
con.commit()
con.close()