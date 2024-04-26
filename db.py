import sqlite3

class db_manager():

        def __init__(self):
              self.con = sqlite3.connect("survey.db")
              self.cur = self.con.cursor()
        
        def create_table(self,table):
            return self.cur.execute(table)

        def insert_into_table(self, data):
            return self.cur.execute("INSERT INTO survey VALUES(?, ?, ?)", data)

        def select(self):
            res=self.cur.execute("SELECT survey FROM survey")
            return res.fetchone()

        def update(self,data):
            return self.cur.execute("Update survey set status=? where count=3", data)

        def commit(self):
            return self.con.commit()

        def delete(self):
            return self.cur.execute('DELETE FROM survey')

        def close(self):
            return self.con.close()

