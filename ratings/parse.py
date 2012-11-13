# !/usr/bin/python 

"""
Main file for analizing and returning results
Currently returns only raw_data:

list of movies in format:
{u'movie': {u'mpaa': u'PG-13', u'cast': [{u'id': 162659559, u'name': u'Morgan Spurlock'}, 
{u'id': 162659562, u'name': u'Dr. Daryl Isaacs'}, {u'id': 770690679, u'name': u'Alexandra Jamieson'}], 
u'title': u'Super Size Me', u'url': u'http://www.flixster.com/movie/super-size-me/', 
u'poster': {u'mobile': u'http://content6.flixster.com/movie/25/38/253828_mob.jpg', 
u'profile': u'http://content6.flixster.com/movie/25/38/253828_pro.jpg', 
u'thumbnail': u'http://content6.flixster.com/movie/25/38/253828_tmb.jpg'}, 
u'tomatometer': 93, u'audienceScore': 69, u'dvdReleaseDate': u'Sep 28, 2004', 
u'consensus': u'Entertaining doc about the adverse effects of eating fast food.', 
u'runningTime': u'1 hr. 36 min.', u'synopsis': u'First-time director Morgan Spurlock 
takes a look at the subject of obesity in the United States, specifically zeroing in on the...', 
u'year': 2003, u'id': 10060, u'vanity': u'super-size-me'}, u'review': u'', u'scoreCss': u'50', 
u'lastUpdated': u'3 days ago', u'score': u'5.0', u'ratingSource': u'Flixster', 
u'user': {u'id': xyz, u'firstName': u'xyz'}, u'id': u'xyz_10060'}

TODO: 
- add search(based on movie title, score, ...) 
- add nicer output 
- import to sqlite db
	
"""
import json
import io
import csv

class Result(object):

    def __init__(self):
        """ """

    def get_raw_data(self, filename):
        """ returns raw data - movies list after parsing json """
        f = io.open(filename, 'r', encoding='latin-1')		
        data = json.loads(f.readline())
        f.close()
        return data
    
    def export_file(self, input_filename, output_filename):
        """ export to .csv file """
        f = io.open(input_filename, 'r', encoding='latin-1')
        data = json.loads(f.readline())
        f.close()
        f = csv.writer(open(output_filename, 'wb+'))
        f.writerow(['title', 'score'])
        for element in data:
            row = [element['movie']['title'], element['score']]
            f.writerow([unicode(s).encode("utf-8") for s in row])
