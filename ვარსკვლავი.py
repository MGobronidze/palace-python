import turtle

# ფანჯრის შექმნა და კონფიგურაცია
screen = turtle.Screen()
screen.bgcolor("black")  # ფონის ფერი
screen.title("ვარსკვლავის ნახაზი")

# Turtle ობიექტის შექმნა
pen = turtle.Turtle()
pen.shape("turtle")        # ფორმა "turtle"
pen.color("yellow")        # ფანქრის ფერი
pen.width(3)               # ხაზის სისქე
pen.speed(5)               # სიჩქარე

# ვარსკვლავის დახაზვა
for _ in range(5):  # 5 წვერი
    pen.forward(200)  # გადაადგილება წინ
    pen.right(144)    # მარჯვენა მხარეს 144 გრადუსით ბრუნვა

# ვარსკვლავის შიგნით მცირე წრის დახაზვა
pen.penup()               # გადაადგილება ხაზის გარეშე
pen.goto(0, -50)          # ცენტრში გადასვლა
pen.pendown()             # ხაზის დახაზვის აქტივაცია
pen.color("blue")         # ფერის შეცვლა
pen.circle(50)            # 50 პიქსელის რადიუსის წრე

# ფანჯრის დახურვა
screen.mainloop()
