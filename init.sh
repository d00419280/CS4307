#!/bin/bash
rm SocialMediadb.db
chmod 755 init.py
./init.py
chmod 755 createuser.py
./createuser.py u1 123
./createuser.py u2 345
./createuser.py u3 678
chmod 755 follow.py
./follow.py u1 u2
./follow.py u1 u3
./follow.py u2 u3
chmod 755 post.py
chmod 755 like.py
chmod 755 ban.py

./post.py u3 "See: u1, u2, u3. Like: u1, u2, u3. Total likes: 3"
./like.py u1 3541
./like.py u2 3541
./like.py u3 3541

sleep 1
./post.py u2 "See: u1, u2. Like: u1. Total likes: 1"
./like.py u1 2808

sleep 1
./post.py u1 "See: u1. Likes: none. Total likes: 0"

sleep 1
./post.py u3 "You shouldn't be seeing this."
./ban.py 2685