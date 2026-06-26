class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    def add_mark(self, mark):
        try:
            mark = float(mark)
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100.")
            self.marks_list.append(mark)

        except ValueError as e:
            print("Error:", e)
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    def display_info(self):
        print("\n****** Student Details ******")
        print("Name : ", self.name)
        print("Roll No : ", self.roll_no)
        print("Marks : ", self.marks_list)
        print("Average Marks : ", self.get_average())
try:
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    student = Student(name, roll_no)

    # Add 5 subject marks
    print("\nEnter marks for 5 subjects:")
    for i in range(5):
        mark = input(f"Subject {i+1}: ")
        student.add_mark(mark)

    # Display student information
    student.display_info()
except Exception as e:
    print("Unexpected Error:", e)