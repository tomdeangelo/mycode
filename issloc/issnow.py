#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    print(resp)
    long = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    timestamp = resp["timestamp"]
    print(f"Timestamp: {timestamp}")
    print(f"Longitude: {long}")
    print(f"Latitude: {lat}")

if __name__ == "__main__":
    main()
