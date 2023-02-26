#!/bin/bash
chmod 755 init.py
./init.py
chmod 755 createuser.py
./createuser.py user1 123
./createuser.py user2 345
./createuser.py user3 678
chmod 755 follow.py
./follow.py user1 user2
./follow.py user1 user3
./follow.py user2 user3