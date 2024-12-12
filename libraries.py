# Project: Understanding Popular Python Libraries and pip Usage

# This project demonstrates the installation and basic usage of popular Python libraries: NumPy, Pandas, and Matplotlib.
# Follow the examples below to understand their functionalities.

# Step 1: Installing Libraries using pip
# Open your terminal or command prompt and run the following commands to install the libraries:
# pip install numpy
# pip install pandas
# pip install matplotlib

# Step 2: Using NumPy for Numerical Operations
import numpy as np

# Creating a NumPy array
array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", array)

# Performing basic operations
print("Array Mean:", np.mean(array))
print("Array Standard Deviation:", np.std(array))
print("Array Squared:", array ** 2)

# Step 3: Using Pandas for Data Manipulation
import pandas as pd

# Creating a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

# Analyzing the DataFrame
print("\nAverage Age:", df['Age'].mean())
print("\nSalary Statistics:")
print(df['Salary'].describe())

# Step 4: Using Matplotlib for Data Visualization
import matplotlib.pyplot as plt

# Plotting a simple line chart
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y, label='y = x^2', color='blue', marker='o')
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()

# Plotting a bar chart
names = df['Name']
salaries = df['Salary']

plt.bar(names, salaries, color='green')
plt.title('Salaries by Name')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()

# Additional Matplotlib Project: Pie Chart
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 30, 20, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Programming Language Popularity')
plt.show()


