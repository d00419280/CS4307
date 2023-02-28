'bash init.sh' removes the database if it already exists, generates it,
populates it with some users and activity. The post contents detail the
expected results for a given post in regards to visibility, likes, 
moderation. To use manually:

./createuser.py [an email] [a password]
./follow.py [your email] [the email you want to follow]
./like.py [your email] [the post ID]
./post.py [your email] [Post contents]
./ban.py [post ID to hide]

Use these commands to populate the database:
  ./createmanyusers #num of users to create
  ./followmanyusers #num of follows to create
  ./createmanyposts #num of posts to create
  ./createmanylikes #num of likes to create