from romipi_astar.romipi_driver import AStar
import time

romi = AStar()
line= 0.0
rotate = 0.0

def Check():
    romi.twist(line, rotate)

#does The Action 
while True:
    line = 0.30
    rotate = 0.80
    Check()

# stop motors and shut down light
romi.twist(0.0, 0.0)
romi.pixels(0, 0, 0)
