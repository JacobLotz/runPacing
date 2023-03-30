import datetime

def roundMicroseconds(time):
	"""
   Function that rounds datetime data objects to seconds.
	"""
	time += datetime.timedelta(seconds=round(time.microseconds/1000000))
	time -= datetime.timedelta(microseconds=time.microseconds)
	return time

def calcPacing(dist, hours = 0, minutes = 0, seconds = 0, printresult = True):
	"""
	Function that calculates the required pace based on the given distance
	(in km) and goal time (in hours, minutes and seconds).
	The function prints all data and returns the pacing in a datetime object.
	"""
	# Create time object
	time = datetime.timedelta(hours = hours, minutes =  minutes, seconds = seconds)

	# Velocity per km
	pace = time/dist;

	# Round
	pace = roundMicroseconds(pace)

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
	time = pace*dist;

	# Round
	time = roundMicroseconds(time)

	if (printresult == True):
		print("Distance: " + str(dist) + "    Pace: " + str(pace) + "    Running time: " + str(time))
	return time;