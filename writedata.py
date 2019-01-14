
import pprint
import sys
import pickle
import csv

def main(argv):
	assert len(argv) == 2
	csv_file_name = argv[0]
	data_file_name = argv[1]

	file = open(data_file_name, 'rb')
	data = pickle.load(file)
	file.close()

	file.close()
	with open(csv_file_name, mode='w') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(['location', 'movie', 'rank', 'account', 'ipv4', 'cdn_name', 'cdn_id'])

		for location, l_dict in data.items():
			for movie, m_dict in l_dict.items():
				for rank, e_dict in m_dict.items():
					for account, cdn in e_dict.items():
						ipv4 = cdn['dns']['ipv4']
						cdn_name = cdn['name']
						cdn_id = cdn['id']
						writer.writerow([location, movie, rank, account, ipv4, cdn_name, cdn_id])
main(sys.argv[1:])