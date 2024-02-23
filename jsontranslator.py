import tkinter as tk
import json
import xml.etree.ElementTree as ET

def convert_json_to_xml():
    input_json = json_input.get("1.0", "end-1c")
    try:
        json_data = json.loads(input_json)
        xml_data = dict_to_xml(json_data)
        xml_output.delete("1.0", tk.END)
        xml_output.insert(tk.END, xml_data)
    except json.JSONDecodeError as e:
        xml_output.delete("1.0", tk.END)
        xml_output.insert(tk.END, "Error: Invalid JSON format")

def dict_to_xml(d):
    root = ET.Element('root')
    def _dict_to_xml(parent, d):
        for key, value in d.items():
            if isinstance(value, dict):
                elem = ET.Element(key)
                parent.append(elem)
                _dict_to_xml(elem, value)
            else:
                elem = ET.Element(key)
                elem.text = str(value)
                parent.append(elem)
    _dict_to_xml(root, d)
    return ET.tostring(root, encoding='unicode')

# Create the main window
root = tk.Tk()
root.title("JSON to XML Converter")

# Create widgets
tk.Label(root, text="Enter JSON:").pack()
json_input = tk.Text(root, height=5, width=50)
json_input.pack()

convert_button = tk.Button(root, text="Convert", command=convert_json_to_xml)
convert_button.pack()

tk.Label(root, text="Result XML:").pack()
xml_output = tk.Text(root, height=5, width=50)
xml_output.pack()

# Start the main loop
root.mainloop()