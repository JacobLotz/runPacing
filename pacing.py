import datetime

def devideDateTime(time, divider):
   """
   Function that converts date time to a total of seconds and
   performs a devision. Converts seconds back to datetime format.
   """
   totals  = time.total_seconds() 
   totals /= divider

   return datetime.timedelta(seconds = totals)

def multiplyDateTime(time, mult):
   """
   Function that converts date time to a total of seconds and
   performs a devision. Converts seconds back to datetime format.
   """
   totals  = time.total_seconds() 
   totals *= mult

   return datetime.timedelta(seconds = totals)

def roundToSeconds(time):
   """
   Function that rounds datetime data objects to seconds.
   """
   ms = time.microseconds

   if ms >= 500000:
      time += datetime.timedelta(seconds=1)

   return time - datetime.timedelta(microseconds = ms)

def calcPacing(dist, hours = 0, minutes = 0, seconds = 0, printresult = True):
	"""
	Function that calculates the required pace based on the given distance
	(in km) and goal time (in hours, minutes and seconds).
	The function prints all data and returns the pacing in a datetime object.
	"""
	# Create time object
	time = datetime.timedelta(hours = hours, minutes =  minutes, seconds = seconds)

	# Velocity per km
	pace = devideDateTime(time, dist)

	# Round
	pace = roundToSeconds(pace)

	if (printresult == True):	
		print("Distance: " + str(dist) + "    Running time: " + str(time) + "    Pace: " + str(pace))
	return pace;

def calcRevPacing(dist, minutes = 0, seconds = 0, printresult = True):
	"""
	Function that calculates the goal time based on the given distance
	(in km) and pacing (in minutes and seconds).
	The function prints all data and returns the goal time in a datetime object.
	"""
	# Create time object
	pace = datetime.timedelta(minutes =  minutes, seconds = seconds)

	# Velocity per km
	time = multiplyDateTime(pace, dist);

	# Round
	time = roundToSeconds(time)

	if (printresult == True):
		print("Distance: " + str(dist) + "    Pace: " + str(pace) + "    Running time: " + str(time))
	return time;
	