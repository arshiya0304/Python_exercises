import pandas as pd

data = {
    "name": ["Arjun", "Priya", "Sanjay", "Divya", "Rohit", "Sneha"],
    "department": ["IT", "IT", "DevOps", "HR", "Finance", "IT"],
    "salary": [55000, 72000, 68000, 48000, 91000, 83000]
}

df = pd.DataFrame(data)

threshold = df["salary"].quantile(0.75)

result = df[df["salary"] > threshold]

print("75th Percentile Salary:", threshold)
print("\nEmployees above 75th percentile:")
print(result)