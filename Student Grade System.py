
# Simple Student Grade management system
#Initialize empty dictionary
student_grade = {}

# add student function
def add_student(name,grade):
    student_grade[name] = grade
    #Rammani 23
    print(f"Added {name} with {grade}.")


# update student function
def update_student(name,grade):
    if name in student_grade:
        update_student[name] = grade
        return f"{name} is Updated with {grade}"
    else:
        print(f"{name} Nhi hai kuchh yha fir se try karo...!")
    
# delete student details function
def delete_student(name):
    if name in student_grade:
        delete_student.remove[name]
        return f"{name} is successfully deleted"
    else:
        print(f"{name} Name ka Nhi hai kuchh yha fir se try karo...!")
 
#to view all student details function
def display_student():
    for name, grade in student_grade.items():
        print(f"{name} : {grade}")
    else:
        return f"Student Nhi mil rha..!"
    

def main():    
    while True:
        print("\nSwagat hai apka student grade system me...!")
        print("---------------------x---------------------------")
        print("1. Add Student\n2. Update Student\n3. Delete student \n4. View Details\n5. Exit/Stop")

        Choice = int(input("Kya  karna hai Bolo= "))
        if Choice == 1:
            total_num = int(input("Kitne student add karna hai = "))
            for i in range(1, total_num + 1):
        # task_name = input(f"Enter task name {i}: ")
        # tasks.append(task_name)
                name = input(f"Enter Student {i} name ")
                grade = int(input(f"Enter Student {i} grade "))
                add_student(name,grade)
        
        elif Choice == 2:
            name = input("Enter Student name ")
            grade = int(input("Enter Student grade "))
            update_student(name,grade)

        elif Choice == 3:
            name = input("Enter Student name you want to delete ")
            delete_student(name)

        elif Choice == 4:
            display_student()
        
        elif Choice == 5:
            print("Acha chalta hu duaaon me yaad rakhna...!")
            break

        else:
            print("Galat ..Ek dam galat input")

        
            
main()