#-------------------------- IMPORTS-----------------------
import warnings
import pandas as pd
warnings.filterwarnings('ignore')
import connect

#-----------------------END IMPORTS-----------------------

conn = connect.connect()
cur = conn.cursor()

class DBData:
    #-------------------------- Data -------------------------
    def getData():
        views_query = """
        SELECT
            doubts.question,
            doubt_answers.answer
        FROM
            doubts
            JOIN doubt_answers_doubt_links ON doubts.id = doubt_answers_doubt_links.doubt_id
            JOIN doubt_answers ON doubt_answers.id = doubt_answers_doubt_links.doubt_answer_id;"""
            
        cur.execute(views_query)
        data = pd.DataFrame.from_dict(cur.fetchall())
        colnames = ['question', 'answer']
        data.columns = colnames
        data.reset_index(drop=True, inplace=True)
        return data
    
    
