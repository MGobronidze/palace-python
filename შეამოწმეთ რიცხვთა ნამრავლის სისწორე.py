import random

def multiplication_quiz():
    print("მოგესალმები! ეს არის ცხრილის გამრავლების ტესტი.")
    correct_answers = 0  # სწორ პასუხთა მთვლელი
    
    # თითოეულ ტესტზე 5 შემთხვევითი კითხვა
    for i in range(1, 6):
        # შემთხვევითი რიცხვების გენერაცია (1-დან 10-მდე)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        
        # მოთამაშის შეყვანილი პასუხის მიღება
        try:
            answer = int(input(f"{i}) {num1} x {num2} = "))
            
            # პასუხის შემოწმება
            if answer == num1 * num2:
                print("სწორია! ✔")
                correct_answers += 1
            else:
                print(f"არასწორია. სწორი პასუხია {num1 * num2}.")
                
        except ValueError:
            print("გთხოვთ, შეიყვანოთ ციფრი.") 

    # საბოლოო შედეგის ჩვენება
    print(f"\nტესტის დასრულება! შენ დააგროვე {correct_answers} ქულა 5-დან.")

# ტესტის დაწყება
multiplication_quiz()
