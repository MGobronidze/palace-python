import random

# ფუნქცია - შემთხვევითი მათემატიკური შეკითხვის შექმნისთვის
def generate_question():
    num1 = random.randint(1, 10)  # მთელი რიცხვები
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*", "/"])  # ოპერატორი

    # ოპერაციის გათვალისწინებით სწორი პასუხის გამოთვლა
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = round(num1 / num2, 2)  # ათწილადი მნიშნელობები (float)
    
    return f"{num1} {operation} {num2}", answer  # დავბრუნოთ კითხვა და სწორი პასუხი

# ფუნქცია - თამაშის ძირითადი ლოგიკისათვის
def math_game(questions=5):
    score = 0  # ქულა
    print("მოგესალმებით მათემატიკური თამაშის ფარგლებში!")
    
    for i in range(1, questions + 1):  # ციკლი - თითოეული კითხვისთვის
        question, correct_answer = generate_question()
        print(f"\nშეკითხვა {i}: {question}")
        
        try:
            user_answer = float(input("შეიყვანეთ პასუხი: "))  # მომხმარებლის პასუხის მიღება
            
            # პასუხის შემოწმება
            if user_answer == correct_answer:
                print("სწორია!")
                score += 1  # სწორი პასუხის შემთხვევაში ქულის ზრდა
            else:
                print(f"არასწორია. სწორი პასუხი არის: {correct_answer}")
        
        except ValueError:
            print("გთხოვთ შეიყვანოთ რიცხვი.")  # შეცდომის დამუშავება

    # საბოლოო შედეგი
    print(f"\nთამაში დასრულდა! შენ მოაგროვე {score} ქულა {questions}-დან.")
    
    # ლოგიკური შემოწმება - საბოლოო შეფასებისათვის
    if score == questions:
        print("შესანიშნავი შედეგი!")
    elif score > questions / 2:
        print("კარგია! შეიძლება კიდევ გაუმჯობესება.")
    else:
        print("ცოტა ვარჯიში არ გაწყენდა.")

# თამაში იწყება ამ ფუნქციის გამოძახებით
math_game(questions=5)
