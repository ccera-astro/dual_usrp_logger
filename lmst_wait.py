#!/usr/bin/python3

import time
import sys
import os
import ephem
import argparse

# Given longitude(decimal degrees as a float)
#
# Return the current sidereal time as a string with
#  "," separated tokens
#
def cur_sidereal(longitude):
    longstr = "%02d" % int(longitude)
    longstr = longstr + ":"
    longitude = abs(longitude)
    frac = longitude - int(longitude)
    frac *= 60
    mins = int(frac)
    longstr += "%02d" % mins
    longstr += ":00"
    x = ephem.Observer()
    x.date = ephem.now()
    x.long = longstr
    jdate = ephem.julian_date(x)
    tokens=str(x.sidereal_time()).split(":")
    hours=int(tokens[0])
    minutes=int(tokens[1])
    seconds=int(float(tokens[2]))
    sidt = "%02d,%02d,%02d" % (hours, minutes, seconds)
    return (sidt)

TENSECS = 10.0/3600.0
parser = argparse.ArgumentParser(description="Wait for a given LMST then exit")
parser.add_argument("--longitude", type=float, help="Local longitude", required=True)
parser.add_argument("--lmst", type=float, help="LMST to wait for", required=True)

args = parser.parse_args()

while True:
    x = cur_sidereal(args.longitude)
    x = x.split(",")
    lmst = float(x[0])
    lmst += float(x[1])/60.0
    lmst += float(x[2])/3600.0
    
    if (lmst >= args.lmst and lmst <= (args.lmst + TENSECS)):
        break

    time.sleep(1.0)

