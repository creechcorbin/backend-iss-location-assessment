#!/usr/bin/env python

__author__ = 'Corbin Creech worked alongside Peyton Glover'

import requests
import turtle
import time


def getData():
    result = []
    response = requests.get('http://api.open-notify.org/astros.json')
    response = response.json()
    for person in response['people']:
        result.append(person['name'])
        result.append(person['craft'])
    result.append(
        'Number of people on spacecraft: {}'.format(len(response['people']))
        )
    print(result)

def getCoords():
    result = []
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response = response.json()
    result.append(response['iss_position'])
    result.append('Timestamp: {}'.format(response['timestamp']))
    print(result)
    return result

def get_passover_time():
    location = {'lat': 39.7683333, 'lon': -86.1580556}
    response = requests.get('http://api.open-notify.org/iss-pass.json', location)
    response = response.json()
    print(response)
    return response

def track_pos():
    pass_time = get_passover_time()

    screen = turtle.Screen()
    screen.setup(width=720, height=360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('./map.gif')
    screen.screensize(720, 360)
    screen.register_shape('./iss.gif')
    
    indy_lat = 39.7683333
    indy_lon = -86.1580556

    yellow_dot = turtle.Turtle()

    yellow_dot.penup()
    yellow_dot.goto(indy_lon, indy_lat)
    yellow_dot.dot(10, "yellow")

    coords = getCoords()
    iss_lat = coords[0]['latitude']
    iss_long = coords[0]['longitude']
    
    iss = turtle.Turtle()

    iss.penup()
    iss.shape('./iss.gif')
    iss.setheading(90)
    iss.goto(float(iss_long), float(iss_lat))

    human_time = time.ctime(pass_time['response'][0]['risetime'])
    yellow_dot.write(str(human_time), align='center', font=("Arial", 12, "bold"))

    return screen



def main():
    getData()
    getCoords()
    get_passover_time()
    test = track_pos()
    test.exitonclick()



if __name__ == '__main__':
    main()
