import pandas as pd
import xml.etree.ElementTree as ET
from lxml import etree

# Example XML file
xml_data = '''
<root>
    <person>
        <name>John Doe</name>
        <age>30</age>
        <city>New York</city>
    </person>
    <person>
        <name>Jane Smith</name>
        <age>25</age>
        <city>London</city>
    </person>
</root>
'''
# Read the Excel file into a pandas DataFrame
df = pd.read_excel('input.xlsx')

# Create the root element for the XML
root = ET.Element('data')

# Iterate over the rows of the DataFrame
for _, row in df.iterrows():
    # Create a child element for each row
    item = ET.SubElement(root, 'item')

    # Iterate over the columns of the row
    for col_name, col_value in row.items():
        # Create a sub-element for each column
        sub_element = ET.SubElement(item, col_name)
        sub_element.text = str(col_value)

# Parsing XML data from file
root_element = ET.parse('sample.xml')

# Parsing XML data as string using ElementTree
root_element = ET.fromstring(xml_data)

# Access specific elements and their data using ElementTree
for person_element in root_element.findall('person'):
    name = person_element.find('name').text
    age = person_element.find('age').text
    city = person_element.find('city').text
    print(f"Name: {name}, Age: {age}, City: {city}")

# Parsing XML using lxml
lxml_root = etree.fromstring(xml_data)

# Access specific elements and their data using lxml
for person_element in lxml_root.xpath('person'):
    name = person_element.xpath('name/text()')[0]
    age = person_element.xpath('age/text()')[0]
    city = person_element.xpath('city/text()')[0]
    print(f"Name: {name}, Age: {age}, City: {city}")
