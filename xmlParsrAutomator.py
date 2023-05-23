import pandas as pd
from bs4 import BeautifulSoup           #  API for extracting data from HTML or XML documents
import xml.sax                          # event-driven parsing approach
import xml.dom.minidom as minidom       # allows you to parse an XML document into a DOM tree, navigate the tree structure using methods like getElementsByTagName(), 
import xml.etree.ElementTree as ET
from lxml import etree                  # easy-to-use interface for XML and HTML parsing

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

# Reading in from file and establishing the root element.
tree = ET.parse('country_data.xml')
root = tree.getroot()

# Reading in from string:
root = ET.fromstring(country_data_as_string)

# After having parsed your file, you can use the handle to write to file again:
tree.write("{name}.xml".format(name=myname))

# Getting data from the XML tree:
#(Here, for “child” you can put in any “child” or “subchild” of the file)

for mychild in root.iter('child'):
    print(mychild.attrib)
    
# Every child has attributes, that is called by child.attrib and a text that is it covering child.text, both of which can be called and changed.
# Changing data:
for child in root.iter('child'):
    change_text = "fart{}".format(child.text) 
    child.text = change_text
    child.set('attribute', 'change')
    
 # Removing childs:
for child in root.findall('child'):
    rank = int(child.find('rank').text)
    if rank > 50:
        root.remove(child)
        
# Building XML:
  # building elements
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
  #showing tree
ET.dump(a)       
