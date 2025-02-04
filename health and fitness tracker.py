details=[]
import secrets,os
import string,csv
from verify_email import verify_email
import mysql.connector as mc
from email.message import EmailMessage
import ssl
import smtplib
import random
from datetime import datetime
import re
import urllib.request
from pytube import YouTube
import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
us=""
phone=0
height=0
sex=""
emu=""

def welcome():
    print("#_#_#_#_#_#_#_#_ WELCOME TO HEALTH AND FITNESS TRACKER _#_#_#_#_#_#_#_#")
    print("\n")
    print("%_%_%_%_%_%_%_%_ PLEASE ENTER THE FOLLOWING DETAILS _%_%_%_%_%_%_%_%_%")
    print()
    def user_input():
        global details,us,phone,sex,height,emu
        user_name=input("enter the user name:")
        print()
        age=int(input("enter the age:"))
        print()
        us=user_name
        def email():
            global emu
            em=input("enter the gmail id:")
            emu=em
        email() 
        ph=int(input("enter the phone no:"))
        print()
        phone=ph
        def gen():
            global sex
            s=input("enter gender;male or female:")
            sex=s
            print()
            if s.upper()!="MALE" and s.upper()!="FEMALE":
                print("invalid gender:")
                gen()
        gen()
        w=int(input("enter your weight:"))
        print()
        def height1():
            global height
            h=int(input("enter your height inn cm::)"))
            print()
            if h>=122 and h<=214:
                height=h
                pass
            else:
                print("invalid height:")
                height1()
        height1()
        d1,a1,b1="","",""
        details=[user_name,ph,emu,age,sex,w,height]
        def bp1(n):
            global details,b1
            if n.upper()=="NO":
                b1=None;details.append(b1)
            elif n.upper()=="YES":details.append(n)
            else:
                print("invalid,reply yes or no for blood pressure:")
                bp1(input("do you have blood pressure,enter yes or no:"))
                print()
        bp1(input("do you have blood pressure,enter yes or no:"))
        print()
        def dia1(n):
            global details,d1
            if n.upper()=="NO":
                d1=None;details.append(d1)
            elif n.upper()=="YES":details.append(n)
            else:
                print("invalid,reply yes or no for diabetes:")
                dia1(input("do you have diabetes,enter yes or no:"))
                print()
        dia1(input("do you have diabetes,enter yes or no:"))
        print()
        def all1(n):
            global details,a1
            if n.upper()=="NO":
                a1=None;details.append(a1)
            elif n.upper()=="YES":a2=input("enter your allergy name:");details.append(a2)
            else:
                print("invalid,reply yes or no allergies:")
                all1(input("are you allergic to anything,enter yes or no"))
        all1(input("are you allergic to anything,enter yes or no"))
        print()
    user_input()
    def user_authentication():
        global us,phone,details
        def passwd():
            pwd=""
            letters = string.ascii_letters
            digits = string.digits
            special_chars ="__"
            alphabet = letters + digits + special_chars
            pwd_length =6
            pwd+=us+"_"
            for i in range(pwd_length):
              pwd += ''.join(secrets.choice(alphabet))
            cfile=open("users.csv","r")
            cr=csv.reader(cfile)
            psflag=False
            for i in cr:
                if i[1]==pwd:
                    psflag=True
                    passwd()
            if psflag==False:
                return pwd
        pwd=passwd()
        def psw(a,b):
            input1=input("enter the user id to view the password:")
            print()
            input2=int(input("enter the phone number to view thw password:"))
            print()
            if input1==a and input2==b:
                apppass="makn afsj xyyw jnwu"
                email_sender="fitnessworkouttoday@gmail.com"
                email_password=apppass

                email_receiver=emu
                subject="WELCOME TO HEALTH AND FITNESS APP"
                body=f"YOUR PASSWORD IS {pwd} PLEASE SAVE THE PASSWORD FOR FURTHER VERIFICATIONS \n THANKYOU {us}"
                em=EmailMessage()
                em['From']=email_sender
                em['To']=email_receiver
                em['subject']=subject
                em.set_content(body)
                context=ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                    smtp.login(email_sender,email_password)
                    smtp.sendmail(email_sender,email_receiver,em.as_string())
                print("*_*_*_*_*_*_*_*YOUR PASSWORD IS SENT TO YOUR GMAILID PLEASE SAVE THE PASSWORD,*_*_*_*_*_*_*_*_*_*")
                details.insert(1,pwd)
                
            else:
                print("*_*_*_*_*_*_*_*_*_*_*_*_*_*user_name and phone number did not match*_*_*_*_*_*_*_*_*_*_*_*_*")
                psw(us,phone)
        psw(us,phone)
        print("_*_*_*_*_*_*_*_\t\tENTER YOUR GOAL\t\t_*_*_*_*_*_*_*_")
        print()
        i=1
        while i==1:
            print("1...WEIGHT LOSS\n2...STRENGTH TRAINING\n3...FLEXIBILITY TRAINING\n4...TO GET STRONGER and INCREASE METABOLISM & MAINTAIN HEALTHY BODY  WEIGHT")
            gch=int(input("ENTER YOUR GOAL CHOICE:"))
            if gch==1:
                goal="WEIGHTLOSS"
                details+=[goal]
                i+=1
            elif gch==2:
                goal="STRENGTH_TRAINING"
                details+=[goal]
                i+=1
            elif gch==3:
                goal="FLEXI_TRAINING"
                details+=[goal]
                i+=1
            elif gch==4:
                goal="STRONGER"
                details+=[goal]
                i+=1
            elif i==2:
                print("\t\t*_*_*_*_*_*_*\tGOAL SET\t_*_*_*_*_*_*_*")
                break
            else:
                print("invalid choice")
    user_authentication()

    def insert_csv1_DB():
        global details
        cfile=open("users.csv","a",newline="")
        cw=csv.writer(cfile)
        cw.writerow(details)
        
        return details[0],details[1],details[-1]
    info=insert_csv1_DB()
    def insert_tableDB(det):
        table_name=det[1]
        connector=mc.connect(host="localhost",user="root",passwd="michael1958")
        curm=connector.cursor()
        if det[-1].upper()=="WEIGHTLOSS":
            curm.execute("use weightloss")
            sql_statement = f"CREATE TABLE {table_name}(date DATE, day INT, url VARCHAR(100), sleep INT, water_intake VARCHAR(20), PRIMARY KEY (date));"
            curm.execute(sql_statement)
            connector.commit()
            connector.close()
        elif det[-1].upper()=="STRENGTH_TRAINING":
            curm.execute("use strength_training")
            sql_statement = f"CREATE TABLE {table_name}(date DATE, day INT, url VARCHAR(100), sleep INT, water_intake VARCHAR(20), PRIMARY KEY (date));"
            curm.execute(sql_statement)
            connector.commit()
            connector.close()
        elif det[-1].upper()=="FLEXIBILITY_TRAINING":
            curm.execute("use FLEXI_TRAINING ")
            sql_statement = f"CREATE TABLE {table_name}(date DATE, day INT, url VARCHAR(100), sleep INT, water_intake VARCHAR(20), PRIMARY KEY (date));"
            curm.execute(sql_statement)
            connector.commit()
            connector.close()
        elif det[-1].upper()=="STRONGER":
            curm.execute("use STRONGER;")
            sql_statement = f"CREATE TABLE {table_name}(date DATE, day INT, url VARCHAR(100), sleep INT, water_intake VARCHAR(20), PRIMARY KEY (date));"
            curm.execute(sql_statement)
            connector.commit()
            connector.close()
            
    insert_tableDB(info)
    handf_home()
    
