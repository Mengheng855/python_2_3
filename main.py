student=[]
while True:
    print("---------Menu--------")
    print("1.Add student")
    print("2.Show data student")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Exit")
    opt=input("Input option (1-5) : ")
    if opt=="1":
        print("---------Input--------")
        size=int(input("Input size : "))
        for x in range(0,size):
            student_name=input(f"Input student [{x+1}]: ").lower()
            student.append(student_name)
    elif opt=="2":
        print("---------Output--------")
        for x in range(len(student)):
            print(f"{x+1}.{student[x]}")
    elif opt=="3":
        print("---------Update--------")
        number=int(input("Input number of student : "))
        new_student=input("Input new student : ")
        student[number-1]=new_student
        for x in range(len(student)):
            print(f"{x+1}.{student[x]}")
    elif opt=="4":
        delete=input("input name student that you want to delete : ").lower()
        student.remove(delete)
        for x in range(len(student)):
            print(f"{x+1}.{student[x]}")
    elif opt=="5":
        print("exit")
        break
    else:
        print("invalid number ! try again")