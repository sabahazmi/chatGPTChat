import os
  
def config():
    db = {
        'host': os.environ.get('host'),
        'database': os.environ.get('database'),
        'user': os.environ.get('user'),
        'password': os.environ.get('password')
    }
    return db