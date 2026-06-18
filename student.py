import json
import os
import getpass
import hashlib
def load():
    if os.path.exists("data.json"): 
        # check for the path if exist in the current directory or not if exist then open the file and load the data from it otherwise return empty list
        with open("data.json","r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []
def save_data(x):
    with open("data.json","w") as f:
        json.dump(x,f,indent=4)
students = load()

def add_students():
        while True:
            sid = input("Enter student_id:  ").strip()
            if sid =='':
                print("Invalid student_id, it should not be empty")
                sid = input("Enter student_id: ").strip()

                # check for the student_id if it is empty then print invalid student_id and ask for the input again
            elif sid.isalpha():
                print('Invalid student_id, it should be an integer')
                sid = input("Enter student_id: ").strip()
                # check for the student_id if it is not an integer then print invalid student_id and ask for the input again
            elif int(sid) <= 0:
                print("Invalid student_id")
                sid = input("Enter student_id:  ").strip()
                # check for the student_id if it is less than or equal to 0 then print invalid student_id and ask for the input again
            
            for s in students:
                if s["id"] == sid:
                # Student exists — just add a new semester
                    sem = int(input("Enter semester (1/2/3): "))
                    while True:
                        gpa = float(input("Enter GPA: "))
                        if 0 < gpa <= 4.0:
                            break
                        print("Invalid GPA")
                    s["semesters"][str(sem)] = gpa
                    print("Semester GPA added!")
                    save_data(students)
                    return

            while True:
                name = input("Enter  name of student: ")
                if not name.isalpha():
                    print("Invalid name, it should contain only letters")
                    # check for the name if it contains any character other than letters then print invalid name and ask for the input again
                elif len(name) <=3:
                    print("Invalid name, it should be more than 3 characters")
                    # check for the name if it is less than or equal to 3 characters then print invalid name and ask for the input again
                elif name=="":
                    print("Invalid name, it should not be empty")
                    # check for the name if it is empty then print invalid name and ask for the input again
                else:
                    break
        
            while True:
                    
                faculty = input("Enter student faculty: ")
                if faculty=='':
                    print("Invalid faculty, it should not be empty")
                    # check for the faculty if it is empty then print invalid faculty and ask for the input again
                elif not faculty.isalpha():
                    print("Invalid faculty, it should contain only letters")
                    # check for the faculty if it contains any character other than letters then print invalid faculty and ask for the input again
                else:
                    break
            sem = int(input("Enter semester (1/2/3): "))
            while True:
                gpa = float(input("Enter GPA: "))
                if gpa > 0 and gpa <= 4.0:
                    break
                print("Invalid GPA")
            dic = {"id": sid, "name": name, "faculty": faculty, "semesters": {str(sem): gpa}}
            students.append(dic)
            print("Data added Successfully")
            save_data(students)
            user_input = input("Do you want to add more students? (y/n) ").strip().lower()
            if user_input != "y":
                break
            

def view_students():
    # check for the students list if it is empty then print no students found otherwise print the required student data in the format of student_id, name, faculty and semesters with gpa
    if not students:
        print("No students found!")
        return
    print("View of Student_data\n")
    for data in students:
        sems = " | ".join([f"Sem{k}:{v}" for k, v in data["semesters"].items()])
        print(f"Student_id:{data['id']}|Name:{data['name']}|Faculty:{data['faculty']}|{sems}")

def search_students():
    user_input=input('''
            Search by:  
            1. Student_id               
            2. Name
            3. Faculty
            4. Gpa:    ''').strip()
    if user_input == "1":
        sid = input("Enter the student_id to search: ").strip()
        for data in students:
            if data["id"] == sid:
                # check for the student_id if it is found in the students list then print the required student data otherwise print student_id not found
                sems = " | ".join([f"Sem{k}:{v}" for k, v in data["semesters"].items()])
                print(f"Student_id:{data['id']}|Name:{data['name']}|Faculty:{data['faculty']}|{sems}")
                break
    elif user_input == "2":
        name = input('Enter the name to search: ').strip()
        for data in students:
            if data["name"].lower() == name.lower():
                # check for the name if it is found in the students list then print the required student data otherwise print name not found
                sems = " | ".join([f"Sem{k}:{v}" for k, v in data["semesters"].items()])
                print(f"Student_id:{data['id']}|Name:{data['name']}|Faculty:{data['faculty']}|{sems}")
                break
    elif user_input == "3":
        faculty = input('Enter the faculty to search: ').strip()
        for data in students:
            if data["faculty"].lower() == faculty.lower():
                # check for the faculty if it is found in the students list then print the required student data otherwise print faculty not found
                sems = " | ".join([f"Sem{k}:{v}" for k, v in data["semesters"].items()])
                print(f"Student_id:{data['id']}|Name:{data['name']}|Faculty:{data['faculty']}|{sems}")
    
    elif user_input == "4":
        try:
            gpa = float(input('Enter the GPA to search: '))
        except ValueError:
            print("Invalid GPA input.")
            return

        found = False
        for data in students:
            matching = []
            for sem, sem_gpa in data["semesters"].items():
                if abs(sem_gpa - gpa) < 1e-9:   # floating‑point tolerance
                    matching.append((sem, sem_gpa))
            if matching:
                found = True
                sem_str = " | ".join([f"Sem{k}:{v}" for k, v in matching])
                print(f"Student_id:{data['id']}|Name:{data['name']}|Faculty:{data['faculty']}|{sem_str}")

        if not found:
            print(f"No student found with GPA {gpa}.")
        
    else:
        print("Student_id not found")
def delete_data():
    sid = input("Enter the student_id to search to delete: ")
    for data in students:
        if data["id"] == sid:
            # check for the student_id if it is found in the students list then ask for confirmation to delete the data of that student if user confirms then delete the data of that student otherwise print data deletion cancelled
            confirm = input(f"Are you sure to delete '{data['name']}' press:(y/n)")
            if confirm.lower() == "y":
                students.remove(data)
                print(f"Data of Student '{data['name']}' removed")
                save_data(students)
            else:
                print("Data deletion cancelled")
            break
    else:
        print("Student_id not found to remove")  
    
def update_students():
    sid = input("Enter the student_id to update: ")
    for data in students:
        if data["id"] == sid:
            # check for the student_id if it is found in the students list then ask for the new id, name, faculty and gpa of that student and update the data of that student with the new data otherwise print student_id not found
            new_id = input("Enter the new id of student: ").strip()
            for s in students:
                if s["id"] == new_id and s != data:
                    print("ID Already exists")
                    return
            data["id"] = new_id
            data["name"] = input("Enter name of student: ")

            data["faculty"] = input("Enter  faculty of student: ")
            sem = input("Enter semester to update GPA (1/2/3) or press Enter to skip: ").strip()
            if sem:
                if sem in data["semesters"]:
                    try:
                        new_gpa = float(input("Enter new GPA: "))
                        if 0 < new_gpa <= 4.0:
                            data["semesters"][sem] = new_gpa
                            print(f"GPA for semester {sem} updated.")
                        else:
                            print("Invalid GPA (must be between 0 and 4.0).")
                    except ValueError:
                        print("Invalid number entered.")
                else:
                    print(f"Semester {sem} not found for this student.") 
            save_data(students)
            print("Data updated successfully.")
            break
    else:
        print("Student id not found!")
def topper_student():
    # check for the students list if it is empty then print data of students not found otherwise find the student with the highest gpa and print the required student data in the format of student_id, name, faculty and gpa
    if not students:
        print("Data of students not found")
        return

    max_avg = 0
    toppers = []

    for s in students:
        sem_list = list(s["semesters"].values())
        if not sem_list:          # skip students with no semesters
            continue
        avg = sum(sem_list) / len(sem_list)

        if avg > max_avg:
            max_avg = avg
            toppers = [s]
        elif avg == max_avg:      # tie – multiple toppers
            toppers.append(s)

    if not toppers:
        print("No student has semester data.")
        return

    print(f"\n🏆 Topper student(s) with Average GPA: {max_avg:.2f}")
    for t in toppers:
        sems_str = " | ".join([f"Sem{k}:{v}" for k, v in t["semesters"].items()])
        print(f"Student_id:{t['id']}|Name:{t['name']}|Faculty:{t['faculty']}|{sems_str}|Avg GPA:{max_avg:.2f}")


def show_progression():
    # check for the students list if it is empty then print data of students not found otherwise ask for the student_id to check the progression of that student and print the progression of that student in the format of semester1 gpa → semester2 gpa: Progressing/Degrading/No change
    sid = (input("Enter student_id to check progression: "))
    for data in students:
        if data["id"] == sid:
            sems = data["semesters"]
            if len(sems) < 2:
                print("Need at least 2 semesters to compare.")
                return
            sorted_keys = sorted(sems.keys())
            for i in range(1, len(sorted_keys)):
                g1 = sems[sorted_keys[i-1]]
                g2 = sems[sorted_keys[i]]
                if g2 > g1:
                    print(f"Sem{sorted_keys[i-1]} → Sem{sorted_keys[i]}: Progressing ({g1} → {g2})")
                elif g2 < g1:
                    print(f"Sem{sorted_keys[i-1]} → Sem{sorted_keys[i]}: Degrading ({g1} → {g2})")
                else:
                    print(f"Sem{sorted_keys[i-1]} → Sem{sorted_keys[i]}: No change")
            return
    print("Student not found")
def delete_all():
    # check for the students list if it is empty then print data of students not found otherwise ask for confirmation to delete all student data if user confirms then delete all student data otherwise print deletion cancelled
    confirm = input("Are you sure you want to delete all student data? (y/n): ")
    if confirm.lower() == "y":
        students.clear()
        save_data(students)
        print("All student data deleted.")
    else:
        print("Deletion cancelled.")
def main():
    while True:
        print("="*100)
        print("STUDENT MANAGEMENT SYSTEM\n")
        print("1.Add Student")
        print("2.View Students")
        print("3.Search Student")
        print("4.Delete Student_data")
        print("5.Edit Student_data")
        print("6.Topper Student")
        print("7.Delete All Student Data")
        print("8.Show Progression")
        print("9.Exit The Entry ")
        print("="*100)
        choice = input("Enter the choice in (1,2,3,4,5,6,7,8,9) : ").strip()
        if choice == "1":
            add_students()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_students()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            update_students()
        elif choice == "6":
            topper_student()
        elif choice == "7":
            delete_all()
        elif choice == "8":
            show_progression()
        elif choice == "9":
            break
        else:
            print("Invalid choice")



def login():
    USERNAME = "bpuk"
    # Pre‑compute hash of the password "@1@2" (you can change it)
    PASSWORD_HASH = hashlib.sha256("@1@2".encode()).hexdigest()
    attempt = 3
    while attempt > 0:
        username = input("Enter the username: ")
        password = getpass.getpass("Enter the password: ")  # input is masked
        # Hash the entered password and compare
        if username == USERNAME and hashlib.sha256(password.encode()).hexdigest() == PASSWORD_HASH:
            main()
            return
        else:
            attempt -= 1
            print(f"Invalid credentials. Left attempt is {attempt}")
    print("Failed to login. Exiting.")

login()


    

