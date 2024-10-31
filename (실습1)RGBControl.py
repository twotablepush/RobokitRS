from RobokitRS import *
rs = RobokitRS.RobokitRS()
rs.port_open("/dev/tty.usbserial-0001")    # 로직에 나온 이름 찾아서 넣기

rs.set_rgb_led_color(4, 100, 100, 100)  # 포트번호, 빨, 초, 파
rs.delay(2)

rs.set_rgb_led_color(4, 100, 0, 0)  # red
rs.delay(2)

rs.set_rgb_led_color(4, 0, 100, 0)  # green
rs.delay(2)

rs.set_rgb_led_brightness(4, 50)    # led 밝기 줄이기 (가능한지 확인)
rs.delay(2)

rs.set_rgb_led_brightness(4, 25)    # led 밝기 줄이기 (가능한지 확인)
rs.delay(2)

rs.set_rgb_led_off(4)  # LED 끄기