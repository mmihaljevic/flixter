#! /usr/bin/python

"""
Nice way to trick Flixter - change userAgent so we don't get 403 :)

"""

from urllib import FancyURLopener

class UrlOpener(FancyURLopener):

	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


