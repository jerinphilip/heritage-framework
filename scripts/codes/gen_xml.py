"""Module to genarate xml file for a heritage site.
"""

import sys
import sqlite3
import read_data 
import xml.etree.cElementTree as element_tree

def generate_xml(db_filename, store_path):
    """Generates and stores the xml file.
    """
    try:
        conn = sqlite3.connect(db_filename)
        conn.execute('SELECT * FROM haritage')
    except:
        print "DB Connection Error"

    monument = element_tree.Element("monument")
    
    # there will be a for loop here for all the interest points in database
    interest_point = element_tree.SubElement(monument, "ip")
    element_tree.SubElement(interest_point, "title").text = "ip title"
    element_tree.SubElement(interest_point, "lat").text = "ip lat"
    element_tree.SubElement(interest_point, "long").text = "ip long"
    element_tree.SubElement(interest_point, "caption").text = "ip caption"
    element_tree.SubElement(interest_point, "image").text = "ip image"
    element_tree.SubElement(interest_point, "info").text = "ip info"

    xml_tree = element_tree.ElementTree(monument)
    xml_tree.write(store_path + 'heritage.xml')

if __name__ == "__main__":
    generate_xml(sys.argv[1], sys.argv[2])
