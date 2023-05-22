import pandas as pd

# Read the Excel file
data = pd.read_excel('data.xlsx')

# Parsing and Extracting Data
name = data['Name']
age = data['Age']
skills = data['Skills']

# Transforming Data
uppercase_name = name.str.upper()
birth_year = pd.datetime.now().year - age
formatted_skills = skills.str.replace(',', ', ')

# Printing the Extracted and Transformed Data
print("Name:", uppercase_name)
print("Age:", age)
print("Birth Year:", birth_year)
print("Skills:", formatted_skills)
