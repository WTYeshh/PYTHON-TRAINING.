class College:
    name = "Gopalan College of Engineering and Management"
    location = "Hoodi"

    def __init__(self, student_name: str, age: int, department: str) -> None:
        self.student_name = student_name
        self.age = age
        self.department = department

    def display(self) -> None:
        print(
            f"{self.student_name} is {self.age} years old and studies "
            f"{self.department} at {self.name}, {self.location}."
        )


def main() -> None:
    students = [
        College("Ram", 20, "CSE"),
        College("Raj", 21, "ECE"),
    ]
    for student in students:
        student.display()


if __name__ == "__main__":
    main()

