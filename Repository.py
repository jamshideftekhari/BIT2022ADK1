import mysql.connector

class Repository(object):
    Dk1DB = object
    mycursor = object
    RowsList = []
    # to set connection up
    def SetConnection(self):
        #self.Dk1DB = mysql.connector.connect(
        #          host = "jameflex.mysql.database.azure.com",
        #          user = "jamshid",
        #          password = "Eftekhar2003",
        #          database = "dk12021"
        #          )
        self.Dk1DB = mysql.connector.connect(
                  host = "localhost",
                  user = "root",
                  password = "jam2003eft",
                  database = "BIT2022A"
                  )
        self.mycursor = self.Dk1DB.cursor()
    # to print all table elements  
    def GetAll(self):
        print(self.Dk1DB)
        # mycursor = self.Dk1DB.cursor()
        self.mycursor.execute("select * from DK1_Members")
        personResult = self.mycursor.fetchall()
        for x in personResult:
            print(x)

    # to get all table elements as a list
    def GetAllTolist(self):   
        self.mycursor.execute("select * from DK1_Members")
        RowsList = self.mycursor.fetchall()
        return RowsList     

    # add a row to the table.
    def AddRow(self):
        self.mycursor.execute(" insert into DK1_Members (StudId, FName, LName, Age, MemType, FavoritChips) values ('StudId','LName', 'FName', 20, 'MemType', 'Chips Name') ")
        self.Dk1DB.commit()
        print(self.mycursor.rowcount, " record inserted")
