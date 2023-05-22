import json
#Assume Json file below
'''
{
  "name": "Talat Mahmood",
  "age": 48,
  "skills": ["Python", "Ai", "SQL"]
}
'''

# Read the JSON file
with open('data.json') as file:
    data = json.load(file)

# Parsing and Extracting Data
name = data['name']
age = data['age']
skills = data['skills']

# Transforming Data
uppercase_name = name.upper()
birth_year = 2023 - age
formatted_skills = ', '.join(skills)

# Printing the Extracted and Transformed Data
print(f"Name: {uppercase_name}")
print(f"Age: {age} (Birth Year: {birth_year})")
print(f"Skills: {formatted_skills}")