def modification_csv1_DB():
    def m():
        usu=input("user name ")
        print()
        pwu=input("enter your password:")
        return usu,pwu
    z=m()
    while True:
        print("*_*_*_*_*_*_*_*_*_*_*_*_*_*TO MODIFY PRESS ANY ONE OF THE DETAILS*_*_*_*_*_*_*_*_*_*_*_*_*_*")
        print("1.....PHONE NO\n2.....WEIGHT\n3.....HEIGHT\n4....DONE MODIFICATION")
        mch=int(input("%_%_%_%_%_%_%_ENTER YOUR CHOICE:)%_%_%_%_%_%_%_%"))
        if mch==1:
            cfile1=open("users.csv","r")
            cfile2=open("temp.csv","w")
            cr=csv.reader(cfile1)
            cw=csv.writer(cfile2)
            flag=True
            for i in cr:
                if i[0]==z[0] and i[1]==z[1]:
                    newp=input("enter your new phone no:")
                    cw.writerow([i[0],i[1]]+[newp]+i[3::])
                    flag=False
                else:

                    cw.writerow(i)
            if flag==True:
                m()
            else:
                cfile1.close()
                cfile2.close()
                os.remove("users.csv")
                os.rename("temp.csv","users.csv")
                print("\t\t_*_*PHONE_NO WAS MODIFIED :)_*_*\t\t")
        elif mch==2:
            cfile1=open("users.csv","r")
            cfile2=open("temp.csv","w")
            cr=csv.reader(cfile1)
            cw=csv.writer(cfile2)
            flag=True
            for i in cr:
                if i[0]==z[0] and i[1]==z[1]:
                    newp=input("enter your the WEIGHT to update:")
                    cw.writerow(i[0:6:]+[newp]+i[7::])
                    flag=False
                else:
                    cw.writerow(i)
            if flag==True:
                m()
            else:
                cfile1.close()
                cfile2.close()
                os.remove("users.csv")
                os.rename("temp.csv","users.csv")
                print("\t\t_*_*WEIGHT WAS UPDATED :)_*_*\t\t")
        elif mch==3:
            cfile1=open("users.csv","r")
            cfile2=open("temp.csv","w")
            cr=csv.reader(cfile1)
            cw=csv.writer(cfile2)
            flag=True
            for i in cr:
                if i[0]==z[0] and i[1]==z[1]:
                    newp=input("enter your the HEIGHT to update:")
                    cw.writerow(i[0:7:]+[newp]+i[8::])
                    flag=False
                else:
                    cw.writerow(i)
            if flag==True:
                m()
            else:
                cfile1.close()
                cfile2.close()
                os.remove("users.csv")
                os.rename("temp.csv","users.csv")
                print("\t\t_*_*HEIGHT WAS UPDATED :)_*_*\t\t")
        
        elif mch==4:
            print("\t\t\t*_*_*_*_*_*_*_*_*_MODIFICATION DONE_*_*_*_*_*_*_*_*_*_*_")
            break
        else:
            print("\t\t***********YOUR CHOICE IS INVALID****************")
    handf_home()
    
