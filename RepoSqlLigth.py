import sqlite3

class RepoSqlLight():
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
    def create_table(self, table_name, columns):
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(sql)
        self.conn.commit()   
        
    def InsertExample(self):
        self.cursor.execute(" insert into DK1_Members (StudId, FName, LName, Age, MemType, FavoritChips) values ('jame','eftekhari', 'jamshid', 58, 'teacher', 'sea salt') ") 
        self.conn.commit()    
        
    def add_row(self, table_name, values):
        sql = f"INSERT INTO {table_name} VALUES ({values})"
        self.cursor.execute(sql)
        self.conn.commit()   
    
    def get_all(self, table_name):
        sql = f"SELECT * FROM {table_name}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows    
        
if __name__ == '__main__':
    db_name = 'dk1.db'
    table_name = 'DK1_Members'
    columns = 'StudId TEXT, FName TEXT, LName TEXT, Age INTEGER, MemType TEXT, FavoritChips TEXT'
    values = "'StudId','LName', 'FName', 20, 'MemType', 'Chips Name'"
        
    repo = RepoSqlLight(db_name)
   # repo.create_table(table_name, columns)
    repo.add_row(table_name, values)
    repo.InsertExample()
        