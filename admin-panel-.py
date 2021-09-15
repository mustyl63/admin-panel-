#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Lutfen Siteyi Giriniz: \n(site www.example.com ): ")
	print "\n\nPanel Araniyor.... : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(9); print "############################"
	Space(9); print "#   Yapan Chinger          #"
	Space(9); print "#   Yardimci Stranger5     #"
	Space(9); print "#   Turk Hack Team Turkiye #"
	Space(9); print "############################"

Credit()
findAdmin()
