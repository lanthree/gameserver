import xml.etree.ElementTree as ET

def init_conf(conf_file):
	tree = ET.parse(conf_file)
	root = tree.getroot()

	conf = {}
	for child in root:
		conf[child.tag] = {"text":child.text, "attr": child.attrib}
	return conf

conf = init_conf("./conf/conf.xml")

if __name__ == "__main__":
	print(conf)
