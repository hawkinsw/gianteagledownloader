#!/bin/env python3

from bs4 import BeautifulSoup
import requests

class GiantEagleQuery:
	def __init__(self, latitude: float, longitude: float):
		self.latitude = latitude
		self.longitude = longitude

	def __repr__(self):
		return "{\"storeData\":\"\",\"loggedIn\":0," + \
			"\"lat\":" + str(self.latitude) + "," + \
			"\"lng\":" + str(self.longitude) + "}"

class GiantEagle:
	def __init__(self, soup: BeautifulSoup):
		self.soup = soup

class GiantEagleQueryDownloader:
	def __init__(self, query: GiantEagleQuery):
		self.cookies = {}
		self.query = {}
		self.headers = {}
		self.query["formParams"] = str(query)
		self.url = "http://gianteagle.medrefill.com/geweb/getStoreList.htm"


	def post(self):
		safety_response = requests.post("https://gianteagle.medrefill.com/geweb/appload.htm")
		csrfToken = safety_response.json()["token"][0]
		self.headers["csrfPreventionSalt"] = csrfToken
		return requests.post(self.url, cookies = safety_response.cookies, data=self.query, headers = self.headers)

if __name__ == "__main__":
	# First, do the download.

	geq = GiantEagleQuery(40.4172871, -82.90712300000001)
	geqd = GiantEagleQueryDownloader(geq)

	print(geqd.post().json()["data"]["stores"])
