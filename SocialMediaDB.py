import os
import sqlite3
import urllib.parse

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class SocialMediaDB:
    def __init__(self):
        self.connection = sqlite3.connect("SocialMediadb.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

        self.cursor = self.connection.cursor()
        #self.cursor,self.cursor.lastrowid

    def __del__(self):
        self.connection.close()

    def createUserTable(self):
        #self.cursor.execute("CREATE TABLE IF NOT EXISTS users (email TEXT, name TEXT, password TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (email, name, password)")
        self.connection.commit()

    def createFollowTable(self):
        #self.cursor.execute("CREATE TABLE IF NOT EXISTS follows (email TEXT, followed_email TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS follows (email, followed_email)")
        self.connection.commit()

    def createPostTable(self):
        #self.cursor.execute("CREATE TABLE IF NOT EXISTS posts (post_id SERIAL PRIMARY KEY,email TEXT, time TEXT,content TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS posts (post_id,email, time,content)")
        self.connection.commit()

    def createLikeTable(self):
        #self.cursor.execute("CREATE TABLE IF NOT EXISTS  likes (post_id INTEGER,email TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS  likes (post_id,email)")
        self.connection.commit()

    def createBlackList(self):
        #self.cursor.execute("CREATE TABLE IF NOT EXISTS blackList (post_id SERIAL PRIMARY KEY, blocked BOOL)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS blackList (post_id SERIAL PRIMARY KEY, blocked BOOL)")
        self.connection.commit()

    def addUser(self,email,name,password):
        self.cursor.execute("INSERT INTO users (email,name,password) VALUES(?,?,?)",email,name,password)
        self.connection.commit()
    
    def addFollow(self, email,followed_email):
        self.cursor.execute("INSERT INTO follows (email,followed_email) VALUES(?,?)",email,followed_email)
        self.connection.commit()

    def addPost(self,email,time,contents):
        data = [email,time,contents]
        self.cursor.execute("INSERT INTO posts (email,time,contents) VALUES(?,?,?)",email,time,contents)
        self.connection.commit()