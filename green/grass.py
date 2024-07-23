import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Add a new column
df['Salary'] = [50000, 60000, 70000, 80000]

# Filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]

# Sort DataFrame by 'Salary' in descending order
sorted_df = df.sort_values(by='Salary', ascending=False)

# Group by 'City' and calculate the mean Age
grouped_df = df.groupby('City')['Age'].mean()

# Display the results
print("\nDataFrame with New Column:")
print(df)

print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

print("\nSorted DataFrame by Salary:")
print(sorted_df)

print("\nGrouped DataFrame by City with Mean Age:")
print(grouped_df)