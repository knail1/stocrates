import MySQLdb
db=MySQLdb.connect(passwd="x",db="mysql")
# update passwd to make this work on server
c.execute(""" SELECT * FROM user """)
c.fetchall()
