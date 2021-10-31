import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='Mysql@12345')
cur=con.cursor()
cur.execute("create database if not exists Health1")
cur.execute("USE Health1")
con.commit()
usd=""

def new_func():
    s= """1. Headache \t 2. Seizures \t 3. Dizziness \n 4. Loss of Vision \t 5. Bleeding \t 6. Paralysis \n 7. Sensitivity of light \t 8. Body pain \t 9. Vomiting"""
    s1="""10. Loose Motion \t 11. Fatigue \t 12. Cough \n 13. Shortness of breath \t 14. Cold sweat \t 15. Indigestion \n 16. Chest Pressure \t 17. Fever \t 18. Chills"""
    s2="""19. Change in skin color \t 20. Itchiness \t 21. Sore throat \n 22. Watery Eyes \t 23. Runny Nose \t 24. Sensitivity to Light \ n 25. Sensitivity to Light"""
    return s,s1,s2

def insertion():
    cur.execute("create table Patient(USERID varchar(20) NOT NULL,NAME varchar(30) NOT NULL,Phone_No varchar(11), PASSWORD varchar(18) NOT NULL ,Location varchar(15),Email_ID varchar(40),Organization_Name varchar(40), date_of_birth varchar(15), Age int(20),Gender varchar(10), city varchar(20)")
    cur.execute("create table Doctor(EMP_ID varchar(20) NOT NULL, NAME varchar(30) NOT NULL,Phone_No varchar(20), PASSWORD varchar(18) NOT NULL, Hospital_name varchar(15),Email_ID varchar(40),Years_of_Exp varchar(3), Gender varchar(6), Age int(20),Date_Of_birth varchar(15), city varchar(20))")
    cur.execute("create table Hospital(NAME_OF_HOSPITAL varchar(20) NAME_OF_PATIENTS varchar(30), ROOM_NO_PAT varchar(4), Admitted_date varchar(15), Beds_Available_covid int(2), Beds_available_other(2) NAME_OF_DOCTOR varchar (15), Doctor_ID varchar (10), type varchar(10))")
    cur.execute("create table Visit(NAME Patient_name varchar(30), Doctor_Name varchar(30), Time varchar(16), Date varchar(15), Hospital_name varchar(15))")
    cur.commit()
Loc=["At Home", "In hospital","Discharged and at home"]
cur.execute("SHOW TABLES")
tables=["Patient", "Doctor", "Hospital1", "Hospital2", "Hospital3", "Visit"]
exist=cur.fetchall()
if len(exist)==0:
    insertion()

dang_dis = ["tuberculosis", "brain hemorrhages", "jaundice", "heart attack"]
common_dis = ["common cold", "viral fever", "allergy", "cough"]
pandemic = ["COVID-19"]
flg=1
while flag!=0:
    def symp_disease():
        L,c,p=[],0,0
        ind,m=0,0
        """//dictionary for disease:symptoms"""
        dict_symptoms = {"COVID-19":("fever","cough","fatigue","sore throat","headache"),"brain haemorrhage":("headache","seizures","dizziness","loss of vision","paralysis","bleeding","sensitivity to light"),"tuberculosis":("body pain","vomiting","fatigue","cough","loose motion"),
        "heart attack":("fatigue","dizziness","shortness of breath","chest pressure","cold sweat","indigestion","body pain"),"jaundice":("fever","chills","change in skin color","itchiness"),"common cold":("itchiness","watery eyes","body pain","runny nose"),"migraine":("sensitivity to light","sensitivity of sound","dizziness","headache")}
    
        print("Please Enter symptoms from following: ")
        print(new_func())
        ch=list(input("Enter here : "))

        for key,values in dict_symptoms.items():
            for i in values:
                if ch in i:
                    c+=1
            p=c//len(i)*100
            L.append(p)
            p=0
        m=max(L)
        for i in range(len(L)):
            if L[i]==m:
                return key
    
    def book_appointment():
        print("Please enter symptoms : ")
        dis = symp_disease()
        print("Closest match to disease is : ", dis)
        if dis in dang_dis:
            ch=input("We suggest booking an immediate appointment. Press (y/n) to continue : ")
            if ch=='n':
                print("Okay. Taking you to home page")
                exit()
            elif ch=='y':
                print("Please wait a moment... Finding doctors near you ")
                cur.execute("SELECT CITY,CITY FROM DOCTORS as d,PATIENTS as p WHERE '{}'=p.USERID AND d.CITY=p.CITY").format(userid)
                L=cur.fetchall()
                print("We found these doctors in your area : ")
                for i in L:
                    print(i, end=" ")
        if dis in common_dis:
            print("You can visit doctors near you. They will prescribe necessary medicines")
            w=input("Do you want us to book an appointment for you?🥺 (y/n)")
            if w=='y':
            print("Please wait a moment... Finding doctors near you ")
            cur.execute("SELECT CITY,CITY FROM DOCTORS as d,PATIENTS as p WHERE '{}'=p.USERID AND d.CITY=p.CITY").format(userid)
            L=cur.fetchall()
            print("We found these doctors in your area : ")
            for i in L:
                print(i, end=" ")
        elif w=='n':
            print("Ok.. taking you back to home page")
            exit()

    def check_bed_availibilty():
        hp=input("Enter hospital : ")
        cur.execute("SELECT NAME FROM HOSPITAL AS h WHERE h.name = hp")
        d=cur.fetchall()
        if hp in d:
            dis=input("Enter disease of patient : ")
            if dis in dang_dis:
                cur.execute("SELECT Beds_availibilty_others from HOSPITAL")
                l=cur.fetchall()
                if l[0]>0:
                    return "BEDS IN THIS HOSPITAL ARE AVAILABLE" 
                return "SORRY! BEDS IN THIS HOSPITAL ARE NOT AVAILABLE"
            if dis in common_dis:
                return "Such Diseases can be treated at home. Please consult doctors for medicines"
            if dis in pandemic:
                cur.execute("SELECT Beds_availibilty_covid FROM HOSPITAL as h WHERE h.name = hp")
                l=cur.fetchall()
                if l[0]>0:
                    return "BEDS IN THIS HOSPITAL ARE AVAILABLE" 
                return "SORRY! BEDS IN THIS HOSPITAL ARE NOT AVAILABLE"

    print("What do you want to do : ")
    print("1. Check-up/Self diagnosis at home \n 2. Book Appointment with doctors near you \n 3. Check Availibilty of beds in hospital near you \n 4. Exit")
    ch=input("Enter your choice : ")

    if ch=='1':
        symp_disease()

    elif ch=='2':
        book_appointment()

    elif ch=='3':
            check_bed_availibilty()

    elif ch=='4':
        print("Please Visit again")
        exit()


    else:
        print("Wrong number. Taking you back!")
        continue


