import sqlite3
class Person:
    def __init__(self,id_num=-1, Name="", FName="", Age=-1):
        self.Name=Name
        self.id_num=id_num
        self.FName=FName
        self.Age=Age
        self.conn = sqlite3.connect("person.db")
        # Create a cursor
        self.cursor = self.conn.cursor()
    def __str__(self):
        return f"Name:{self.Name},FatherName:{self.FName},Id:{self.id_num},Age:{self.id_num}"
    def LoadfromDB(self,id_num):
        self.cursor.execute(f"""
        Select * from Person_Table where
        id={id_num}
        """)
        result=self.cursor.fetchone()
        self.id_num=result[0]
        self.Name=result[1]
        self.FName=result[2]
        self.Age=result[3]
    def InsertInDb(self):
        self.cursor.execute(f"""
        Insert into Person_Table values ({self.id_num},'{self.Name}','{self.FName}',{self.Age})
""")
        self.conn.commit()
        self.conn.close()
conn=sqlite3.connect("person.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Person_Table(
id INTEGER PRIMARYKEY,
name TEXT,
fathername TEXT,
age TEXT
)
""")
# Commit changes
conn.commit()

# Close the connection
conn.close()

#p2=Person(2,"Babar","Azam",21)
#p2.InsertInDb()
p1=Person()
p1.LoadfromDB(2)
print(p1)
