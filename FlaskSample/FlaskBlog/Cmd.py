'''
- Command to create DB file as per FlaskBlog mention
- Sqlite DB file will be create in same directory as source code
'''
from FlaskBlog.models import db, User, Post

db.create_all()

'''
- drop all tables
'''
#db.drop_all()

'''
get user list
'''
