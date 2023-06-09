import datetime
from pacing import *

"""
This file tests the functions in pacing.py
"""
def test_roundToSeconds():
   ref_time = datetime.timedelta(minutes = 14, seconds = 10)
   test_time = datetime.timedelta(hours = 1, minutes = 39, seconds = 7)

   test_time /= 7
   
   test_time = roundToSeconds(test_time)

   assert test_time == ref_time, "Other value expected"

def test_calcPacing():
   ref_pace = datetime.timedelta(minutes = 6)
   test_dist = 10

   test_pace = calcPacing(test_dist, hours = 1, minutes = 0, seconds = 0, printresult = False)
   assert test_pace == ref_pace, "Other value expected"

   test_pace = calcPacing(test_dist, hours = 1, printresult = False)
   assert test_pace == ref_pace, "Other value expected"

def test_calcRevPacing():
	test_dist = 10
	ref_time = datetime.timedelta(hours = 1)

	test_time = calcRevPacing(test_dist, minutes = 6, seconds = 0, printresult = False)

	assert test_time == ref_time, "Other value expected"

def test_devideDateTime():
	test_time = datetime.timedelta(minutes = 30, microseconds = 30)
	ref_time = datetime.timedelta(minutes = 8, seconds = 34, microseconds = 285723)

	test_time = devideDateTime(test_time, 3.5)

	assert test_time == ref_time, "Other value expected"

def test_multiplyDateTime():
	test_time = datetime.timedelta(minutes = 30, microseconds = 30)
	ref_time = datetime.timedelta(hours = 1, minutes = 15, microseconds = 75)

	test_time = multiplyDateTime(test_time, 2.5)

	assert test_time == ref_time, "Other value expected"
