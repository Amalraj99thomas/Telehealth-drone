"""
Simple script for take off and control with arrow keys
"""


import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil



#-- Connect to the vehicle
print('Connecting...')
vehicle = connect('udp:127.0.0.1:14551')

#-- Setup the commanded flying speed
gnd_speed = 5 # [m/s]

#-- Define arm and takeoff
def arm_and_takeoff(altitude):

   while not vehicle.is_armable:
      print("waiting to be armable")
      time.sleep(1)

   print("Arming motors")
   vehicle.mode = VehicleMode("GUIDED")
   vehicle.armed = True

   while not vehicle.armed: time.sleep(1)

   print("Taking Off")
   vehicle.simple_takeoff(altitude)

   while True:
      v_alt = vehicle.location.global_relative_frame.alt
      print(">> Altitude = %.1f m"%v_alt)
      if v_alt >= altitude - 1.0:
          print("Target altitude reached")
          break
      time.sleep(1)

#---- MAIN FUNCTION
#- Takeoff
arm_and_takeoff(5)

print("Autopilot Firmware version: ", vehicle.version)
print("Autopilot capabilities (supports ftp): ", vehicle.capabilities.ftp)
print("Global Location: ", vehicle.location.global_frame)
print("Global Location (relative altitude): ", vehicle.location.global_relative_frame)
print("Local Location: ", vehicle.location.local_frame)    #NED
print("Velocity: ", vehicle.velocity)
print("Attitude: ", vehicle.attitude)
print("GPS: ", vehicle.gps_0)
print("Groundspeed: ", vehicle.groundspeed)
print("Airspeed: ", vehicle.airspeed)
print("Gimbal status: ", vehicle.gimbal)
print("Battery: ", vehicle.battery)
print("EKF OK?: ", vehicle.ekf_ok)
print("Last Heartbeat: ", vehicle.last_heartbeat)
print("Rangefinder: ", vehicle.rangefinder)
print("Rangefinder distance: ", vehicle.rangefinder.distance)
print("Rangefinder voltage: ", vehicle.rangefinder.voltage)
print("Heading: ", vehicle.heading)
print("Is Armable?: ", vehicle.is_armable)
print("System status: ", vehicle.system_status.state)
print("Mode: ", vehicle.mode.name)    # settable
print("Armed: ", vehicle.armed)    # settable
