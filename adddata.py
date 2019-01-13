import pymsl
import pprint
import os
import pickle
import sys

"""
evironment variables:

NFLIXACCOUNTS: email and passwords in "user1:password1,user2:password2" format
NFLIXLOCATION: location of machine that code is running on
MOVIE: list of netflix movie IDs in "movie1,movie2" format
"""

def main(argv):
	assert(len(argv)) == 1
	DATA_FILE = argv[0]
	NFLIXLOCATION = "NFLIXLOCATION"
	NFLIXACCOUNTS = "NFLIXACCOUNTS"
	NFLIXMOVIES = "NFLIXMOVIES"

	file_path = os.path.dirname(os.path.realpath(__file__)) + '/' + DATA_FILE
	# reads current rankings data from disk
	try:
		file = open(file_path, 'rb')
		data = pickle.load(file)
		file.close()
	except FileNotFoundError:
		data = {}

	# retrieve cdn rankings
	location = os.environ[NFLIXLOCATION]
	account_numer = 1
	accounts = os.environ[NFLIXACCOUNTS].split(',')
	total = len(accounts)
	for account in accounts:
		email, password = account.split(':')
		print("getting data for account " + str(account_numer) + " of " + str(total))
		

		user_auth_data = {
			    'scheme': 'EMAIL_PASSWORD',
			    'authdata': {
			        'email': email,
			        'password': password
			    }
			 }
		client = pymsl.MslClient(user_auth_data)
		for movie in os.environ[NFLIXMOVIES].split(','):
			cdns = client.load_manifest(int(movie))["result"]["servers"]
			for c in cdns:
				data.setdefault(location, {}).setdefault(movie, {}).setdefault(c['rank'], {})[str(account_numer)] = c
		account_numer += 1

	# write back data to disk
	file = open(file_path, "wb")
	pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
	file.close()
main(sys.argv[1:])

