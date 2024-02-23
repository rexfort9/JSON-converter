JSON to XML Converter
====
This script is a simple GUI application that allows to convert JSON data into XML format using the [Python Tkinter](https://docs.python.org/3/library/tkinter.html) module for the graphical interface, json module for parsing JSON data, and [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html) module for generating XML output.
----

How the Script Works <br>
----
Operation <br>
	• import the necessary modules: tkinter for creating the GUI, json for handling JSON data, and xml.etree.ElementTree for working with XML data <br> 
	• convert_json_to_xml() function is defined to convert JSON data to XML format. It reads the JSON data inputted by the user, converts it to a Python dictionary using json.loads(), and then calls the dict_to_xml() function to convert the dictionary into XML format <br>
	• dict_to_xml() function recursively converts a Python dictionary into an XML element structure using the ElementTree module <br>
	• the main window of the GUI application is created using tk.Tk() and set the title to "JSON to XML Converter <br>
	• adds necessary widgets, like asking labels, inputting widget, button-trigger the conversion, result label, text widget displaying XML output data <br>

Additional Notes <br>
----
The script handles errors by displaying a message if the input JSON data is invalid<br>
The conversion process involves parsing the JSON data into a Python dictionary and constructing the equivalent XML structure before displaying the result.

<br>
### TO RUN IT: <br>
• Run the script in a Python environment that supports the Tkinter GUI library <br>
• Enter the JSON data in the input box and click the "Convert" button to generate the corresponding XML output
