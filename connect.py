import psycopg2
from config import config
  
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(host=params['host'],
            database=params['database'],
            user=params['user'],
            password=params['password']
        )
        print('CONNECTED!')
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    return conn
