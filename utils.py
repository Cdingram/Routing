GOOGLE_API_FILE = "google_api.txt"

def get_google_api_key():
	with open(GOOGLE_API_FILE, 'r') as my_file:
		key = my_file.readline()

	return key