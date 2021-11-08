# Lief Johnson
# joh19151
# CSCI 1133 Section 050
# Assignment 2

#==========================================
# Purpose: min_conversion takes a minute value, checks if it's greater than or equal to 60, and if so, subtracts 60 from it
# Input Parameter(s): min represents the number of minutes
# Return Value(s): the final min value. If min >= 60, that's the min value - 60, but if not, it's just min
#==========================================

def min_conversion(min):
	if min >= 60:
		min -= 60
	return min

#==========================================
# Purpose: oral_exam_sign_up prints out a list of 10-minute time slots and the amount of time slots available, while also taking into account a lunch period of 30 minutes and a gap of 5 minutes between slots
# Input Parameter(s): start_time represents the beginning of the time slots, in hours, end_time represents the end of the time slots, in hours, and lunch_time represents the time that the lunch period occurs, in hours. lunch_time is optional
# Return Value(s): the amount of time slots. Theoretically, this is as low as 2 but in most use cases it'll be 4 or more
#==========================================

def oral_exam_sign_up(start_time, end_time, lunch_time=0):
	slots = 0

	if start_time != int(start_time) or end_time != int(end_time) or lunch_time != int(lunch_time):
		print("Arguments must be integers. Please try again.")
		
	elif start_time not in range(1,13) or end_time not in range(1,13) or lunch_time not in range(0,13):
		print("Arguments must be between 1 and 12. Please try again.")
		
	else:
		current_hr = start_time
		current_hr_24 = start_time
		current_min = 0
		
		if start_time >= end_time:
			end_time += 12
			
		while current_hr_24 < end_time:
                        
			if current_hr == lunch_time and current_min == 0:
				current_min = 30
				
			else:
                                
				if int(current_min) < 10:
					current_min = "0" + str(current_min)
				time1 = [current_hr, current_min]
				
				new_min = int(current_min) + 10
				
				if new_min >= 60 and current_hr == 12:
					current_hr -= 11
					current_hr_24 += 1
					new_min = min_conversion(new_min)
				elif new_min >= 60:
					current_hr += 1
					current_hr_24 += 1
					new_min = min_conversion(new_min)
					
				time2 = [current_hr, new_min]
				
				slots += 1
				
				print(str(time1[0]) + ":" + str(time1[1]) + "-" + str(time2[0]) + ":" + str(time2[1]))
				
				current_min = int(new_min) + 5
				
				if current_min >= 60 and current_hr == 12:
					current_hr -= 11
					current_hr_24 += 1
					current_min = min_conversion(current_min)
				elif current_min >= 60:
					current_hr += 1
					current_hr_24 += 1
					current_min = min_conversion(current_min)

	return slots
