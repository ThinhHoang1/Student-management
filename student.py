import sys

from student import student
lst = []

def create():
    global lst
    rollnum = input("Enter Rollnum: ")
    name = input("Enter name: ")
    engish = input("Enter English mark: ")
    math = input("Enter math mark: ")
    chemistry = input("Enter chemistry mark: ")
    phone_number = input("Enter phone number: ")
    i = student(rollnum,name,engish,math,chemistry,phone_number)
    lst.append(i)



def modify():
    global lst
    if len(lst) == 0:
        print("STUDENT LIST ARE CURRENTLY EMPTY")
    else:
        rollnum = input("Enter Rollnum: ")
        for i in lst:
            if i.get_rollnum() == rollnum:
                i.set_name(input("Enter new name: "))
                i.set_english(input("Enter new English mark: "))
                i.set_math(input("Enter new Math mark: "))
                i.set_chemistry(input("Enter new chemistry mark: "))
                i.set_phone_number(input("Enter new phone number: "))
                print("Student info have changed successfully ")

def delete():
    global lst
    rolll = input("Enter roll num student need to delete: ")
    for i in lst:
        if i.get_rollnum() == rolll:
            lst.remove(i)
            print("Student have been deleted successfully")

def search():
    global lst
    roll_num = input("Enter roll num student to search student: ")
    for i in lst:
        if i.get_rollnum() == roll_num:
            print("Roll num:", i.get_rollnum(),)
            print("Name: ",i.get_name())
            print("English: ",i.Eget_mark())
            print("Math:", i.Mget_mark())
            print("Chemistry: ",i.cget_mark())
            print("Phone number: ",i.getphone())

def report():
    global lst
    if len(lst) == 0:
        print("STUDENT LIST CURRENTLY EMPTY")
    else:
        for i in lst:
            i.show()
        with open("st.txt", "w") as f:
            for i in lst:
                f.write("Roll num: " + i.get_rollnum())
                f.write("\n")
                f.write("Name: " + i.get_name())
                f.write("\n")
                f.write("English: " + i.Eget_mark())
                f.write("\n")
                f.write("Math: " + i.Mget_mark())
                f.write("\n")
                f.write("Chemistry: " + i.cget_mark())
                f.write("\n")
                f.write("Phone number: " + i.getphone())
                f.write("\n")
                f.write("----------------\n")



while True:
    print("1.Admin")
    print("2.Report")
    print("3.Exit")
    user = input("Enter your option: ")
    if str(user).isdigit():
        user = int(user)
        if user == 1:
            print("1.Create pupil profile: ")
            print("2.Modify pupil profile: ")
            print("3.Delete pupil: ")
            print("4.Search pupil:")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                create()
            if choice == 2:
                modify()
            if choice == 3:
                delete()
            if choice == 4:
                search()

        if user == 2:
            report()
        if user == 3:
            sys.exit()




