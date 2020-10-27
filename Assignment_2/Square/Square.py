#!/usr/bin/python2
#
# Move the robot forwards and backwards
from romipi_astar.romipi_driver
import AStar
import time

motor_delay_s = 2.0
forward_speed_m_s = 0.1
stop_speed_m_s = 0.0
romi = AStar()

def Square(duration_s):
    for i in range(duration_s):
            romi.twist(duration_s*2,0.0)
            time.sleep(1.0)
            romi.twist(0.0, 3.14/2)
            time.sleep(1.0)



Square(10.0)