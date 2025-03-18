from functools import reduce

# სტუდენტების მონაცემები
students = []

# გლობალური ცვლადი - უნიკალური ID
student_id = 1


def add_student(name, grades):
    """სტუდენტის დამატება"""
    global student_id  # გლობალური ცვლადის გამოყენება
    students.append({"id": student_id, "name": name, "grades": tuple(grades)})
    student_id += 1


# ფუნქციის გამოძახების მაგალითი
add_student("Alice", [80, 90, 85])
add_student("Bob", [70, 75, 80])
add_student("Charlie", [95, 85, 92])
print("სტუდენტები დამატების შემდეგ:", students)

def update_student_name(student_id, new_name):
    """სტუდენტის სახელის განახლება"""
    for student in students:
        if student["id"] == student_id:
            student["name"] = new_name
            break
        
        
update_student_name(2, "Nino")
print("After updating name:", students)