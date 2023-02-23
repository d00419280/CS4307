#!/usr/bin/env python3

import sqlite3
import sys
if len(sys.argv) > 1:
    email = sys.argv[1]
else:
    print("Provide an email to fetch a feed for")
    sys.exit(1)

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.excecute(f"SELECT a.content, a.email, a.time, COUNT(c.email) \
FROM posts AS a \
JOIN follows AS b ON b.email = {email} AND b.email = a.followed_email \
JOIN likes AS c ON a.post_id = c.post_id \
GROUP BY a.post_id \
ORDER BY time")
for row in res:
    print(row[0])
    print(f"Posted by {row[1]} on {row[2]}, {row[3]} likes.")
    print()