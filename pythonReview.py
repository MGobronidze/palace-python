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


def calculate_average(grades):
    """ლამბდას ფუნქციით საშუალო ქულის გამოთვლა"""
    return reduce(lambda x, y: x + y, grades) / len(grades)


# ფუნქციის გამოძახების მაგალითი
example_grades = [80, 90, 85]
average = calculate_average(example_grades)
print("საშუალო ქულა:", average)


def filter_students(min_grade):
    """ფილტრი: სტუდენტები, რომელთაც აქვთ მინიმუმ გარკვეული ქულა"""
    return list(filter(lambda student: all(g >= min_grade for g in student["grades"]), students))


# ფუნქციის გამოძახების მაგალითი
filtered = filter_students(85)
print("სტუდენტები მინიმალური ქულით 85:", filtered)


def update_student_name(student_id, new_name):
    """სტუდენტის სახელის განახლება"""
    for student in students:
        if student["id"] == student_id:
            student["name"] = new_name
            break


# ფუნქციის გამოძახების მაგალითი
update_student_name(1, "Alice Updated")
print("სტუდენტები სახელის განახლების შემდეგ:", students)


def delete_student(student_id):
    """სტუდენტის წაშლა ID-ის მიხედვით"""
    global students
    students = [student for student in students if student["id"] != student_id]


# ფუნქციის გამოძახების მაგალითი
delete_student(2)
print("სტუდენტები წაშლის შემდეგ:", students)


def find_student_by_id(student_id):
    """სტუდენტის დეტალების პოვნა ID-ის მიხედვით"""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


# ფუნქციის გამოძახების მაგალითი
student = find_student_by_id(1)
print("ID=1 სტუდენტის დეტალები:", student)


def find_top_student():
    """მაქსიმალური ქულის მქონე სტუდენტის პოვნა"""
    if not students:
        return None
    return max(students, key=lambda student: calculate_average(student["grades"]))


# ფუნქციის გამოძახების მაგალითი
top_student = find_top_student()
print("საუკეთესო სტუდენტი საშუალო ქულის მიხედვით:", top_student)


def sort_students_by_average():
    """სტუდენტების დალაგება საშუალო ქულის მიხედვით"""
    return sorted(students, key=lambda student: calculate_average(student["grades"]), reverse=True)


# ფუნქციის გამოძახების მაგალითი
sorted_students = sort_students_by_average()
print("სტუდენტები დალაგებული საშუალო ქულით:", sorted_students)


def get_subjects():
    """სიმრავლეების გამოყენება უნიკალური საგნების მიღებისთვის"""
    subjects = {"Math", "Science", "History", "Art"}
    return subjects


# ფუნქციის გამოძახების მაგალითი
subjects = get_subjects()
extra_subjects = {"Music", "Art"}
all_subjects = subjects.union(extra_subjects)
print("ყველა საგანი:", all_subjects)
