import os # for running commands related to installing dependencies
import json # for reading config.json
import time # for converting unix epoch time to human readable time and for sleeping

try:
	import requests # for pulling data from metro transit's servers
except:
	os.system("sudo python3 -m pip install requests")
	os.system("clear")
	import requests

#commented out for now until RGBMatrix implementation is finished
#try:
	#from rgbmatrix import RGBMatrix, RGBMatrixOptions
#except:
	#from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions

with open("./config.json", "r") as file:
	config = json.load(file)
	preferred_routes = config["preferred"]["preferred_routes"]
	preferred_stops = config["preferred"]["preferred_stops"]
	sleep_time = config["settings"]["refresh_rate_seconds"]
	delay_print = config["settings"]["print_delay"] # prints delay of current departure (ex. x bus is scheduled for 6:00 PM. Currently running 2 minutes and 0 seconds late.)
	delayed_departure_print = config["settings"]["print_delayed_departure"] # prints time of departure with delay (ex. x bus is scheduled for 6:00 PM. Currently running 2 minutes and 0 seconds late. (6:02 PM with delay.))
	file.close()

while True:
	for stop in preferred_stops:
		request_url = "https://svc.metrotransit.org/nextripv2/" + str(stop)
		response = requests.get(request_url)
		json_data = response.json()
		for departure in json_data["departures"]:
			if departure["route_id"] in preferred_routes:
				departure_time = departure["departure_time"]
				if "terminal" in departure:
					route = departure["route_id"] + departure["terminal"]
				else:
					route = departure["route_id"]
				match departure["direction_text"]:
					case "WB":
						direction = "westbound"
					case "EB":
						direction = "eastbound"
					case "NB":
						direction = "northbound"
					case "SB":
						direction = "southbound"
					case _:
						direction = ""
				print("A", direction, "Route", route, "bus is scheduled to arrive at stop ID", departure["stop_id"], "(" + json_data["stops"][0]["description"] + ")", "at", time.strftime("%I:%M %p.", time.localtime(departure_time)))
	time.sleep(sleep_time)
	os.system("clear")

##feed = gtfs_realtime_pb2.FeedMessage()
##response = requests.get("https://svc.metrotransit.org/mtgtfs/tripupdates.pb")
##feed.ParseFromString(response.content)
##for entity in feed.entity:
    ##if entity.trip_update.trip.route_id == "11" or entity.trip_update.trip.route_id == "18" and entity.trip_update.trip.direction_id == 1:
        ##print(entity.trip_update)
        ##for key in entity.trip_update.stop_time_update:
            ##if key.stop_id == "17978":
                ##print("The next " + entity.trip_update.trip.route_id + " bus is scheduled to come at ", end="")
                ##print(time.strftime("%I:%M %p", time.localtime(key.departure.time)), end="")
                ##print(". Currently running ", end="")
                ##print(f"{abs(key.departure.delay//60)} minutes and {abs(key.departure.delay%60)} seconds", end="")
                ##if key.departure.delay >= 0:
                    ##print(" late. ", end="")
                ##else:
                    ##print(" early. ", end="")
                ##print("(" + time.strftime("%I:%M %p", time.localtime(key.departure.time + key.departure.delay)), end="")
                ##print(" with delay.)")