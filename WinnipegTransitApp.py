 # Name: Wai Lit Yeung 
 # Program: Business Information Technology
 # Course: ADEV-3011 Internet of Things
 # Created: 07 Sept 2023
 # Updated:
 #
import json
from requests import get
from colorama import just_fix_windows_console, Fore, Style
from dateutil.parser import parse

class WinnipegTransitApp():
    
    API_KEY = "HYAl66qBR4ZEpkMXs9nU"

    #get_bus_stops
    def get_bus_stops(self, lon, lat, distance):
        url_stops = f"https://api.winnipegtransit.com/v3/stops.json?lon={lon}&lat={lat}&distance={distance}&api-key={self.API_KEY}"
        resp_stops = get(url_stops).json()
        print(f"Stops available {distance}m from coordinates ({lon}, {lat})")
        return resp_stops
    
    #print_bus_stops
    def print_bus_stops(self, resp_stops):
        stop_list = []
        print(f"\tNumber \tName")
        for stop in resp_stops['stops']:
            print(f"\t{stop['number']} \t{stop['name']}")
            #add the stop number to stop list for user input validation
            stop_list.append(str(stop['number']))
        return stop_list
    
    #get_bus_schedule
    def get_bus_schedule(self, number):
        url_schedule = f"https://api.winnipegtransit.com/v3/stops/{number}/schedule.json?api-key={self.API_KEY}"
        resp_schedule = get(url_schedule).json()
        return resp_schedule
    
    #print_bus_schedule
    def print_bus_schedule(self, resp_schedules):
        just_fix_windows_console()
        print(f"Arrival times ({Fore.GREEN}green=on_time, {Fore.RED}red=late, {Fore.BLUE}blue=early):", end='')
        print(Style.RESET_ALL)
        for route_schedule in resp_schedules['stop-schedule']['route-schedules']:
            for schedule_stops in route_schedule['scheduled-stops']:
                scheduled_dt = parse(schedule_stops['times']['arrival']['scheduled'])
                scheduled_dt_24 = scheduled_dt.strftime('%H:%M:%S')
                estimated_dt = parse(schedule_stops['times']['arrival']['estimated'])
                estimated_dt_24 = estimated_dt.strftime('%H:%M:%S')
                if scheduled_dt_24 < estimated_dt_24:
                    color = Fore.RED 
                elif scheduled_dt_24 > estimated_dt_24:
                     color =Fore.BLUE
                else: color = Fore.GREEN
                print(f"\t{color}Route: {route_schedule['route']['number']} \tScheduled: {scheduled_dt_24} \tEstimated: {estimated_dt_24}")
        print(Style.RESET_ALL)

#main
def main():
    lon=-97.104689 #-97.138  # GPS longitude of location
    lat=49.856916#49.895   # GPS latitude of location
    distance=300 # radius in meters to search around GPS coordinates
    app = WinnipegTransitApp()
    resp_stops = app.get_bus_stops(lon, lat, distance)
    stop_list = app.print_bus_stops(resp_stops)
    
    #Validate user input on the stop list
    while True:
        user_input = input("Enter stop number: ")
        if user_input in stop_list:
            break
        print(f"Invalid Bus stop")
    
    resp_schedules = app.get_bus_schedule(user_input)
    app.print_bus_schedule(resp_schedules)

#entry point
if __name__ == "__main__":
    main()
