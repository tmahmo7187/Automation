def compare_xsd_files(previous_xsd_file, current_xsd_file):
    with open(previous_xsd_file, 'r') as previous_file:
        previous_content = previous_file.read()
    
    with open(current_xsd_file, 'r') as current_file:
        current_content = current_file.read()
    
    if previous_content == current_content:
        print("XSD files are identical.")
    else:
        print("XSD files have differences.")

previous_xsd_file = "path/to/previous.xsd"
current_xsd_file = "path/to/current.xsd"

compare_xsd_files(previous_xsd_file, current_xsd_file)
