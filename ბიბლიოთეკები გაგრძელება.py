# 1. აუცილებელი ბიბლიოთეკების ინსტალაცია
# დარწმუნდით, რომ NumPy, Pandas და Matplotlib არის დაინსტალირებული. შეგიძლიათ გამოიყენოთ შემდეგი ბრძანება:
# pip install numpy pandas matplotlib

# 2. ბიბლიოთეკების ჩატვირთვა
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#მონაცემთა შესაქმნელად გამოიყენეთ Pandas DataFrame. მაგალითი:
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Math": [85, 92, 78, 88, 95],
    "Science": [90, 89, 95, 86, 80],
    "History": [78, 85, 88, 92, 84],
}

df = pd.DataFrame(data)
print(df)

#გამოიყენეთ NumPy საშუალო, მაქსიმალური და მინიმალური ქულების დასათვლად:

# თითოეული მოსწავლის საშუალო ქულა
df["Average"] = df[["Math", "Science", "History"]].mean(axis=1)

# საუკეთესო და ყველაზე დაბალი ქულები
max_scores = df[["Math", "Science", "History"]].max().to_dict()
min_scores = df[["Math", "Science", "History"]].min().to_dict()

print("საუკეთესო ქულები თითოეულ საგანში:", max_scores)
print("ყველაზე დაბალი ქულები თითოეულ საგანში:", min_scores)


#შექმენით დიაგრამა, რომელიც აჩვენებს მოსწავლეების საშუალო ქულებს:

# მოსწავლეების სახელები და საშუალო ქულები
names = df["Name"]
averages = df["Average"]

plt.bar(names, averages, color="skyblue")
plt.title("მოსწავლეების საშუალო ქულები")
plt.xlabel("მოსწავლეები")
plt.ylabel("საშუალო ქულა")
plt.ylim(0, 100)
plt.show()


#შექმენით ხაზოვანი გრაფიკი, რომელიც აჩვენებს თითოეული მოსწავლის ქულების დინამიკას საგნებში:

# თითოეული მოსწავლის ქულების დინამიკა
for name in df["Name"]:
    scores = df[df["Name"] == name][["Math", "Science", "History"]].values.flatten()
    plt.plot(["Math", "Science", "History"], scores, marker="o", label=name)

plt.title("მოსწავლეების ქულების დინამიკა")
plt.xlabel("საგნები")
plt.ylabel("ქულები")
plt.legend(title="მოსწავლეები")
plt.grid()
plt.show()


#დაუმატეთ ფუნქცია, რომელიც მოსწავლეებს საშუალებას მისცემს, ახალი მონაცემები შეიყვანონ პროგრამულად:
def add_student():
    name = input("შეიყვანეთ მოსწავლის სახელი: ")
    math = int(input("შეიყვანეთ მათემატიკის ქულა: "))
    science = int(input("შეიყვანეთ ბუნებისმეტყველების ქულა: "))
    history = int(input("შეიყვანეთ ისტორიის ქულა: "))
    
    new_data = {"Name": name, "Math": math, "Science": science, "History": history}
    global df
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df["Average"] = df[["Math", "Science", "History"]].mean(axis=1)

add_student()
print(df)


#შექმენით პი-დიაგრამა, რომელიც აჩვენებს თითო საგნის წილს საერთო ქულებში:

# თითო საგნის წილი
subject_totals = df[["Math", "Science", "History"]].sum()

plt.pie(
    subject_totals, 
    labels=subject_totals.index, 
    autopct="%1.1f%%", 
    startangle=90, 
    colors=["lightcoral", "lightblue", "lightgreen"]
)
plt.title("საგნების წილი საერთო ქულებში")
plt.show()


#გამოიყენეთ სხვადასხვა ფერები, რათა დაბალი და მაღალი საშუალო ქულები გამოარჩიოთ:

colors = ["green" if avg >= 85 else "red" for avg in df["Average"]]

plt.bar(df["Name"], df["Average"], color=colors)
plt.title("მოსწავლეების საშუალო ქულები (ფერების მიხედვით)")
plt.xlabel("მოსწავლეები")
plt.ylabel("საშუალო ქულა")
plt.ylim(0, 100)
plt.show()


#დაამატეთ ფუნქცია, რომელიც სორტირებას გააკეთებს საშუალო ქულების მიხედვით:
def sort_students(by="Average", ascending=False):
    global df
    df = df.sort_values(by=by, ascending=ascending)
    print(df)

# სორტირება საშუალო ქულების მიხედვით კლებადობით
sort_students()





