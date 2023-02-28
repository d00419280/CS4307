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
res = cur.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
if not res:
    print(f"The user {email} does not exist")
    sys.exit(1)
    
res = cur.execute("SELECT b.content, b.email, b.time, COUNT(c.email), d.blocked, b.post_id \
FROM follows AS a \
JOIN posts AS b ON a.followed_email = b.email AND a.email = ? \
LEFT JOIN likes AS c ON b.post_id = c.post_id \
LEFT JOIN bans as d ON b.post_id = d.post_id \
GROUP BY b.post_id \
ORDER BY time", (email,))
print()
for row in res:
    if row[4]:
        continue
    print(row[0])
    print(f"Posted by {row[1]} on {row[2]}, {row[3]} likes.")
    cur2 = con.cursor()
    res2 = cur2.execute("SELECT * FROM likes WHERE post_id = ? AND email = ?", (row[5], email))
    if res2.fetchone():
        print("You liked this post")
    print(f"Post ID: {row[5]}")
    print()

con.close()