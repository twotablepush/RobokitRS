from RobokitRS import *
rs = RobokitRS.RobokitRS()
rs.port_open("com3")
rs.set_pin_mode(12, RobokitRS.Modes.INPUT)
rs.set_pin_mode(13, RobokitRS.Modes.INPUT)

rs.sonar_begin(2)
while(True):
    SONAR = rs.sonar_read(2)
    if SONAR >= 2 and SONAR <= 5:
        rs.set_rgb_led_red(3)
        rs.set_rgb_led_on(3)
    elif SONAR >= 6 and SONAR <= 10:
        rs.set_rgb_led_orange(3)
        rs.set_rgb_led_on(3)
    elif SONAR >= 11 and SONAR <= 15:
        rs.set_rgb_led_yellow(3)
        rs.set_rgb_led_on(3)
    elif SONAR >= 16 and SONAR <= 20:
        rs.set_rgb_led_green(3)
        rs.set_rgb_led_on(3)
    else:
        rs.set_rgb_led_off(3)

    IR_L = rs.digital_read(12)
    IR_R = rs.digital_read(13)
    if IR_R == 1:
        rs.set_rgb_led_pink(3)
        rs.set_rgb_led_on(3)
    else:
        rs.set_rgb_led_off(3)
    
    if IR_L == 1:
        rs.set_rgb_led_purple(3)
        rs.set_rgb_led_on(3)
    else:
        rs.set_rgb_led_off(3)