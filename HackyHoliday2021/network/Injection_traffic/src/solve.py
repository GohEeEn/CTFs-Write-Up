#!/usr/bin/env python3

from pyshark import *
import re


"""
Credit goes to : Cryptocat (https://www.youtube.com/watch?v=u1Sh5TZN5Ug&t=435s)

References :

- https://github.com/KimiNewt/pyshark
- https://docs.python.org/3/howto/regex.html
"""

capture = FileCapture('./traffic.pcap')

# Fake flag to be updated as pcap processed
flag = list("CTF{deadbeefdeadc0dedeadbeefdeadc0de}")


for i, packet in enumerate(capture):

	try:

		sql_query = packet.tds.query

		if 'SUBSTRING' in sql_query:

			# If the response length is 200 then the query request gets a successful response
			if capture[i + 1].length == '200':

				# Extract the char position and decimal value
				# Example : SELECT * FROM articles where article_id = 100 AND
				# UNICODE(SUBSTRING((SELECT TOP 1 ISNULL(CAST(master..syscolumns.name AS NVARCHAR(4000)),CHAR(32))
				# FROM master..syscolumns,master..sysobjects WHERE master..syscolumns.id=master..sysobjects.id
				# AND master..sysobjects.name=CHAR(101)+CHAR(110)+CHAR(99)+CHAR(114)+CHAR(121)+CHAR(112)+CHAR(116)+CHAR(105)+CHAR(111)+CHAR(110)+CHAR(95)+CHAR(107)+CHAR(101)+CHAR(121)+CHAR(115)
				# AND master..syscolumns.name NOT IN (SELECT TOP 0 master..syscolumns.name FROM master..syscolumns,master..sysobjects
				# WHERE master..syscolumns.id=master..sysobjects.id
				# AND master..sysobjects.name=CHAR(101)+CHAR(110)+CHAR(99)+CHAR(114)+CHAR(121)+CHAR(112)+CHAR(116)+CHAR(105)+CHAR(111)+CHAR(110)+CHAR(95)+CHAR(107)+CHAR(101)+CHAR(121)+CHAR(115)
				# ORDER BY master..syscolumns.name) ORDER BY master..syscolumns.name),1,1))>107

				# Extracted will be : ,1,1))>107
				extracted = re.match(r'.*,(\d+),\d+\)\)\>(\d+)', sql_query, re.M | re.I)
				char_index = extracted.group(1)
				char_value = extracted.group(2)

				# Update the flag : -1 because array index starts with 0, while +1 as great than '>' was used in the success full SQLi payload instead of greater or equal
				flag[int(char_index) - 1] = chr(int(char_value) + 1)

	except AttributeError as e:
		pass

# Output the flag
print(''.join(flag))