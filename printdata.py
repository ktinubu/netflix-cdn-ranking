
import pprint
import sys
import pickle

def main(argv):
	assert (len(argv)) > 0
	assert (len(argv)) < 3
	file = open(argv[0], "rb")
	first_data = pickle.load(file)
	file.close()
	for i in range(len(argv)):
		file = open(argv[0], "rb")
		data = pickle.load(file)
		file.close()
		pp = pprint.PrettyPrinter(width=41, compact=True)
		pp.pprint(data)
		if i != 0:
			if data == first_data:
				print("manifest data " + str(i+1) + " is the same as manifest data 0")
			else:
				print("manifest data " + str(i+1) + " is different to manifest data 0")

main(sys.argv[1:])