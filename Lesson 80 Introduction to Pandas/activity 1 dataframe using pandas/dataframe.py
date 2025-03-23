import pandas as pd

# Create a dictionary with data
data = {
    'Name': ['Martha', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['Dallas', 'Los Angeles', 'New Jersey', 'Houston']
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)