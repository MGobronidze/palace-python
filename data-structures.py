# 📌 მომხმარებელთა მონაცემთა ბაზა (ლექსიკონი)
users_db = {}  
user_ids = set()  # უნიკალური ID-ების შესანახად

# 📌 ახალი მომხმარებლის დამატება
def add_user(user_id, name, age, city):
    if user_id in user_ids:
        print("❌ ეს ID უკვე არსებობს!")
        return
    users_db[user_id] = [name, age, city]  # ინფორმაცია სიაში ვინახავთ
    user_ids.add(user_id)  # ID-ს ვამატებთ set-ში
    print(f"✅ {name} წარმატებით დაემატა!")

# 📌 მომხმარებლის მოძიება ID-ის მიხედვით
def get_user(user_id):
    return users_db.get(user_id, "❌ ასეთი მომხმარებელი არ არსებობს!")

# 📌 მომხმარებლის განახლება
def update_user(user_id, name=None, age=None, city=None):
    if user_id not in users_db:
        print("❌ ასეთი მომხმარებელი არ არსებობს!")
        return
    if name:
        users_db[user_id][0] = name
    if age:
        users_db[user_id][1] = age
    if city:
        users_db[user_id][2] = city
    print(f"✅ {user_id}-ის მონაცემები განახლდა!")

# 📌 ყველა მომხმარებლის ჩვენება
def show_users():
    if not users_db:
        print("📭 მონაცემთა ბაზა ცარიელია!")
    else:
        print("\n📋 მომხმარებელთა სია:")
        for user_id, data in users_db.items():
            print(f"🆔 {user_id}: {data[0]}, {data[1]} წლის, {data[2]}")

# 📌 მომხმარებლის წაშლა
def delete_user(user_id):
    if user_id in users_db:
        del users_db[user_id]
        user_ids.remove(user_id)
        print(f"🗑️ {user_id} წაიშალა!")
    else:
        print("❌ ასეთი მომხმარებელი არ არსებობს!")

# 📌 ტესტირება
add_user(1, "გიორგი", 25, "თბილისი")
add_user(2, "ანა", 22, "ბათუმი")
add_user(3, "ლევანი", 30, "ქუთაისი")

print("\n🔍 მომხმარებლის ძიება ID 2:")
print(get_user(2))  # ანა, 22 წლის, ბათუმი

update_user(2, age=23)  # ანას ასაკის განახლება
show_users()  # ყველა მომხმარებლის ჩვენება

delete_user(1)  # გიორგი წაიშალა
show_users()  # დარჩენილი მომხმარებლები