def today_workout():
    print("_*_*_*_*_*_*_*_*TODAY'S WORKOUT_*_*_*_*_*_*_*_*")
    mcc=mc.connect(host="localhost",user="root",passwd="michael1958")
    mys_cur=mcc.cursor()
    user=input("enter the user name to track activiity:")
    print()
    pass1=input("enter your password to track activiity::")
    cfile=open("users.csv","r")
    cr=csv.reader(cfile)
    db,table="",""
    flag=True
    for i in cr:
        if i[0]==user and i[1]==pass1:
            db=i[-1]
            table=pass1
            flag=False
    cfile.close()
    if flag==True:
        print(f"{user} and {pass1} is not found ")
        choice_act=input("would you like to create a new  username and password::(Y/N)::")
        if choice_act.upper()=="Y":welcome()
        else:today_workout()
        
    elif flag==False:
        tfile=open("motivational_qoutes.txt","r")
        tr=tfile.readlines()
        q=random.randint(0,99)
        qoute=tr[q]
        tfile.close()
        cfile=open("users.csv","r")
        cr=csv.reader(cfile)
        for i in cr:
            
            if i[0]==user and i[1]==pass1:
                em=i[3]
                
                if i[-1]=="WEIGHTLOSS":
                    mys_cur.execute(f"use {db};")
                    mys_cur.execute(f"SELECT * FROM {table} ;")
                    user_info=mys_cur.fetchall()
                    if user_info==[]:
                        yes_day=0
                        yes_url=""
                    else:
                        z=user_info[-1]
                        yes_day,yes_url=z[1],z[2]
                    
                    mys_cur.execute("SELECT * FROM urlweightloss;") 
                    URLS=mys_cur.fetchall()
                    today_day=0
                    today_url=""
                    for i in URLS:
                        if i[0]==yes_day and i[-1]==yes_url:
                            today_day=yes_day+1
                            break
                        elif yes_day==0 and yes_url=="":
                            today_day=i[0]
                            break
                    today_url=""
                    for i in URLS:
                        if i[0]==today_day:
                            today_url=i[-1]
                    current_datetime=datetime.now()
                    current_date=current_datetime.date()
                    current_date_str=current_date.strftime("%Y-%m-%d")
                    QUERY="INSERT INTO "+table+"(DATE,DAY,URL)VALUES('{}',{},'{}')".format(current_date_str,today_day,today_url)
                    mys_cur.execute(QUERY)
                    mcc.commit()
                    apppass="makn afsj xyyw jnwu"
                    email_sender="fitnessworkouttoday@gmail.com"
                    email_password=apppass

                    email_receiver=em
                    subject="today's workout"
                    
                    body=f"ready to beat the workout?\n {today_day} {today_url}\n {qoute}\n by health and fitness"
                    
                    em=EmailMessage()
                    em['From']=email_sender
                    em['To']=email_receiver
                    em['subject']=subject
                    em.set_content(body)
                    context=ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                        smtp.login(email_sender,email_password)
                        smtp.sendmail(email_sender,email_receiver,em.as_string())
                    print("\t\tworkout sent through gmail :)\t\t kindly check your mail :)")
                    
                elif i[-1]=="STRENGTH_TRAINING":
                    mys_cur.execute(f"use {db};")
                    mys_cur.execute(f"SELECT * FROM {table} ;")
                    user_info=mys_cur.fetchall()
                    if user_info==[]:
                        yes_day=0
                        yes_url=""
                    else:
                        z=user_info[-1]
                        yes_day,yes_url=z[1],z[2]
                    
                    mys_cur.execute("SELECT * FROM urlstrength;") 
                    URLS=mys_cur.fetchall()
                    today_day=0
                    today_url=""
                    for i in URLS:
                        if i[0]==yes_day and i[-1]==yes_url:
                            today_day=yes_day+1
                            break
                        elif yes_day==0 and yes_url=="":
                            today_day=i[0]
                            break
                    today_url=""
                    for i in URLS:
                        if i[0]==today_day:
                            today_url=i[-1]
                    current_datetime=datetime.now()
                    current_date=current_datetime.date()
                    current_date_str=current_date.strftime("%Y-%m-%d")
                    QUERY="INSERT INTO "+table+"(DATE,DAY,URL)VALUES('{}',{},'{}')".format(current_date_str,today_day,today_url)
                    mys_cur.execute(QUERY)
                    mcc.commit()
                    apppass="makn afsj xyyw jnwu"
                    email_sender="fitnessworkouttoday@gmail.com"
                    email_password=apppass

                    email_receiver=em
                    subject="today's workout"
                    
                    body=f"ready to beat the workout?\n {today_day} {today_url}\n {qoute}\n by health and fitness"
                    
                    em=EmailMessage()
                    em['From']=email_sender
                    em['To']=email_receiver
                    em['subject']=subject
                    em.set_content(body)
                    context=ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                        smtp.login(email_sender,email_password)
                        smtp.sendmail(email_sender,email_receiver,em.as_string())
                    print("\t\tworkout sent through gmail :)\t\t kindly check your mail :)")

                elif i[-1]=="FLEXIBILITY_TRAINING":
                    mys_cur.execute(f"use {db};")
                    mys_cur.execute(f"SELECT * FROM {table} ;")
                    user_info=mys_cur.fetchall()
                    if user_info==[]:
                        yes_day=0
                        yes_url=""
                    else:
                        z=user_info[-1]
                        yes_day,yes_url=z[1],z[2]
                    
                    mys_cur.execute("SELECT * FROM FLEXI_URL;") 
                    URLS=mys_cur.fetchall()
                    today_day=0
                    today_url=""
                    for i in URLS:
                        if i[0]==yes_day and i[-1]==yes_url:
                            today_day=yes_day+1
                            break
                        elif yes_day==0 and yes_url=="":
                            today_day=i[0]
                            break
                    today_url=""
                    for i in URLS:
                        if i[0]==today_day:
                            today_url=i[-1]
                    current_datetime=datetime.now()
                    current_date=current_datetime.date()
                    current_date_str=current_date.strftime("%Y-%m-%d")
                    QUERY="INSERT INTO "+table+"(DATE,DAY,URL)VALUES('{}',{},'{}')".format(current_date_str,today_day,today_url)
                    mys_cur.execute(QUERY)
                    mcc.commit()
                    apppass="makn afsj xyyw jnwu"
                    email_sender="fitnessworkouttoday@gmail.com"
                    email_password=apppass

                    email_receiver=em
                    subject="today's workout"
                    
                    body=f"ready to beat the workout?\n {today_day} {today_url}\n {qoute}\n by health and fitness"
                    
                    em=EmailMessage()
                    em['From']=email_sender
                    em['To']=email_receiver
                    em['subject']=subject
                    em.set_content(body)
                    context=ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                        smtp.login(email_sender,email_password)
                        smtp.sendmail(email_sender,email_receiver,em.as_string())
                    print("\t\tworkout sent through gmail :)\t\t kindly check your mail :)")

                elif i[-1]=="STRONGER":
                    mys_cur.execute(f"use {db};")
                    mys_cur.execute(f"SELECT * FROM {table} ;")
                    user_info=mys_cur.fetchall()
                    if user_info==[]:
                        yes_day=0
                        yes_url=""
                    else:
                        z=user_info[-1]
                        yes_day,yes_url=z[1],z[2]
                    
                    mys_cur.execute("SELECT * FROM STONGER_URL;") 
                    URLS=mys_cur.fetchall()
                    today_day=0
                    today_url=""
                    for i in URLS:
                        if i[0]==yes_day and i[-1]==yes_url:
                            today_day=yes_day+1
                            break
                        elif yes_day==0 and yes_url=="":
                            today_day=i[0]
                            break
                    today_url=""
                    for i in URLS:
                        if i[0]==today_day:
                            today_url=i[-1]
                    current_datetime=datetime.now()
                    current_date=current_datetime.date()
                    current_date_str=current_date.strftime("%Y-%m-%d")
                    QUERY="INSERT INTO "+table+"(DATE,DAY,URL)VALUES('{}',{},'{}')".format(current_date_str,today_day,today_url)
                    mys_cur.execute(QUERY)
                    mcc.commit()
                    apppass="makn afsj xyyw jnwu"
                    email_sender="fitnessworkouttoday@gmail.com"
                    email_password=apppass

                    email_receiver=em
                    subject="today's workout"
                    
                    body=f"ready to beat the workout?\n {today_day} {today_url}\n {qoute}\n by health and fitness"
                    
                    em=EmailMessage()
                    em['From']=email_sender
                    em['To']=email_receiver
                    em['subject']=subject
                    em.set_content(body)
                    context=ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                        smtp.login(email_sender,email_password)
                        smtp.sendmail(email_sender,email_receiver,em.as_string())
                    print("\t\tworkout sent through gmail :)\t\t kindly check your mail :)")
            
    mcc.close()
    handf_home()
    
