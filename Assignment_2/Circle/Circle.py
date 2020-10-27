#!/usr/bin/python2
#
# Move the robot forwards and backwards
from romipi_astar.romipi_driver import AStar
import time

motor_delay_s = 2.0
forward_speed_m_s = 0.1
stop_speed_m_s = 0.0
romi = AStar()

def Circle(duration_s):
     romi.twist(2*3.14,2*3.14/duration_s)
     time.sleep(duration_s)


Circle(10.0)