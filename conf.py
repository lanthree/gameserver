import xml.etree.ElementTree as ET

if __name__ == "__main__":
	tree = ET.parse("./conf/conf.xml")
	root = tree.getroot()

	print(root.tag)
	print(root.attrib)

	for child in root:
		print(child.tag, child.attrib, child.text)
	
