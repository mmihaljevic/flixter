# !/usr/bin/python

""" 
	get ratings
"""

import url_opener


class Rating(object):


	def __init__(self, user_ID, num_ratings):
		""" defines url based on given user id and number of ratings """		
		if user_ID is None:
			raise KeyError('user id cannot be empty')	
		if num_ratings is None:
			raise KeyError('number of ratings must be set')

		self.opener = url_opener.UrlOpener()
		self.url = "http://www.flixster.com/api/users/%s/movies/ratings?scoreTypes=numeric&page=1&limit=%s" % (user_ID, num_ratings)


	def read(self, filename):
		""" reads data from url and saves it to filename """
		if filename is None:
			raise KeyError('filename must be set')

		data = self.opener.open(self.url)
		content = data.read().strip()

		with open(filename, 'w') as f:
			f.write(content)
