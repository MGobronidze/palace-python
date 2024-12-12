import turtle

# ფანჯრის გახსნა და ობიექტის შექმნა
screen = turtle.Screen()
pen = turtle.Turtle()

# რვაკუთხედის დახაზვა
for _ in range(8):
    pen.forward(100)  # მოძრაობს 100 პიქსელით წინ
    pen.right(45)     # ბრუნავს მარჯვენა 45 გრადუსით

# ფანჯრის დახურვა
screen.mainloop()
