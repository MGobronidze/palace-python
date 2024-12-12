import turtle

# ფანჯრის გახსნა და ობიექტის შექმნა
screen = turtle.Screen()
pen = turtle.Turtle()

# სამკუთხედის დახაზვა
for _ in range(3):
    pen.forward(100)  # მოძრაობს 100 პიქსელით წინ
    pen.right(120)    # ბრუნავს მარჯვენა 120 გრადუსით

# ფანჯრის დახურვა
screen.mainloop()
