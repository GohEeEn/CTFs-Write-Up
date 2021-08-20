#!/usr/bin/env python3


"""
	HackyHolidays2021 Crypto challenge - Cute Invoice

	Reference : https://www.youtube.com/watch?v=u1Sh5TZN5Ug&t=2292s (Crypto-cat)

"""


# ALLCHARS : All characters enabled on QtPass
# Reference : https://github.com/IJHack/QtPass/blob/master/src/passwordconfiguration.h
charset = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-+={}[]|:;<>,.?')
pwd_len = 16	# Password length

# file = open("qtpass_list.txt", "a+")

# QTime::msec indicates this is merely "the millisecond part (0 to 999) of the time", eg. only 1000 possibilities of generated sequences of passwords
# Reference : https://github.com/IJHack/QtPass/issues/338
for x in range(1, 1000):

	password = ''


	# The generator has a single value as state, which is modified by its transition algorithm on each advance
	# ie. Util::rand() == (x = x * 48271 % 2147483647)
	# Reference : http://www.cplusplus.com/reference/random/minstd_rand/
	state = x * 48271 % 2147483647

	for i in range(pwd_len):

		index = state % len(charset)		# int index = Util::rand() % charset.length();
		nextChar = charset[index]			# QChar nextChar = charset.at(index);
		password += str(nextChar)			# passwd.append(nextChar);
		state = state * 48271 % 2147483647

	print(str(password))					# Generate relevant password list
