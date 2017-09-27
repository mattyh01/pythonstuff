import os, sys, MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="Entrop1a!",
                     db="python_test"
                     )

cur = db.cursor()

#def findpass(name):

name = raw_input("Hello - please input your name to receive your password: ")
cur.execute("""SELECT pass FROM passtable WHERE name = %s""", [name])
rows = cur.fetchall()

if not rows:
    print "%s not found - please try again" % name
#    findpass(name)
else:
    for row in rows:
        print row[0]

db.close()
