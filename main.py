import sqlite3
db=sqlite3.connect('app.db')
cr=db.cursor()
#commit and close fnc
def co_close():
    db.commit()
    db.close()
    print('connection to database is closed')

#my user id
uid = 13
input_message="""
what do you want to do? 
"s"=>show all skills
"a"=>add a new skill
"d"=>delete a skill
"u"=>update ur progress
"q"=Quit
choose the option:
"""
user_input=input(input_message).strip().lower()
#define the methods
def show_skills():
    choooose=input('do u want to see all or for the current user y/n: ').strip().lower()
    if choooose=='y':
        cr.execute(f"SELECT * FROM SKILLS ORDER BY userid asc")
        result = cr.fetchall()
        print(f"u have {len(result)} skills")
        if len(result) == 0:
            pass
        else:
            print("showing skills with progress: ")
            for i in result:
                print(f"skill => {i[0]}", end=" ")
                print(f"progress => {i[1]}%", end=" ")
                print(f"uid => {i[2]}")
    elif choooose=='n':
        cr.execute(f"SELECT * FROM SKILLS WHERE userid={uid} ORDER BY name asc")
        result = cr.fetchall()
        print(f"u have {len(result)} skills")
        if len(result) == 0:
            pass
        else:
            print("showing skills with progress: ")
            for i in result:
                print(f"skill => {i[0]}", end=" ")
                print(f"progress => {i[1]}%", end=" ")
                print(f"uid => {i[2]}")
    else:
        print('kos omak')
    co_close()
def add_skill():
    sk=input("enter the skill u wish to add => ").strip().capitalize()
    cr.execute(f"SELECT name FROM SKILLS WHERE name= '{sk}' and userid={uid}")
    result = cr.fetchone()
    if result!=None:#this user has this skill
        print('this skill already exist to this user')
        choose=input("do u want to update it? y/n ").lower()
        if choose=='n':
            pass
        elif choose=='y':
            prog = input("enter ur new progress => ").strip()
            cr.execute(f"UPDATE SKILLS SET progress= '{prog}' WHERE name= '{sk}' and userid= '{uid}'")
        else:
            print("kos omak")
    else:
        prog = input("enter ur progress => ").strip()
        cr.execute(f"INSERT INTO SKILLS(name,progress,userid) VALUES('{sk}',{prog},'{uid}')")
        choose = input("do u wish to add somthing again? y/n").strip().lower()
        if choose == 'n':
            co_close()
        elif choose == 'y':
            add_skill()
        else:
            print("kos omak")
        co_close()
def delete_skill():
    skdel=input("choose the skill u want to delete: ").strip().capitalize()
    cr.execute(f"DELETE FROM SKILLS WHERE name='{skdel}'")
    print("column has been removed!")
    choose = input("do u wish to delete somthing again? y/n").strip().lower()
    if choose == 'n':
        pass
    elif choose == 'y':
        delete_skill()
    else:
        print("kos omak")
    co_close()

def update_skill():
    the_change=input("enter name of the skill u want to update: ").strip().capitalize()
    prog = input("enter ur new progress => ").strip()
    cr.execute(f"UPDATE SKILLS SET progress= '{prog}' WHERE name= '{the_change}' and userid= '{uid}'")
    co_close()

commands_list=['s','a','d','u','q']
if user_input in commands_list:
    #print('we shall commence')
    if user_input=="s":
        show_skills()
    elif user_input=="a":
        add_skill()
    elif user_input=="d":
        delete_skill()
    elif user_input=="u":
        update_skill()
    else:
        print("app is closed")

else:
    print('fk u')


