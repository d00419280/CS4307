import os
import psycopg2
import psycopg2.extras
import urllib.parse

class SocialMediaDB:
    def __init__(self):
        urllib.parse.uses_netloc.append("postgres")
        url = urllib.parse.urlparse(os.environ["DATABASE_URL"])

        self.connection = psycopg2.connect(
            cursor_factory=psycopg2.extras.RealDictCursor,
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )

        self.cursor = self.connection.cursor()
        #self.cursor,self.cursor.lastrowid

    def __del__(self):
        self.connection.close()

    def createUserTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (email TEXT, name TEXT, password TEXT)")
        self.connection.commit()

    def createFollowTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS follows (email TEXT, followed_email TEXT)")
        self.connection.commit()

    def createPostTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS posts (post_id SERIAL PRIMARY KEY,email TEXT, time TEXT,content TEXT)")
        self.connection.commit()

    def createLikeTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS  likes (post_id INTEGER,email TEXT)")
        self.connection.commit()

    def createBlackList(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS blackList (post_id SERIAL PRIMARY KEY, blocked BOOL)")
        self.connection.commit()

    def addUser(self,email,name,password):
        data = [email,name,password]
        self.cursor.execute("INSERT INTO users (email,name,password) VALUES(%s,%s,%s)",data)
        self.connection.commit()
    
    def addFollow(self, email,followed_email):
        data = [email,followed_email]
        self.cursor.execute("INSERT INTO follows (email,followed_email) VALUES(%s,%s)",data)
        self.connection.commit()

    def addPost(self,email,time,contents):
        data = [email,time,contents]
        self.cursor.execute("INSERT INTO posts (email,time,contents) VALUES(%s,%s,%s)",data)
        self.connection.commit()