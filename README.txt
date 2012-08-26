**** USAGE *****
1. GET RATINGS:
Saves fetched data into file FILENAME

Warning: this could take a bit longer :) 

>>> import ratings
>>> r = ratings.Rating('USER_ID','NUM_RATINGS')
>>> r.read('FILENAME')

2. PARSE RATINGS:
Parse output from FILENAME and returns data - list of rated movies

>>> import parse
>>> p = parse.Result()
>>> f = p.get_raw_data(FILENAME)
>>> f[0]['movie']['title'] # returns first movie 
u'Super Size Me'

an example of one movie data slot:
>>> f[0]
# formated to be easier to find keywords
{
	u'movie': {
			u'mpaa': u'PG-13', 
			u'cast': [
				{u'id': 162659559, u'name': u'Morgan Spurlock'}, 
				{u'id': 162659562, u'name': u'Dr. Daryl Isaacs'}, 
				{u'id': 770690679, u'name': u'Alexandra Jamieson'}], 
			u'title': u'Super Size Me', 
			u'url': u'http://www.flixster.com/movie/super-size-me/', 
			u'poster': {u'mobile': u'http://content6.flixster.com/movie/25/38/253828_mob.jpg', 
			u'profile': u'http://content6.flixster.com/movie/25/38/253828_pro.jpg', 
			u'thumbnail': u'http://content6.flixster.com/movie/25/38/253828_tmb.jpg'}, 
			u'tomatometer': 93, 
			u'audienceScore': 69, 
			u'dvdReleaseDate': u'Sep 28, 2004', 
			u'consensus': u'Entertaining doc about the adverse effects of eating fast food.', 
			u'runningTime': u'1 hr. 36 min.', 
			u'synopsis': u'First-time director Morgan Spurlock takes a look at the subject of obesity in the United States, specifically zeroing in on the...', 
			u'year': 2003, 
			u'id': 10060, 
			u'vanity': u'super-size-me'}, 
	u'review': u'', 
	u'scoreCss': u'50', 
	u'lastUpdated': u'3 days ago', 
	u'score': u'5.0', 
	u'ratingSource': u'Flixster', 
	u'user': {u'id': USERID, u'firstName': u'NAME'}, 
	u'id': u'UID_10060'}




TODO:
1. search (movie name, rating, date,..)
2. nicer output
3. store to sqlite3 - easier to get data

