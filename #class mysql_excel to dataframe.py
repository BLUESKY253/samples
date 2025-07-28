#class mysql_excel to dataframe 
import mysql.connector
import pandas as pd
import openpyxl

class DATABASE:

    def __int__(self,database,cursor):
        self.database=database
        self.cursor=cursor

    def mysql_to_df(self):
        #database=mysql.connector.connect(host ='localhost', user='root', password='badasht1234',database='2000_library')
        database=mysql.connector.connect(host =str(input("Host : ")), user=str(input("Username : ")), password=str(input("Password : ")),database=str(input("database : ")))

        cursor = database.cursor()

        table=str(input(f"table: "))

        query = f"SELECT * FROM {table}"
        cursor.execute(query)

        column_names = cursor.column_names

        column_names_list = list(column_names)

        myresult = cursor.fetchall()

        df = pd.DataFrame(myresult, columns=column_names_list)

        cursor.close()

        index = str(input("if you want to vhange the index column enter sselected column name(if not just click 'enter'): "))
        try:
            df.set_index(index, inplace=True)
        except:
            pass

        print(df)

    def excel_to_df(self):
        #'C:\\Users\\PC\\Desktop\\FSI-2023-DOWNLOAD.xlsx'
        #Sheet1 

        excel_file_path = str(input("File location: "))
        sheet_name = str(input("Sheet name: ")) 

        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        
        index = str(input("if you want to vhange the index column enter sselected column name(if not just click 'enter'): "))
        try:
            df.set_index(index, inplace=True)
        except:
            pass
        
        print(df)

    def create_mysql(self):

        #database=mysql.connector.connect(host ='localhost', user='root', password='badasht1234',database='2000_library')
        database=mysql.connector.connect(host =str(input("Host : ")), user=str(input("Username : ")), password=str(input("Password : ")),database=str(input("database : ")))
        cursor=database.cursor()

        try:
            cursor.execute("CREATE DATABASE 2000_library")
        except:
            print("database '2000_library' already exists")
        cursor.execute("USE 2000_library")
        books=""" CREATE TABLE books (
                    shomarande INT AUTO_INCREMENT primary key,
                    name varchar(200),
                    author VARCHAR(200),
                    genre VARCHAR(200),
                    date VARCHAR(200),
                    amount INT 
                    )"""

        try:
            cursor.execute(books)
        except:
            print("table books already exist")

        print("DATABASE SUCCEFULLY CREATED")

        cursor=database.cursor()
        cursor.execute("USE 2000_library")

        books="INSERT INTO books (name , author , genre , available , date , amount) VALUES ( %s, %s, %s, %s, %s , %s)"
        val_books = [ 
        ("gone with the wind" , "margaret mitchell" , "historical fiction,romance" , 0 , "1936" , 2),
        ("one hundred years of solitude" , "gabriel garcía marquez" , "magical realisim" , 0 , "1967" , 2),
        ("the lord of the rings" , "j.r.r. tolkien" , "fantasy,adventure" , 0 , "1954" , 3),
        ("moby dick" , "herman melville" , "adventure,epic"  , 0 , "1851" , 1),
        ("frankenstein" , "mary shelley" , "horror" , 0 , "1818" , 2),
        ("david copperfield" , "charles dickens" , "novel" , 0 , "1850" , 1),
        ("shahname" , "ferdosi" , "poetry" , 0 , "1832" , 4),
        ("the divan of hafez" , "hafez" , "poetry" , 0 , "1850" , 3),
        ("raz haye faza" , "scientist" , "scientific" , 0 , "2020" , 2),
        ("zaban badan" , "psychologist" , "scientific" , 0 , "2010" , 5)
        ]

        cursor.executemany ( books,val_books ) 
        database.commit()
        print(f" {cursor.rowcount} was inserted ")

run=DATABASE()

while True:
    q="y"
    while q=="y":
        ask=str(input("\n📚 Dataframe 📚\n1.create mysql database 2.mysql to dataframe 3.excel to dataframe 4.Exit :  "))

        if ask=="1":

            run.create_mysql()

        if ask=="2":

            run.mysql_to_df()

        if ask=="3":

            run.excel_to_df()

        if ask=="4":
            break

        else:
            continue  

    q2=input("\nType 'q' to exit or anything else to continue: ").lower()

    if q2=="q":
        break

print("\nGoodbye")