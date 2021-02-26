# This file is executed on every boot (including wake-boot from deepsleep)
import os,network
import sys
import machine
import socket
import time
from machine import Pin
SSID="15-3-201"
PASSWORD="1234567890abc"
wlan=None
def connectWifi(ssid,passwd):
  global wlan
  cnt=0
  
  print("Start Wifi  NIC.")
  wlan=network.WLAN(network.STA_IF)                     #create a wlan object
  wlan.active(True)                                     #Activate the network interface
  print()
  print("Connect Wifi.",end="")
  #wlan.disconnect()                                     #Disconnect the last connected WiFi
  wlan.connect(ssid,passwd)                             #connect wifi
  while(wlan.isconnected()==False):
    cnt=cnt+1
    time.sleep(0.5)
    if cnt>60:
        machine.reset()
  print(" OK.")
  print("IP ADDR:",wlan.ifconfig())  
  print()
  print()  
  print("NTP sync",end="")
  return True
connectWifi(SSID,PASSWORD)



