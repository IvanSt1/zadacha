from students import *
def vyvod_menu():
    print("1. View BD")
    print("2. Output BD")
    print("0. Exit")


def vyvod_files(f1, f2, f3):
    for lines in f1:
        print(lines, end="")
    for lines in f2:
        print(lines, end="")
    for lines in f3:
        print(lines, end="")



def output_files(f_student, f_subject, f_marks):
    output = open("otput.txt", "w")
    n,surname,name,secondname,room=map(str,f_student.readline().split())
    x=student(n,surname,name,secondname,room, [0,0])
    print(x.get_name())

def Dialog():
    f_student = open("student.txt", "r")
    f_subject = open("subject.txt", "r")
    f_marks = open("marks.txt", "r")
    x = -1
    while x != 0:
        x = -1
        while x < 0 or x > 2:
            vyvod_menu()
            x = input()
            try:
                x = int(x)
            except ValueError:
                return False
        if x == 1:
            vyvod_files(f_student, f_subject, f_marks)
        elif x == 2:
            output_files(f_student, f_subject, f_marks)
    return True
