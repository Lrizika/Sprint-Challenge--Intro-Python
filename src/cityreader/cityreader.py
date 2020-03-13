#!/usr/bin/env python

import os
import csv

from typing import List, Union

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City:
	def __init__(
			self,
			name: str,
			lat: Union[float, int, str],
			lon: Union[float, int, str]
	):
		'''
		A city.

		Args:
			name (str): Name of the city.
			lat (Union[float, int, str]): Latitude.
			lon (Union[float, int, str]): Longitude.
		'''

		self.name = name
		self.lat = float(lat)
		self.lon = float(lon)

	def __repr__(self):
		return f'<{self.__class__.__name__}: "{self.name}", {self.lat}, {self.lon}>'


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.


# TODO Implement the functionality to read from the 'cities.csv' file
# For each city record, create a new City instance and add it to the
# `cities` list
CSV_FIELD_NAMES = ['city', 'state_name', 'county_name', 'lat',
	'lng', 'population', 'density', 'timezone', 'zips']


def cityreader(
		cities: List[City] = None,
		path: str = 'cities.csv',
		field_names: List[str] = CSV_FIELD_NAMES
) -> List[City]:
	'''
	Reads a CSV of cities into a list of City objects.

	Args:
		cities (List[City], optional): If provided, new City objects will be added to this list.
			If omitted, a new list of City objects will be created.
		path (str, optional): Defaults to 'cities.csv'. CSV file path.
		field_names (List[str], optional): Defaults to CSV_FIELD_NAMES. Format of the CSV.

	Returns:
		List[City]: A list of City objects from the CSV.
	'''

	# Avoid issues with mutable arguments
	if cities is None:
		cities = []

	with open(os.path.join(
			os.path.dirname(__file__),
			path), 'r'
	) as csv_file:
		reader = csv.DictReader(csv_file, field_names)
		next(reader)  # Skip the header
		for record in reader:
			cities.append(
				City(
					record['city'],
					record['lat'],
					record['lng'],
				)
			)

	return cities


cities = cityreader()

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
	print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user


def cityreader_stretch(lat1, lon1, lat2, lon2, cities):
	# within will hold the cities that fall within the specified region
	within = []

	min_lat = float(min(lat1, lat2))
	max_lat = float(max(lat1, lat2))
	min_lon = float(min(lon1, lon2))
	max_lon = float(max(lon1, lon2))

	for city in cities:
		if (
				city.lat <= max_lat and
				city.lat >= min_lat and
				city.lon <= max_lon and
				city.lon >= min_lon
		):
			within.append(city)

	return within
