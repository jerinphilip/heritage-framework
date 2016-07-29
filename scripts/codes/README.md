The proposed design of the Web app + Android app -

* The submit form in the web will create a new entry in the database interest\_points table with the name, location, caption, images\_store\_paths and info as per the xml format being used by Harshil
* The script gen_xml.py can be used to get all the data in the desired xml format
* For fetching latitude and logitude from an image (for the purposes of returning the images in the vicinity of an interest point location), the script read_data.py can be used
* To add the latitude and longitude data to an image submitted in the web form, the script write_data.py can be used. This ensures that all the images have GPS content (fetched from the Golconda map coordinate system in the web interface).
