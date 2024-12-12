import turtle

# ფანჯრის გახსნა და ობიექტის შექმნა
screen = turtle.Screen()
pen = turtle.Turtle()

# კვადრატის დახაზვა
for _ in range(4):
    pen.forward(100)  # მოძრაობს 100 პიქსელით წინ
    pen.right(90)     # ბრუნავს მარჯვენა 90 გრადუსით

# ფანჯრის დახურვა
screen.mainloop()
