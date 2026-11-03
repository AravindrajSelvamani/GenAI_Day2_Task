"""
Student Grade Manager

Markrange Grade
90 to 100   A
80 to 89    B
70 to 79    C
60 to 69    D
Below 60    E

"""

def get_grade(mark):
    if mark >= 90 and mark <= 100:
        return 'A'
    elif mark >= 80 and mark < 90:
        return 'B'
    elif mark >= 70 and mark < 80:
        return 'C'
    elif mark >= 60 and mark < 70:
        return 'D'
    else:
        return 'E'

def add_student(studentsdetails):
    while True:
        name = input("Enter student name: ").strip()
        if name == "" or  any(x["Name"].lower() == name.lower() for x in studentsdetails):
            print("Please Enter valid Student Name \n")
            continue
        break

    while True:
        mark = input("Enter student mark 0 to 100 :: ").strip()
        try:
            mark = float(mark)
            if mark < 0 or mark > 100:
                print("Please Enter valid Student mark 0 t0 100 ...")
                continue
        except ValueError:
            print("Please Enter valid Student mark ..")
            continue
        break
        
    grade = get_grade(mark)
    studentsdetails.append({"Name": name, "Mark": mark, "Grade":grade})
    #print(studentsdetails)
        

def show_StudentInfo(studentsdetails):
    #print(studentsdetails)
    if not studentsdetails:
        print("Student details as Empty")
        return
    print("_" * 50)
    print(f'{"Name":<12}{"Mark":<6}{"Grade":<6}')
    Mark = []
    for x in studentsdetails:
        print(f'{x["Name"]:<12}{x["Mark"]:<6}{x["Grade"]:<6}')
        Mark.append(x["Mark"])

    minMark = min(Mark)
    maxMark = max(Mark)
    AvgMark = round(sum(Mark)/len(Mark),4)

    print(f"\nAverage:{AvgMark:<6}Highest:{maxMark:<6}Lowest:{minMark:<6}")
    print("_" * 50)
            

def main():
    try:
        #add code
        studentsdetails = []
        while True:
            print("\n \nwelcome to Student Grade Manager\n")
            print("1. Add Student name and grade")
            print("2. Show Student details")
            print("3. exit\n")

            userInput = input("choose the menu :: ").strip()
            try:
                userInput = int(userInput)
            except ValueError:
                print("Enter Number from 1 to 3...")
                continue
            
            if userInput == 1:
                #print("add student")
                add_student(studentsdetails)
                continue
            elif userInput == 2:
                show_StudentInfo(studentsdetails)
                continue
            elif userInput == 3:
                print("closing the student grade manager")
                break
            else:
                print("Enter the valid number from 1 to 3...")
                continue

    except Exception as e:
        print(f"Error in main function :: {e}")


if __name__ == "__main__":
    main()

