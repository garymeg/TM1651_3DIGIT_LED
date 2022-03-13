"""Command-line program to control a 3 digit LED TM1651 display. 
the ones used in GOTEK usb floppy drives
(c)copyright Gary Metheringham 

Modyfied from Battery display by
Copyright (C) 2020-2021 Koen Vervloesem
SPDX-License-Identifier: MIT
"""
import argparse
import sys
from time import sleep

from psutil import cpu_percent
from RPi.GPIO import cleanup
import psutil  # pylint: disable=no-name-in-module

from TM1651 import LED_Display
clock_pin = 22 #Can be any RPi Gpio pin
data_pin = 23   #Can be any RPi Gpio pin
segments = 8    #Left over from battery display
brightness = 3  #Self explanitory
blank = True   #Blank or 0 for unused (Padding) numbers 001,012 or   1,   12



def CPU():
    display = LED_Display(clock_pin, data_pin, segments, blank)
    display.set_brightness(brightness)
    while True:
        i = int(psutil.cpu_percent())
        display.show(i)
        sleep(0.5)
    
if __name__ == "__main__":
   CPU()

        