import mysql.connector
import requests
from bs4 import BeautifulSoup
import time

code = 0

while(True):
    code+=1

    # column name

    url = "https://www.tgju.org/profile/price_dollar_rl/history"
    response = requests.get(url)
    content = BeautifulSoup(response.text,'html.parser')
    result= content.find(class_= "text-center").text
    all = result.split()

    column_name = []
    for i in range(14):
        column_name.append(all[i])
    column_name.remove('/')
    column_name.remove('/')
    column_name.remove('تاریخ')
    column_name.remove('تاریخ')
    column_name.remove('تغییر')
    column_name.remove('تغییر')


    #mysql create columns

    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='badasht1234',
    )

    cursor = database.cursor()

    try:
        cursor.execute(f"CREATE DATABASE money_2000")
    except:
        print("database already exists")

    cursor.execute("USE money_2000")

    try:
        table=""" CREATE TABLE dollar (
                            ID_dollar INT
        )"""
        cursor.execute(table)
    except:
        print("table already exists")
        

    for i in column_name:
        try:
            cursor.execute(f"ALTER TABLE dollar ADD COLUMN {i} VARCHAR(50)")
        except:
            pass

    print("Done")

    database.commit()

    cursor.execute("USE money_2000")


    #get data

    response = requests.get(url)
    content = BeautifulSoup(response.text,'html.parser')
    result= content.find(id= "table-list").text
    money_list = result.split()


    #already exists

    datalist = []
    alredy_exist=[]


    cursor.execute(f"select شمسی from dollar")
    myresult = cursor.fetchall()

    o=-1
    for i in myresult:
        o+=1
        myresult2=myresult[o]
        (myresult3,)=myresult2
        alredy_exist.append(myresult3)

    for i in alredy_exist:
        if i in money_list:
            index1 = money_list.index(i)+1
            index2= index1-8
            del money_list[index2:index1]



    #list to multiple tuples

    data = []
    count = len(money_list)/8
    count = int(count)
    o=0
    s=8
    for i in range(count):
        list_to_tuple = tuple(money_list[o:s]) 
        data.append(list_to_tuple)
        o+=8
        s+=8 


    #inserting data to database

    cursor.execute("USE money_2000")

    x= len(column_name) - 1
    icon = x * '%s,' + '%s'

    column_name_string = ", ".join(column_name)

    add_data=f"INSERT INTO dollar ({column_name_string}) VALUES ({icon})"

    cursor.executemany(add_data,data ) 

    database.commit()
    print(f" {cursor.rowcount} was inserted ")

    print(f"code has runned for {code} times")
    print("==================================================")

    cursor.close()
    time.sleep(3)
    #time should be 86400 