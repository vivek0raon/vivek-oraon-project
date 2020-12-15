import mysql.connector
import sys
connect= mysql.connector.connect(host="localhost",user="root",database="quizdata")
mycursor=connect.cursor()
def scoreupdate(level,score,u_name):
    if level=='s':
        mycursor.execute("select s_score from u_score where name='"+u_name+"'")
        s_score=mycursor.fetchall()
        if s_score[0][0]<score:
            update="update u_score set s_score=%s where name=%s"
            mycursor.execute(update,(str(score),u_name))
            connect.commit()
    if level=='m':
        mycursor.execute("select m_score from u_score where name='"+u_name+"'")
        m_score=mycursor.fetchall()
        if m_score[0][0]<score:
            update="update u_score set m_score=%s where name=%s"
            mycursor.execute(update,(str(score),u_name))
            connect.commit()
    if level=='h':
        mycursor.execute("select h_score from u_score where name='"+u_name+"'")
        h_score=mycursor.fetchall()
        if h_score[0][0]<score:
            update="update u_score set h_score=%s where name=%s"
            mycursor.execute(update,(str(score),u_name))
            connect.commit()
def play(level,u_name):
    print("current player="+u_name)
    print("\t\t**QUIZ STARTED**")
    b=0
    c=1
    mycursor.execute("select * from questions")
    data=mycursor.fetchall()
    lenght=len(data)
    for i in data:
        option=['A','B','C','D']
        if i[7]==level:
            option.remove(i[5].upper())
            print("\n"+str(c)+"."+i[0]+" point-("+str(i[6])+")")
            print(" A) "+i[1]+"  B) "+i[2]+"  C) "+i[3]+"  D) "+i[4])
            useranswer=input("enter  your option=>")
            if useranswer.upper()==i[5].upper():
                print("correct",end="")
                b=b+i[6]
                print("\t\tcurrent score=",b)
            else:
                if useranswer.upper() in option:
                    print("wrong answer")
                else:
                    print("invalid choice")
                print("correct option=",i[5],"\t\tcurrent score=",b)
            scoreupdate(level,b,u_name)
            c=c+1
        else:
            if data.index(i)==lenght-1:
                print("NO questions were addded on this level")

userlogin=input("\t\t\tQUIZ APP\nCHOOSE-\n1.sign in\n2.sign up\n3.Add questions\n=> ")
if userlogin=='1':
    u_name=input("\nenter your unique name:")
    u_pass=input("enter your password:")
    mycursor.execute("select * from userdata")
    userdata=mycursor.fetchall()
    count=0
    for i in userdata:
        if i[0]==u_name and i[1]==u_pass:
            count=1
            choice1=input("welcome back what you want 'p' to play now 's' to see your hightest scores:")
            if choice1=='p':
                hardness=input("enter hardness level:\n'h'-hard\n'm'-medium\n's'-simple\n=>")
                if hardness=='h':
                    play('h',u_name)
                if hardness=='m':
                    play('m',u_name)
                if hardness=='s':
                    play('s',u_name)
            if choice1=='s':
                mycursor.execute("select * from u_score")
                userscore=mycursor.fetchall()
                for j in userscore:
                    if j[0]==u_name:
                        print("level\t\thighest score")
                        print("simple\t\t",j[1],"\nmedium\t\t",j[2],"\nhard\t\t",j[3])
    if count==0:
        print("username or password is wrong please choose sign up if you are a new user or recheck your password")
elif userlogin=='2':
    u_name=input("enter your unique name:")
    mycursor.execute("select * from userdata")
    userdata=mycursor.fetchall()
    for i in userdata:
        if i[0]==u_name:
            sys.exit("this username is already registerd try again using other name")
    u_pass=input("enter your password:")
    in_sql="insert into userdata values('"+u_name+"','"+u_pass+"')"
    in_score="insert into u_score values('"+u_name+"',"+str(0)+","+str(0)+","+str(0)+")"
    mycursor.execute(in_sql)
    mycursor.execute(in_score)
    connect.commit()
    choice2=input("\nenter 'p' to playnow 'e' to exit:")
    if choice2=='p':
        hardness=input("enter hardness level:\n  'h'-hard\n  'm'-medium\n  's'-simple\n=>")
        if hardness=='h':
            play('h',u_name)
        if hardness=='m':
            play('m',u_name)
        if hardness=='s':
            play('s',u_name)
    else:
        print(" see you next time")
elif userlogin=='3':
    question=input("enter the question description:")
    option_1=input("enter the option a:")
    option_2=input("enter the option b:")
    option_3=input("enter the option c:")
    option_4=input("enter the option d:")
    correct_option=input("correct option:")
    marks=int(input("enter marks:"))
    hardness_level=input("enter 'h' for hard, enter 'm' for medium,enter 's' for simple:")
    sql_in= "insert into questions values('"+question+ "','" +option_1+ "','" + option_2 +"','" + option_3 +"','"+ option_4 +"','"+correct_option+"',"+str(marks)+",'"+hardness_level+"')"
    mycursor.execute(sql_in)
    connect.commit()
    print("your question has been added.")
else:
    print("wrong choice")
