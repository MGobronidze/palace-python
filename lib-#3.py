import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. მონაცემთა გენერაცია
ages = np.random.randint(15, 66, size=100)
incomes = np.random.randint(500, 5001, size=100)
product_scores = np.random.randint(1, 11, size=100)

# 2. მონაცემთა ჩატვირთვა DataFrame-ში
data = pd.DataFrame({
    'Age': ages,
    'Income': incomes,
    'Product_Score': product_scores
})

# 3. მონაცემთა ანალიზი
print("Age Statistics:")
print(data['Age'].describe())

print("\nIncome Statistics:")
print(f"Mean: {data['Income'].mean()}, Median: {data['Income'].median()}")

print("\nFiltered Data:")
filtered_data = data[(data['Income'] > 3000) & (data['Product_Score'] > 8)]
print(filtered_data)

# 4. ვიზუალიზაცია
plt.figure(figsize=(10, 6))

# ჰისტოგრამა ასაკისთვის
plt.subplot(2, 2, 1)
plt.hist(data['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution')

# ხაზოვანი დიაგრამა ასაკსა და შემოსავალს შორის
plt.subplot(2, 2, 2)
plt.plot(data['Age'], data['Income'], 'o-', color='orange')
plt.title('Age vs Income')

# Scatter Plot შემოსავალსა და პროდუქტის ქულას შორის
plt.subplot(2, 2, 3)
plt.scatter(data['Income'], data['Product_Score'], color='green')
plt.title('Income vs Product Score')

plt.tight_layout()
plt.show()
