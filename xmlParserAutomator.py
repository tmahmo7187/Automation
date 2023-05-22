import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('example.xml')

# Get the root element
root = tree.getroot()

# Access specific elements and their attributes
for child in root:
    print(child.tag, child.attrib)

# Extract data from specific elements
element_data = root.find('element_name').text
