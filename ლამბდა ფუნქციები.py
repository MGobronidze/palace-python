from functools import reduce

# გლობალური ცვლადი
students_scores = [56, 78, 90, 65, 87, 92, 45, 89, 74, 53]

def analyze_scores():
    # ლოკალური სქოუფი
    passing_score = 60  # ქულა, რომელიც განსაზღვრავს ჩაბარებას

    # Map: ყველა ქულას გავზრდით 5 ქულით (ბონუს ქულები)
    adjusted_scores = list(map(lambda x: x + 5, students_scores))
    print("Adjusted Scores (with bonus):", adjusted_scores)

    # Filter: ფილტრავს მხოლოდ ჩაბარებული სტუდენტების ქულებს
    passing_scores = list(filter(lambda x: x >= passing_score, adjusted_scores))
    print("Passing Scores:", passing_scores)

    # Reduce: გამოთვლის ჩაბარებული სტუდენტების ქულების ჯამს
    total_passing_score = reduce(lambda x, y: x + y, passing_scores)
    print("Total Passing Score:", total_passing_score)

    # Nested Function: საშუალო ქულის გამოთვლა
    def calculate_average(scores):
        return sum(scores) / len(scores)

    # ლოკალური ფუნქციის გამოყენება
    average_score = calculate_average(students_scores)
    print("Average Score of All Students:", round(average_score, 2))

# ფუნქციის გამოძახება
analyze_scores()
