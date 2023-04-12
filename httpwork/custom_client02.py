#!/usr/bin/env python3
"""Alta3 Research | rzfeeser@alta3.com
   (improved) http.client to create a simple HTTP client."""

import http.client

def main():

    user_response = input("What type of connection would you like to test?")
    user_response = user_response.upper()
    ## think of this as setting up the connection
    conn = http.client.HTTPConnection("localhost", 9021)

    ## Send an HTTP request and store the HTTP response
    ##    from our webserver
    conn.request(user_response, '/')

    ## Returns just the response that has been associated with
    ##    the **conn** object.
    res = conn.getresponse()
    
    ## response status and the reason to the screen.
    print(res.status, res.reason)

    ## this time we'll issue GET
#    conn.request('GET', '/')
    
    ## res is equal to the response associated with conn
#    res = conn.getresponse()
    
    ## print the response status code and reason
#    print(res.status, res.reason)
    
    ## page_data is all of the data associated with res 
    page_data = res.read()

    ## this will point out all of the data associated with res
    print(page_data)
    page_data_str = page_data.decode("utf-8")
    with open('get_data.txt', 'w') as file:
        file.write(page_data_str)

if __name__ == "__main__":
    main()

