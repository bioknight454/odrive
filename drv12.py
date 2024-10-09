import odrive
from odrive.enums import *
import time

odrv0 = odrive.find_any()
odrv0.axis0.motor.config.pre_calibrated = True
odrv0.axis0.controller.input_vel = 30
odrv0.axis0.requested_state = odrive.enums.AXIS_STATE_CLOSED_LOOP_CONTROL

odrv0.axis1.motor.config.pre_calibrated = True
odrv0.axis1.requested_state = odrive.enums.AXIS_STATE_CLOSED_LOOP_CONTROL
odrv0.axis1.controller.input_vel = 30
while True:
    # time.sleep(5)
    odrv0.axis0.controller.input_vel = 60
    odrv0.axis1.controller.input_vel = 60
    # time.sleep(5)
    # odrv0.axis0.controller.input_vel = 0
    # time.sleep(5)
    # odrv0.axis0.controller.input_vel = 50
    # time.sleep(5)
    # odrv0.axis0.controller.input_vel = 0