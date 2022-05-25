#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    epoch_time = resp["timestamp"]
    ts= datetime.datetime.fromtimestamp( epoch_time )
    print(f"""
CURRENT LOCATION OF THE ISS:
{ts}
Lon: {resp["iss_position"]["longitude"]}
Lat: {resp["iss_position"]["latitude"]} """)

if __name__ == "__main__":
    main()