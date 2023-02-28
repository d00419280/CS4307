#!/usr/bin/env python3

import sqlite3

con = sqlite3.connect("SocialMediadb.db")
cur = con.cursor()
res = cur.execute("SELECT b.email, COUNT(b.email) AS total \
FROM bans AS a \
JOIN posts AS b ON a.post_id = b.post_id \
WHERE a.blocked \
GROUP BY b.email \
ORDER BY total DESC \
LIMIT 1")

verybadman = res.fetchone()[0]
print(f"The user with the most banned posts is {verybadman}")
print(f"Hiding all posts by {verybadman}")

res = cur.execute("SELECT post_id FROM posts WHERE email = ?", (verybadman,))
for row in res:
    cur.execute("INSERT INTO bans (post_id, blocked) \
    VALUES(?, ?)", (int(row[0]), True))

con.commit()
con.close()