def activity_tracking():
    mcc=mc.connect(host="localhost",user="root",passwd="michael1958")
    mys_cur=mcc.cursor()
    user=input("enter the user name to track activiity:")
    print()
    pass1=input("enter your password to track activiity::")
    cfile=open("users.csv","r")
    cr=csv.reader(cfile)
    db,table="",""
    flag=True
    for i in cr:
        if i[0]==user and i[1]==pass1:
            db=i[-1]
            table=pass1
            flag=False
    
    if flag==True:
        print(f"{user} and {pass1} is not found ")
        choice_act=input("would you like to create a new  username and password::(Y/N)::")
        if choice_act.upper()=="Y":welcome()
        elif choice_act.upper()=="N":activity_tracking()
    elif flag==False:
        mys_cur.execute(f"use {db};")
        mys_cur.execute(f"SELECT  * FROM {table}")
        z=mys_cur.fetchall()
        last_info=z[-1]
        ldate=last_info[0]
        sleep=input("enter the sleep you've had last night:")
        water=input("enter the water intake in litres:")
        ac="UPDATE "+table+" SET SLEEP='{}',WATER_INTAKE='{}' where date='{}'".format(sleep,water,ldate)
        mys_cur.execute(ac)
        mcc.commit()
        mcc.close()
    handf_home()
    
