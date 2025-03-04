import mysql.connector
from datetime import datetime

class HOTEL:

    class DATABASE:

        def __int__(self,database,cursor):
            self.database=database
            self.cursor=cursor

        def Connect(self):
            self.database = mysql.connector.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "badasht1234"
            )
            print("Connected")
        
        def create(self):
            
            cursor=self.database.cursor()

            try:
                cursor.execute("CREATE DATABASE 2000_hotel")
            except:
                print("database '2000_hotel' already exists")
            cursor.execute("USE 2000_hotel")
            reservation=""" CREATE TABLE reservation (
                                room_number INT,
                                bed_number INT,
                                tedad_nafarat INT,
                                name varchar(50),
                                kod_meli VARCHAR(10),
                                available TINYINT(1),
                                taahol BOOL,
                                zaman_v DATETIME,
                                zaman_kh DATETIME,
                                spend_time VARCHAR(100),
                                reason VARCHAR(200)
                                )"""
            parking=""" CREATE TABLE parking (
                        shomare_jaygah INT,
                        pelak VARCHAR(7),
                        number VARCHAR(11),
                        available TINYINT(1),
                        saat_v DATETIME,
                        saat_kh DATETIME,
                        spend_time VARCHAR(100)
                        )"""
            store =""" CREATE TABLE store (
                        nam_kala VARCHAR(50) NOT NULL ,
                        price INT (20) ,
                        stock INT (20) ,
                        store VARCHAR(50)
                        )"""
            clinic =""" CREATE TABLE clinic (
                        shomare_nobat INT,
                        name VARCHAR(50),
                        kod_meli VARCHAR(10),
                        available TINYINT(1),
                        saat FLOAT(50),
                        doctor VARCHAR(200)
                        )"""
            accounting=""" CREATE TABLE accounting (
                        day VARCHAR(200),
                        reservation_profit BIGINT,
                        reservation_payment BIGINT,
                        restaurant_profit BIGINT,
                        restaurant_payment BIGINT,
                        parking_payment BIGINT,
                        store_profit BIGINT,
                        store_payment BIGINT,
                        clinic_payment BIGINT,
                        staff_payment BIGINT,
                        etc_profit BIGINT,
                        etc_payment BIGINT,
                        total BIGINT
                        )"""
            staff="""CREATE TABLE staff (                        
                        name VARCHAR(100),
                        kod_meli VARCHAR(50),
                        number VARCHAR(50),
                        salary BIGINT,
                        total_salary BIGINT,
                        saat_kari VARCHAR(100),
                        section VARCHAR(100),
                        title VARCHAR(100),
                        credit_card VARCHAR(50)
                        )"""
            storage="""CREATE TABLE storage (                        
                        shomarande INT AUTO_INCREMENT primary key,
                        code VARCHAR(50),
                        name_mahsool VARCHAR(100),
                        section VARCHAR(50),
                        price BIGINT,
                        total_price BIGINT,
                        amount INT(20)
                        )"""
            try:
                cursor.execute(reservation)
            except:
                print("table reservation already exist")
            try:
                cursor.execute(parking)
            except:
                print("table parking already exist")
            try:
                cursor.execute(store)
            except:
                print("table store already exist")
            try:
                cursor.execute(clinic)
            except:
                print("table clinic already exist")
            try:
                cursor.execute(accounting)
            except:
                print("table accounting already exist")
            try:
                cursor.execute(staff)
            except:
                print("table staff already exist")
            try:
                cursor.execute(storage)
            except:
                print("table storage already exist")

            print("DATABASE SUCCEFULLY CREATED")
                
        def fill(self):
            cursor=self.database.cursor()
            cursor.execute("USE 2000_hotel")
            #reservation#############################################
            reservation="INSERT INTO reservation (room_number) VALUES ( %s )"
            o = 0
            for i in range (100):
                o +=1
                val = [(o,)]
                cursor.executemany ( reservation,val )
                self.database.commit()
            
            o = 0
            for i in range (100):
                o +=1
                val = [(o,)]
                cursor.execute (f"update reservation set available=0 where room_number={o}")
                self.database.commit()

            o=0
            for i in range (30):
                o +=1
                val = [(o,)]
                cursor.execute (f"update reservation set bed_number=1 where room_number={o}")
                self.database.commit()

            o=30
            for i in range (30):
                o +=1
                val = [(o,)]
                cursor.execute (f"update reservation set bed_number=2 where room_number={o}")
                self.database.commit()
            
            o=60
            for i in range (30):
                o +=1
                val = [(o,)]
                cursor.execute (f"update reservation set bed_number=3 where room_number={o}")
                self.database.commit()

            o=90
            for i in range (10):
                o +=1
                val = [(o,)]
                cursor.execute (f"update reservation set bed_number=6 where room_number={o}")
                self.database.commit()

            #parking#############################################
            parking="INSERT INTO parking (shomare_jaygah) VALUES ( %s )"
            o = 0
            for i in range (100):
                o +=1
                val = [(o,)]
                cursor.executemany ( parking,val )
                self.database.commit()

            o = 0
            for i in range (100):
                o +=1
                val = [(o,)]
                cursor.execute (f"update parking set available=0 where shomare_jaygah={o}")
                self.database.commit()
            #store#############################################
            store="INSERT INTO store ( nam_kala , price , stock , store) VALUES ( %s, %s, %s, %s)"
            val_store = [ 
            ("soda" , "12000" , "110" , "supermarket"),
            ("chips" , "15000" , "100" , "supermarket"),
            ("pop corn" , "10000" , "50" , "supermarket"),
            ("jelly" , "6000" , "200"  ,"supermarket"),
            ("ice cream" , "8000" , "150" , "supermarket"),
            ("sarmakhordegi bozorghsalan(sb)" , "12000" , "110" , "pharmacy"),
            ("estaminiphone" , "15000" , "100" , "pharmacy"),
            ("cherk khosk kon" , "10000" , "50" , "pharmacy")
            ]

            cursor.executemany ( store,val_store ) 
            self.database.commit()
            print(f" {cursor.rowcount} was inserted ")
            #clinic#############################################
            clinic="INSERT INTO clinic (shomare_nobat) VALUES ( %s )"
            o = 0
            for i in range (48):
                o +=1
                val = [(o,)]
                cursor.executemany ( clinic,val )
                self.database.commit()

            o = 0
            i = 0
            for j in range (48):
                o +=1
                i +=0.5
                cursor.execute (f"update clinic set saat={i} where shomare_nobat={o}")
                self.database.commit()

            o= 0
            for i in range (24):
                o +=1
                cursor.execute (f"update clinic set doctor='Elahi' where shomare_nobat={o}")
                self.database.commit()

            o= 24
            for i in range (24):
                o +=1
                cursor.execute (f"update clinic set doctor='Panahi' where shomare_nobat={o}")
                self.database.commit()    

            o= 0
            for i in range (48):
                o +=1
                cursor.execute (f"update clinic set available=0 where shomare_nobat={o}")
                self.database.commit()
            print("DATABASE SUCCESSFULLY UPDATED")

    class RESERVATION:
        def __int__(self,database,cursor):
            self.database=database
            self.cursor=cursor

        def Connect(self):
            self.database = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "badasht1234"
            )
            print("Connected")

        def reserve(self):
            while True:
                valid=["1","2","3","4"]
                cursor=self.database.cursor()
                cursor.execute("USE 2000_hotel")
                print('be bakhsh reserve othagh khosh amamdid')

                chand_nafareh=str(input("othagh chand nafare bashe?\n1.tak nafareh 2.do nafareh 3.se nafareh 4.6 nafareh(vip) 5.khorooj\n----> "))
                
                if chand_nafareh=="5":
                    print("be salamat")
                    break
                
                elif chand_nafareh in valid:
                    if chand_nafareh=="4":
                        chand_nafareh="6"
                    cursor.execute(f"select room_number from reservation where available=0 and bed_number={chand_nafareh}")

                    myresult = cursor.fetchall()
                    which_room=str(input(f"otagh haye kali {chand_nafareh} nafareh\n{myresult}\nkodam otagh ra mikhahid?(shomare an ra type konid)\n---->  "))
                    
                    name=str(input("nam shoma:  "))
                    cursor.execute (f"update reservation set name='{name}' where room_number={which_room}")
                    while True:
                        kod_meli=input("kod meli shoma:  ")
                        if len(kod_meli)==10:
                            cursor.execute(f"update reservation set kod_meli='{kod_meli}' where room_number={which_room} and available=0")
                            enter=input("zaman:  ")
                            cursor.execute(f"update reservation set zaman_v='{enter}' where room_number={which_room} and available=0")
                            reason=str(input("elat mosaferat:  "))
                            cursor.execute(f"update reservation set reason='{reason}' where room_number={which_room} and available=0")
                            if chand_nafareh=="2" or "3" or "4":
                                married=str(input("vasiat taahol(1---moteahel  2---mojarad)\n:  "))
                                if married=="1":
                                    married=1
                                if married=="2":
                                    married=0
                                cursor.execute(f"update reservation set taahol='{married}' where room_number={which_room} and available=0")
                                cursor.execute(f"update reservation set available=1 where room_number={which_room}")
                            self.database.commit()
                            print("ROOM SUCCESSFULLY RESERVED")
                            break
                        else:
                            q1=input("kod meli ehtebah ast(talash mojada--->y  khorooj az reserve--->n ) ").lower
                            if q1=="n":
                                break

                else:
                    print("INVALID CHOICE")
                q=str(input("otagh digari reserve konim? y/n :   ")).lower()
                if q=="n":
                    print("be salamat")
                    break

        def rendition(self):
            days_list=[]
            valid_kod=[]
            cursor=self.database.cursor()
            cursor.execute("USE 2000_hotel")
            print('be bakhsh tahvil othagh khosh amamdid')
            while True:

                while True:
                    
                    kod_meli=str(input("kod meli shoma:  "))
                    cursor.execute(f"select kod_meli from reservation where available=1")
                    myresult1=cursor.fetchall()
                    o=-1
                    for i in myresult1:
                        o+=1
                        myresult2=myresult1[o]
                        (myresult3,)=myresult2
                        valid_kod.append(myresult3)

                    if len(kod_meli)==10 and kod_meli in valid_kod:
                            
                        cursor.execute(f"select bed_number from reservation where kod_meli={kod_meli}")
                        multi = cursor.fetchall()
                        myroom1=multi
                        myroom2=myroom1[0]
                        (myroom3,)=myroom2

                    
                        cursor.execute(f"select room_number from reservation where kod_meli={kod_meli} and available=1")
                        myresult = cursor.fetchall()
                        w_room=input(f"kodam otagh ra tahvil midahid?\n{myresult}\n--> ")
                        try:
                            ex_date=datetime.now()

                            cursor.execute (f"update reservation set available=0 where kod_meli={kod_meli} and room_number={w_room}")
                            cursor.execute(f"select zaman_v from reservation where kod_meli={kod_meli} and room_number={w_room}")

                            myresult = cursor.fetchall()
                            myresult1=myresult
                            myresult2=myresult1[0]
                            (myresult3,)=myresult2
                            en_year=(myresult3.year)
                            en_month=(myresult3.month)
                            en_day=(myresult3.day)
                            en_hour=(myresult3.hour)
                            en_minute=(myresult3.minute)
                            en_second=(myresult3.second)

                            en_date_big=f"{en_year}/{en_month}/{en_day}"
                            en_date_small=f"{en_hour}:{en_minute}:{en_second}"

                            ex_year=(ex_date.year)
                            ex_month=(ex_date.month)
                            ex_day=(ex_date.day)
                            ex_hour=(ex_date.hour)
                            ex_minute=(ex_date.minute)
                            ex_second=(ex_date.second)

                            ex_date_big=f"{ex_year}/{ex_month}/{ex_day}"
                            ex_date_small=f"{ex_hour}:{ex_minute}:{ex_second}"

                            d1_big = datetime.strptime(en_date_big, "%Y/%m/%d")
                            d2_big = datetime.strptime(ex_date_big, "%Y/%m/%d")

                            delta_big = (d2_big - d1_big)

                            d1_small = datetime.strptime(en_date_small, "%H:%M:%S")
                            d2_small = datetime.strptime(ex_date_small, "%H:%M:%S")

                            delta_small= (d2_small - d1_small)

                            print(f'zaman eghamat:{delta_big.days} days and {delta_small} hours')
                            if  delta_big.days>=0:
                                delta=1
                            else:
                                delta=delta_big.days
                            payment=delta*int(myroom3)*1000000

                            cursor.execute(f"select day from accounting")
                            myresult1=cursor.fetchall()
                            o=-1
                            for i in myresult1:
                                o+=1
                                myresult2=myresult1[o]
                                (myresult3,)=myresult2
                                days_list.append(myresult3)

                            if ex_date_big not in days_list:
                                sql="INSERT INTO accounting (day) VALUES ( %s )"
                                val=[[(ex_date_big),]]
                                cursor.executemany ( sql,val )
                                self.database.commit()
                            
                            cursor.execute (f"select reservation_profit from accounting where day='{ex_date_big}'")
                            myresult = cursor.fetchall()

                            try:
                                myresult1=myresult
                                myresult2=myresult1[0]
                                (myresult3,)=myresult2
                                payment_t=payment+int(myresult3)
                                print(f'kol : {payment_t:,} Toman')
                                cursor.execute (f"update accounting set reservation_profit={payment_t} where day='{ex_date_big}'")
                                self.database.commit()
                            except:
                                cursor.execute (f"update accounting set reservation_profit={payment} where day='{ex_date_big}'")
                                self.database.commit()
                                print(f'kol : {payment:,} Toman')


                            break
                                
                        except:
                            q1=input("shomare otagh eshtebah ast(talash mojadad--->y  khorooj az reserve--->n ) ").lower
                            if q1=="n":
                                break                                
                    else:
                        q1=input("otaghi ba in kod meli reserve nashode ast(talash mojada--->y  khorooj az reserve--->n ) ").lower
                        if q1=="n":
                            break
                            
                self.database.commit()
                print("ROOM SUCCESSFULLY RENDIATED")

                q=str(input("otagh digari tahvil bedahim? y/n :   ")).lower()
                if q=="n":
                    print("be salamat")
                    break

    class RESTAURANT:
        def __int__(self,database,cursor):
            self.database=database
            self.cursor=cursor

        def Connect(self):
            self.database = mysql.connector.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "badasht1234",
                database = "2000_hotel"
            )
            print("Connected")

        def __init__(self,tedad=[0,0,0,0,0,0,0,0,0,0,0,0,0],sefaresh=[],list_a5ll=["0.peperooni","1.makhloot","2.ghorme_sabzi","3.morgh_spicy","4.panj_tikeh","5.sokhari_sadeh","6.kalam","7.shirazi","8.fasl","9.abjo eslami","10.cola","11.dogh","12.ab"]
        ,payment=0,ch=[0,1,2,3,4,5,6,7,8,9,10,11,12],ch1=['0','1','2','3','4','5','6','7','8','9','10','11','12']):
            
            self.tedad=[0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.sefaresh=[]
            self.list_all=["0.peperooni","1.makhloot","2.ghorme_sabzi","3.morgh_spicy","4.panj_tikeh","5.sokhari_sadeh","6.kalam","7.shirazi","8.fasl","9.abjo eslami","10.cola","11.dogh","12.ab"]
            self.payment=payment
            self.ch=[0,1,2,3,4,5,6,7,8,9,10,11,12]
            self.ch1=['0','1','2','3','4','5','6','7','8','9','10','11','12']

        def sefareshgir_add(self):
            
            dictall={'0.pizza peperooni':85000,'1.pizza makhloot':75000,'2.pizza ghorme sabzi':129000,'3.morgh spicy':700000,'4.morgh panj tikeh':625000,'5.morgh sokhari sadeh':46700,'6.salad kalam':25000,'7.salad shirazi':32000,'8.salad fasl':15000,'9.abjo eslami': 78000,'10.cola':104000,'11.dogh':17000,'12.ab':5000,13:'chizi nemikham'}

            print("\033[1;31;40mWelcome to ultimate resturant")

            for x, y in dictall.items():
                print(x, y)
            hame =str(input('\033[36mchi meil darid? '))
            if hame in self.ch1:
                hame1=int(hame)
                ezafi=str(input("chand adad?:  "))

                if ezafi.isdigit() ==True:
                    ezafi_int=int(ezafi)
                    ezafi_n=self.list_all[hame1]
                    
                    if ezafi_n not in self.sefaresh:
                        self.sefaresh.append(ezafi_n)
                    ezafi2=self.tedad[hame1]
                    ezafi3=ezafi2+ezafi_int
                    self.tedad[hame1]=ezafi3
                    print("ADDED")
                else:
                    print("PLEASE TYPE a VALID NUMBER")
        
        def sefareshgir_remove(self):

            if len(self.sefaresh)==0:
                print("YOU HAVE NOT ORDERED ANYTHING")

            else:
                for i in self.sefaresh:
                    print(f"___{i}___")

                q1=input("shomare chizi ra ke mikhahid hazf kond ra type konid(type 13 to cancel):  ")
                if q1.isdigit()==True and q1 in self.ch1:

                    q=int(q1)
                    name=self.list_all[q]
                    hazfi2=self.tedad[q]

                    if q in self.ch and hazfi2>0: 

                        q3=input(f"self.tedad : {hazfi2} \nchandta mikhahi hazf konid?:  ")
                        if q3.isdigit() == True:
                            q2=int(q3)
                            hazfi3=hazfi2-q2
                            if hazfi3<0:
                                hazfi3=0
                            self.tedad.pop(q)
                            self.tedad.insert(q,hazfi3)
                            if hazfi3<=0:
                                self.sefaresh.remove(name)
                            print("REMOVED")

                        else:
                            print("PLEASE TYPE a VALID NUMBER")
                else:
                    print("PLEASE TYPE a VALID NUMBER")
            
        def show_factor(self):

            print('______________________sefareshat shoma_______________________')
            if self.tedad[0]>0:
                print(f'    {self.tedad[0]}____________peperooni_____________{self.tedad[0]*850000:,} toman')
            if self.tedad[1]>0:
                print(f'    {self.tedad[1]}_____________makhloot______________{self.tedad[1]*75000:,} toman')
            if self.tedad[2]>0:
                print(f'    {self.tedad[2]}___________ghorme_sabzi___________{self.tedad[2]*129000:,} toman')    
            if self.tedad[3]>0:
                print(f'    {self.tedad[3]}_______________spicy______________{self.tedad[3]*700000:,} toman')
            if self.tedad[4]>0:
                print(f'    {self.tedad[4]}____________panj_tikeh____________{self.tedad[4]*625000:,} toman')
            if self.tedad[5]>0:
                print(f'    {self.tedad[5]}___________sokhari_sadeh___________{self.tedad[5]*46700:,} toman')
            if self.tedad[6]>0:
                print(f'    {self.tedad[6]}_________________kalam_____________{self.tedad[6]*25000:,} toman')
            if self.tedad[7]>0:
                print(f'    {self.tedad[7]}_______________shirazi_____________{self.tedad[7]*32000:,} toman')
            if self.tedad[8]>0:
                print(f'    {self.tedad[8]}________________fasl_______________{self.tedad[8]*15000:,} toman')
            if self.tedad[9]>0:
                print(f'    {self.tedad[9]}___________abjo_eslami____________{self.tedad[9]*129000:,} toman')
            if self.tedad[10]>0:
                print(f'    {self.tedad[10]}_____________cola_______________{self.tedad[10]*104000:,} toman')
            if self.tedad[11]>0:
                print(f'    {self.tedad[11]}_____________dogh_______________{self.tedad[11]*17000:,} toman')
            if self.tedad[12]>0:
                print(f'    {self.tedad[12]}______________ab_________________{self.tedad[12]*5000:,} toman')
            print('________________________________________________________________')
        
        def factor(self):
            days_list=[]
            cursor=self.database.cursor()
            ex_date=datetime.now()

            self.payment=self.tedad[0]*850000+self.tedad[1]*75000+self.tedad[2]*129000+self.tedad[3]*700000+self.tedad[4]*625000+self.tedad[5]*46700+self.tedad[6]*25000+self.tedad[7]*32000+self.tedad[8]*15000+self.tedad[9]*129000+self.tedad[10]*104000+self.tedad[11]*17000+self.tedad[12]*5000
            print(f"TOTAL PRICE :  {self.payment:,} TOMAN")
            
            ex_date=datetime.now()

            ex_year=(ex_date.year)
            ex_month=(ex_date.month)
            ex_day=(ex_date.day)

            ex_date_big=f"{ex_year}/{ex_month}/{ex_day}"

            cursor.execute(f"select day from accounting")
            myresult1=cursor.fetchall()
            o=-1
            for i in myresult1:
                o+=1
                myresult2=myresult1[o]
                (myresult3,)=myresult2
                days_list.append(myresult3)

            if ex_date_big not in days_list:
                sql="INSERT INTO accounting (day) VALUES ( %s )"
                val=[[(ex_date_big),]]
                cursor.executemany ( sql,val )
                self.database.commit()
            
            cursor.execute (f"select restaurant_profit from accounting where day='{ex_date_big}'")
            myresult = cursor.fetchall()

            try:
                myresult1=myresult
                myresult2=myresult1[0]
                (myresult3,)=myresult2
                payment_t=self.payment+int(myresult3)

                cursor.execute (f"update accounting set restaurant_profit={payment_t} where day='{ex_date_big}'")
                self.database.commit()
            except:
                cursor.execute (f"update accounting set restaurant_profit={self.payment} where day='{ex_date_big}'")
                self.database.commit()

    class PARKING:
        def __int__(self,database,cursor):
            self.database=database
            self.cursor=cursor

        def Connect(self):
            self.database = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "badasht1234"
            )
            print("Connected")        

        def enter(self):
            print("PARKING HOTEL 2000\nENTER")
            while True:
                cursor=self.database.cursor()
                cursor.execute("USE 2000_hotel")
                cursor.execute("SELECT shomare_jaygah FROM parking where available=0")
                myresult=cursor.fetchall()
                for i in myresult:
                    print(i)
                try:
                    slot=int(input("jaygah mored nazar: "))
                    pelak=input("pelak: ")

                    list_pelak=[]

                    cursor=self.database.cursor()
                    cursor.execute(f"select pelak from parking where available=1")
                    myresult = cursor.fetchall()

                    o=-1
                    for i in myresult:
                        o+=1
                        myresult2=myresult[o]
                        (myresult3,)=myresult2
                        list_pelak.append(myresult3)

                    if pelak not in list_pelak:
                        cursor.execute (f"update parking set pelak='{pelak}' where shomare_jaygah={slot} and available=0")
                        while True:
                            number=input("phone number: ")
                            if len(number)==10:
                                cursor.execute (f"update parking set number={number} where shomare_jaygah={slot} and available=0")
                                date=input("zaman vorood: ")
                                cursor.execute (f"update parking set saat_v='{date}' where shomare_jaygah={slot} and available=0")
                                cursor.execute (f"update parking set available=1 where shomare_jaygah={slot}")
                                self.database.commit()
                                print("JAYGAH GEREFTEH SHOD ✔")
                                break
                            else:
                                q=input("INVALID PHONE NUMBER\n try again? y/n : ").lower()
                                if q=="n":
                                    break
                    else:
                        print("PELAK ALREADY EXISTS")
                except:
                    q=input("ERROR\n try again? y/n : ").lower()
                    if q=="n":
                        break
                q=input("Enter another car? y/n : ").lower()
                if q=="y":
                    continue
                else:
                    break


        def exit(self):
            print("PARKING HOTEL 2000\nEXIT")
            while True:
                cursor=self.database.cursor()
                cursor.execute("USE 2000_HOTEL")
                
                while True:
                    try:
                        pelak=input("pelak: ")
                        en_date=cursor.execute(f"SELECT saat_v FROM parking where available=1 and pelak='{pelak}'")
                        en_date = cursor.fetchall()
                        myresult1=en_date
                        myresult2=myresult1[0]
                        (myresult3,)=myresult2
                        ex_date=input("zaman khorroj: ")
                        #payment=myresult3-ex_date
                        #print(f"FACTOR:{payment} TOMAN")
                        cursor.execute (f"update parking set available=0 where pelak='{pelak}'")
                        self.database.commit()
                        print("CAR SUCCESSFULLY REMOVED ✔")
                        break
                    except:
                        q=input("ERROR\n try again? y/n : ").lower()
                        if q=="n":
                            break
                q=input("Remove another car? y/n : ").lower()
                if q=="y":
                    continue
                else:
                    break

    class STORE:
        def shopping(self):
            print("be forroshgah hotel 2000 kosh amadid")
            #auto connect
            database = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "badasht1234",
            )
            cursor=database.cursor()
            total=0
            order=[]
            number=[]
            price_order=[]

            cursor.execute(f"USE 2000_hotel")

            while True:
                store=str(input("ba kodam bakhsh kar darid?\n1.supermarket 2.pharmacy : "))

                if store=="1" or store=="2":

                    if store=="1":
                        store="supermarket"
                    elif store=="2":
                        store="pharmacy"

                    nam_kala=[]
                    price=[]
                    stock=[]

                    cursor=database.cursor()
                    cursor.execute(f"select nam_kala from store where store='{store}'")
                    myresult = cursor.fetchall()

                    o=-1
                    for i in myresult:
                        o+=1
                        myresult2=myresult[o]
                        (myresult3,)=myresult2
                        nam_kala.append(myresult3)

                    cursor.execute(f"select price from store where store='{store}'")
                    myresult = cursor.fetchall()

                    o=-1
                    for i in myresult:
                        o+=1
                        myresult2=myresult[o]
                        (myresult3,)=myresult2
                        price.append(myresult3)

                    cursor.execute(f"select stock from store where store='{store}'")
                    myresult = cursor.fetchall()

                    o=-1
                    for i in myresult:
                        o+=1
                        myresult2=myresult[o]
                        (myresult3,)=myresult2
                        stock.append(myresult3)

                    o=-1
                    for i in range(len(nam_kala)):
                        o+=1
                        print(f"{o}.nam kala:{nam_kala[o]} _____________ price:{price[o]} _____________ stock:{stock[o]}")
                    #input

                    order_ask=int(input("shomare kala mored nazar ra type konid: "))

                    order_name=nam_kala[order_ask]
                    order_price=price[order_ask]
                    order_stock=stock[order_ask]

                    tedad=int(input("chand adad: "))

                    #stock
                    snew=order_stock-tedad
                    if snew>=0:
                        pay=tedad*order_price
                        total+=pay

                        if order_name not in order:
                            order.append(order_name)
                            number.append(tedad)
                            price_order.append(order_price)
                        else:
                            ind_1=order.index(order_name)
                            number_exe=number[ind_1]
                            number_exe1=number_exe+tedad
                            number.insert(ind_1,number_exe1)
                        cursor.execute(f"UPDATE store SET stock={snew} WHERE nam_kala='{order_name}'")
                        database.commit()

                        #factor
                        o=-1
                        print("factor shoma")
                        for i in order:
                            o+=1
                            print(f"{order[o]}----------{number[o]} adad---------- {number[o]*price_order[o]:,} toman")
                        print(f"TOATAL--- {total:,} TOMAN")
                        days_list=[]
                        cursor=database.cursor()

                        ex_date=datetime.now()

                        ex_year=(ex_date.year)
                        ex_month=(ex_date.month)
                        ex_day=(ex_date.day)

                        ex_date_big=f"{ex_year}/{ex_month}/{ex_day}"

                        cursor.execute(f"select day from accounting")
                        myresult1=cursor.fetchall()
                        o=-1
                        for i in myresult1:
                            o+=1
                            myresult2=myresult1[o]
                            (myresult3,)=myresult2
                            days_list.append(myresult3)

                        if ex_date_big not in days_list:
                            sql="INSERT INTO accounting (day) VALUES ( %s )"
                            val=[[(ex_date_big),]]
                            cursor.executemany ( sql,val )
                            database.commit()
                        
                        cursor.execute (f"select store_profit from accounting where day='{ex_date_big}'")
                        myresult = cursor.fetchall()

                        try:
                            myresult1=myresult
                            myresult2=myresult1[0]
                            (myresult3,)=myresult2
                            payment_t=total+int(myresult3)
                            cursor.execute (f"update accounting set store_profit={payment_t} where day='{ex_date_big}'")
                            database.commit()
                        except:
                            cursor.execute (f"update accounting set store_profit={total} where day='{ex_date_big}'")
                            database.commit()
                    else:
                        print("dar anbar kafi nist")

                else:
                    print("INVALID INPUT")
                q=str(input("PRESS Q TO FINISH OR ANYTHING ELSE TO CONTINUE : ")).lower()
                if q=="q":
                    break
            print("be salamat")

    class CLINIC:
        def __init__(self,name="",kodmeli="",doctor="",nobat=""):
            self.name=name
            self.kodmeli=kodmeli
            self.doctor=doctor
            self.nobat=nobat
        
        def show(self):
            if self.name=="":
                print("nobati reserv nashod")
            else:
                print(f"agha/khanom {self.name} ba khod meli {self.kodmeli} shoma dar saat {self.nobat} ba doctor {self.doctor} gharar visit darid")
        
        def booking(self):
            database = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "badasht1234",
            database="2000_hotel"
            )

            list_nobat=[]
            list_saat=[]
            list_doctor=[]
            list_kodmeli=[]

            cursor=database.cursor()
            cursor.execute(f"select shomare_nobat from clinic where available=0")
            myresult = cursor.fetchall()

            o=-1
            for i in myresult:
                o+=1
                myresult2=myresult[o]
                (myresult3,)=myresult2
                list_nobat.append(myresult3)

            cursor.execute(f"select saat from clinic where available=0")
            myresult = cursor.fetchall()

            o=-1
            for i in myresult:
                o+=1
                myresult2=myresult[o]
                (myresult3,)=myresult2
                list_saat.append(myresult3)

            cursor.execute(f"select doctor from clinic where available=0")
            myresult = cursor.fetchall()

            o=-1
            for i in myresult:
                o+=1
                myresult2=myresult[o]
                (myresult3,)=myresult2
                list_doctor.append(myresult3)

            cursor.execute(f"select kod_meli from clinic where available=1")
            myresult = cursor.fetchall()

            o=-1
            for i in myresult:
                o+=1
                myresult2=myresult[o]
                (myresult3,)=myresult2
                list_kodmeli.append(myresult3)
        
            o=-1
            for i in range(len(list_nobat)):
                o+=1
                print(f"shomare nobat:{list_nobat[o]} _____________ saat:{list_saat[o]} _____________ doctor:{list_doctor[o]}")
            q_s=input("shomare nobat mored nazar ra type konid: ")
            if q_s.isdigit()==True:
                q=int(q_s)
                if q in list_nobat:
                    
                    while True:
                        
                        self.kodmeli=str(input("kod meli: "))

                        if self.kodmeli.isdigit():
                        
                            if len(self.kodmeli)==10:

                                if self.kodmeli not in list_kodmeli:
                                    self.name=input("nam va nam khanevadegi: ")

                                    cursor.execute (f"update clinic set name='{self.name}' where shomare_nobat={q}")
                                    cursor.execute (f"update clinic set kod_meli='{self.kodmeli}' where shomare_nobat={q}")
                                    cursor.execute (f"update clinic set available=1 where shomare_nobat={q}")
                                    database.commit()

                                    cursor.execute(f"select saat from clinic where shomare_nobat={q}")
                                    myresult_all = cursor.fetchall()
                                    myresult1=myresult_all
                                    myresult2=myresult1[0]
                                    (myresult3,)=myresult2
                                    self.nobat=myresult3
                                    
                                    cursor.execute(f"select doctor from clinic where shomare_nobat={q}")
                                    myresult = cursor.fetchall()
                                    myresult1=myresult
                                    myresult2=myresult1[0]
                                    (myresult3,)=myresult2
                                    self.doctor=myresult3
                                    print("DONE!")
                                    break
                                else:
                                    q1=input("SHOMA AZ GHABL NOBAT GEREFTEID\nTry again? Y/N : ").lower()
                                    if q1=="y":
                                        continue
                                    else:
                                        break
                            else:
                                q1=input("INVALID CODE\nTry again? Y/N : ").lower()
                                if q1=="y":
                                    continue
                                else:
                                    break
                        else:
                            q1=input("INVALID CODE\nTry again? Y/N : ").lower()
                        if q1=="y":
                                continue
                        else:
                                break
                else:
                    print("INVALID")
            else:
                print("INVALID")

    class ACCOUNTING:
        pass

run=HOTEL.DATABASE()
run.Connect()
run.create()
run.fill()