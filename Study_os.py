print("    STUDY OS")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your corse: ")
subjects = input("Enter your Subjects: ")


profile = {
    "NAME" : name,
    "AGE" : age,
    "COURSE" : course,
    "SUBJECTS" : subjects,
}

task_list = []
notes_list = []
subject_list = subjects.split(",")

while True:
    print(f"\n\nHello {name}!\n\n1.Profile\n2.Subjects\n3.Tasks\n4.Notes\n5.Marks\n6.Reports\n7.Exit")
    choice = int(input())
    if choice == 7:
        break


    elif choice == 1:
        print("Profile")
        print(profile)


    elif choice == 2:
        print("Your Subjects: ",subjects)


    elif choice == 3:
        print("Tasks")
        print("1.add task\n2.veiw taks\n3.Back")
        task_choice = int(input())
        if task_choice == 1:
            task = input("enter your task: ")
            task_list.append(task)
        elif task_choice == 2:
            print(task_list)
        elif task_choice == 3:
         continue

    elif choice == 4:
        print("Notes")
        print("1.add Notes\n2.veiw Notes\n3.Back")
        notes_choice = int(input())
        if notes_choice == 1:
            notes = input("enter your notes: ")
            notes_list.append(notes)
        elif notes_choice == 2:
            print(notes_list)
        elif notes_choice == 3:
            continue

    elif choice == 5:
        print("Marks")
        subject_list[0] = int(input(f"enter your {subject_list[0]} marks: "))


    