def nutrition_ideas():
    def get_eligible_videos(query, channel_name=None):
        query = query.replace(' ', '+')
        channel_name = channel_name.replace(' ', '+') if channel_name else None

        url = f"https://www.youtube.com/results?search_query={query}"
        url += f"+channel:{channel_name}" if channel_name else ""

        try:
            html = urllib.request.urlopen(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

            eligible_videos = []
            unique_video_ids = set() 

            if video_ids:
                for video_id in video_ids:
                    if video_id not in unique_video_ids:
                        video_url = f"https://www.youtube.com/watch?v={video_id}"
                        yt = YouTube(video_url)
                        if yt.length > 60:
                            eligible_videos.append({
                                'title': yt.title,
                                'thumbnail_url': yt.thumbnail_url,
                                'video_url': video_url
                            })
                            unique_video_ids.add(video_id)

                return eligible_videos

        except Exception as e:
            print(f"An error occurred: {e}")

        return None
    def play_video(video):
        print("\nPlaying YouTube video:")
        print("Title:", video['title'])
        print("Thumbnail URL:", video['thumbnail_url'])

        webbrowser.open(video['video_url'])

    if __name__ == "__main__":
        query = input("Enter the search query: ")
        channel_name = input("Enter the channel name (optional): ")

        eligible_videos = get_eligible_videos(query, channel_name)

        if eligible_videos:
            print("\nEligible Videos:")
            for i, video in enumerate(eligible_videos):
                print(f"{i + 1}. {video['title']}")

            choice = input("\nEnter the number of the video you want to play (or 'q' to quit): ")
            if choice.lower() != 'q':
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(eligible_videos):
                        play_video(eligible_videos[choice - 1])
                    else:
                        print("Invalid choice. Exiting.")
                except ValueError:
                    print("Invalid input. Exiting.")
        else:
            print("No eligible videos found in the search results.")
    handf_home()

def authenticate_user(username, password):
    csv_file_path = r"C:\Users\priya\OneDrive\Documents\projects\users.csv"
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return row
    return None

def show_user_details(root, username, password_entry):
    user_details = authenticate_user(username, password_entry)

    if user_details:
        details_window = tk.Toplevel(root)
        details_window.title(f"Welcome back {username}")
        details_window.configure(bg="#fef8dd")
        l = ["Phone Number", "Email ID", "Age", "Gender", "Weight", "Height", "Blood Pressure", "Diabetes", "Allergies"]
        d = user_details[2:]
        c = ["#317873", "#874C62", "#D2B48C", "#DC143C", "#FFE135", "#DE5D83", "#C54B8C", "#8B5076", "#B7410E"]
        r = 0
        for label, value, color in zip(l, d, c):
            label_widget = ttk.Label(details_window, text=f"{label}:", font=("Helvetica", 12), background="#fef8dd", foreground="#0A1172")
            label_widget.grid(row=r, column=0, padx=10, pady=5, sticky="w")
            
            value_widget = ttk.Label(details_window, text=value, font=("Helvetica", 12), background="#fef8dd", foreground=color)
            value_widget.grid(row=r, column=1, padx=10, pady=5, sticky="w")
            r += 1
    else:
        messagebox.showerror("Error", "Invalid username or password")

def profile_management():
    # Create the main window
    root = tk.Tk()
    root.title("User Details")
    root.configure(bg="#F19CBB")  # AMARANTH color

    # Create and configure the style for themed widgets
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 12), foreground="white", background="#F19CBB")
    style.configure("TButton", padding=10, font=("Helvetica", 12))
    style.configure("TEntry", padding=10, font=("Helvetica", 12))

    # Create and place themed widgets
    username_label = ttk.Label(root, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    username_entry = ttk.Entry(root)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = ttk.Label(root, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    password_entry = ttk.Entry(root, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    login_button = ttk.Button(root, text="Login", command=lambda: show_user_details(root, username_entry.get(), password_entry.get()))
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Start the Tkinter event loop
    root.mainloop()
    handf_home()    
def analytics():
    input_username = input("enter the username:")
    print()
    input_password = input("enter the password:")

    with open('users.csv', 'r') as cfile:
        csv_reader = csv.reader(cfile)
        csv_data = list(csv_reader)


    for i in csv_data:
        if i[0] == input_username and i[1] == input_password:
            db = i[-1]
            table = input_password
            
            connection_params = {'host': 'localhost', 'user': 'root', 'password': 'michael1958', 'database': f"{db}"}
            
         
            sql_query = f"SELECT date, sleep, water_intake FROM {table};"
            conn = mc.connect(**connection_params)
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query)
                sql_data = cursor.fetchall()
            conn.close()

            sql_df = pd.DataFrame(sql_data)
            sql_df['date'] = pd.to_datetime(sql_df['date'])

            # Step 4: Data Visualization
            plt.figure(figsize=(10, 6),facecolor='#f0ffff')
            plt.plot(sql_df['date'], sql_df['sleep'], label='Sleep', marker='o',color='#ffb90f')
            plt.plot(sql_df['date'], sql_df['water_intake'], label='Water Intake', marker='o',color='#00c5cd')

            # Customize the plot
            plt.title(f'User Consistency Over Time - {input_username}',color='#8b0a50')
            plt.xlabel('Date',color='#228b22')
            plt.ylabel('Sleep Hours / Water Intake (in liters)',color='#228b22')
            plt.legend()
            plt.grid(True)
            with open(r"C:\Users\priya\OneDrive\Documents\projects\motivational_qoutes.txt", 'r') as quote_file:
                mq = quote_file.readlines()
                r=random.randint(0,99)
                motivational_quote=mq[r]
            plt.annotate(motivational_quote, xy=(0.5, -0.14), xycoords='axes fraction',ha='center', va='center', fontsize=11,color='#ee0000', bbox=dict(boxstyle="round", alpha=0.1))
            plt.show()
            break  
    else:
        print("Invalid username or password.")
    handf_home()

def logout():
    print("\t\t**************** LOGOUT *************")
    print()
    u=input("enter the user name:")
    print()
    p=input("enter the password:")
    cfile1=open("users.csv","r")
    cfile2=open("temp.csv","w",newline="")
    cr=csv.reader(cfile1)
    cw=csv.writer(cfile2)
    for i in cr:
        if i[0]==u and i[1]==p:
            print("****************************DELETING ALL THE DATA PERMANENTLY **************************")
            db=i[-1]
            table=p
            mcc=mc.connect(host="localhost",user="root",passwd="michael1958")
            mys_cur=mcc.cursor()
            mys_cur.execute(f"use {db};")
            mys_cur.execute(f"drop table {table}")
            mcc.close()
        else:cw.writerow(i)
    cfile1.close()
    cfile2.close()
    os.remove("users.csv")
    os.rename("temp.csv","users.csv")
    handf_home()

def handf_home():
    while True:
        print("\t\t_*_*_*_*1. LOGIN HEALTH AND FITNESS TRACKER APP _*_*_*_*\t\t")
        print("\n")
        print("\t\t_*_*_*_*2. MODIFY USER INFORMATION _*_*_*_*\t\t")
        print("\n")
        print("\t\t_*_*_*_*3. TODAY'S WORKOUT _*_*_*_*_*\t\t")
        print("\n")
        print("\t\t_*_*_*_*4. ACTIVITY TRACKING _*_*_*_*\t\t")
        print("\n")
        print("\t\t_*_*_*_*5. NUTRITIONAL IDEAS _*_*_*_*\t\t")
        print("\n")
        print("\t\t_*_*_*_*6. USER PROFILE MANAGEMENT _*_*_*_*\t\t")
        print("\n")
        print("\t\t_*_*_*_*7. USER CONSISTENCY GRAPH _*_*_*_*\t\t")
        print("\n")
        print("\t\t_*_*_*_*8. LOGOUT _*_*_*_*_*_*\t\t")
        print("\n")
        print("\t\t_*_*_*_*0. TO EXIT THE APP _*_*_*_*_*\t\t")
        print("\n")

        ch=int(input("ENTER THE CHOICE :"))

        print()
        if ch==1:
            welcome()

        elif ch==2:
            modification_csv1_DB()

        elif ch==3:
            today_workout()

        elif ch==4:
            activity_tracking()

        elif ch==5:
            nutrition_ideas()

        elif ch==6:
            profile_management()

        elif ch==7:
            analytics()

        elif ch==8:
            logout()

        elif ch==0:
            break

        else:
            print("*************\tYOUR CHOICE IS INVALID\t****************")

handf_home()
    
                    
    

